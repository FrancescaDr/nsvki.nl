#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, Blueprint
from flask.ext.babel import _

blueprint = Blueprint('page', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    return render_template('association.htm', title=_('Association'))


@blueprint.route('/links', methods=['GET'])
def links():
    return render_template('links.htm', title=_('Links'))


@blueprint.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.htm', title=_('Contact'))
