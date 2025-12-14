import csv
import os

class product:
    def __init__(self,name,price,qty):
        self.name = name
        self.price = price
        self.qty = qty

    def __add__(self,Amount):
        self.qty+=Amount
        return self
    
    def __sub__(self,Amount):
        if self.qty<Amount:
            raise ValueError("Not enough in stock")
        else:
            self.qty-=Amount
        return self
    
    def __str__(self):
        return f"{self.name} | Price: {self.price} | Qty: {self.qty}"
    

class Inventory:
    FILE = "inventory.csv"

    def __init__(self):
        self.product=[]
        self.LoadFile()

    
    def LoadFile(self):
        if not os.path.exists(Inventory.FILE):
            return
        with open(Inventory.FILE,'r') as File:
            reader = csv.reader(File)
            for row in reader:
                name,price,qty = row
                self.product.append(product(name,price,int(qty)))

    def SaveFile(self):
        try:
            with open(Inventory.FILE,'w',newline="") as File:
                writer = csv.writer(File)
                for row in self.product:
                    writer.writerow([row.name,row.price,row.qty])
        except Exception as e:
            print("Error saveing file")

    def AddProduct(self,name,price,qty):
        self.product.append(product(name,price,qty))
        self.SaveFile()

    
    def FindProduct(self,name):
        for p in self.product:
            if p.name.lower() == name.lower():
                return p    
        return None
    
    def ShowAll(self):
        if not self.product:
            print("No products in inventory")
        else:
            for p in self.product:
                print(p)

def Line():
    print("*"*40)


def main():
    Inv = Inventory()
    while True:
        print("\n=== SHOP INVENTORY SYSTEM ===")
        print("1.Add New Product")
        print("2.Restock Product(+ operator)")
        print("3.Sell Product(- operator)")
        print("4.Show All Products")
        print("5.Exit")
        Line()
        Choice = int(input("Choose option:"))
        Line()

        if Choice == 1: #Add new product
            name = input("Product name:")
            price = float(input("Price:"))
            qty = int(input("Quantity:"))
            Inv.AddProduct(name,price,qty)
            print("Product add")
            Line()
        elif Choice ==2: #Restock
            name = input("Product to restore:")
            SProduct = Inv.FindProduct(name)
            if SProduct:
                Amount = int(input("Add how many: "))
                SProduct + Amount
                Inv.SaveFile()

            else:
                print("Product not found!")
            Line()

        elif Choice ==3: #Sell
            name = input("Product to sell:")
            SProduct = Inv.FindProduct(name)
            if SProduct:
                Amount = int(input("Sell how many:"))
                try:
                    SProduct-Amount
                    Inv.SaveFile()
                    print("Sold:",SProduct)
                except:
                    print("Error")

            else:
                print("Product not found:")

            Line()

        elif Choice ==4: #Show
            Inv.ShowAll()
        elif Choice ==5: #Exit
            print("Tat Tar!")
            break
        else:
            print("Invalid Choice!Try again")

    







if __name__=="__main__":
    main()



        


    
