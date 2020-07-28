from datetime import date, timedelta

WEEK_DAYS = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

def meetup(year, month, week, day_of_week):
    all_dates = []
    for i in range(0, 6):
        for d in [date(year, month, i) for i in range(1,8)]:
            day_index = d + timedelta(days=i * 7)
            if day_index.month == month:
                all_dates.append(day_index)

    all_dates = list(filter(lambda d: d.weekday() == WEEK_DAYS[day_of_week], all_dates))
    if week == 'teenth':
        day = list(filter(lambda d: d.day > 12 and d.day < 20, all_dates))[0]
    elif week == '1st':
        day = all_dates[0]
    elif week == '2nd':
        day = all_dates[1]
    elif week == '3rd':
        day = all_dates[2]
    elif week == '4th':
        day = all_dates[3]
    elif week == '5th':
        if len(all_dates) >= 5:
            day = all_dates[4]
        else:
            raise MeetupDayException('None exist day')
    elif week == 'last':
        day = all_dates[-1]
    
    return day


class MeetupDayException(Exception):
    pass