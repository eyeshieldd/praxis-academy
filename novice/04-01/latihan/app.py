from flask import Flask, render_template, abort
app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return 'Hello World'

@app.route('/hi/<name>')
def say_hi(name):
    return 'Hello, %s!' % (name)

@app.route('/age/<int:age>')
def show_age(age):
    return 'Age is %d!' % (age)

def about():
    return "about page"

app.add_url_rule('/', 'about', about)

if __name__=='__main__':
    app.run(debug=True)