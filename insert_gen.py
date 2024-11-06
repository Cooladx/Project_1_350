import csv

def csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping):
    seen_rows = set()

    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        for csv_column in column_mapping.keys():
            if csv_column not in headers:
                raise ValueError(f"Column '{csv_column}' not found in CSV file.")

        with open(sql_file_path, mode='w') as sql_file:
            for row in csv_reader:
                row_values = tuple(row[csv_column] for csv_column in column_mapping.keys())
                if row_values in seen_rows:
                    continue 
                seen_rows.add(row_values)
                
                values = ', '.join([f"'{row[csv_column]}'" for csv_column in column_mapping.keys()])
                table_columns = ', '.join(column_mapping.values())
                sql_statement = f"INSERT INTO {table_name} ({table_columns}) VALUES ({values});\n"
                sql_file.write(sql_statement)

# ==============================
# CHANGE THESE VARIABLES AS NEEDED
# Copy and paste the generated insert statements into the correct position in the conglomerate insert file
# ==============================
csv_file_path = 'cscpopendata.csv' # set the path to the CSV file
sql_file_path = 'temp_insert_statements.sql' # set the path to the SQL insert file
table_name = '"Primary_Category"' # set the table name KEEP SAME QUOTATIONS
column_mapping = {
    'PrimaryCategoryId': '"Category_ID"',
    'PrimaryCategory': '"Category_Name"'
}  # Specify the mapping from CSV columns to table columns

csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping)