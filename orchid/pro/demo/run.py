from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
	return 'The Index Page'

@app.route('/demo/test',methods=['GET','POST','PATCH','PUT','DELET'])
def demo():
    type1 = request.args.get('type1')
    type2 = request.args.get('type2')
    print(type1,type2)
    return 'The Demo Page ' + 'type1 ='+type1 + ' ' + 'type2 ='+type2


if __name__ == '__main__':
    app.run()