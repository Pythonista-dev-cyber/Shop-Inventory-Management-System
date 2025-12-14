# Shop Inventory Management System

## Overview
The Shop Inventory Management System is a Python console-based application designed to manage products in a small shop. It allows users to add new products, restock existing items, sell products, and view the current inventory. All inventory data is saved in a CSV file, ensuring data persistence between program runs.

This project demonstrates object-oriented programming concepts, file handling, and basic operator overloading in Python.

---

## Technologies Used
Python • CSV • File Handling • Object-Oriented Programming

---

## Features
- Add new products to the inventory
- Restock products using operator overloading (`+`)
- Sell products using operator overloading (`-`)
- Automatically save inventory data to a CSV file
- Load existing inventory data when the program starts
- Display all products with name, price, and quantity
- Menu-driven interface for easy interaction

---

## How It Works
1. The program loads inventory data from `inventory.csv` if it exists.
2. Users select actions from a menu.
3. Product quantities are updated using custom `+` and `-` operators.
4. All changes are saved back to the CSV file automatically.
5. The program continues running until the user chooses to exit.

---

## How to Run

1. Make sure Python 3 is installed on your computer.

2. Open **Command Prompt** (Win + R → type `cmd` → Enter).

3. Choose a directory and create a folder:
```bash
mkdir shop-inventory-system
cd shop-inventory-system
```
4.clone the project on the terminal with
```bash
git clone https://github.com/Pythonista-dev-cyber/Shop-Inventory-Management-System.git
```
and type code . to open vs code.

5.make sure both sg_exports_analysis.py and sgexports_dataset 2.csv are in the same folder.

6.run it.
