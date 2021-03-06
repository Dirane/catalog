from functools import wraps
from flask import redirect, request, url_for
from flask import session as login_session
#To be used for authentication user view and authorized actions 
def authentication_needed(f):
    '''Checks to see whether a user is logged in'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function