from flask import Flask,render_template

app = Flask(__name__)#create an instance of the flask class

@app.route('/')# / landing page(home page)
def home():
    return render_template('index.html')
    ##return 'Hello,World'

@app.route('/about')
def about():
    return 'the about page'
@app.route("/login")
def login():
    return render_template('login.html')

if __name__ =='__main__':#run the app
    app.run()