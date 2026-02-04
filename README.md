# Welcome to My Select Query
***

## Task
The task is to create a class that can query CSV data efficiently.
The challenge is to correctly parse the CSV, find the right column, and return all rows matching a specific value without errors. Handling CSV strings with multiple rows and columns is the core difficulty.

## Description
I solved the problem by splitting the CSV content into lines and separating the headers from the data rows. I then implemented a where() method that finds the index of the target column, iterates through each row, splits it into columns, compares the target column to the given criteria, and collects all matching rows into a list to return.

## Installation
No special installation is needed beyond Python. Simply save the Python file and import it in your project.
If running from a terminal, you can use:
python my_select_query.py

## Usage
You first create an instance of the class with CSV content as a string:
query = MySelectQuery(csv_content)
Then you can call the where method to search:
results = query.where("name", "Andre Brown")
It will return a list of strings representing all rows where the column matches the criteria.

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
