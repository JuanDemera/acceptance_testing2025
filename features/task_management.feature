Feature: Manage tasks in the to-do list

  Scenario: Adding a new task
    Given I have a new to-do list
    When I add a task with title "Buy groceries"
    Then the task "Buy groceries" should be in the to-do list

  Scenario: Listing all tasks
    Given I have a to-do list with tasks
    When I list the tasks
    Then I should see "Buy groceries"

  Scenario: Marking a task as completed
    Given I have a task "Buy groceries" in the to-do list
    When I mark the task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  Scenario: Clearing all tasks
    Given I have tasks in the to-do list
    When I clear the to-do list
    Then the to-do list should be empty

  Scenario: Updating an existing task
    Given I have a task "Buy groceries" in the to-do list
    When I update the task "Buy groceries" title to "Buy milk"
    Then the task "Buy milk" should be in the to-do list

  Scenario: Trying to mark a non-existent task as completed
    Given I have tasks in the to-do list
    When I try to mark a non-existent task as completed
    Then I should see an error message "Task not found"