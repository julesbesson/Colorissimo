# Colorissimo

## Description
A short program that runs a color test. I personnaly do not believe in such tests, but I did this to prevent my mother from buying a 500€ app from a quack. If you are into these "rits", you should consider taking a step back and look on what you are doing, why you are doing, and how is what you are doing coherent. Although it can be useful to help making a diagnosis on you mental state, it cannot possibly be as powerfull as described by its inventor.

## How to use
First download the whole repository and store it in a folder with path will be denominated by *path_to_folder*.

### Using python from terminal
Make sure you have installed the following packages:
- *numpy*
- *matplotlib*
- *tkmacosx* (if you work on mac)
 
Then run the file *colorissimo.py*, by typing in terminal:  
$ python -m /path_to_folder/colorissimo.py  
or  
$ cd /path_to_folder  
$ python -m colorissimo.py  
Then enjoy!

### Creating an app

#### On MacOs
An app can be created with the *py2app* package for a simpler use.
For this, install the *py2app* package, then type in terminal:  
$ cd path_to_folder  
$ rm -rf build dist  
$ python setup.py py2app -A  
The app should then be in the dist folder.

## Incoming changes
The programm shall be more complete, by allowing the practitioner to set his color preferences, his name, and also making a complete test with a pdf document for a report using LaTeX.
