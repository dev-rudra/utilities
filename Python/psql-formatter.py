#!/usr/bin/python3

import argparse

# Command-line arguments
helper = argparse.ArgumentParser(description="Convert data from a text file to PSQL format.")
helper.add_argument("-i", "--input", help="Input file path (e.g., input.txt)", required=True)
helper.add_argument("-o", "--output", help="Output file path (e.g., output.sql)", required=True)
helper.add_argument("--table", help="Table name for the SQL statements", required=True)

# Parse the command-line arguments
args = helper.parse_args()

# Get the input and output file paths from the parsed arguments
inputFile = args.input
outputFile = args.output
table_name = args.table

# Initialize an empty list to store the INSERT statements
sql_statements = []

with open(inputFile, 'r') as f:
    lines = f.readlines()

# Extract column names from the first line
columns = lines[0].strip().split('|')

# Initialize an empty list to store the VALUES
values = []

# Process the data rows starting from the second line
for line in lines[1:]:
    row_values = line.strip().split('|')

    # Check if the number of values matches the number of columns
    if len(row_values) == len(columns):
        # Format the values and add them to the VALUES list
        formatted_values = []
        for value in row_values:
            # Check if the value is an integer or a PostgreSQL keyword
            if value.isdigit() or value in ['CURRENT_DATE', 'NULL']:
                formatted_values.append(value)
            else:
                formatted_values.append(f"'{value.strip()}'")
        values.append(', '.join(formatted_values))

# Create a single INSERT statement with all the VALUES
if values:
    insert_values = '),\n('.join(values)
    insert_statement = (
        f"INSERT INTO {table_name} ({', '.join(columns)})\n"
        f"VALUES\n"
        f"({insert_values});"
    )
    sql_statements.append(insert_statement)

with open(outputFile, 'w') as sql_file:
    sql_file.write('\n'.join(sql_statements))

print(f"SQL Statements have been written to {outputFile} 😆.")
