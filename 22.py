import re

password = "StrongPass123"

# Проверка пароля: минимум 8 символов, хотя бы одна буква и одна цифра
pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

match = re.search(pattern, password)

if match:
    print("Пароль надёжный ✅")
else:
    print("Пароль не подходит ❌")
