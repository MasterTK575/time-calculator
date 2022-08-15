# calculating the minutes would work with 24hrs format, but not with AM/PM

def add_time(start, duration):
    # making a dictionary with am/pm to show time format
    # we can later iterate through it with two variables to show change in day
    timeformat = dict()
    timeformat["AM"]= [12, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11]
    timeformat["PM"]= [12, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11]

    days = ["monday", "tuesday", "wedesnday", "thursday", "friday", "saturday", "sunday"]

    # split the start to get time and format
    parameters = start.split()
    format = parameters[1]
    starttime = parameters[0]
    hourform = starttime.split(":")

    # find the starting point (in AM/PM)
    if int(hourform[0]) == 12:
        poshour = 0
    else:
        poshour = int(hourform[0])


    # calculate the minutes
    def calc_minutes(hourform):
        hourform = hourform.split(":")
        minutes = (int(hourform[0])*60) + int(hourform[1])
        return minutes

    tottime = calc_minutes(starttime) + calc_minutes(duration)

    # transform back into hour format
    def hour_form(min):
        hours = min / 60
        hours = str(hours).split(".")
        minutes = min % 60
        formatted = hours[0] + ":" + str(minutes)
        return formatted

    tottime = hour_form(tottime)

    return tottime

print(add_time("3:00 PM", "3:10"))
