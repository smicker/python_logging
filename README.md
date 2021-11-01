
## About
This is a demo that demonstrates how to use the very nice built in logger package in Python.
It shows how to use different config files, logging to console and to file and also timed rotating logs. It uses the flag 'w' in the logging config files which means that it will open (create if not exist) the log file, erase everything and start printing from the top of the file. Using 'a' would instead append the text to the bottom of the file.

## Execution
Run this from the project folder by:  
```python3 main.py```

## Documentation
Nice info on rotating logs:  
https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/  

### TimedRotatingFileHandler
For TimedRotatingFileHandler you can use:
- seconds (s)
- minute (m)
- hour (h)
- day (d)
- w0-w6 (weekday, 0=Monday)
- midnight

The args used in this example, in rotating_log.conf is  
```args=('%(logfilepath)s/minrotatinglogg.log', 's', 10, 6)```  
This is 's' for seconds and 10 seconds and 6 old log files which means:  
When this code is run, it will start logging into the first log file with the extension .log. When the next log comes, that is more than 10 seconds after the first one, the current *.log file will be renamed to *.log.<YYYY-MM-DD_hh-mm-ss> and a new file *.log will be created. The log is now instead printed to the the new *.log file. If we have more than 6 old log files the last one will now be deleted. Eg. we will have 7 rotating log files, changed every 10 seconds.  
To know what arguments to put in, you can look at the TimedRotatingFileHandler constructor. It looks like this:  
```def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)```

### RotatingFileHandler
Those logs are instead rotated when the file size exceeds a set value. This kind is not included in this demo but it can be implemented in the same way as for TimedRotating logs.