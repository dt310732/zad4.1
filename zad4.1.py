class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        if self.hours < 10:
            h = f"0{str(self.hours)}"
        else:
            h = str(self.hours)
        if self.minutes < 10:
            m = "0" + str(self.minutes)
        else:
            m = str(self.minutes)     
        if self.seconds < 10:
            s = "0" + str(self.seconds)
        else:
            s = str(self.seconds)
        
        return h + ":" + m + ":" + s
    

obj1 = Time(9,9,9)
print(obj1.display())