from flask import Flask,make_response,redirect,abort
from flask import render_template
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


'''index() 函数注册为程序根地址的处理程序'''
@app.route('/',)
def index():
    # 1
    # return '<h1>Hello, % s!</h1>'
    # 2
    '''
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
    '''
    #3
    #return redirect('http://www.baidu.com')
    #4
    return render_template('index.html')



@app.route('/user/<id>')
def get_user(id):
    #1
    '''
    user = False #load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, % s</h1>' % user
    '''
    #2
    return render_template('user.html', name=id)





if __name__ == '__main__':
    app.run()
