import MySQLdb
import pandas as pd

def get_table_name(url):
    return url.split("/")[-1].replace(".csv", "")

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="123456",
                     db="testdb")

cur = db.cursor()
url = "/home/vuhaison/Documents/customer3.csv"
name = get_table_name(url)
fields = list(pd.read_csv(url, nrows=0))
cur.execute(f"create table {name}(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY)")

for i in fields:
    cur.execute(f"alter table {name} add {i} varchar(225)")


input_value = ",".join(str(s) for s in fields)
data = pd.read_csv(url)
row_qty = len(data) - 1
for j in range(0, row_qty):
    row = list(data.iloc[j, :])
    input_data = "'" + "','".join(str(s) for s in row) + "'"
    cur.execute(f"insert into {name}({input_value}) values ({input_data})")

db.commit()
db.close()
print("Create success")