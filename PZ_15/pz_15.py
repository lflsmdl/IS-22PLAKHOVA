# Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
# должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
# ФИО мастера, вид изделия, материал, стоимость работ.
import sqlite3
conn = sqlite3.connect('jewerly.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Изделие
(id INTEGER PRIMARY KEY AUTOINCREMENT,
ФИО_клиента TEXT,
ФИО_мастера TEXT,
вид_изделия TEXT,
материал TEXT,
стоимость_работ REAL)''')

def add_product(фио_клиента, фио_мастера, вид_изделия, материал, стоимость_работ):
    cursor.execute("INSERT INTO Изделие (ФИО_клиента, ФИО_мастера, вид_изделия, материал, стоимость_работ) VALUES (?, ?, ?, ?, ?)", (фио_клиента, фио_мастера, вид_изделия, материал, стоимость_работ))
    conn.commit()
    print("Изделие добавлено успешно")
def show_products():
    cursor.execute("SELECT * FROM Изделие")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

add_product("Иванов Иван", "Петров Петр", "Кольцо", "Золото", 500)
add_product("Петрова Ольга", "Сидоров Алексей", "Подвеска", "Серебро", 300)
show_products()

conn.close()