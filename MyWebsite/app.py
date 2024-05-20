from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        return render_template('homepage.html', name=name, city=city)
    return render_template('login.html')

@app.route('/blogs')
def blogs():
    # You can fetch blog data from a database here
    return render_template('blogs.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/gallery')
def gallery():
    # You can fetch gallery images from a database here
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
