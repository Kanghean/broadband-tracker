import speedtest
import datetime
import csv
from pathlib import Path

class SpeedTest:

    def __init__(self, path_name, file_name):
        self.path_name = Path(path_name)
        self.file_name = file_name
        self.headers = ["Test time", "Upload speed", "Download speed"]

        #makes sure there is a folder
        self.path_name.mkdir(parents=True, exist_ok=True)
        
    def measure(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)

        wifi = speedtest.Speedtest()
        wifi.get_best_server()

        print("Start finding upload")
        upload = wifi.upload()

        print("Start finding download")
        download = wifi.download()

        upload_mbps = SpeedTest.change_to_mbps(upload)
        download_mbps = SpeedTest.change_to_mbps(download)

        print(f"The upload speed is {upload_mbps:.2f}")
        print(f"The download speed is {download_mbps:.2f}")

        return {self.headers[0] : current_time,
                self.headers[1] : upload_mbps,
                self.headers[2] : download_mbps}
    
    @staticmethod
    def change_to_mbps(number):
        return number / (1024 * 1024)
    
    def save_data(self, results):

        file_location = self.csv_file

        #checks if the file exists 
        need_headers = not file_location.exists() or file_location.stat().st_size == 0

        with open(file_location, mode = 'a', newline="") as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=self.headers)
            if need_headers:
                writer.writeheader()

            writer.writerow(results)

    def run_once(self):
        results = self.measure()
        self.save_data(results)

    @property
    def csv_file(self):
        return self.path_name / self.file_name
    
    def __repr__(self):
        return f"Speedtest( Path = {self.path_name}, File = {self.file_name})"
