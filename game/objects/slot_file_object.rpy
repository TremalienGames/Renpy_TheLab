init python:
    class SlotFileObject:

        def __init__(self, name, screenshot, date, number):
            self.name = name
            self.screenshot = screenshot
            self.date = date
            self.number = number

        def getDate(self):
            return self.date

        def ToString(self):
            return "Date:" , self.date, " Number:", self.number , "\n, Name:" , self.name
