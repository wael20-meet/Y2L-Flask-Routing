from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def homepage():
	return  render_template("hello.html")

@app.route('/store')



#####################


if __name__ == '__main__':
    app.run(debug=True)