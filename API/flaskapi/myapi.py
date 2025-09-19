from flask import Flask, jsonify, request
from classes.mycar import Car

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from your new falsk API'})
@app.route('/api/car', methods=['POST'])
def create_car():
    data = request.get_json()
    try:
     make = data.get['make']
     model = data.get['model']
     year = data.get['year']

     if not all([make, model, year]):
        return jsonify({'error': 'Missing data'}), 400
    
     car = Car(make, model, year)
     return jsonify({'car':car.__dict__}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


if __name__ == '__main__':
    app.run(debug=True) 