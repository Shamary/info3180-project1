"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, json, jsonify, Response
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm,UpForm
from models import UserProfile,Profile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
            # Get the username and password values from the form.
            uname=form.username.data;
            pwd=form.password.data;
            
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
            user= UserProfile.query.filter_by(username=uname, password=pwd).first()
            # get user id, load into session
            if(user):
                login_user(user)

                # remember to flash a message to the user
                flash("login successful")
                return redirect(url_for("secure_page")) # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)


@app.route("/secure_page")
@login_required
def secure_page():
    return render_template("secure_page.html");

@app.route("/logout")
@login_required
def logout():
    logout_user()
    
    flash("logged out")
    return redirect(url_for('home'))


#################project###################

@app.route("/profile",methods=["GET","POST"])################ADD
def add_profile():
    form=UpForm()
    if(form.validate_on_submit()):
        flash("Is valid")
        fname=form.fname.data
        lname=form.lname.data
        uname=form.uname.data;
        uage=form.age.data
        gen=form.gender.data
        bio=form.biography.data
        
        profile=Profile(first_name=fname,last_name=lname,username=uname,age=uage,gender=gen,biography=bio)
        
        db.session.add(profile)
        db.session.commit()
        
        return redirect(url_for('home'))
            
    return render_template("add_profile.html",form=form);

@app.route("/profiles",methods=["GET","POST"])##############GET +
def view_profiles():
    if(request.method=="POST"):
        all_profiles=list(Profile.query.with_entities(Profile.username,Profile.id))
        jres= json.dumps(all_profiles)
        res=Response(response=jres,status=200,mimetype="application/json")
        
        return res
    else:
        all_profiles=Profile.query.all()
        return render_template("profiles.html",all_profiles=all_profiles);

@app.route("/profile/<userid>",methods=["GET","POST"])############GET 1
def view1_profile(userid):
    #uid=request.GET.get('<userid>','')
    if(request.method=="POST"):
        profile1=list((Profile.query.filter_by(id=userid))
                      .with_entities(Profile.username,Profile.id,Profile.gender,Profile.age))
        jres= json.dumps(profile1)
        res=Response(response=jres,status=200,mimetype="application/json")
        
        return res
    else:
        prof=Profile.query.filter_by(id=userid)
        return render_template("profile.html",prof=prof)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
