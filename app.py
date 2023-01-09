from flask import Flask, render_template, redirect, request, flash, url_for
import requests
from requests.exceptions import ConnectionError


app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        message = request.form["messageBox"]
        try:
            r = requests.post('http://lovebox.pythonanywhere.com/', json = {"message" : message})
            response = r.json()
            flash('Message sent successfully')
        except ConnectionError as e:    # This is the correct syntax
            flash("Uh oh! Looks like the API is under construction!")
            return redirect(url_for('index'))
    return render_template('index.html')    


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')