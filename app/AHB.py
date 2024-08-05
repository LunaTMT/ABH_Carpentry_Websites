"""
This is where the routes are defined. 
It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.
"""

from flask import render_template, Blueprint, redirect, url_for, flash
from .forms import ContactForm
import json

bp = Blueprint('AHB', __name__)

@bp.route('/')
@bp.route('/home')
def index():
    form = ContactForm()
    return render_template('1_HOME/index.html', form=form)


@bp.route('/')
@bp.route('/services')
def services():
    with open('json/services.json') as f:
        data = json.load(f)
    services = data.get('services', [])

    return render_template('2_SERVICES/services.html', services=services)


@bp.route('/')
@bp.route('/portfolio')
def portfolio():
    return render_template('3_PORTFOLIO/portfolio.html')


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

    return render_template('4_CONTACT/contact.html', form=form)



@bp.route('/success')
def success():
    return render_template('CODES/success.html')
