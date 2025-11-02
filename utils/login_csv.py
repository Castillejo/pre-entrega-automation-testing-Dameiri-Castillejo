import csv
from pathlib import Path

def get_login_csv(csv_file="data_login.csv"):

    # csv_file = get_file_path(csv_file, "data")

    csv_file = Path(__file__).parent.parent / "data" / csv_file
    # ../data/data_login.csv
    casos = []

    with open(csv_file, newline="" ) as  h:
        read = csv.DictReader(h)
       
        for i in read:
            username = i["username"]
            password = i["password"]
            login_example= i["login_example"].lower() == "true" #obligarlo a que sea un boleano
            casos.append((username,password,login_example))

    return casos