import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

URL = "https://world.openfoodfacts.org"
HEADERS = {
    "User-Agent": "PatienceInventoryApp/1.0(patience@example.com)"
}


@app.route("/")
def home():
    return "Hello, Patience!"

#MOCK database looks like the Open Food Facts API structure
inventory = [
    {
        "status": 1,
        "product": {
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "quantity": 50,
        "price": 40,
        "barcode": "123456789012",
        "ingredients_text": "Filtered water,almonds,cane sugar,sea salt"}
    },
    {
       "status": 2,
       "product": {
               "product_name": "Organic Apple",
               "brands": "Pink Lady",
               "quantity": 50,
               "price": 40,
               "barcode": "123456789012",
               "ingredients_text": "Farm fresh organic apples"
    },
        },
]

next_status = 3

#route to get the inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

#route to get one item
@app.route("/inventory/<int:status>", methods=["GET"])
def get_item(status):
    item = next((item for item in inventory if item["status"] == status), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

#route to add an item to the inventory
@app.route("/inventory", methods=["POST"])
def add_item():
    global next_status
    data = request.get_json()

    if not data or "product_name" not in data:
        return jsonify({"error": "Missing product_name"}), 400

    new_item = {
        "status": next_status,
        "product": {
            "product_name": data["product_name"],
            "brands": data.get("brands", ""),
            "quantity": data.get("quantity", 0),
            "price": data.get("price", 0),
            "barcode": data.get("barcode", ""),
            "ingredients_text": data.get("ingredients_text", "")
        }
    }
#instruct inventory to append the new item to the inventory list
    inventory.append(new_item)
    next_status += 1
    return jsonify({"message": "Item added successfully"}), 201


#route to update an item or change the details
@app.route("/inventory/<int:status>", methods=["PATCH"])
def update_item(status):
    item = next((item for item in inventory if item["status"] == status), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input found"}), 400

    for key, value in data.items():
        if key in item["product"]:
            item["product"][key] = value

    return jsonify(item), 200

#route to remove an inventory item
@app.route("/inventory/<int:status>", methods=["DELETE"])
def remove_item(status):

    global inventory
    item= next((item for item in inventory if item["status"] == status), None)
    if not item:
        return jsonify ({"error": "Item not found"}), 404
    inventory=[item for item in inventory if item ["status"] != status]
    return jsonify ({"message":f" Item with {status} removed successfully"}), 200

#API fetching
@app.route("/off/product/<barcode>", methods = ["GET"])
def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v3.6/product/{barcode}.json"
    response= requests.get(url, headers =HEADERS)
    data = response.json()
    return jsonify(data.get("product",{})), response.status_code

if __name__ == "__main__":
    app.run(debug=True)