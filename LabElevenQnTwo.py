# clockTime class
class clockTime:

    # constructor
    def __init__(self):
        # initialize attributes to None
        self.hours = None
        self.minutes = None
        self.seconds = None

    # assign input hours to attribute hours
    def setHours(self, h):
        self.hours = h

    # assign input minutes to attribute minutes
    def setMinutes(self, m):
        self.minutes = m

    # assign input seconds to attribute seconds
    def setSeconds(self, s):
        self.seconds = s

    # set time by referencing to function in the class
    def setTime(self, h, m, s):
        self.setHours(h)
        self.setMinutes(m)
        self.setSeconds(s)

    # display values assigned to attributes
    def showTime(self):
        print("Time:", self.hours, ":", self.minutes, ":", self.seconds)


def main():
    # user input of hours, minutes and seconds value
    hours = input("Enter hours value: ")
    minutes = input("Enter minutes value: ")
    seconds = input("Enter seconds value: ")
    # create a clockTime object
    ct = clockTime()
    # set time based on user input
    ct.setTime(hours, minutes, seconds)
    # display time
    ct.showTime()

main()