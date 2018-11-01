'''
Video
https://www.youtube.com/watch?v=eirjjyP2qcQ&index=24&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''


import datetime
import sys
# print(dir(datetime))
# print(dir(datetime.datetime))
print(sys.path.append('c:/users/phani/anaconda3/lib/site-packages'))  #---------> Adding pytz to sys variables.
import pytz

d = datetime.date(2018, 8, 19)
print(d)

#---------datetime.date---------------
tday = datetime.date.today()
print('today->',tday)
print('today.Day ->',tday.day)
print('today.Month ->',tday.month)
print('today.Year ->',tday.year)
print('today.Weekday ->',tday.weekday())    # Monday=0  Sunday=6
print('IsoWeekday ->',tday.isoweekday())   # Monday=1 Sunday=7
print('IsoCalendar ->',tday.isocalendar())
print('Isoformat ->',tday.isoformat())
print('Today.Max ->',tday.max)
print('Today.Min ->', tday.min)
print()
print()

#-----------datetime.timedelta---------------------
tdelta = datetime.timedelta(days=7)
print('A week later will be ',tday + tdelta)
print('A week earlier was ',tday - tdelta)
print()

# date2 = date1 + timedelta
# timedelta = date1 + date2
actual_bday = datetime.date(1992, 3, 20)
bday = datetime.date(2018, 3, 20)
next_bday = datetime.date(2019, 3, 20)
till_bday = tday - bday
to_next_bday = next_bday - tday
days_since_birth = tday - actual_bday
print('Days since I was born are ', days_since_birth)
print(days_since_birth.days,' days ', days_since_birth.total_seconds() , ' seconds')
print('Days since my birthday this year ', till_bday)
print(till_bday.days,' days ', till_bday.total_seconds() , ' seconds')
print('Days to my next birthday are ', to_next_bday)
print(to_next_bday.days, ' days ', to_next_bday.total_seconds() , ' seconds')
print()
print()


#---------datetime.time--------------------------------
t=datetime.time(1,6,30,100)
print(t)
print()


#----------datetime.datetime-----------------------------
dt = datetime.datetime(2018, 8,19,1,8,45,10000)
print(dt.date())
print(dt.time())

print(dt)

tdelta = datetime.timedelta(days=4,hours=12)
print('After 4 days and 12 hours from now, datetime would be ',dt+tdelta)
print()
print()

# Different constructors for datetime
dt_today = datetime.datetime.today()   # returns current local datetime
dt_now = datetime.datetime.now()       # you can pass a timezone. if timezone is not passed, it will return local datetime
dt_utcnow = datetime.datetime.utcnow()  # you can pass a timezone.
print('datetime.today()', dt_today)
print('datetime.now', dt_now)
print('datetime.utcnow', dt_utcnow)
print()
print()


#--------------Using pytz--------------------------------------
dt = datetime.datetime(2018,8,19,1,30,35,tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)    # Creates a current datetime using timezone info.
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# ---Converting UTC timezone(or from any timezone) to any timezone
dt_cdt = dt_now.astimezone(pytz.timezone('US/Central'))  # creating datetime with Central timezone
print('Central time->',dt_cdt)

dt_edt = dt_now.astimezone(pytz.timezone('US/Eastern'))
print('Eastern time->',dt_edt)
print()

# for tz in pytz.all_timezones:
#     print(tz)
print()

# ---Converting Naive time to any timezone
dt_now = datetime.datetime.now()
print(dt_now)

dt_edt = dt_now.astimezone(tz=pytz.timezone('US/Eastern'))
print('Eastern time->',dt_edt)
print()
print()



#------------Formatting DateTimes-------------------------------------
'''
Datetime to specific string -> date_str_var.strftime('pattern')
String to specific datetime -> datetime.datetime.strptime(date_str_var, 'pattern')
'''

dt_now = datetime.datetime.now(tz=pytz.timezone('US/Central'))
print(dt_now.strftime('%B %d, %Y'))     #--> Refer documentation

# String to datetime
dt_str = 'August 19, 2018'
dt= datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)