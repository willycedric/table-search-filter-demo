@table
#noinspection GherkinScenarioToScenarioOutline
Feature: Table filter

   As a user when in enter a search criteria in the 
   task table's filter the resulting result(s) should match 
   the search criteria

    Background: 
        Given the task table is displayed
    @task
    Scenario: Using task name as search criteria
    When i enter the task name as search <criteria>
    Then the table should contains only the task matching the search <criteria> name
    Examples:Available
        | criteria |
        |Wireframes	|
        |Landing Page|

    @assignee
    Scenario: Using Assignee name as search criteria
    When i enter the assignee name as search <criteria>
    Then the table should contains only the task matching the search <criteria> name
    Examples:Assignee
        | criteria |
        |John Smith	|
        |Emily John |
        
    @status
   Scenario: Using status as search criteria
    When i enter the task status as search <criteria>
    Then the table should contains the tasks matching the <criteria> with the correct <occurrence>
    Examples:Assignee
        | criteria | occurrence|
        |in progress | 3      |
        |failed qa   |   2    |
        |completed   |  1     |

      @unavailable
    Scenario: Using an unavailabe search criteria
      When i enter an unavailable search <criteria>
      Then the table should contains the message "No results found"
      Examples: Unavailable
        |criteria|
        |pommery |
        |xxx000x |