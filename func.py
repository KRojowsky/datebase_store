class Products:
    def __init__(self, name, price, quantity, weight):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight

    def welcome_function(self):
        print("Welcome to the product database.")

    def data_check(self):
        print(f"\nData validation:\nName: {self.name}\n"
              f"Price: {self.price}(zł)\n"f"Quantity: {self.quantity}"
              f"\nWeight: {self.weight}(kg)\n")

        while True:
            try:
                good = int(input("Confirm data compliance(1(true)/0(false)): "))
                break
            except:
                print("Encorrect value was entered. Try again...")
        return good

    def save_data(self):
        data_file = open("data_file.txt", "a+")
        data_file.write(f"\nName: {self.name}\n"
              f"Price: {self.price}(zł)\n"f"Quantity: {self.quantity}"
              f"\nWeight: {self.weight}(kg)\n")
        data_file.close()

    def delete_info(self):
        print("Deletion of entered data...\n")

    def re_data(self):
        while True:
            try:
                value = input("Finish entering data into the databas"
                             "(1(true)/0(false))?: ")
                break
            except:
                print("Encorrect value was entered. Try again...")

        return value
####################################################################################################################################
class Enter_products:
    def enter_name(self):
        while True:
            try:
                name = input("Enter product name: ")
                break
            except:
                print("Encorrect data was entered. Try again...")
        return name

    def enter_price(self):
        while True:
            try:
                price = float(input("Enter the price of the product: "))
                break
            except:
                print("Data entry error. Try again...")
        return price

    def enter_quantity(self):
        while True:
            try:
                quantity = int(input("Enter the quantity of the product: "))
                break
            except:
                 print("Quantity entry error. Try again...")
        return quantity

    def enter_weight(self):
        while True:
            try:
                weight = float(input("Enter the weight of the product: "))
                break
            except:
                print("Weight entry error. Try again...")
        return weight