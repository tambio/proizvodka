import psycopg2
import tkinter as tk
from config import db_name, user, password, host
        
# Определите переменную icon до её использования


try:
    with psycopg2.connect(database=db_name, user=user, host=host, password=password) as conn:
        print("Connected to the database")
        
        def showbrand():
            with conn.cursor() as curs:
                curs.execute(f"SELECT * FROM brands")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
                
                
        def showcategories():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM categories")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
        
        def showproducts():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM products")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
        
        def showwarehouses():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM warehouses")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)

        def showorder():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM orders")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
        

        def showorderedProducts():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM ordered_product")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
 
        def showcustomer():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM customers")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
              
        def showinventory():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM inventory")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)

        def showcartsProduct():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM cartproduct")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)

        def showfeedBacks():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM feedbacks")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
                
                formatted_data = "Названия столбцов:\n"

                formatted_data += "\t".join(column_names) + "\n"
                
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)
        
        def showdiscounts():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM discounts")
                result = curs.fetchall()
                formatted_data = "Названия столбцов:\n"
                column_names = [desc[0] for desc in curs.description]
                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)    

        def showdeliveries():
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM deliveries")
                result = curs.fetchall()
                column_names = [desc[0] for desc in curs.description]
        
                formatted_data = "Названия столбцов:\n"
                formatted_data += "\t".join(column_names) + "\n"
        
                formatted_data += "\n"
                for row in result:
                    formatted_data += "\t".join(map(str, row)) + "\n"

                text_widget.delete("1.0", "end")
                text_widget.insert("1.0", formatted_data)



                
        root = tk.Tk()
        root.geometry("1000x1000")
        root.title("MultiShop")
        icon = tk.PhotoImage(file="icon.png")
        root.tk.call('wm', 'iconphoto', root._w, icon)
        text_widget = tk.Text(root, width=80, height=15)
        text_widget.pack()

        brands = tk.Button(root, text="Бренды", command=showbrand, width=20, height=2)
        brands.pack()
        categories = tk.Button(root, text="Категории", command=showcategories , width=20, height=2)
        categories.pack()
        products = tk.Button(root, text="Продукты", command=showproducts, width=20, height=2)
        products.pack()
        warehouses = tk.Button(root, text="Склад", command=showwarehouses, width=20, height=2)
        warehouses.pack()
        order = tk.Button(root, text="Заказ", command=showorder, width=20, height=2)
        order.pack()
        orderedProducts = tk.Button(root, text="Заказанные товары", command=showorderedProducts, width=20, height=2)
        orderedProducts.pack()
        customer = tk.Button(root, text="Покупатель", command=showcustomer,width=20, height=2)
        customer.pack()
        inventory = tk.Button(root, text="Наличие товара", command=showinventory,width=20, height=2)
        inventory.pack()
        cartProducts = tk.Button(root, text="Корзина", command=showcartsProduct,width=20, height=2)
        cartProducts.pack()
        feedBacks = tk.Button(root, text="Отзывы", command=showfeedBacks,width=20, height=2)
        feedBacks.pack()
        discounts = tk.Button(root, text="Скидки", command=showdiscounts,width=20, height=2)
        discounts.pack()
        deliveries = tk.Button(root, text="Доставка", command=showdeliveries, width=20, height=2)
        deliveries.pack()    
        root.mainloop()
        
except psycopg2.Error as e:
    print(f"An error occurred: {e}")
