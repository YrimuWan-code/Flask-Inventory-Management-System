# Flask Inventory Management System

This project provides a beginner-friendly Flask backend API and a command-line interface (CLI) for managing product inventory and looking up product details by barcode. It helps track stock quantities and prices while connecting local inventory management with external product data from the Open Food Facts API. Built as a class assignment to practice RESTful API routes, external API requests, and Git feature branching.
 
**Author(s):** Patience ([https://github.com/YrimuWan-code])

## Built With
* Python 3
* Flask
* Requests
* Open Food Facts API

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
* Python 3.10+
* pip

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>

### Navigate to the project directory:
cd Flask-Inventory-Management-System

### Activate your virtual environment (if using venv) and install dependencies
source venv/bin/activate
pip install flask requests

### Usage
1. Start the Flask server in one terminal:
python3 app.py

2. Then run the CLI front end in a second terminal:
python3 cli.py

### Example Output
--- Inventory Menu ---
1 - View inventory
2 - Add new item
3 - Update item price or stock
4 - Delete product
5 - Find item on Open Food Facts API
6 - Quit
Type a number: 5
Enter barcode: 3017624010701

### Project Structure

├── app.py               # Flask backend with CRUD routes and Open Food Facts proxy route
├── cli.py               # Beginner-friendly CLI menu for interacting with the API
├── venv/                # Local Python virtual environment
├── __pycache__/         # Python bytecode cache files
└── README.md            # Project documentation

### Git Branches

* feature/API-design — Initial API design and setup

* feature/CRUD-routing — Inventory CRUD endpoints (GET, POST, PATCH, DELETE)

* feature/API-fetching — Open Food Facts barcode lookup integration

* feature/CLI-front-end — Command-line interface for interacting with the API

* feature/README — Project documentation (README.md)covering setup, usage, project structure and Git branches

### Acknowledgements

* Open Food Facts API for product lookup data
