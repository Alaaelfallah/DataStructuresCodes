from clock2 import clock
#examples usages:
my_clock=clock(11,30)
your_clock=clock(11)
your_clock.settime(23,59,59)
your_clock.tic()
print(my_clock)
print(your_clock)
print(my_clock.sub(your_clock))

