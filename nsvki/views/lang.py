from flask import Blueprint, redirect, make_response, request, url_for
from flask.ext.babel import refresh
from config import LANGUAGES

blueprint = Blueprint('lang', __name__)


def redirect_url(default='page.index'):
    return request.args.get('next') or request.referrer or url_for(default)


@blueprint.route('/lang/<path:lang>', methods=['GET'])
def set_lang(lang):
    if lang not in LANGUAGES.keys():
        return redirect('page.index')

    rv = make_response(redirect(redirect_url()))
    rv.set_cookie('username', 'the username')
    refresh()
    return rv
