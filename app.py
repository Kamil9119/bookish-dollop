from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Simulated in-memory storage for numbers and SMS
numbers_db = []
sms_db = {}

# Generate a random phone number
def generate_phone_number():
    country_code = "+1"  # USA for demo
    area_code = random.randint(100, 999)
    first_part = random.randint(100, 999)
    second_part = random.randint(1000, 9999)
    return f"{country_code}{area_code}{first_part}{second_part}"

# Generate a 6-digit OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# Initialize some numbers
for _ in range(5):  # Generate 5 numbers
    number = generate_phone_number()
    numbers_db.append(number)
    sms_db[number] = []  # Empty SMS list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/numbers', methods=['GET'])
def get_numbers():
    return jsonify(numbers_db)

@app.route('/api/sms/<number>', methods=['GET'])
def get_sms(number):
    # Simulate receiving an SMS with OTP
    if number in sms_db and random.random() < 0.7:  # 70% chance of new SMS
        otp = generate_otp()
        sms = f"Verification Code: {otp}"
        sms_db[number].append(sms)
    return jsonify(sms_db.get(number, []))

if __name__ == '__main__':
    app.run(debug=True)