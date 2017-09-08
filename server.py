from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",phrase="hello",times = 5)
#
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
   name = request.form['name_val']
	 # Here's the line that changed. We're rendering a template from a post route now.
   return render_template('index.html', name =name)

# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
