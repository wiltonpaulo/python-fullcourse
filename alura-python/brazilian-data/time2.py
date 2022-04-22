from datetime import datetime, timedelta

now = datetime.today()
print(now)


yesterday = now - timedelta(days=365)
print(yesterday)
