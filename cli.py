import requests

#address to run the app
url = "http://127.0.0.1:5000"

#Showing the menu
while True:
    print("\n--- Inventory Menu ---")
    print("1 - View inventory")
    print("2 - Add new item")
    print("3 - Update item price or stock")
    print("4 - Delete product")
    print("5 - Find item on Open Food Facts API")
    print("6 - Quit")

    choice = input("Type a number: ")

    #Error handling
    try:
        #Viewing all inventory items
        if choice == "1":
            response = requests.get(url + "/inventory")
            print(response.json())

        #Adding a new item to the inventory
        elif choice == "2":
            name = input("Product name: ")
            brand = input("Brand: ")
            price = int(input("Price: "))
            qty = int(input("Quantity: "))

            item = {
                "product_name": name,
                "brands": brand,
                "price": price,
                "quantity": qty
            }

            response = requests.post(url + "/inventory", json=item)
            print(response.json())

        #Updating price or quantity of an item
        elif choice == "3":
            item_id = int(input("Item status ID to update: "))
            what_to_update = input("Type 'price' or 'quantity': ")

            if what_to_update == "price":
                new_price = int(input("New price: "))
                response = requests.patch(url + "/inventory/" + str(item_id), json={"price": new_price})
                print(response.json())
            elif what_to_update == "quantity":
                new_qty = int(input("New quantity: "))
                response = requests.patch(url + "/inventory/" + str(item_id), json={"quantity": new_qty})
                print(response.json())
            else:
                print("Please type 'price' or 'quantity'.")

        #Deleting a product from inventory by the status ID
        elif choice == "4":
            item_id = int(input("Item status ID to delete: "))
            response = requests.delete(url + "/inventory/" + str(item_id))
            print(response.json())

        #Searching  Open Food Facts API using the barcode
        elif choice == "5":
            barcode = input("Enter barcode: ")
            response = requests.get(url + "/off/product/" + barcode)
            print(response.json())

        #Closing the CLI
        elif choice == "6":
            print("Bye!")
            break

        #For edge cases
        else:
            print("Please pick a number from 1 to 6.")

    #If user enters a letter instead of number
    except ValueError:
        print("Please enter a valid number.")

    #If the request fails
    except requests.exceptions.RequestException:
        print("API error: Could not connect to the server.")