from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'wlFw0WP7SrNmAMF1wJaUSjWMTYdTay8EDIA3FPQhbo9c7wQ9rIdQrzJRzcN1o3mp'
app.debug=True

@app.route('/',methods=['GET','POST'])
def index():
    session['loggedin'] = True

    return render_template('index.html',session=session)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
