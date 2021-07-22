from flask import Flask,jsonify,request
app=Flask(__name__)
tasks = [
     {'id':1,
    'Contact': "9030434342",
    'Name': "kavitha"
    'done': False
    },
    {'id':2,
    'Contact': "9724901253",
    'Name': "Vasu"
    'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    contact = {
        'id':tasks[-1]['id'] + 1
        'Name': request.json['Name'],
        'Contact':request.json.get('Contact,"'),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })

if(__name__ == "__main__"):
    app.run(debug="True")