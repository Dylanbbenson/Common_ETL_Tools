import requests
import json
import csv

#update the values of the following variables
api_url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
csv_file_path = './data/US_Population.csv'
api_key = 'private_key_here' #only necessary for private api access

#public api option
response = requests.get(api_url)

#private api option
'''
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
response = requests.get(api_url, headers=headers)
'''

def main():

    if response.status_code == 200:
        try:
            data = response.json()['data']
            field_names = list(data[0].keys())

            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names, extrasaction='ignore', delimiter=',')
                csv_writer.writeheader()

                for row_data in data:
                    csv_writer.writerow(row_data)

            print(f"CSV file saved at {csv_file_path}")

        except json.JSONDecodeError as e:
            print(f"Error occured while getting response: {e}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()