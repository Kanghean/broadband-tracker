from tracker import SpeedTest
import schedule
import time
import datetime
import speedtest

test = SpeedTest('data', 'tracker.csv')

def safe_to_run():

    try:
        test.run_once()
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Data retreived successful!")
    except speedtest.ConfigRetrievalError:
        print("Couldn't retrieve data. I will try next hour!")
    
    except ConnectionError:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]There was no internet connection. I will try next hour!")
    
    except TimeoutError:
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]Retreiving data too fast. I will try next hour!")

    except Exception:
        print((f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Something happened {Exception}"))

print(datetime.datetime.now().strftime("%H:%M:%S"))
schedule.every().minute.at(":00").do(safe_to_run)
print(test)

while True:
    schedule.run_pending()
    time.sleep(1)

