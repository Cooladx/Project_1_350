import csv

# This file is mainly to be used for brand table as csv didn't have IDs mainly for it.
# Therefore, there is bound to be a lot of duplicates as id ranges 1 to 114000+ so this function will 
#  clean up a lot of residual copies of the same brand and contain them in one unique id. 
# Function takes csv file path, table_name (configs below) and column mapping from the csv file (configs below)
# Returns SQL inserts to be utilized for the toxins Database. 
def csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping):
    seen_brand_names = set()  # Track unique BrandName to avoid duplicates
    brand_id_counter = 1  # Initialize auto-incrementing BrandId

    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        # Ensure column names match exactly
        for csv_column in column_mapping.keys():
            if csv_column not in headers:
                raise ValueError(f"Column '{csv_column}' not found in CSV file.")

        with open(sql_file_path, mode='w') as sql_file:
            for row in csv_reader:
                brand_name = row['BrandName'].strip()  # Get and clean BrandName

                # Skip if BrandName is already processed
                if brand_name in seen_brand_names:
                    continue  # Skip duplicate BrandNames
                
                seen_brand_names.add(brand_name)  # Mark this BrandName as processed
                
                # Use the auto-incrementing counter as BrandId
                brand_id = brand_id_counter
                brand_id_counter += 1  # Increment for the next unique ID
                
                # Prepare SQL values with the new BrandId and cleaned BrandName
                values = f"'{brand_id}', '{brand_name}'"
                table_columns = ', '.join(column_mapping.values())
                sql_statement = f"INSERT INTO {table_name} ({table_columns}) VALUES ({values});\n"
                sql_file.write(sql_statement)

# ==============================
# CHANGE THESE VARIABLES AS NEEDED
# ==============================
csv_file_path = 'cscpopendata.csv'  # Set the path to the CSV file
sql_file_path = 'temp_insert_statements.sql'  # Set the path to the SQL insert file
table_name = '"Brand"'  # Set the table name KEEP SAME QUOTATIONS
column_mapping = {
    'BrandId': '"Brand_ID"',       # The script will auto-generate BrandId
    'BrandName': '"Brand_Name"'
}  # Specify the mapping from CSV columns to table columns

csv_to_sql(csv_file_path, sql_file_path, table_name, column_mapping)
