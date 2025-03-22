from datetime import datetime

now = datetime.now()  # Текущая дата и время
new_year = datetime(now.year + 1, 1, 1)  # 1 января следующего года

delta = new_year - now  # Разница между датами

print("До Нового года осталось:", delta.days, "дней")
