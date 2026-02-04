import csv
from io import StringIO

class MySelectQuery:
    def __init__(self, csv_content):
        self.csv_content = csv_content
        self.lines = csv_content.strip().split("\n")
        self.headers = self.lines[0].split(",")
        self.rows = self.lines[1:]

    def where(self, column_name, criteria):
        index = self.headers.index(column_name)
        result = []
        for row in self.rows:
            column = row.split(',')
            if column[index] == criteria:
                result.append(row)
        return result


    
