from src.tracker import SpeedTest
import schedule
import time
import datetime

test = SpeedTest('data', 'tracker.csv')

print(datetime.datetime.now().strftime("%H:%M:%S"))
print(test)
test.run_once()

