# table search filter demo

### Purpose
using pytest and pytest-bdd to test the a table filter
<https://www.seleniumeasy.com/test/table-search-filter-demo.html>

### Setup
`pipenv install`

### Test Execution
###### to run all
`python -m pytest `
###### to run the scenario based on task name
`python -m pytest -k "task"`
###### to run the scenario based on assignee name
`python -m pytest -k "assignee"`
###### to run the scenario based on status 
`python -m pytest -k "status"`
###### to run the scenario based on unavailable entries
`python -m pytest -k "entries"`


