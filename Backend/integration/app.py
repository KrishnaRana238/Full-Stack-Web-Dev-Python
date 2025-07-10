from flask import Flask, render_template, redirect, url_for, flash, request, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'learnonline_secret_key_2024'  # Strong secret key for sessions

# Simple user storage (in production, use a database)
users_db = {}
user_data = {}

# Landing page route
@app.route('/')
def landing():
    return render_template('landingpage.html')

# Main dashboard route (requires login)
@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    
    user_email = session['user_email']
    user_name = session.get('user_name', 'Student')
    return render_template('index.html', user_name=user_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        
        email = data.get('email')
        password = data.get('password')
        
        # Simple authentication (in production, use proper password hashing)
        if email in users_db and users_db[email]['password'] == password:
            session['user_email'] = email
            session['user_name'] = users_db[email]['name']
            
            if request.is_json:
                return jsonify({'success': True, 'redirect': url_for('dashboard')})
            else:
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
        else:
            if request.is_json:
                return jsonify({'success': False, 'message': 'Invalid email or password'})
            else:
                flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() if request.is_json else request.form
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    
    # Validation
    if not all([name, email, password, confirm_password]):
        return jsonify({'success': False, 'message': 'All fields are required'})
    
    if password != confirm_password:
        return jsonify({'success': False, 'message': 'Passwords do not match'})
    
    if email in users_db:
        return jsonify({'success': False, 'message': 'Email already registered'})
    
    # Store user (in production, hash the password)
    users_db[email] = {
        'name': name,
        'password': password,
        'applied_courses': []
    }
    
    if request.is_json:
        return jsonify({'success': True, 'message': 'Account created successfully'})
    else:
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('landing'))

@app.route('/courses')
def courses():
    if 'user_email' not in session:
        flash('Please log in to access courses.', 'warning')
        return redirect(url_for('login'))
    return render_template("courses.html")

@app.route('/applied')
def applied():
    if 'user_email' not in session:
        flash('Please log in to access applied courses.', 'warning')
        return redirect(url_for('login'))
    
    user_email = session['user_email']
    applied_courses = users_db.get(user_email, {}).get('applied_courses', [])
    return render_template("appliedcourse.html", applied_courses=applied_courses)

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/settings')
def settings():
    if 'user_email' not in session:
        flash('Please log in to access settings.', 'warning')
        return redirect(url_for('login'))
    
    user_email = session['user_email']
    user_info = users_db.get(user_email, {})
    return render_template("setting.html", user_info=user_info)

@app.route('/apply_course', methods=['POST'])
def apply_course():
    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in first'})
    
    data = request.get_json()
    course_title = data.get('course')
    
    user_email = session['user_email']
    if user_email in users_db:
        if 'applied_courses' not in users_db[user_email]:
            users_db[user_email]['applied_courses'] = []
        
        # Check if course is already applied
        if course_title not in users_db[user_email]['applied_courses']:
            users_db[user_email]['applied_courses'].append(course_title)
            return jsonify({'success': True, 'message': 'Course applied successfully!'})
        else:
            return jsonify({'success': False, 'message': 'Already applied for this course'})
    
    return jsonify({'success': False, 'message': 'User not found'})

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in first'})
    
    data = request.get_json()
    user_email = session['user_email']
    
    if user_email in users_db:
        # Update user information
        if 'name' in data:
            users_db[user_email]['name'] = data['name']
            session['user_name'] = data['name']
        if 'phone' in data:
            users_db[user_email]['phone'] = data['phone']
        if 'bio' in data:
            users_db[user_email]['bio'] = data['bio']
        
        return jsonify({'success': True, 'message': 'Profile updated successfully!'})
    
    return jsonify({'success': False, 'message': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
