from flask import Blueprint, jsonify, render_template, request
from .form_fields import RegistrationForm

auth = Blueprint('auth', __name__)



@auth.route('/', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()

    #validate on submit returns true if all checks clear out and false otherwise
    if reg_form.validate_on_submit():
        return 'form_validated'
    

    return render_template('register.html', form = reg_form)