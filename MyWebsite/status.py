from flask import Flask, render_template, request, redirect, url_for
import threading
import requests
import time

app = Flask(__name__)

# Define your subdomains and their corresponding URLs
subdomains = {
    'Login': 'http://localhost:5000/login',
    'Blogs': 'http://localhost:5000/blogs',
    'Contact Us': 'http://localhost:5000/contactUs',
    'Gallery': 'http://localhost:5000/gallery'
    'Homepage': 'http://localhost:5000/homepage'
}

status_table = []

def check_status():
    global status_table
    while True:
        status_table.clear()
        for name, url in subdomains.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    status = 'UP'
                else:
                    status = 'DOWN'
            except requests.ConnectionError:
                status = 'DOWN'
            status_table.append([name, status])
        time.sleep(60)  # Wait for 1 minute before checking again

@app.route('/')
def index():
    return redirect(url_for('status'))

@app.route('/status')
def status():
    return render_template('status.html', status_table=status_table)

if __name__ == '__main__':
    # Start a separate thread to continuously check the status
    status_checker_thread = threading.Thread(target=check_status)
    status_checker_thread.daemon = True
    status_checker_thread.start()

    # Run the Flask application
    app.run(debug=True)
