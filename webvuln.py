from flask import Flask, request, redirect, render_template_string, render_template, send_file
import requests
import os

app = Flask(__name__)
app.secret_key = 'insecure-secret-key'

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

# Vulnerability 1: Server-Side Template Injection (SSTI) leading to RCE
@app.route('/profile/<username>')
def profile(username):
    template = f'''<h1>Profile page for {username}</h1>
                 <p>Welcome to your profile!</p>'''
    return render_template_string(template)

# Vulnerability 2: Cross-Site Scripting (XSS)
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f'''<h1>Search Results</h1>
              <p>Showing results for: {query}</p>
              <a href="/">Back to Home</a>'''

# Vulnerability 3: Server-Side Request Forgery (SSRF)
@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    if url:
        response = requests.get(url)
        return response.text
    return 'Enter URL parameter'

# Vulnerability 4: Local File Inclusion (LFI)
@app.route('/file')
def get_file():
    filename = request.args.get('name', '')
    if filename:
        return send_file(filename)
    return 'Enter file name parameter'

# Vulnerability 5: Open Redirect
@app.route('/redirect')
def unsafe_redirect():
    target = request.args.get('target', '')
    if target:
        return redirect(target)
    return 'Enter target parameter'

if __name__ == '__main__':
    app.run(debug=True)
