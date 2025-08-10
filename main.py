from fastapi import FastAPI

app = FastAPI()

to_do_list = [
    {"todo_id" : 1, "todo_name" : "Sport", "todo_description" : "Go to the gym"},
    {"todo_id" : 2, "todo_name" : "Meditate", "todo_description" : "Meditate for 20 minutes"},
    {"todo_id" : 3, "todo_name" : "Gaming", "todo_description" : "Play a video game"},
    {"todo_id" : 4, "todo_name" : "Tournament", "todo_description" : "Play a basketball tournament"},
    {"todo_id" : 5, "todo_name" : "Cinema", "todo_description" : "Watch a new movie"},

 ]

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/todo/{todo_id}")
def get_item(todo_id: int):
    for todo in to_do_list:
        if todo["todo_id"] == todo_id:
            return todo
    


    return {"error" : "Item not found"}


        



