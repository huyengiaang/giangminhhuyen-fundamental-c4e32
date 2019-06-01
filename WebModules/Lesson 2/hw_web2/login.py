from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html", login=login)

@app.route('/', methods=['POST']) 
def login():
    user_name = request.form.get('name')
    pass_word = request.form.get('pass')
    if user_name == 'gmhuyen' and pass_word == 'gmh1106':
        return 'Login Successful!'
    else:
        return 'Login Failed!'
    return render_template("login.html", login=login)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

