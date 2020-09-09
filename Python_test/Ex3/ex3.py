import requests
import json
import pandas as pd

res = requests.get("https://50cfe3fd1fbce9da08507875d77688eb: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@haison1111.myshopify.com/admin/api/2020-07/customers.json")

json_data = json.load(res.text)
mail = []
first_name = []
last_name = []
orders_count = []
phone = []
currency = []

for i in json_data["customers"]:
    mail.append(i["email"])
    first_name.append(i["first_name"])
    last_name.append(i["last_name"])
    orders_count.append(i["orders_count"])
    phone.append(i["phone"])
    currency.append(i["currency"])

data = {'mail': [str(e) for e in mail],
        'first_name': [str(e) for e in first_name],
        'last_name': [str(e) for e in last_name],
        'orders_count': [str(e) for e in orders_count],
        'phone': [str(e) for e in phone],
        'currency': [str(e) for e in currency],
        }

df = pd.DataFrame (data, columns = ["mail", "first_name", "last_name", "orders_count", "phone", "currency"])