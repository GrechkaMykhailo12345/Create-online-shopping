import sqlite3

def connect_db(db_name="shop.db"):
    return sqlite3.connect(db_name)

def run_query(cursor, query):
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            for row in cursor.fetchall():
                print(row)
        else:
            print("Запит виконано успішно.")
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    conn = connect_db()
    cursor = conn.cursor()

    print("Інтерактивний режим SQL-запитів. Введіть 'exit' для виходу.")
    print("Введіть ваш SQL-запит нижче:\n")

    while True:
        user_input = input("SQL> ")
        if user_input.lower() == "exit":
            break
        run_query(cursor, user_input)

    save = input("Зберегти зміни? (так/ні): ").strip().lower()
    if save == "так":
        conn.commit()
        print("Зміни збережено")
    else:
        conn.rollback()
        print("Зміни скасовано")

    conn.close()

if __name__ == "__main__":
    main()
