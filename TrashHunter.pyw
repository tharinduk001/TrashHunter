import os
import shutil
import getpass
import schedule
import datetime
import time

class Cleaner():
    def __init__(self) -> None:
        self.username = getpass.getuser()
        self.job_one,self.job_two = "Passed","Passed";

    def clean(self,url:str,job_id:str) -> None:
        files = os.listdir(url)
    
        for file in files:
            filepath = os.path.join(url,file)
            try:
                if os.path.isfile(filepath):
                    os.unlink(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
            except WindowsError as e:
                self.job_one = self.job_two = "Your system is almost clean!"
            except Exception as e:
                if job_id == "job_one":
                    self.job_one = f"Failed - {e}"
                else:
                    self.job_two = f"Failed - {e}"
    
    def log(self):
        with open(f"C:\\Users\\{self.username}\\Desktop\\TrashCleaner_report.txt",'a') as file:
            file.write(f"{datetime.datetime.now()} \t >> Job 1 :  {self.job_one} \t >> Job 2 : {self.job_two} \n")


dir1:str = f"C:\\Users\\{getpass.getuser()}\\AppData\\local\\Temp"
dir2:str = "C:\\Windows\\Temp"

def start_cleaner():    
    if __name__ == "__main__":
        job = Cleaner()
        job.clean(dir1,"job_one")
        job.clean(dir2,"job_two")
        job.log()

schedule.every(15).minutes.do(start_cleaner)

while True:
    schedule.run_pending()
    time.sleep(1)


      
