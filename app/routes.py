# Define Routes and handle Request

from flask import render_template, request, redirect, url_for, Flask, flash, session
import sqlite3
from app import app
from app.logic import calculated_estimate
from werkzeug.security import generate_password_hash, check_password_hash


def get_db():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # Get user Input
        fence_perimeter = request.form.get('fence_perimeter')
        fence_height = request.form.get('fence_height')
        perimeter_corners = request.form.get('perimeter_corners')
        fence_type = request.form.get('fence_type')
        fence_wire_thickness = request.form.get('fence_wire_thickness')
        fence_appeture = request.form.get('fence_appeture')
        fence_overhang_request = request.form.get('fence_overhang_request')
        fence_overhang_type = request.form.get('fence_overhang_type')
        
        # Convert inputs into correct data types
        fence_perimeter = float(fence_perimeter.strip())
        perimeter_corners = float(perimeter_corners.strip())
        fence_height = str(fence_height)
        fence_type = str(fence_type)
        fence_wire_thickness = str(fence_wire_thickness)
        fence_appeture = str(fence_appeture)
        fence_overhang_request = str(fence_overhang_request)
        fence_overhang_type = str(fence_overhang_type)
        
        # Perform Calculations
        fence_result = calculated_estimate(fence_perimeter, fence_height, perimeter_corners, fence_type,fence_wire_thickness, fence_appeture, fence_overhang_request, fence_overhang_type)
        
        # Redirect to the results page, passing the result
        return render_template('results.html', fence_result=fence_result)
    return render_template('input_form.html')

@app.route('/results')
def results():
    # Get the result from the query parameters
    fence_result = request.args.get('fence_result')
    
    # Render the results page and display the result
    return render_template('results.html', fence_result=fence_result)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        
        conn = get_db()
        try:
            conn.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, hashed_password, email))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Username already exists')
            return redirect(url_for('register'))
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username, )).fetchone()
        
        if user and check_password_hash(user['password'], password):
           flash('Successful Login')
           return redirect(url_for('index'))
        else:
            flash('Invalid credenyials')
            
    return render_template('index.html')