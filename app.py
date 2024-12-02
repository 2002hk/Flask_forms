from flask import(Flask,
                  render_template,
                  redirect,
                  url_for,
                  flash)
app=Flask(__name__)
app.config['SECRET_KEY']="dscampusx"

@app.route('/')
@app.route('/home')
def home():
    return 

@app.route('/signup',methods=['GET','POST'])
def signup():
    return

@app.route('/login',methods=['GET','POST'])
def login():
    return

if __name__=="__main__":
    app.run(debug=True)