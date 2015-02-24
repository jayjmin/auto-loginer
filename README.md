# auto-loginer

This project is to develop a automatic loginer for Newman College internet. The program checks internet connection status by accessing Newman's intranet login page every 5 seconds, and try to login if the internet is not connected.

If your computer cannot reach to Newman's intranet login site for any reason, the program will be stopped and exited. You need to restart the program once you have connection to Newman network.

#Installation
Downalod auto-loginer.py file into your local computer in Newman network.
You also need Python to run this program.

#How to run the program
Open Terminal or any command line prompt which can execute python program, and use the following command:
	python auto-loginer.py

This will prompt you to input ID and PASSWORD for the first time, and whether you want to save them to the local file named 'login.info' in encoded format. If the save file exists, it simply reads the file and uses them to log in. (WARNING: although the information is saved in encoded format, it is not secure. Please use it at your own risk, otherwise do not save the information.)

