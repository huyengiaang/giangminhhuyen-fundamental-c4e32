from flask import Flask, render_template
app = Flask(__name__)

@app.route('/add/<name>')
def say_hi_name(name):
    return 'hello ' + name

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

