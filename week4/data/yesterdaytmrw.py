import datetime
days = datetime.timedelta(days=1)
yesterday = datetime.date.today() - days
tomorrow = datetime.date.today() + days

print (f" this is yesterday: {yesterday}, this is today: {datetime.date.today()}, this is tomorrow:  {tomorrow}")