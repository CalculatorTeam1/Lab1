from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    pass
    # TODO: Implement all maths operations, handle received data, send response


if __name__ == '__main__':
    app.run(debug=True)
