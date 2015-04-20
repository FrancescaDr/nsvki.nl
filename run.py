#!venv/bin/python
# encoding: utf-8
from flask_failsafe import failsafe


@failsafe
def create_app():
    from nsvki import application

    return application
if __name__ == '__main__':
    create_app().run(debug=True)
