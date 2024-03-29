from flask import Flask, render_template, request, flash
from flask_babel import Babel, _
# from flask.ext.babel import Babel, _
   

app = Flask(__name__)
# app.config.from_pyfile('babel.cfg')
babel = Babel(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/text")
def text():
    flash(_('Your post is now live!'))
    return render_template('index.html')

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(['en', 'rw'])
    return 'rw'

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)