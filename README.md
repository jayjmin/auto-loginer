# auto-loginer

This project is to develop a automatic loginer for Newman College internet. The program checks internet connection status by accessing Newman's intranet login page every 5 seconds, and try to login if the internet is not connected.

If your computer cannot reach to Newman's intranet login site for any reason, the program will be stopped and exited. You need to restart the program once you have connection to Newman network.

#Usage 1 (ID/PW not saved)
	python auto-loginer.py <ID>

This will prompt to input PASSWORD. The ID and PASSWORD provided will NOT be saved in any form. This is the most secure method as it does not save password. However, you should provide password every time whenever you run the program.

#Usage 2 (Save and load from file)
	python auto-loginer.py

This will prompt to ask ID and PASSWORD for the first time, and save them to the local file named 'login.info' in encoded format. From the second time, it simply reads the saved file and uses them to log in. (WARNING: although the information is saved in encoded format, it is not secure. Please use it at your own risk, or use the first method which does not store any information.)

