from flask import Blueprint, redirect, render_template, request, flash, url_for, jsonify
from flask_login import login_required, current_user


chat = Blueprint('chat', __name__)

ROOMS = ['gaming', 'movies', 'music', 'sports', 'education']

@chat.route('/chat')
@login_required
def home():
    return render_template('chat.html', username = current_user.username, rooms = ROOMS)