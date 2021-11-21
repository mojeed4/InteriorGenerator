import tkinter

def daily_routine(day):
    routine = ['Brush Teeth', 'Celebrate Grace', 'Hit the Gym']

    if day == 'monday':
        routine.append('Go for lectures')
        routine.append('Grab lunch')
        routine.append('Meditate')

    elif day == 'tuesday':
        routine.append('Walk my dog')
        routine.append('Hang out with the boys')

    elif day == 'wednesday':
        routine.append('Go for lectures')
        routine.append('Celebrate more grace')

    elif day == 'thursday':
        routine.append('Play video games')
        routine.append('Learn some python programming')

    elif day == 'friday':
        routine.append('Attend classes')
        routine.append('Grab lunch')
        routine.append('prepare for TGIF')

    elif day == 'saturday':
        routine.append('Visit the pantry')
        routine.append('Cook in the kitchen')
        routine.append('Hit the club')

    elif day == 'sunday':
        routine.append('Celebrate plenty grace')
        routine.append('Read some books')
        routine.append('Hang out with the boys')

    else:
        return ['Invalid Entry, enter a new day']

    routine.append('Eat dinner')
    routine.append('Lights out')

    return routine


the_day = input('What day of the week is it? \n')
the_day = the_day.lower()
result = '\n'.join(daily_routine(the_day))
print()
print(result)