import csv

def csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping):
    seen_rows = set()

    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        # Ensure specified columns exist in the CSV
        for csv_column in column_mapping.keys():
            if csv_column not in headers:
                raise ValueError(f"Column '{csv_column}' not found in CSV file.")

        with open(sql_file_path, mode='w') as sql_file:
            for row in csv_reader:
                row_values = tuple(row[csv_column] for csv_column in column_mapping.keys())
                if row_values in seen_rows:
                    continue  # Skip duplicate rows
                seen_rows.add(row_values)
                
                values = ', '.join(["'{}'".format(row[csv_column].replace("'", "''")) for csv_column in column_mapping.keys()])
                table_columns = ', '.join(column_mapping.values())
                sql_statement = "INSERT INTO {} ({}) VALUES ({});\n".format(table_name, table_columns, values)
                sql_file.write(sql_statement)

# ==============================
# CHANGE THESE VARIABLES AS NEEDED
# Copy and paste the generated insert statements into the correct position in the conglomerate insert file
# ==============================
csv_file_path = 'cscpopendata.csv' # set the path to the CSV file
sql_file_path = 'temp_insert_statements.sql' # set the path to the SQL insert file
<<<<<<< Updated upstream
table_name = '"Brand"' # set the table name KEEP SAME QUOTATIONS
column_mapping = {
    'BrandId': '"Brand_ID"',
    'BrandName': '"Brand_Name"'
=======
table_name = '"Product"' # set the table name KEEP SAME QUOTATIONS
column_mapping = {
    'CDPHId': '"Product_ID"',
    'ProductName': '"Product_Name"',
    'CompanyId': '"Company_ID"',
    # 'BrandId': '"Brand_ID"',
    'PrimaryCategoryId': '"Primary_Category_ID"',
    'SubCategoryId': '"Sub_Category_ID"',
>>>>>>> Stashed changes
}  # Specify the mapping from CSV columns to table columns

csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping)