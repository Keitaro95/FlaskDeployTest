from flask import render_template, Blueprint

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/page/<int:id>')
def show_page(id):
    return render_template("page.html", id=id)
