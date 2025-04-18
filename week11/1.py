import psycopg2
from config import load_config

def update_phone_byname(first_name, new_phone_number):
    # SQL-запрос на поиск id по имени
    find_sql = """SELECT id FROM contacts WHERE first_name = %s"""
    
    # SQL-запрос на обновление номера по contact_id
    update_sql = """UPDATE phone_numbers SET phone_number = %s WHERE contact_id = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Шаг 1: ищем пользователя по имени
                cur.execute(find_sql, (first_name,))
                result = cur.fetchone()
                
                if result is None:
                    print("Контакт не найден ❌")
                    return False
                else:
                    contact_id = result[0]  # получаем id

                    # Шаг 2: обновляем номер
                    cur.execute(update_sql, (new_phone_number, contact_id))
                    conn.commit()
                    print("Номер успешно обновлён ✅")
                    return True

    except(Exception, psycopg2.DatabaseError) as error:
        print("Произошла ошибка:", error)
        return False


first_name = input("Введите имя: ")
new_phone_number = input("Введите новый номер телефона: ")

update_phone_byname(first_name, new_phone_number)