import pickle
import json

def update_price(price, method, param):
    if method == "add":
        return price + param
    elif method == "sub":
        return price - param
    elif method == "percent+":
        return price * (1 + param/100)
    elif method == "percent-":
        return price * (1 - param/100)
    else:
        raise ValueError(f"Неизвестный метод обновления цены: {method}")

with open("C:/Users/Mitya/Downloads/2_2/fourth_task_products.pkl", "rb") as pkl_file:
    products = pickle.load(pkl_file)

with open("C:/Users/Mitya/Downloads/2_2/fourth_task_updates.json", "r", encoding="utf-8") as json_file:
    price_updates = json.load(json_file)

for update in price_updates:
    name = update["name"]
    method = update["method"]
    param = update["param"]
    
    for product in products:
        if product["name"] == name:
            product["price"] = update_price(product["price"], method, param)
            break

output_pkl_file = "updated_products.pkl"
with open(output_pkl_file, "wb") as pkl_file:
    pickle.dump(products, pkl_file)

print("Цены успешно обновлены и сохранены в формате pkl.")
