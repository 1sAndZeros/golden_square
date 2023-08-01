class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if task == '':
            raise Exception('No task given')
        self.task = task
        self.complete = False

    def mark_complete(self):
        if self.complete == True:
            raise Exception('Task is already complete')
        self.complete = True