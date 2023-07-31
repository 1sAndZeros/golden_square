from lib.task_list import *
import pytest

def test_add_task_name_task_details():
    tasks = TaskList()
    tasks.add('Laundry', 'Do the laundry')
    assert tasks.task_list == {'Laundry': 'Do the laundry'}

def test_add_task_name_but_no_details():
    tasks = TaskList()
    with pytest.raises(Exception) as error:
        tasks.add('Laundry', '')
    error_message = str(error.value)
    assert error_message == 'Please enter both task name and details'

def test_get_list():
    tasks = TaskList()
    tasks.add('Laundry', 'Do the laundry')
    tasks.add('Shopping', 'Buy eggs and milk')
    assert tasks.get_list() == {'Laundry': 'Do the laundry', 'Shopping': 'Buy eggs and milk'}

def test_remove_task():
    tasks = TaskList()
    tasks.add('Laundry', 'Do the laundry')
    tasks.add('Shopping', 'Buy eggs and milk')
    tasks.remove_task('Laundry')
    assert tasks.task_list == {'Shopping': 'Buy eggs and milk'}

def test_get_list_with_empty_list():
    tasks = TaskList()
    assert tasks.get_list() == 'There are no tasks in the list'

def test_remove_nonexistant_task():
    tasks = TaskList()
    tasks.add('Laundry', 'Do the laundry')
    with pytest.raises(Exception) as error:
        tasks.remove_task('shopping')
    error_message = str(error.value)
    assert error_message == 'This task does not exist'