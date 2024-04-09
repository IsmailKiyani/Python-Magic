pip install plyer

#It will work on the PC, will not work on Jupyter
import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(title="TESTING !!",app_name ="Single SignOn", toast=False,message="Checking the Desktop Notification",timeout=5)
    time.sleep(3600)