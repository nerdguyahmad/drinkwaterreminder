
# Importing time and notification from pyler

import time
from plyer import notification

if __name__=="__main__":
	while True:
 	# Making a notification

		notification.notify(            # using notify function
			title= "Reminder: Drink Water",  # title of notification
			message= "Water is important for your health. Please drink some and then continue your work!",  # Message in notification
			app_icon= ".\water.ico", # Displaying an icon in notification
			timeout= 10  # Notification will stay for 10 seconds
			)
		time.sleep(60*60) # it will run in background and will execute every 1 hour


