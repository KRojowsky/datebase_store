from func import Products
from func import Enter_products

start = Products("", 0, 0, 0)
start.welcome_function()

def input_data_function():
    data = Enter_products()
    product_name = data.enter_name()
    product_prize = data.enter_price()
    product_quantity = data.enter_quantity()
    product_weight = data.enter_weight()

    update_data = Products(product_name, product_prize,
                       product_quantity, product_weight)

    if update_data.data_check() == 1:
        update_data.save_data()
    else:
        update_data.delete_info()
        input_data_function()

    if update_data.re_data() == 0:
        input_data_function()

input_data_function()