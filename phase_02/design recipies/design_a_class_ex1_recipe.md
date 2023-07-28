# Task Tracker Class Design Recipe

## Describe the problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## Design class interface

```python

class TaskList:
    # User-facing properties:
    # task_list - list
    def __init__(self):
        self.task_list = {}
        # key - task name
        # value - description of task
        pass
    
    def add_task(self, task_name, task_details):
    '''
    Parameters:
        task_name: string
        task_details: string
    returns None
    Side effects:
        adds task name and details to task dict
    '''
    pass
    def get_list(self):
    '''
    Parameters:
        None
    returns list of tasks
    Side effects:
        no side effects
    '''
    pass

    def remove_task(self, task_name):
    '''
    Parameters:
        name of task they want to remove
    returns None
    Side effects:
        remove a key-value pair of the task_name : task from self.task_list dict
    '''
    pass
```

## Tests

```python
'''
Given a task name and task details
add it to dict
task_list = TaskList()
task_list.add('Laundry', 'Do the laundry') -> {'Laundry': 'Do the laundry'}
Given a task name but no details
Raise exception saying to add both task name and details
task_list = TaskList()
task_list.add('Laundry') -> raise exception 'Please add both task name and details'

When get list is called
Return dictionary of tasks
task_list = TaskList()
task_list.add('Laundry', 'Do the laundry')
task_list.get_list() = {'Laundry': 'Do the laundry'}

Given a task name to remove
remove task name and details pair from the dictionary
task_list = TaskList()
task_list.add('Laundry', 'Do the laundry')
task_list.remove_task('Laundry') -> {}

Given an empty task list
return message saying that there are no tasks
task_list = TaskList()
task_list.get_list() -> 'There are no tasks in the list'

When given a task to remove that does not exist in list
return error message saying task does not exist
task_list = TaskList()
task_list.remove_task('shopping') -> 'This task does not exist'
'''
```
