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
    def update(self,unit,value):
        match unit:
            case 'h':
                self.hours += value
            case 'm':
                self.minutes += value
            case 's':
                self.seconds += value
            case _:
                print('Wrong type!')
        
        self.normalize()

    def normalize(self):
        #sekundy wiekszę np 90 -> 1:30
        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        # minuty tak samo
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        #godziny 23 -> +2 -> 1
        while self.hours >= 24:
            self.hours -= 24
        while self.hours < 0:
            self.hours += 24

obj1 = Time(23,9,9)
print(obj1.display())
obj1.update('h', 2)
print(obj1.display())
