#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, Blueprint, request
from flask.ext.babel import _

blueprint = Blueprint('page', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    lang = request.cookies.get('lang')
    if not lang:
        return render_template('en/association.htm', title=_('Association'))
    else:
        return render_template('%s/association.htm' % lang,
                               title=_('Association'))


@blueprint.route('/masters/amsterdam', methods=['GET'])
def amsterdam():
    return render_template('en/amsterdam.htm', title="Masters in Amsterdam")

@blueprint.route('/links', methods=['GET'])
def links():
    lang = request.cookies.get('lang')
    if not lang:
        return render_template('en/links.htm', title=_('Links'))
    else:
        return render_template('%s/links.htm' % lang, title=_('Links'))


@blueprint.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.htm', title=_('Contact'))
