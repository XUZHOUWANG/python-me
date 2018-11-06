


class Person(object):
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def full_name(self):
        return "%s %s" %(self.first,self.last)
    
    def __str__(self):
        return "Person:" + self.full_name()

person=Person('clark','kent')
print person
