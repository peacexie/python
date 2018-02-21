from flask import Blueprint, render_template
front = Blueprint('front', __name__)

@front.route('/')
@front.route('/<mkv>')
def index(mkv=''):
    return render_template('front/home/index.htm')