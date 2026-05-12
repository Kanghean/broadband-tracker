from src.tracker import SpeedTest
import schedule
import time
import datetime

test = SpeedTest('data', 'tracker.csv')

print(datetime.datetime.now().strftime("%H:%M:%S"))
schedule.every().minute.at(":00").do(test.run_once)
print(test)

while True:
    schedule.run_pending()
    time.sleep(1)