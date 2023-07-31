from lib.todo import *
import pytest

# Test task is added correctly on initialisation
def test_task_added_correctly():
    todo_1 = Todo('Take a bath')
    assert todo_1.task == 'Take a bath'

# Test when task is an empty 
# string, should raise Exception
def test_task_as_empty_string():
    with pytest.raises(Exception) as e:
        todo_1 = Todo('')
    error_message = str(e.value)
    assert error_message == 'No task given'

# Test task is initially not complete
def test_task_complete_initially_false():
    todo_1 = Todo('Take a bath')
    assert todo_1.complete == False

# Test task is marked as complete correctly
def test_task_is_marked_complete():
    todo_1 = Todo('Take a bath')
    todo_1.mark_complete()
    assert todo_1.complete == True

# Raise Exception if task is already complete
def test_task_is_already_complete():
    todo_1 = Todo('Take a bath')
    todo_1.mark_complete()
    with pytest.raises(Exception) as e:
        todo_1.mark_complete()
    error_message = str(e.value)
    assert error_message == 'Task is already complete'