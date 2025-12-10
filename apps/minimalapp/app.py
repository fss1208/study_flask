from flask import Flask, render_template, url_for, request, redirect
from flask import current_app, g

app = Flask(__name__)
app.config['SECRET_KEY'] = '2AZMss3p5QPbcY2hBs'

@app.route('/')
def index():
    return 'Hello, FlaskBook!'

@app.route('/hello/<string:name>', methods=['GET'], endpoint='hello-endpoint')
def hello(name):
    return render_template('index.html', name=name)

@app.route('/name/<name>')
def show_name(name):
    return f'Hello, {name}!'

###########################################################################

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if (request.method == "POST"):
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        print(username, email, description, sep='\n')
        # redirect to contact end-point
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

###########################################################################

with app.test_request_context("/users?updated=true"):
    print(url_for('index'))
    print(url_for('static', filename='style.css'))
    print(url_for('hello-endpoint', name='ksh'))
    print(url_for('show_name', name='AK', page='1', date='2025-12-10'))
    print(request.args.get('updated'))

ctx = app.app_context()
ctx.push()
print(current_app.name)
g.connection = 'Connection'
print(g.connection)
ctx.pop()

if __name__ == '__main__':
    app.run(debug=True)