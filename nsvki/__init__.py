from flask import Flask, render_template, request, flash
from flask.ext.babel import Babel
from config import LANGUAGES

import datetime
import json
import os
import sys

version = 'v1.0.0'

application = Flask(__name__)
application.config.from_object('config')
babel = Babel(application)


@babel.localeselector
def get_locale():
    lang = request.cookies.get('lang')
    if lang:
        return lang
    return request.accept_languages.best_match(list(LANGUAGES.keys()))


def static_url(url):
    return url + '?v=' + version


def is_module(path):
    init_path = os.path.join(path, '__init__.py')

    if os.path.isdir(path) and os.path.exists(init_path):
        return True
    elif os.path.isfile(path) and os.path.splitext(path)[1] == '.py':
        return True

    return False


def import_module(name, globals=globals(), locals=locals(), fromlist=[],
                  level=-1):
    __import__(name)

    return sys.modules[name]


def register_views(application, path, extension=''):
    application_path = os.path.dirname(os.path.abspath(application.root_path))

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Check if the current file is a module.
        if is_module(file_path):
            # Get the module name from the file path.
            module_name = os.path.splitext(file_path)[0]
            module_name = os.path.relpath(module_name, application_path)
            module_name = module_name.replace('/', '.')

            blueprint = getattr(import_module(module_name), 'blueprint', None)

            if blueprint:
                print(('Imported: {0}'.format(module_name)))
                application.register_blueprint(blueprint)


application.jinja_env.globals.update(enumerate=enumerate)
application.jinja_env.globals.update(render_template=render_template)
application.jinja_env.globals.update(datetime=datetime)
application.jinja_env.globals.update(json=json)
application.jinja_env.globals.update(len=len)
application.jinja_env.globals.update(isinstance=isinstance)
application.jinja_env.globals.update(list=list)
application.jinja_env.globals.update(request=request)
application.jinja_env.globals.update(static_url=static_url)
application.jinja_env.globals.update(flash=flash)

# Register all views in the view directory
path = os.path.dirname(os.path.abspath(__file__))
register_views(application, os.path.join(path, 'views'))
