# What it does

This script has my own basic Selenium Web Driver wrapper.  
Due to this wrapper I:  
 - open start page with chrome and login to camunda page
 - fill start process page with Ajax forms according with form data getting from .xls file.
 - repeat this step for required number test cases  

Project config are in config.py

# How it works
To install dependencies, I recommend you use pipenv.
```
pipenv install
```
Otherwise, you have to install:
- Pandas
- Selenium


To start script, you may type:
```
python run.py
```

Test_funcs.py is contain basic actions in browser which are wrapped in my selenium wrapper. 