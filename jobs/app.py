import flask from Flask , render_template

add = Flask(__name__)

@app.route('/')
@app.route('/job')
def jobs():
    return render_template('index.html')
