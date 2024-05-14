# Day19: revenge of http
from flask import Flask
from markupsafe import  escape
from flask import render_template
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html') # ,name="WORLD")
    

@app.route("/hello/<name>")
def say_hello(name):
    return f'''<html>
    <head><title>Hello world</title></head>
    <body><h1>Hello {escape(name)}</h1></body>
    </html>'''

@app.route("/users/")
def list_users():
    return "['user':{'name':'Leonardo,'surname':'Barozzi'},'user':{'name':'Antonino,'surname':'Foti'}]"

@app.route("/users/<int:id>")
def get_user(id):
    return f"{{'user':{{'id':{id},'name':'Leonardo,'surname':'Barozzi'}} }}"

@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    return f'deleted {id}'

# '''
@app.route("/form_test", methods=["GET"])
def render_form():
    # abort(415)
    return render_template('Myform.html'),204
# '''

@app.route("/form_test", methods=["POST"])
def test_form():
    '''
    if request.method=='GET':
        return render_template('Myform.html',test="Antani")
    # '''
    myname= request.form["firstname"]
    mysurname= request.form["lastname"]
    # request.files['']
    return jsonify({'name':myname,'surname':mysurname})


def main():
    # Default 127.0.0.1 (localhost) : 5000
    app.run(host='0.0.0.0',port =5001)
    pass


if __name__=="__main__":
    main()