from functools import wraps
from flask import *
from ciphering import CatCyphers
from SiteManager import SiteManager

Cipherer = CatCyphers()
app = Flask(__name__)
Manager = SiteManager()
enabled = True


def catch_custom_exception(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        from time import sleep
        sleep(1)
        if enabled:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                Manager.raise_operating_error(func.__name__, e)
                return f'Oops. {e}'
        else:
            return 'Nope.'
    return decorated_function


@app.route('/', methods=['GET'])
@catch_custom_exception
def index():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    with open('log.txt', 'a') as log:
        log.write(f'ACS : IND : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
    return ''


@app.route('/fetch_res', methods=['GET'])
@catch_custom_exception
def fetching_res():
    with open('CIPHERTEXT_STORAGE.txt') as f:
        return '<pre>' + f.read().replace('\n', '<br>') + '</pre>'


@app.route('/enabling', methods=['GET'])
def enabling():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    if auth['authorized']:
        global enabled
        enabled = True if not enabled else False
        return f'Now {enabled}.'
    return Response(status=404)


@app.route('/authorise', methods=['GET'])
@catch_custom_exception
def authorization(ip=None):
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    with open('log.txt', 'a') as log:
        log.write(f'ACS : ATH : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
    if not ip: ip = request.cookies.get('us_id')
    ADMINISTRATION_KEY_FOR_AUTHORISING = 'iwontfuckingauthoriseyoumydude'
    if request.args.get('admin_key') == ADMINISTRATION_KEY_FOR_AUTHORISING:
        auth = Manager.get_authorization(ip)
        with open('log.txt', 'a') as log:
            log.write(f'ACS : ATH : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
        result = Manager.authorize_user_by_request(ip)
        with open('log.txt', 'a') as log:
            log.write(f'ATH : {'DND' if not result else 'PER'}\n')
        with open('auth_log.txt', 'a') as log:
            log.write(f'AUTHORIZATION COMPLETED BY THE APPROVAL OF THE MAIN CONSOLE: {ip}\n')
        return 'Denied.' if not result else 'Permitted.'
    else:
        return Response(status=404)


@app.route('/login', methods=['GET', 'POST'])
@catch_custom_exception
def login():
    if request.args.get('username') and request.args.get('password'):
        res = Manager.login_user_id([request.args.get('username'), request.args.get('password')]).split(': ')
        if res[0] == 'Registered':
            resp=make_response('Registered.')
            resp.set_cookie('us_id', res[1])
            return resp
    return 'Registration needed.'


@app.route('/check_log', methods=['GET'])
@catch_custom_exception
def check_log():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    with open('log.txt', 'a') as log:
        log.write(f'ACS : ALG : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
    if auth['authorized'] == 'Y':
        with open('log.txt') as log:
            res = log.read().replace('\n', '<br>')
        if request.args.get('clear'):
            if request.args.get('clear').lower() == 'y':
                with open('log.txt', 'w') as _: pass
        return res
    return Response(status=404)


@app.route('/check_error_log', methods=['GET'])
@catch_custom_exception
def check_error_log():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    with open('log.txt', 'a') as log:
        log.write(f'ACS : ERR : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
    if auth['authorized'] == 'Y':
        with open('error_log.txt') as er_log:
            res = er_log.read().replace('\n', '<br>')
        if request.args.get('clear'):
            if request.args.get('clear').lower() == 'y':
                with open('error_log.txt', 'w') as _: pass
        return res
    return Response(status=404)


@app.route('/check_user_log', methods=['GET'])
@catch_custom_exception
def check_user_log():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    with open('log.txt', 'a') as log:
        log.write(f'ACS : USR : AUTH-{auth['authorized']} : {request.cookies.get('us_id')}\n')
    if auth['authorized'] == 'Y':
        with open('user_authorization.txt') as er_log:
            return er_log.read().replace('\n', '<br>')
    return Response(status=404)


@app.route('/cipher', methods=['GET'])
@catch_custom_exception
def cipher():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    if auth['authorized'] == 'Y':
        return str(Cipherer.funcs['cipher'][request.args.get('author')][request.args.get('step')](*request.args.get('data').split(':')))
    return Response(status=404)


@app.route('/decipher', methods=['GET'])
@catch_custom_exception
def decipher():
    auth = Manager.get_authorization(request.cookies.get('us_id'))
    if not auth: return redirect(url_for('login'))
    if auth['authorized'] == 'Y':
        return Cipherer.funcs['decipher'][request.args.get('author')][request.args.get('step')](*request.args.get('data').split(':'))
    return Response(status=404)


if __name__ == '__main__':
    app.run('localhost', 443)
