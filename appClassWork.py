
from flask import Flask, request, jsonify
from environment import env
from pymongo import MongoClient

client = MongoClient(env["MONGO_URI"])

print(env["MONGO_URI"])

app = Flask(__name__)

db = client.test

logs1 = db.logs1

# JS EQ: const app = express()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Hello World!"

@app.route('/logs', methods=['GET'])
def get_logs():
    result = logs1.find()
    print(result)
    return jsonify([{'_id': str(log['_id']), 'message': log['message']} for log in result]) 

@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    result = logs1.insert_one({'message': data['message']})
    return str(result.inserted_id), 201

# @app.route('/example/<id>/<wow>', methods=['GET'])
# def param_example(id, wow):
#     print(id, wow)
#     return id

# @app.route('/whatever', methods=["POST"])
# def whatever():
#     data = request.get_json()
#     print(data)
#     return data

# @app.route('/hello/<name>', methods=['GET'])
# def hello(name):
#     return (f"Hello {name}")

# @app.route('/add<num1>/<num2>', methods=['GET'])
# def sum(num1, num2):
#     sum = {(int(num1)+int(num2))}
#     return sum

# @app.route('/greet/<name>', methods=['GET'])
# def greet(name):
#     names = [
#         "Steven",
#         "Dominic",
#         "Dawn",
#         "Fede",
#         "Matthew",
#         "Victor",
#         "Brian",
#         "Fuzzy",
#         "Gowri",
#         "Mitchell",
#         "Hilal",
#         "Justin",
#         "Darya",
#         "Andrew",
#     ]
#     if name in names:
#         return(f"Hello {name}")
#     else:
#         return (f"Hello stranger")

if __name__ == '__main__':
    app.run(debug=True)