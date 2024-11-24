import json
import msgpack
import os

def aggregate_product_info(products):
    aggregated_info = {}

    for product in products:
        name = product["name"]
        price = product["price"]

        if name not in aggregated_info:
            aggregated_info[name] = {
                "prices": [],
                "avg_price": 0,
                "max_price": 0,
                "min_price": float("inf")
            }

        aggregated_info[name]["prices"].append(price)
        aggregated_info[name]["avg_price"] = sum(aggregated_info[name]["prices"]) / len(aggregated_info[name]["prices"])
        aggregated_info[name]["max_price"] = max(aggregated_info[name]["prices"])
        aggregated_info[name]["min_price"] = min(aggregated_info[name]["prices"])

    for product_info in aggregated_info.values():
        del product_info["prices"]

    return aggregated_info


with open("C:/Users/Mitya/Downloads/2_2/third_task.json", "r", encoding='utf-8') as file:
    products = json.load(file)
aggregated_info = aggregate_product_info(products)

with open("aggregated_data.json", "w") as json_file:
    json.dump(aggregated_info, json_file, indent=4)

with open("aggregated_data.msgpack", "wb") as msgpack_file:
    msgpack_file.write(msgpack.packb(aggregated_info))

json_size = os.path.getsize("aggregated_data.json")
msgpack_size = os.path.getsize("aggregated_data.msgpack")

print(f"Размер JSON файла: {json_size} байт")
print(f"Размер MessagePack файла: {msgpack_size} байт")