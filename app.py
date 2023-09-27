import requests as reqs
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)       
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        default_value = '127.0.0.1'
        url = request.form.get('link', default_value)
        return redirect(url_for('check_status', url=url))

    return render_template("index.html")


@app.route("/<path:url>")
def check_status(url): # METHOD CHECKS SITE STATUS
    if "http://" not in url: 
        url = f"http://{url}"
    
    res = reqs.get(url, timeout=45)
    status = res.status_code

    return f"URL: {url}\nStatus: {status}"

@app.route("/test")
def show_test():
    return render_template('test.html', site="GOOGLE", link="https://www.google.com/")




