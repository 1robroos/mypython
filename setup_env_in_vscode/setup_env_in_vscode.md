# How to setup vscode for your python application

In your python script you might see some vscode comment that it is unable to import a library.

```
from kl import Kl, FileHandler, SpanishTransformer
from textblob import TextBlob
```

There are two remedies for resolving these so called 'dependencies' :

1 - Create a python virtual environment and install the missing libraries in it.
2 - import the missing libraries directly in your machine without a virtual environment.


## Creating a virtual environment

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
pylint
flask
textblob
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

With the command `pip install -r requirements.txt` the libraries will be installed and your dependencies will be resolved.
This way it is easy for other developers to 'adapt' your application to there own environment.




Now there is one more thing you need to do :

Go to ‘Command Palette’ en type “ Python: Select Interpreter” and you will see a list of multiple installed python versions. Pick the one from your just created virtual environment.
This will create a hidden direcory .vscode and in that directory it gives the file 'settings.json' and it looks like:

```
{
    "python.pythonPath": "mypythonvenv/bin/python"
}
```

This way the dependencies are resolved and you can run your app smoothly.


# # Debugging in vscode


Install the vscode extension `tag:debuggers @sort:installs flask  : Python Essentials`
Now I can press F5 and select Flask and then I have to type my .py scriptname.
The debugging starts and the terminal shows:
```
source /media/rob/ubuntu_data/github/1robroos/mypython/mypythonvenv/bin/activate
 * Serving Flask app "mypytest.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

I can add a debug configuration names mypytest.py and it will create a configuration named `launch.json` in a .vscode directory.  
Go to the debug extension and above at 'Run' you can add a configuration. Choose 'Flask' and give your app name again ( your python filename).



It shows that my debug configuration is now saved in .vscode/launch.json:
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

