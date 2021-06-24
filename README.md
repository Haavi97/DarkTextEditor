# Dark Text Editor
> Simple dark text editor GUI using pyQT

I was a bit tired of the Notepad aplication that Windows has for the simple texts since it cannot be configured to be in dark mode. I know I can use some IDE like VSC but for simple things it is handy to have an easy launch simple text editor. That's why I have programmed this one. Also for fun of learning PyQT. 

## Usage

Just run the main file by typing:
```bash
python main.py
```

If you just one to have it as an executable you can use [```pyinstaller```](https://pypi.org/project/pyinstaller/) that can be installed using pip:

```bash
pip install pyinstaller
```

And then run:
```bash
pyinstaller main.py 
```
That will generate the desired .exe file in Windows. 
## Supported encodings
- ```utf-8```
- ```utf-16```
- ```utf-32```
- ```ascii```
- ```ansi```
- ```cp775```, baltic languages


## TODO
 - [ ] Changeable default font
 - [X] App icon (https://programmersought.com/article/86065821752/)
 - [X] Copy-paste erase format
 - [X] Add functionality to change encoding button
 - [X] Add encoding at the bottom
 - [X] Fix opening of file. Fails to open in unicode
 - [ ] Order and clean code
 - [X] Add Ctrl+s functionality
 - [ ] Start optimization
 - [X] Add notification if closing and there is text not saved. 
 - [ ] Fix status bar disappearing content

## Contact
Email: <fortin@taltech.ee>