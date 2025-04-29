from flask import Flask, request, redirect, render_template_string, render_template, send_file
import requests
import os

from jinja2 import Template #Fix for SSTI
from markupsafe import escape #Fix for XSS

app = Flask(__name__)
app.secret_key = 'insecure-secret-key'
ALLOWED_DOMAINS = ['google.com', ''] #Fix for SSRF
BASE_DIR = '/uploads/' #Fix for LFI

# Vulnerable Home Page
@app.route('/')
def home():
    return '''<h1>Vulnerable App</h1>
            <ul>
                <li><a href="/search?q=">XSS Demo</a></li>
                <li><a href="/profile/admin">SSTI Demo</a></li>
                <li><a href="/fetch?url=">SSRF Demo</a></li>
                <li><a href="/file?name=">LFI Demo</a></li>
                <li><a href="/redirect?target=">Open Redirect Demo</a></li>
            </ul>'''

# Vulnerability 1: Server-Side Template Injection (SSTI) leading to RCE Fix Version
@app.route('/profile/<username>')
def profile(username):
    sanitized = escape(username)
    return render_template('profile.html', username=sanitized)

# Vulnerability 2: Cross-Site Scripting (XSS) Fix Version
@app.route('/search')
def search():
    query = escape(request.args.get('q', ''))
    return render_template('search.html', query=query)

# Vulnerability 3: Server-Side Request Forgery (SSRF) Fix Version
def is_allowed(url):
    from urllib.parse import urlparse
    domain = urlparse(url).hostname
    return domain in ALLOWED_DOMAINS

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    if url:
    	if not is_allowed(url):
        	return "Blocked", 403
    	response = requests.get(url)
    	return response.text
    return 'Enter URL parameter'

# Vulnerability 4: Local File Inclusion (LFI) Fix Version
@app.route('/file')
def get_file():
    filename = request.args.get('name', '')
    if not filename:
    	return 'Enter file name parameter'
    safe_path = os.path.join(BASE_DIR, filename)
    if not os.path.realpath(safe_path).startswith(BASE_DIR):
        return "Forbidden", 403
    return send_file(safe_path)

# Vulnerability 5: Open Redirect Fix Version
@app.route('/redirect')
def safe_redirect():
    target = request.args.get('target', '')
    if not target:
    	return 'Enter URL or path target parameter'
    if not target.startswith('/'):
        return "Invalid redirect", 400
    return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)
