from flask import Flask

app = Flask(__name__)

#MOCK database looks like the Open Food Facts API structure
inventory = [
    {
        "status": 1,
        "product": {
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "quantity": 50,
        "price": 40,
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

next_status =3








@app.route("/")
def home():
    return "Hello, Patience!"

if __name__ == "__main__":
    app.run(debug=True)