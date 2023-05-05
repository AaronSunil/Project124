from flask import Flask, jsonify, request
app = Flask(__name__)

List = [
    {
        'id': 1,
        'Contact': u'85564595600',
        'Name': u'Raju',
        'done': False
    },

    {
        'id': 2,
        'Contact': u'7826264554',
        'Name': u'Rahul',
        'done': False
    },
]
 
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
    
    contact = {

    'id': List[-1]['id'] + 1,

    'Name': request.json['Name'],

    'Contact': request.json.get('Contact', ""),

    'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact Added Successfully"
    })


@app.route("/get-data") 

def add_task(): 
    return jsonify({ "data" : List }) 
    if (__name__ == "__main__"): 
        app.run(debug=True)