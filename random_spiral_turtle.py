Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/larso/OneDrive/Desktop/Past Projects/random spiral turtle.py
Traceback (most recent call last):
  File "C:/Users/larso/OneDrive/Desktop/Past Projects/random spiral turtle.py", line 7, in <module>
    (i)
NameError: name 'i' is not defined
>>> 
= RESTART: C:/Users/larso/OneDrive/Desktop/Past Projects/random spiral turtle.py
Traceback (most recent call last):
  File "C:/Users/larso/OneDrive/Desktop/Past Projects/random spiral turtle.py", line 13, in <module>
    t.forward(i/2)
  File "C:\Users\larso\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1638, in forward
    self._go(distance)
  File "C:\Users\larso\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 1606, in _go
    self._goto(ende)
  File "C:\Users\larso\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 3159, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\larso\AppData\Local\Programs\Python\Python39\lib\turtle.py", line 756, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\larso\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2763, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 