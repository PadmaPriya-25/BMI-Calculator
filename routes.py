# app/routes.py
from flask import render_template, request
from app import app

def calculate_bmi(weight, height, units):
    bmi = weight / (height ** 2)
    return bmi
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
@app.route('/')
@app.route('/bmi_form')
def bmi_form():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    units = request.form['units']
    if units == 'imperial':
        height *= 0.3048
        weight *= 0.453592
    bmi = calculate_bmi(weight, height, units)
    bmi_category = get_bmi_category(bmi)
    return render_template('result.html', bmi=bmi, category=bmi_category)
