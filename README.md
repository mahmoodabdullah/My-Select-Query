# My-Select-Query
I solved the problem by splitting the CSV content into lines and separating the headers from the data rows. I then implemented a where() method that finds the index of the target column, iterates through each row, splits it into columns, compares the target column to the given criteria, and collects all matching rows into a list to return.
