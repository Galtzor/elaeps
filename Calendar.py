import datetime
class Calendar():
    def __init__(self):
        self.date = datetime.date.today()
        self.delta = datetime.timedelta(1)     # Ein dag forskjell fra dag til dag.
    def nextDay(self):
        self.date = self.date + self.delta

    def getDate(self):
        return self.date

    def toString(self):
        #Day, Month day, year
        return ("{:s}, {:s} {:d}, {:d}").format(self.weekDay(), self.month(), self.date.day, self.date.year)
    def weekDay(self):
        weekday = self.date.weekday()
        if weekday == 0: return "Monday"
        if weekday == 1: return "Tuesday"
        if weekday == 2: return "Wednesday"
        if weekday == 3: return "Thursday"
        if weekday == 4: return "Friday"
        if weekday == 5: return "Saturday"
        if weekday == 6: return "Sunday"

    def month(self):
        month = self.date.month
        if month == 1: return "January"
        if month == 2: return "February"
        if month == 3: return "March"
        if month == 4: return "April"
        if month == 5: return "May"
        if month == 6: return "June"
        if month == 7: return "July"
        if month == 8: return "August"
        if month == 9: return "September"
        if month == 10: return "October"
        if month == 11: return "November"
        if month == 12: return "December"
