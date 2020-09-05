Creating virtual environments
Creation of virtual environments is done by executing the command venv:
```
python3 -m venv /path/to/new/virtual/environment
```

What I do:

I am in the relative folder named `mypython`
Then I type:
```
python -m venv mypythonvenv
```
Running this command creates the target directory (creating any parent directories that don’t exist already) and places a pyvenv.cfg file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is .venv). It also creates a bin (or Scripts on Windows) subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate for the platform or arguments used at environment creation time). It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory (on Windows, this is Lib\site-packages). If an existing directory is specified, it will be re-used.

So the complete python environment will be created in a subfolder named `mypythonvenv`:
```
ls mypythonvenv/
bin  include  lib  lib64  pyvenv.cfg
```
Note: I add the name `mypythonvenv` into .gitignore.

Now I activate this virtual environment with `source`:

```
source  ./mypythonvenv/bin/activate
(mypythonvenv) (base) [rob@rob-Latitude-5590 mypython (⎈ |N/A:N/A)]$ 
```
Now I am working with this virtual environment.

You can deactivate a virtual environment by typing “deactivate” in your shell. 

I also have a `requirements.txt` file that holds:
```
kl==4.0.2
lint
```
It contains a list of all my dependencies that my application needs to function properly.

So people can choose to use my virtual environment ( download it ), or let people use to install the packages from requirements.txt! ( People still need to create a virtual environment first as a best practice )

So I install the packages with ( I am still in the virtual environment `mypythonvenv` ):
```
pip install -r requirements.txt
```
The output shows:

```
(mypythonvenv) (base) [rob@rob-Latitude-5590 mypython (⎈ |N/A:N/A)]$ pip install -r requirements.txt 
Collecting kl==4.0.2 (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/a1/67/f9f4ead41b1d4d04812e6b788f7680fad58f5d27c50f8d562a6812957a10/kl-4.0.2-py3-none-any.whl
Installing collected packages: kl
Successfully installed kl-4.0.2
```

## How to edit settings.json in Visual Studio Code?

https://supunkavinda.blog/vscode-editing-settings-json

Command pallette:
`Preferences: open workspace settings ( JSON)`
``
	"settings": {
		"python.pythonPath": "/media/rob/ubuntu_data/github/1robroos/mypython/mypythonvenv/bin/python3"
	}
```
The workspace settings file resides here ( for me ):
```
/home/rob/.config/Code/Workspaces/1599287804896/workspace.json
```

I still have a problem with flask :
```
from flask import Flask
```
In my test script the vscode editor warns me "unable to import flask"

SO I add flask into the requirements.txt and run this again:
```
pip install -r requirements.txt
```
flask will be installed in my virtual environment 
I have to save my python script to get rid of the "unable to import flask".



install vscode extension tag:debuggers @sort:installs flask  : Python Essentials
Now I can press F5 and select Flask and then I have to type my .py scriptname.
The debugging starts and the terminal shows:
```
source /media/rob/ubuntu_data/github/1robroos/mypython/mypythonvenv/bin/activate
 * Serving Flask app "mypytest.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


```


I can add a debug configuration names mypytest.py and it will create a configuration named launch.json in a .vscode directory 

It shows that my debug configuration is now saved:
```
   "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "mypytest.py",
```

