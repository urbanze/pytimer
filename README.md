# pytimer
Python Class Software Timer

# Class parameters
pytimer.software_timer(time, autoreload, function, compensation=1)\
Time: Time (sec) to execute callback function.

Autoreload: If autoreload == 1, timer will execute function until .stop(). If 0, function will execute one time.

Function: Function to execute.

Compensation: If compensation == 1, this class calculate time to execute function() and subtract this from user delay, to maintain fixed frequency. If 0, total delay of execution is: Time parameter + function exection time. Default is 1.

# Example
```
import pytimer
import time

def test():
    print("Test")

# Create timer 't1'
# Interval: 500ms
# Autoreload: True
# Function callback: test()
t1 = pytimer.software_timer(0.5, 1, test)

# Start timer
t1.start()

# Wait 5sec
for i in range(5):
    time.sleep(1)

# Stop timer 
t1.stop()
```
