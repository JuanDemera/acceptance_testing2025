from behave import given, when, then
from todo import Task, ToDoList

@given("I have a new to-do list")
def step_new_list(context):
    context.todo = ToDoList()

@given("I have a to-do list with tasks")
@given("I have tasks in the to-do list")
def step_list_with_tasks(context):
    context.todo = ToDoList()
    context.todo.add_task(Task("Buy groceries"))

@given('I have a task "{title}" in the to-do list')
def step_given_task_exists(context, title):
    if not hasattr(context, 'todo'):
        context.todo = ToDoList()
    context.todo.add_task(Task(title))

@when('I add a task with title "{title}"')
def step_add_task(context, title):
    context.todo.add_task(Task(title))

@then('the task "{title}" should be in the to-do list')
@then('I should see "{title}"')
def step_check_task_exists(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title in titles, f'Task "{title}" not found in the to-do list.'

@when("I list the tasks")
def step_list_tasks(context):
    context.task_list = context.todo.list_tasks()

@when('I mark the task "{title}" as completed')
def step_mark_completed(context, title):
    context.message = context.todo.mark_task_completed(title)

@then('the task "{title}" should be marked as completed')
def step_check_completed(context, title):
    for task in context.todo.tasks:
        if task.title == title:
            assert task.completed is True, f'Task "{title}" is not completed.'
            return
    assert False, f'Task "{title}" not found'

@when("I clear the to-do list")
def step_clear_list(context):
    context.todo.clear_all_tasks()

@then("the to-do list should be empty")
def step_check_empty(context):
    assert len(context.todo.list_tasks()) == 0, "To-do list is not empty."

@when('I update the task "{old}" title to "{new}"')
def step_update_task(context, old, new):
    context.todo.update_task_title(old, new)

@then('the updated task "{title}" should be in the to-do list')
def step_check_updated_task(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title in titles, f'Updated task "{title}" not found'

@when("I try to mark a non-existent task as completed")
def step_mark_nonexistent(context):
    context.message = context.todo.mark_task_completed("This task does not exist")

@then('I should see an error message "{msg}"')
def step_error_message(context, msg):
    assert context.message == msg, f'Expected "{msg}", but got "{context.message}"'
