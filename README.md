# CyclomaticComplexity

ScalableComputing Assignment 2 (CyclomaticComplexity Using Rest Services)
===================


Hey! 
This repository contains the server code for the rest based distributed computing task.  This readme contains information about **dependencies and how to run the program** The code was written using **Python 3.5**


>#### <i class="icon-upload"></i> Submission details:
Name: Smarth Katyal
<br>TCD Student ID: 17306092
<br>Email: katyals@tcd.ie

Dependencies
-------------
>- **Python 3.5** (Performance with earlier versions is untested)
>- **Windows based System** (Hard Requirement because pragram internally uses shell commands like mkdir,chdir,etc. )
>- **PIP - Python Package Manager** (Will be used to install other dependencies)
>- **Flask** (pip install Flask)
>- **Flask-RESTful** (pip install Flask-RESTful)
>- **requests** (pip install requests)
>- **lizard** (pip install lizard)


Configuration
-------------

>-  Open the file  **CyclomaticComplexity/com/delegator/master.py** in any text editor and change **self.totalSlaves = 1** to the number of slaves desired.
>- Save and close the file.
>-  Open the file  **CycloCalculator/com/analyzer/slave.py** in any text editor and change **masterip="127.0.0.1"** to IP address of the server where you will run master.py
>- Save and close the file.


Compiling
-------------
>-  No steps required

Running
-------------
>- 1) Navigate to **CyclomaticComplexity/com/delegator/** and run the below command
	 <br>**py master.py**
>- 2) Navigate to **CycloCalculator/com/analyzer/** and run the below command
	 <br>**py slave.py**
   
>- Repeat step 2 'N' times where 'N' is the number of slaves you entered during configuration. By Default it is 1, so you will need to run step two only once.

Working
-------------
>- The slave sends a request to the master to ask for the repository of which it needs to calculate the complexity.
>- The master responds with the URL of the git repo. For demo purpose, we are using the below git repository(Java):
    <br>**https://github.com/smart-fun/XmlToJson**
>- The slave initiates a pull of the repo and confirms to master.
>- After getting confirmation from all slaves that they are ready, the master starts a timer and sends each slave a different commit id for which the complexity is to be calculated
>- After the slave is finished calculating, it sends the calculated value to the master.
>- When the master gets a response from all slaves, it stops the timer & it calculates the average complexity and returns.

Conclusion
-------------
Conclusion uploaded in pdf document-'conclusion.pdf'.
