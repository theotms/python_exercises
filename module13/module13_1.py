from flask import Flask, jsonify

app = Flask(__name__)

def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "Prime": prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
