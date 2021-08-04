from flask import Flask,jsonify,request 

app=Flask(__name__)
@app.route("/")

def hello():
    return "Ninad"

tasks=[
    {
        "id":1,
        "name":"Rohit",
        "contact":1438765543,
        "done":False
    },
   {
        "id":2,
        "name":"Raju",
        "contact":1234123465,
        "done":False
    } 
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)


    task={

        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({

        "status":"success",
        "message":"task added succesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run()