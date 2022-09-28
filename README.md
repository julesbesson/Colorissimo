# Colorissimo
## Description
A short program that runs a color test.  
## How to use
First download the whole repository and store it in a folder with path will be denominated by *path_to_folder*.
### Using python from terminal
Make sure you have installed the following packages:
- numpy
- matplotlib
- tkmacosx
Then run the file *colorissimo.py*, 
$ python -m /path_to_folder/colorissimo.py  
or  
$ cd /path_to_folder  
$ python -m colorissimo.py  
Then enjoy!
### Creating an app
An app can be created with the *py2app package* for a simpler use.
For this, install the *py2app* package, then type in terminal:  
$ cd path_to_folder  
$ rm -rf build dist  
$ python setup.py py2app -A  
The app should then be in the dist folder.
