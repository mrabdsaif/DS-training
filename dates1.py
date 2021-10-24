from datetime import datetime, timedelta
today = datetime.now()
# to concanecate string with dates you need to convert date into string 
print('Today iS: ' + str(today) + '\n')
print('Second is : ' + str(today.second))
print('Minute is : ' + str(today.minute))
print('Hour is : ' + str(today.hour))
print('Day is : ' + str(today.day))
print('Month is : ' + str(today.month))
print('Year is : ' + str(today.year) +'\n')

# timedelta is used to define a period of time

one_day = timedelta(days=1)
one_week = timedelta(weeks=1)

yesterday = today - one_day
today_week_ago = today - one_week

print('Yesterday was : ' + str(yesterday) + '\n')
print('Today week ago was : ' + str(today_week_ago) + '\n')


# Sometimes you get the date as a string and you need to store it as a date
birthday = input('Inter your birthday as dd/mm/yyyy? \n')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y') # or you can use %d/%m/%Y // strptime function allows me to expect to recieve the date as the mensioned format
print('Bierthday is: ' + str(birthday_date))
