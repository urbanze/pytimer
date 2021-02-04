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