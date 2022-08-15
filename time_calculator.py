# calculating the minutes would work with 24hrs format, but not with AM/PM


def add_time(start, duration, input = None):

    # split by hours and minutes
    def split_hrsmin(time):
        timesplit = time.split(":")
        hours = int(timesplit[0])
        minutes = int(timesplit[1])
        return hours, minutes

    # split the start to get time and format
    parameters = start.split()
    format = parameters[1]
    starttime = parameters[0]

    # get the hr format of start time
    hrfrstart = split_hrsmin(starttime)

    # get the hr format of duration
    hrfrdur = split_hrsmin(duration)

    # add up minutes to account for increase in hours
    minutes = hrfrstart[1] + hrfrdur[1]
    if minutes >= 60:
        extrahrs = 1
        minutes = minutes % 60
    else:
        extrahrs = 0

    # add up hours
    tothrs = hrfrstart[0] + hrfrdur[0] + extrahrs

    # by giving AM a count of 0 and PM a count of 1 we know which time format we are at
    if format == "AM":
        formcount = 0
    else:
        formcount = 1

    loopcount = tothrs
    count = 1
    daycount = 0
    # every 12 counts aka hrs we increase the format counter (we ran through one AM/PM cycle)
    # every 24 hrs we increase the day counter
    while loopcount > 0:
        if count % 12 == 0:
            formcount = formcount + 1
            tothrs = tothrs - 12
        if count % 24 == 0:
            daycount = daycount + 1
        count = count + 1
        loopcount = loopcount -1

    # to account for the loop reducing the total hrs to exactly 0
    if tothrs == 0:
        tothrs = 12

    # get the AM/PM format for the result
    if formcount % 2 == 0:
        returnformat = "AM"
    else:
        returnformat = "PM"

    # final formatting for the return
    # to account for minutes being of lenght 1
    if len(str(minutes)) == 1:
        minutesstr = "0" + str(minutes)
    else:
        minutesstr = str(minutes)
    
    # formatting for days later
    # to account for an PM to AM daychange
    if format == "PM" and formcount >= 2:
        daycount = daycount + 1

    if daycount == 0:
        message = ""
    elif daycount == 1:
        message = " (next day)"
    else:
        message = " (" + str(daycount) + " days later" + ")"


    # include calc for actual days
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if input:
        day = input.lower()
        try:
            daypos = days.index(day)
        except:
            print("Error, please make sure the day is spelled correctly")
            quit()
        
        # basically we do a loop and forward the "week" counter each 7 times and then reset
        dayiterable = daypos + daycount
        findday = 0

        while dayiterable > 0:
            if dayiterable % 7 == 0:
                findday = findday - 7
            findday = findday + 1
            dayiterable = dayiterable -1

        newday = days[findday].capitalize()

    if input:
        finalformat = str(tothrs) + ":" + minutesstr + " " + returnformat + ", " + newday + message

    else:
        finalformat = str(tothrs) + ":" + minutesstr + " " + returnformat + message

    return finalformat


print(add_time("8:16 PM", "466:02", "tuesday"))
