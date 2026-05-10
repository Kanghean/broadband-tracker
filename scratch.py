import speedtest
import schedule
import datetime
import time
import csv
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(parents=True, exist_ok=True)
headers = ["Test time", "Upload speed", "Download speed"]

if not Path(data_folder / "tracker.csv").is_file():
    with open(data_folder / "tracker.csv", mode = 'w', newline="") as csvfile:

        write = csv.DictWriter(csvfile, fieldnames = headers)
        write.writeheader()

def speed_test():

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)

    wifi = speedtest.Speedtest()
    wifi.get_best_server()

    print("Start finding upload")
    upload = wifi.upload()

    print("Start finding download")
    download = wifi.download()

    upload_mbps = upload / (1024 * 1024)
    download_mbps = download / (1024 * 1024)

    print(f"The upload speed is {upload_mbps:.2f}")
    print(f"The download speed is {download_mbps:.2f}")

    return {"Test time" : current_time,
            "Upload speed" : upload_mbps,
            "Download speed" : download_mbps}

def save_data(results):
    with open(data_folder / "tracker.csv", mode = 'a', newline="") as csvfile:
        headers = ["Test time", "Upload speed", "Download speed"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerow(results)

def main_job():
    results = speed_test()
    save_data(results)
    print("Data added to csv")

print(datetime.datetime.now().strftime("%H:%M:%S"))
schedule.every().minute.at(":00").do(main_job)

while True:
    schedule.run_pending()
    time.sleep(1)


