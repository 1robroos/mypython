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

# pipenv and anaconda

You can also use pipenv or anaconda for your virtual environemnts  
See: https://www.datacamp.com/community/tutorials/virtual-environment-in-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=255798340456&utm_targetid=aud-390929969673:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9064418

Here some try outs of my own, just to have a history of what I tried:

```
brew install pipenv

Updating Homebrew...
==> Auto-updated Homebrew!
Updated 2 taps (aws/tap and homebrew/core).

==> Installing aws/tap/aws-sam-cli

...

==> Caveats
Python has been installed as
  /home/linuxbrew/.linuxbrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /home/linuxbrew/.linuxbrew/opt/python@3.8/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /home/linuxbrew/.linuxbrew/lib/python3.8/site-packages



See: https://docs.brew.sh/Homebrew-and-Python
==> pipenv
Bash completion has been installed to:
  /home/linuxbrew/.linuxbrew/etc/bash_completion.d
==> python@3.7
Python has been installed as
  /home/linuxbrew/.linuxbrew/opt/python@3.7/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /home/linuxbrew/.linuxbrew/opt/python@3.7/libexec/bin

You can install Python packages with
  /home/linuxbrew/.linuxbrew/opt/python@3.7/bin/pip3 install <package>
They will install into the site-package directory
  /home/linuxbrew/.linuxbrew/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python
...
==> Installing pipenv
...


python@3.7 is keg-only, which means it was not symlinked into /home/linuxbrew/.linuxbrew,
because this is an alternate version of another formula.

If you need to have python@3.7 first in your PATH run:
  echo 'export PATH="/home/linuxbrew/.linuxbrew/opt/python@3.7/bin:$PATH"' >> ~/.profile

For compilers to find python@3.7 you may need to set:
  export LDFLAGS="-L/home/linuxbrew/.linuxbrew/opt/python@3.7/lib"
  export CPPFLAGS="-I/home/linuxbrew/.linuxbrew/opt/python@3.7/include"
```




(base) [rob@rob-Latitude-5590 ~ (⎈ |N/A:N/A)]$ cd /home/linuxbrew/.linuxbrew/opt/python@3.8/libexec/bin
(base) [rob@rob-Latitude-5590 bin (⎈ |N/A:N/A)]$ lt
total 0
lrwxrwxrwx 1 rob rob 26 jul 20 15:26 python-config -> ../../bin/python3.8-config
lrwxrwxrwx 1 rob rob 19 jul 20 15:26 python -> ../../bin/python3.8
lrwxrwxrwx 1 rob rob 18 jul 20 15:26 pydoc -> ../../bin/pydoc3.8
lrwxrwxrwx 1 rob rob 17 jul 20 15:26 idle -> ../../bin/idle3.8
lrwxrwxrwx 1 rob rob 26 sep  6 10:14 easy_install -> ../../bin/easy_install-3.8
lrwxrwxrwx 1 rob rob 16 sep  6 10:14 wheel -> ../../bin/wheel3
lrwxrwxrwx 1 rob rob 14 sep  6 10:14 pip -> ../../bin/pip3
(base) [rob@rob-Latitude-5590 bin (⎈ |N/A:N/A)]$ ./python -V
Python 3.8.5
(base) [rob@rob-Latitude-5590 bin (⎈ |N/A:N/A)]$ pwd
/home/linuxbrew/.linuxbrew/opt/python@3.8/libexec/bin
(base) [rob@rob-Latitude-5590 bin (⎈ |N/A:N/A)]$ ./python -V
Python 3.8.5



## Anaconda distribution

Data scientists tend to use Anaconda distribution, which comes with many useful pre-installed packages, which are easy to install and manage

## Pipenv

A web developer who uses Django, Flask, and other Python-related frameworks can use Pipenv as their Virtual Environment.

### Pipenv is a new and popular way of automatically creating a 'virtualenv' for the project. 

- It creates a Pipfile, which helps to manage the package and can be installed or removed easily. 
- Through Pipenv, 'pip' and 'virtualenv' can be used together to create a Virtual Environment, 
- Pipfile works as the replacement of the 'requirement.txt.' which tracks the package version according to the given project.

$ which pipenv
/home/linuxbrew/.linuxbrew/bin/pipenv

brew I had installed because of sam cli. zie https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html : The recommended approach for installing the AWS SAM CLI on Linux is to use the Homebrew package manager.

Now I also installed pipenv with brew



### Creating a virtualenv for the project. It will reside in ~/.local/share/virtualenvs

For creating the 'virtualenv' for the project, use the following command.  

`pipenv shell` : The command 'pipenv' creates a new 'virtualenv' for the project along with Pipfile side by side.
```
$ pipenv shell
Creating a virtualenv for this project…
Pipfile: /media/rob/ubuntu_data/github/1robroos/vscodetest2/Pipfile
Using /home/linuxbrew/.linuxbrew/bin/python3 (3.8.5) to create virtualenv…
⠋ Creating virtual environment...created virtual environment CPython3.8.5.final.0-64 in 580ms
  creator CPython3Posix(dest=/home/rob/.local/share/virtualenvs/vscodetest2-MG3I48HY, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/rob/.local/share/virtualenv)
    added seed packages: pip==20.2.1, setuptools==49.2.1, wheel==0.34.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /home/rob/.local/share/virtualenvs/vscodetest2-MG3I48HY
requirements.txt found, instead of Pipfile! Converting…
✔ Success! 
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
Launching subshell in virtual environment…
 . /home/rob/.local/share/virtualenvs/vscodetest2-MG3I48HY/bin/activate
(base) [rob@rob-Latitude-5590 vscodetest2 (⎈ |N/A:N/A)]$  . /home/rob/.local/share/virtualenvs/vscodetest2-MG3I48HY/bin/activate
(vscodetest2) (base) [rob@rob-Latitude-5590 vscodetest2 (⎈ |N/A:N/A)]$ 
```


```
$ pipenv install requests
Installing requests…
Adding requests to Pipfile's [packages]…
✔ Installation Succeeded 
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (dc979a)!
Installing dependencies from Pipfile.lock (dc979a)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 20/20 — 00:00:07
```

You can use the following command to deactivate form the current environment. `exit` 

