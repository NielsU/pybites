WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'

def main():
    print(get_workout_motd("frIday"))
    print(get_workout_motd("Sunday"))
    print(get_workout_motd("MonDay"))
    print(get_workout_motd("noday"))
    
def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """
    titled_day = str(day).title()
  
  
    if titled_day not in WORKOUT_SCHEDULE:
        return INVALID_DAY
    elif WORKOUT_SCHEDULE[titled_day] == REST:
        return CHILL_OUT
    else:
        return TRAIN.format(WORKOUT_SCHEDULE[titled_day])    
    
 
    
if __name__ == "__main__":
    main()     