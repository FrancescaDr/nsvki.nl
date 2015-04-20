from flask import request


def return_previous(default='/'):
    return request.args.get('next') or request.referrer or default
