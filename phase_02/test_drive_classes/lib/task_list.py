class TaskList:
    def __init__(self):
        self.task_list = {}
    
    def add(self, task_name, task_details):
        if task_name == '' or task_details == '':
            raise Exception('Please enter both task name and details')
        
        self.task_list[task_name] = task_details
    
    def get_list(self):
        if self.task_list == {}:
            return 'There are no tasks in the list'
        else:
            return self.task_list
    
    def remove_task(self, task_name):
        list_of_task_names = self.task_list.keys()
        if task_name not in list_of_task_names:
            raise Exception('This task does not exist')
        
        del self.task_list[task_name]