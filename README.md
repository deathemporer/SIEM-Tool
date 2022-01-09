## Introduction:
Our project works on log files from Microsoft teams which are converted into structured data through our application. These log files can then be easily read so that we may know the errors we are encountering and can quickly debug minor bugs so that we can continue our work smoothly.

## Methodology:
The application is developed using:
<br>•	Front-end: HTML CSS and JS
<br>•	Back-end: Python, Flask

Input to the program is a log file which is in text format. The file is then parsed to JSON format using Python. This JSON file is read by JS and rendered on to the display using HTML. Filters and sorting is implemented using JS. 

The general architecture of the program is as follows:
1.Download log file and upload to the application
2.The log file is parsed as JSON
3.The JSON file created has some structure in data
4.This data is presented in the form of a table
5.This shows us the errors, error messages and other important info

## How to run:
1.Clone directory onto local machine using
<br>`gh repo clone deathemporer/SIEM-Tool`

2.Open MS Teams and press 
<br>`Ctrl+Shift+Alt+1`
<br>This downloads the log information into the downloads folder.

3.Run the application using the command 
<br>`flask run`

4.Upload the file from the following directory of the generated log folder
<br>`...Downloads\MSTeams Diagnostics Log 5_26_2021__11_05_58_PM\desktop\logs.txt`

5.Filtering/Searching can be done by using the following filters:
<br>`date="sample date"`
<br>`eventCode="sample code"`
<br>`logType="sample type"`
<br>`message="sample text"`

## Sample Screenshots:
![Upload log](https://i.imgur.com/R6eqddM.png)
![Parsed log file](https://i.imgur.com/XumbPM0.png)
![Visualized log](https://i.imgur.com/V67U6aP.png)
![Using filters](https://i.imgur.com/rJtsUt6.png)
![Using sort](https://i.imgur.com/NckBnqY.png)
