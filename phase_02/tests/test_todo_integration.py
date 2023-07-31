from lib.todo import *
from lib.todo_list import *
import pytest

"""
Make a todo instance 
Add to the to do list
Check it's been added
"""
def test_check_adding_one_to_do():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    assert todo_list.todos == [todo_1]

"""
Make two todo instances 
Add to the to do list
Check it's been added
"""
def test_check_adding_two_to_do():
    todo_1 = Todo(task="Take a bath")
    todo_2 = Todo(task="Take a shower")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.todos == [todo_1, todo_2]

"""
Make two todo instances 
Add to the to do list
Add another todo with the same name
Should raise Exception
"""
def test_check_adding_the_same_todo():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a bath")
    with pytest.raises(Exception) as e:
        todo_list.add(todo_2)
    error_message = str(e.value)
    assert error_message == "To do has already been added"

"""
Make two todo instances 
Add to the to do list
Mark one as complete
Return one incomplete task
"""
def test_check_one_incomplete_task():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.incomplete() == [todo_2]

"""
Make two todo instances 
Add to the to do list
Mark both as complete
Return no tasks
"""
def test_no_tasks_incomplete():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todo_list.incomplete() == []

"""
Make two todo instances 
Add to the to do list
Mark none as complete
Return all tasks
"""
def test_no_tasks_complete():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]


"""
Add two todo instances
Add to todo list
Mark one as complete
Return one completed task
"""
def test_one_complete_task():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]

"""
Add two todo instances
Add to todo list
Mark none as complete
Return no completed task
"""
def test_no_completed_tasks():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    assert todo_list.complete() == []

"""
Add two todo instances
Add to todo list
Mark all as complete
Return all completed task
"""
def test_all_completed_tasks():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todo_list.complete() == [todo_1, todo_2]

"""
Add two todo instances
Add to todo list
Mark both tasks as complete
"""
def test_give_up_two_tasks():
    todo_1 = Todo(task="Take a bath")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_2 = Todo(task="Take a shower")
    todo_list.add(todo_2)
    todo_list.give_up() 
    assert todo_list.complete() == [todo_1, todo_2]
    assert todo_list.incomplete() == []
