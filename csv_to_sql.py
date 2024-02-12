import csv
import sys
import os

def infer_data_types(file_path):
    with open(file_path, 'r') as csv_file:
        csv_sniffer = csv.Sniffer()
        sample_data = csv_file.read(1024) 
        dialect = csv_sniffer.sniff(sample_data)
        csv_file.seek(0) 

        csv_reader = csv.reader(csv_file, dialect)
        header = next(csv_reader) 

        # Infer column data types
        type_mapping = {}
        for col in header:
            type_mapping[col] = 'VARCHAR(255)'  

        for row in csv_reader:
            for col, value in zip(header, row):
                try:
                    int(value)
                    type_mapping[col] = 'INT'
                except ValueError:
                    try:
                        float(value)
                        type_mapping[col] = 'NUMERIC' 
                    except ValueError:
                        pass 

    return type_mapping

def csv_to_mysql(file_path):
    table_name = file_path.split('.')[0]
    type_mapping = infer_data_types(file_path)

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader) 

        create_table_statement = f"CREATE TABLE {table_name} ("
        create_table_statement += ', '.join(f'{col} {type_mapping[col]}' for col in header)
        create_table_statement += ');\n'

        with open("./data/"+table_name+".sql", 'w') as file:
            file.write(create_table_statement)

            for row in csv_reader:
                insert_statement = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ("
                insert_statement += ', '.join(value if type_mapping[col] in ['INT', 'NUMERIC'] else f"'{value}'" for col, value in zip(header, row))
                insert_statement += ');\n'
                file.write(insert_statement)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a csv file as a parameter")
        sys.exit(1)

    directory_path = './data/'
    os.makedirs(directory_path, exist_ok=True)

    csv_file_path = sys.argv[1]
    csv_to_mysql(csv_file_path)
