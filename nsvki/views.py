from flask import render_template, Blueprint
from flask.ext.babel import _

blueprint = Blueprint('meme', __name__, url_prefix='/meme')


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('association.htm', title=_('Association'))


@blueprint.route('/create', methods=['GET'])
def links():
    return render_template('links.htm', title=_('Links'))


@blueprint.route('/view/<int:id>', methods=['GET'])
def view():
    return render_template('contact.htm', title=_('Contact'))
