from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy Groceries',
        'descrption': u'Milk, Cheese, Pizza, Fruits',
        'done': False
    },

    {
        'id': 2,
        'title': u'Learn Python',
        'descrption': u'Need to find a good python tutorial on web',
        'done': False
    },
]
 
contact = {

    'id': tasks[-1]['id'] + 1,

    'Name': request.json['Name'],

    'Contact': request.json.get('Contact', ""),

    'done': False
}

@app.route("/")

def hello_world():
     return "Hello World!" 
     
@app.route("/add-data", methods=["POST"]) 

def add_task(): 
    if not request.json: 
        return jsonify({ 
            "status":"error",
            "message": "Please provide the data!" 
            },400) 
@app.route("/get-data") 

def add_task(): 
    return jsonify({ "data" : tasks }) 
    if (__name__ == "__main__"): 
        app.run(debug=True)