init python:
    class Companion(object):
        def __init__(self, name,health,occupation,relationship):
            self.Name = name
            self.Health = health
            self.Occupation = occupation
            self.Relationship = relationship

        @property
        def Output(self):
            return "[self.Name] is your [self.Relationship]"
