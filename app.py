
from flask import Flask, request, jsonify
from environment import env
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(env["MONGO_URI"])

print(env["MONGO_URI"])

app = Flask(__name__)

db = client.test

todos = db.todos

# JS EQ: const app = express()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return "Hello World!"

@app.route('/todos', methods=['GET'])
def get_todos():
    result = todos.find()
    print(result)
    return jsonify([{'_id': str(todo['_id']), 'title': str(todo['title']), 'body': str(todo['body']), 'completed': bool(todo['completed'])} for todo in result]) 

@app.route('/todos/<id>', methods=['GET'])
def get_todo(id):
    print("My id", id)
    result = todos.find_one({"_id": ObjectId(id)})
    print("Results", result)
    return jsonify([{'_id': str(result['_id']), 'title': str(result['title']), 'body': result['body'], 'completed': bool(result['completed'])}]) 

@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    print("My id", id)
    data = request.get_json()
    print("My  update data", data)
    result = todos.find_one_and_update({"_id": ObjectId(id)}, {"$set": {'title': data['title'], 'body': data['body'], 'completed': data['completed']}}, upsert=False)
    print("update result", result)
    return jsonify([{'_id': str(result['_id']), 'title': str(result['title']), 'body': result['body'], 'completed': bool(result['completed'])}])

@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    print("My id", id)
    todos.delete_one({"_id": ObjectId(id)})
    return "deleted"

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    result = todos.insert_one({'title': data['title'], 'body': data['body'], 'completed': data['completed'] })
    return str(result.inserted_id), 201

if __name__ == '__main__':
    app.run(debug=True)