import re
text = "Contact us at support@example.com or sales@shop.com for details."
# Выведи список всех email-адресов

matches = re.findall(r"\b[a-zA-Z0-9!%-+]+@[a-z]+[a-z]", text)

print(matches)
