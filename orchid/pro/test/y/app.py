from flask import Flask,make_response,redirect,abort
from flask import render_template
from flask.ext.bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap(app)


'''index() 函数注册为程序根地址的处理程序'''
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/console')
def console():
    return render_template('index.html')



@app.route('/user/<id>')
def get_user(id):
    return render_template('user.html', name=id)





if __name__ == '__main__':
    app.run()
