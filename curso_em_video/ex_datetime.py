import datetime
#datetime.today () apenas chama fromtimestamp (time.time ())
ddtt = datetime.datetime.today().year
print('datetime.datetime.today().year retorna: ', ddtt)
#datetime.today () não são exatamente iguais, datetime.now () aceita um objeto de fuso horário
ddtn = datetime.datetime.now().year
print('datetime.datetime.now().year retorna: ', ddtn)
ddt = datetime.date.today().year
print('datetime.date.today().year retorna: ', ddt)

#datetime.now()
from datetime import datetime
now = datetime.now()
print('now = ', now)
print('now.year = ', now.year)
print('now.month = ', now.month)
print('now.day = ', now.day)
print('now.hour = ', now.hour)
print('now.minue = ', now.minute)
print('now.second = ', now.second)
print('now.microsecond = ', now.microsecond)
print('now.tzinfo = ', now.tzinfo)
print('now.weekday =  ', now.weekday())#segunda = 0 domingo =6
now = datetime.now()
hora = now.hour
minuto = now.minute
print('Agora são:',hora, ':', minuto)

#datetime.today()
from datetime import datetime
today = datetime.today()
print('today = ', today)
print('today.year = ', today.year)
print('today.month = ', today.month)
print('today.day = ', today.day)
print('today.hour = ', today.hour)
print('today.minue = ', today.minute)
print('today.second = ', today.second)
print('today.microsecond = ', today.microsecond)
# tztime setado para none
print('today.tzinfo = ', today.tzinfo)
print('today.weekday =  ', today.weekday())#segunda = 0 domingo =6
today = datetime.today()
hora = today.hour
minuto = today.minute
print('Agora são:', hora, ':', minuto)

'''
from datetime import datetime

current_month = datetime.now().strftime('%m') // 02 //This is 0 padded
current_month_text = datetime.now().strftime('%h') // Feb
current_month_text = datetime.now().strftime('%B') // February

current_day = datetime.now().strftime('%d')   // 23 //This is also padded
current_day_text = datetime.now().strftime('%a')  // Fri
current_day_full_text = datetime.now().strftime('%A')  // Friday

current_weekday_day_of_today = datetime.now().strftime('%w') //5  Where 0 is Sunday and 6 is Saturday.

current_year_full = datetime.now().strftime('%Y')  // 2018
current_year_short = datetime.now().strftime('%y')  // 18 without century

current_second= datetime.now().strftime('%S') //53
current_minute = datetime.now().strftime('%M') //38
current_hour = datetime.now().strftime('%H') //16 like 4pm
current_hour = datetime.now().strftime('%I') // 04 pm

current_hour_am_pm = datetime.now().strftime('%p') // 4 pm

current_microseconds = datetime.now().strftime('%f') // 623596 Rarely we need.

current_timzone = datetime.now().strftime('%Z') // UTC, EST, CST etc. (empty string if the object is naive).

'''