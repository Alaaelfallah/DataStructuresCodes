class clock:
    def __init__(self,hr=0,min=0,sec=0):
        self.min=min
        self.sec=sec
        self.hr=hr
    def __repr__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def settime(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def tic(self):
        self.sec+=1
        if self.sec>=60:
            self.sec%=60
            self.min+=1
        if self.min>=60:
            self.min%=60
            self.hr+=1
        if self.hr>=24:
            self.hr=0
    def sub(self,other):
        result=0
        result+=(self.sec-other.sec)
        result += (self.min - other.min)*60
        result += (self.hr - other.hr)*60*60
        return abs(result)

#examples usages:
my_clock=clock(11,30)
your_clock=clock(11)
your_clock.settime(23,59,59)
your_clock.tic()
print(my_clock)
print(your_clock)
print(my_clock.sub(your_clock))
if __name__ == "__main__":
    try:
        myclock = clock(100)
    except ValueError:
        myclock = clock()
    another_clock = clock(12,30)

    #another_clock._hr = 50
    print("hello world")
    print(myclock)
    print(another_clock.hr)

    myclock.settime(23,59,59)
    myclock.tic()
    print(myclock)
    print(myclock-another_clock)
    print(another_clock - myclock)


