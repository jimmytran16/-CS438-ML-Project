
# Backend

This is the backend for the Machine Learning project

## Set up environment
- Install Python into your computer https://www.python.org/downloads/ 
- Install the python virtual environment (OPTIONAL) 
```bash
  pip3 install virtualenv
```
- Inside the /server directory, set your virtual environment (OPTIONAL)
```bash
  python3 -m venv env

  source env/bin/activate <-- for Mac
  ./env/Scripts/Activate.ps1 <-- for Windows (issues with activiating: https://peter-whyte.com/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system-powershell/)
```
- Install the required dependencies for the server
```bash
  pip3 install -r requirements.txt
```
- Run the server
```bash
  python3 app.py
```

