from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the Flask application
app = Flask(__name__)

# IMPORTANT: Set a secret key for session management. 
# Replace 'your_secret_key' with a long, random string!
app.secret_key = 'your_secret_key_for_security' 

# --- Routes for all sections to work ---

# 1. The Login Route (The 'Logging Area')
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request is a POST (user submitted the form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # --- Basic Validation (Replace with real database check!) ---
        if username == 'admin' and password == 'password123':
            # Set a session variable to mark the user as logged in
            session['logged_in'] = True
            session['username'] = username
            
            # Redirect to the main index page
            return redirect(url_for('index'))
        else:
            # Display an error message on the login page
            return render_template('login.html', error='Invalid credentials. Try "admin" and "password123".')

    # If the request is a GET (user just navigated to /login)
    return render_template('login.html')

# 2. The Main Page Route (Only accessible if logged in)
@app.route('/')
def index():
    # Check if the user is logged in
    if 'logged_in' in session and session['logged_in']:
        # This section works!
        return render_template('index.html', username=session['username'])
    else:
        # If not logged in, redirect them back to the login page
        return redirect(url_for('login'))

# 3. The Logout Route
@app.route('/logout')
def logout():
    # Remove the session variable, effectively logging the user out
    session.pop('logged_in', None)
    session.pop('username', None)
    
    # Redirect back to the login page
    return redirect(url_for('login'))

# --- Run the application ---
if __name__ == '__main__':
    # Setting debug=True restarts the server automatically on code changes
    app.run(debug=True)
