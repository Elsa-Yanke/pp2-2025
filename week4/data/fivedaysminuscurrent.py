
from datetime import datetime, timedelta

now = datetime.now()
fivedaysago = now - timedelta(days=5)

print("Current Date:", now)
print("Current Date:", fivedaysago)
