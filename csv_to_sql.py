import csv
import sys
import os



def csv_to_mysql(file_path):
    table_name = file_path.split('.')[0]

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Get the header

        create_table_statement = f"CREATE TABLE {table_name} (\n"
        create_table_statement += ', '.join(f'{col} VARCHAR(255)' for col in header)
        create_table_statement += '\n);'

        sql_file = "./data/"+table_name+".sql"

        with open(sql_file, 'w') as file:
            file.write(create_table_statement)

            for row in csv_reader:
                insert_statement = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ("
                insert_statement += ', '.join(f"'{value}'" for value in row)
                insert_statement += ');\n'  # Add a newline character after each insert statement
                file.write(insert_statement)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a csv file as a parameter")
        sys.exit(1)

    directory_path = './data/'
    os.makedirs(directory_path, exist_ok=True)
    
    csv_file_path = sys.argv[1]
    csv_to_mysql(csv_file_path)
