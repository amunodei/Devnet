from flask import Flask, jsonify, request, Response
from classes.mycar import Car
from functools import wraps


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

###
#auth logic 
###

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

def check_auth(username, password):
    return username == VALID_USERNAME and password == VALID_PASSWORD

def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/protected')
@requires_auth  
def protected():
    return jsonify({"You have accessed a protected resource"})


###
#stop auth logic
###



if __name__ == '__main__':
    app.run(debug=True) 