# Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
# должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
# ФИО мастера, вид изделия, материал, стоимость работ.
import sqlite3

conn = sqlite3.connect('jewelry_workshop.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Jewelry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        master_name TEXT,
        item_type TEXT,
        material TEXT,
        work_cost REAL
    )
''')

def add_item(client_name, master_name, item_type, material, work_cost):
    cursor.execute('''
        INSERT INTO Jewelry (client_name, master_name, item_type, material, work_cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (client_name, master_name, item_type, material, work_cost))
    conn.commit()

def find_item_by_client(client_name):
    cursor.execute('SELECT * FROM Jewelry WHERE client_name=?', (client_name,))
    return cursor.fetchall()

def find_item_by_master(master_name):
    cursor.execute('SELECT * FROM Jewelry WHERE master_name=?', (master_name,))
    return cursor.fetchall()

def find_item_by_material(material):
    cursor.execute('SELECT * FROM Jewelry WHERE material=?', (material,))
    return cursor.fetchall()

def delete_item_by_id(item_id):
    cursor.execute('DELETE FROM Jewelry WHERE id=?', (item_id,))
    conn.commit()

def delete_item_by_material(material):
    cursor.execute('DELETE FROM Jewelry WHERE material=?', (material,))
    conn.commit()

def delete_item_by_cost(work_cost):
    cursor.execute('DELETE FROM Jewelry WHERE work_cost=?', (work_cost,))
    conn.commit()

def update_item_cost(item_id, new_cost):
    cursor.execute('UPDATE Jewelry SET work_cost=? WHERE id=?', (new_cost, item_id))
    conn.commit()

def update_item_material(item_id, new_material):
    cursor.execute('UPDATE Jewelry SET material=? WHERE id=?', (new_material, item_id))
    conn.commit()

def update_item_type(item_id, new_type):
    cursor.execute('UPDATE Jewelry SET item_type=? WHERE id=?', (new_type, item_id))
    conn.commit()

add_item('Иванов', 'Петров', 'Кольцо', 'Золото', 500)
add_item('Петрова', 'Сидоров', 'Браслет', 'Серебро', 300)

print(find_item_by_client('Иванов'))
print(find_item_by_master('Петров'))
print(find_item_by_material('Золото'))

delete_item_by_id(1)
delete_item_by_material('Серебро')
delete_item_by_cost(500)

update_item_cost(2, 400)
update_item_material(2, 'Платина')
update_item_type(2, 'Ожерелье')

conn.close()