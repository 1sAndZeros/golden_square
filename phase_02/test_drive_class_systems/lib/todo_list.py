class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        for item in self.todos:
            if todo.task == item.task:
                raise Exception("To do has already been added")
        self.todos.append(todo)

    def incomplete(self):
        return [todo for todo in self.todos if todo.complete == False]

    def complete(self):
        return [todo for todo in self.todos if todo.complete == True]

    def give_up(self):
        for todo in self.todos:
            if todo.complete == False:
                todo.complete = True