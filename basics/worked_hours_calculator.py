# Calculate how many hours do you work per week
worked_hours = float(input('How many hours do you work usually per a day: '))

if worked_hours > 24 or worked_hours < 0:
    print('Invalid value')
    exit()

worked_days = float(input('How many days do you work usually per a week: '))

if worked_days > 7 or worked_hours < 0:
    print('Invalid value')
    exit()

print(f'Usually you work {worked_days * worked_hours} hours per a week')
