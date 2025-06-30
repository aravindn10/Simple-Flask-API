from flask import Flask,request

app = Flask(__name__)

todos=[

]

@app.route("/health")
def hello_world():
    return {
        "status": "Up"
    }

@app.route("/todos", methods=['POST','GET'])
def get_all_todos():
    if request.method == 'POST':
        todo = {
            "message": request.json["todo"],
            "isCompleted": False
        }
        todos.append(todo)
        return {
            "message": "Todo Added"
        }
    if request.method == 'GET':
        return {
            "data": todos
        }
    
@app.route("/todos/complete", methods=['POST'])
def todo_completed():
    i = int(request.json["index"])
    todos[i]["isCompleted"] = True
    return {
        "message": "Todo Completed",
    }

