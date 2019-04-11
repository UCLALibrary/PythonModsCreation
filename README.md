
##### This repository is used to create mods from csv for Green Movement metadata which uses older column names.
# Installation
1. Download [Pycharm Community edition](https://download.jetbrains.com/python/pycharm-community-2019.1.1.exe)
2. Run the exe

## Open Project 

1. Check out an existing project from Version Control. [here](https://www.jetbrains.com/help/pycharm/quick-start-guide.html#checkout-from-vcs)
2. Then, enter a path to the sources and clone the repository to the local host
3. select the open directory option

## Configure project interpreter

#### Docs are [here](https://www.jetbrains.com/help/pycharm/quick-start-guide.html#interpreter)
1. You need to add and configure a project interpreter. In the Settings/Preferences dialog (Ctrl+Alt+S), [here](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
2. click Project Interpreter, then click Add project interpreter, and choose Add .... Depending on your project specifics you can select:
3. In the left-hand pane of the Add Python Interpreter dialog, select Virtualenv Environment. The following actions depend on whether the virtual environment existed before.
+ Specify the location of the new virtual environment in the text field, or click  Virtual environment location and find location in your file system. Note that the directory where the new virtual environment should be located, must be empty!
+ Choose the base interpreter from the list, or click Choose the base interpreter and find the base interpreter in the your file system.
+ Select the Inherit global site-packages checkbox if you want to inherit your global site-packages directory. This checkbox corresponds to the --system-site-packages option of the virtualenv tool.
+ Select the Make available to all projects checkbox, if needed.
4. [here](https://www.jetbrains.com/help/pycharm/project-interpreter.html)

## Run Code 

1. If creating mods for photos run photos.py file
2. Update the code to point to right spreadsheet file location and create the mods directory on Netapp and specify the path in the script.
3. The easiest way to run an application is to right-click its background in the editor, and then choose Run <name> from the context menu:
