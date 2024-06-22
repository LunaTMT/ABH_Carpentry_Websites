"""
This is where the routes are defined. 
It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.
"""

from flask import render_template, Blueprint, redirect, url_for, flash


bp = Blueprint('AHB', __name__)

@bp.route('/')
@bp.route('/home')
def index():
    return render_template('INDEX/index.html')

@bp.route('/')
@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/')
@bp.route('/services')
def services():
    return render_template('services.html')

@bp.route('/')
@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



from .forms import ContactForm

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process the form data
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Here you can perform actions like sending an email,
        # storing the message in a database, etc.

        return redirect(url_for('AHB.success'))

    return render_template('contact.html', form=form)



@bp.route('/success')
def success():
    return render_template('CODES/success.html')
