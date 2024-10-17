# Define Routes and handle Request

from flask import render_template, request, redirect, url_for
from app import app
from app.logic import calculated_estimate

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