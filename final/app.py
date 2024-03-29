import requests
from flask import Flask, render_template, request
import random
from weather import get_weather
from generate_password import generate_password
from motivation import motivational_quotes
from dice import roll_dice
from generate_fibonacci import generate_fibonacci
from zodiac import get_zodiac_sign
from calculator import calculate
from palindrome import is_palindrome
from holiday import get_holiday

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zodiac', methods=['GET', 'POST'])
def zodiac_sign():
    if request.method == 'POST':
        month = int(request.form['month'])
        day = int(request.form['day'])
        sign = get_zodiac_sign(month, day)
        return render_template('zodiac_result.html', sign=sign)
    else:
        return render_template('zodiac_form.html')

@app.route('/holiday', methods=['GET'])
def holiday():
    holidays = get_holiday()
    return render_template('holidays.html', holidays=holidays)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_info = get_weather(city)
        return render_template('weather.html', weather=weather_info)
    else:
        return render_template('weather_form.html')

@app.route('/motivation')
def motivation():
    quote = random.choice(motivational_quotes)
    return render_template('motivation.html', quote=quote)

@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        word = request.form['word']
        result = is_palindrome(word)
        return render_template('palindrome_result.html', word=word, result=result)
    else:
        return render_template('palindrome_form.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        terms = int(request.form['terms'])
        fib_series = generate_fibonacci(terms)
        return render_template('fibonacci_result.html', terms=terms, fib_series=fib_series)
    else:
        return render_template('fibonacci_form.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = calculate(operation, num1, num2)
        return render_template('calculator_result.html', operation=operation, num1=num1, num2=num2, result=result)
    else:
        return render_template('calculator_form.html')

@app.route('/generate_password', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        memorable_word = request.form['memorable_word'].strip().lower()
        birth_year = request.form['birth_year'].strip()
        favorite_color = request.form['favorite_color'].strip().lower()
        lucky_number = request.form['lucky_number'].strip()

        password = generate_password(memorable_word, birth_year, favorite_color, lucky_number)
        return render_template('password_result.html', password=password)
    else:
        return render_template('password_form.html')

@app.route('/dice')
def dice():
    dice_roll = roll_dice()
    return render_template('dice.html', roll=dice_roll)

if __name__ == '__main__':
    app.run(debug=True)
