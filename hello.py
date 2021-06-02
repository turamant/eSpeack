from flask import Flask, url_for, render_template
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    user = {'username': 'miguel'}
    process = os.getpid()
    papka = os.getcwd()
    u = os.getuid()
    g = os.getgid()
    return render_template('index.html', title='Home',
                           user=user, process=process,
                           papka=papka, u=u, g=g)

@app.route('/about/')
def about():
    user = {'username': 'miguel'}
    proc = os.getpid()
    papka = os.getcwd()
    u = os.getuid()
    g = os.getgid()
    return render_template('index.html', user=user,
                           process=proc, papka=papka,
                           u=u, g=g)


if __name__=='__main__':
    app.run(debug=True)