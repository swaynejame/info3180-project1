"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash

from werkzeug.utils import secure_filename

from .forms import ProfileForm

from .models import User

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile')
def profile():
    profile_form = ProfileForm()

    if request.method == 'POST'and profile_form.validate_on_submit():

        photo = profile_form.photo.data
        filename = secure_filename(photo.filename)

        """Render the website's add profile page."""
    return render_template('profile.html',form=profile_form)


@app.route('/profiles')
def listprofiles():
    """Render the website's list of profiles page."""
    return render_template('about.html')


@app.route('/profile/<userid>')
def userprofile():
    """Render the website's individual profile page."""
    return render_template('about.html')

# @app.route('/contact',methods=('GET', 'POST'))
# def contact():
#     contactform = ProfileForm()
#     if request.method == 'POST':
#         if contactform.validate_on_submit():
#             msg = Message(contactform.subject.data, sender=(contactform.name.data,contactform.email.data),
#             recipients=["to@example.com"])
#             msg.body = contactform.message.data
#             mail.send(msg)

#             flash('Email successfully sent','success')
#             flash('You have successfully filled out the form', 'success')

#             return redirect( url_for('home'))
            
#         flash_errors(contactform)
#         """Render website's contact page."""
#     return render_template('contact.html',form=contactform)


###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
