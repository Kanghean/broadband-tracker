from src.tracker import SpeedTest
import datetime

test = SpeedTest('data', 'tracker.csv', 'Home')

print(datetime.datetime.now().strftime("%H:%M:%S"))
print(test)
test.run_once()

