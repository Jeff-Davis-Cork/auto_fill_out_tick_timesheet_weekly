# auto_fill_out_tick_timesheet_weekly

# This script logs into tick (the time-sheet website), adds hours per day for a standard week using Python &amp; Selenium WebDriver

# This script logs into tick, adds hours per day for a standard week

# designed to run on fridays & does not take into account holidays, etc.

# if not already, need to install chromedriver to your computer (http://chromedriver.chromium.org/downloads)

# & run 'pip install selenium' first

sample command line / terminal command to run this script (there are 7 arguments):


---------------------

cd <location of script>

pip install chromedriver_installer   (or just dowload from link above)

pip install selenium

python auto_fill_out_tick.py <tick email> <tick password> "https://<your organization>.tickspot.com/" <project name> <task name> "8" "C:\Program Files\chromedriver.exe"



-------------------------

so the arguments are in ths order: 

1. tickEmail
2. tickPassword
3. baseUrl
4. projectString
5. taskString
6. hoursPerDay 
7. chromeDriverPath 

Happy Time Logging !
