import csv
from salesapp.models import Customer

def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row,"row")
            Customer.objects.create(
                name=row['name'],
                email=row['email'],
                address=row['address']
            )

if __name__ == '__main__':
    csv_file_path = 'data.csv'
    import_data(csv_file_path)