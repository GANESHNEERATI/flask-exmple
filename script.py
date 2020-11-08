from flask import *

app=Flask(__name__)


@app.route('/error')
def error():
    return '<p>enter valid username and password</p>'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['pass']
    if password=='ganesh':
        res=make_response(render_template('success.html'))
        res.set_cookie('email',email)
        return res
    else:
        return redirect(url_for('error'))
@app.route('/viewprofile')
def viewprofile():
    
    email=request.cookies.get('email')
    resp=make_response(render_template('profile.html',name=email))
    return resp

@app.route('/logout')
def logout():
    if request.cookies.get('email'):
        resp = make_response(render_template('login.html'))
        resp.set_cookie('email', expires=0)

        return resp

if __name__ == "__main__":
    app.run(debug=True)