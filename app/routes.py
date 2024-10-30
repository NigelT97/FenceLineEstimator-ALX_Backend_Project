# Define Routes and handle Request

from flask import render_template, request, redirect, url_for, Flask, flash, session, Blueprint
import sqlite3
from app.logic import calculated_estimate
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_db
from datetime import datetime
import random


main_route = Blueprint('main_routes', __name__)

@main_route.route('/')
def index():
    user = session.get('user')
    
    flash("Login Successful!", "success")
    return render_template('index.html', user=user)

@main_route.route('/input', methods=['GET', 'POST'])
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

@main_route.route('/results')
def results():
    # Get the result from the query parameters
    fence_result = request.args.get('fence_result')
   
    # Render the results page and display the result
    return render_template('results.html',customer_name, quote_number, date_time=date_time, fence_result=fence_result)

@main_route.route('/register', methods=['GET', 'POST'])
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
            return redirect(url_for('main_routes.register'))
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('main_routes.login'))
    return render_template('register.html')

@main_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username, )).fetchone()
        
        if user and check_password_hash(user['password'], password):
           session['user'] = {'username': username}
           return redirect(url_for('main_routes.index'))
        else:
            flash('Invalid credentials')
            
    return render_template('index.html')