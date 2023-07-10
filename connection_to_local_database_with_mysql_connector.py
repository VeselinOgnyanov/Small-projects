import mysql.connector

diablo_db = mysql.connector.connect(user='root', password='************', host='127.0.0.1', database='diablo')
if diablo_db.is_connected():
    print("Connection established,")
    print("Diablo database connected! \n")

cursor_diablo_db = diablo_db.cursor()

select_query =\
    "SELECT * FROM items \
    WHERE items.price >= 250.000 \
    ORDER BY items.min_level DESC, items.name ASC\
    LIMIT 35;"

cursor_diablo_db.execute(select_query)
items_data = cursor_diablo_db.fetchall()
for current_item in items_data:
    item_id, item_name, item_type, item_stat, item_price, item_min_level = \
        current_item[0], current_item[1], current_item[2], current_item[3], current_item[4], current_item[5]
    print(f"Item-id: {item_id} \n"
          f"Item-name: {item_name} \n"
          f"Item-type {item_type} \n"
          f"Item-stat {item_stat} \n"
          f"Item-price: {item_price} \n"
          f"Item-min-level: {item_min_level} \n")

cursor_diablo_db.close()
diablo_db.disconnect()

if not diablo_db.is_connected():
    print("Database disconnected!")