import csv
import re

def extract_brand_ids(sql_file_path):
    brand_ids = {}
    with open(sql_file_path, 'r') as sql_file:
        for line in sql_file:
            match = re.search(r"INSERT INTO \"Brand\" \(\"Brand_ID\", \"Brand_Name\"\) VALUES \('(\d+)', '([^']*)'\);", line)
            if match:
                brand_id = match.group(1)
                brand_name = match.group(2).replace("''", "'")
                brand_ids[brand_name] = brand_id
    return brand_ids

def filter_brand_ids(csv_file_path, brand_ids):
    filtered_brand_ids = {}
    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            brand_name = row['BrandName']
            if brand_name in brand_ids:
                filtered_brand_ids[brand_name] = brand_ids[brand_name]
    return filtered_brand_ids

def csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping, filtered_brand_ids):
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
                # Replace BrandName with Brand_ID
                if 'BrandName' in row and 'BrandId' in column_mapping:
                    brand_name = row['BrandName']
                    if brand_name in filtered_brand_ids:
                        row['BrandId'] = filtered_brand_ids[brand_name]
                    else:
                        continue  # Skip rows with unknown brands

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
brands_sql_path = 'brands.sql' # set the path to the brands SQL file

# Extract Brand IDs from brands.sql
brand_ids = extract_brand_ids(brands_sql_path)

# Filter Brand IDs based on the brands present in the CSV file
filtered_brand_ids = filter_brand_ids(csv_file_path, brand_ids)

# Update column_mapping to include BrandId
column_mapping = {
    'CDPHId': '"Product_ID"',
    'ProductName': '"Product_Name"',
    'CompanyId': '"Company_ID"',
    'BrandId': '"Brand_ID"',
    'PrimaryCategoryId': '"Primary_Category_ID"',
    'SubCategoryId': '"Sub_Category_ID"',
}  # Specify the mapping from CSV columns to table columns

table_name = '"Product"' # set the table name KEEP SAME QUOTATIONS

csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping, filtered_brand_ids)