# CLI-cake

Easily pass CLI args into functions. Turn your functions into scripts.

CLI-cake takes this:
```python
import sys
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

caps = False
for arg in args:
    if arg == '--capitalize':
        caps = True
echo(sys.argv[1:], caps)
```
and turns it into this
```python
import clicake

@clicake.runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

echo()
```
```bash
$ python echo.py hello world --capitalize
HELLO WORLD
```

## Why

I realized that when I'm building quick, simple scripts for internal use, I resort to one of two approaches:

1) I just hardcode the values into my script, and just change the values each time I use it
2) I build out some type of custom CLI or gui interface for the script

Both of these approaches have downsides- with the first approach, you end up spending more time between runs editing code, and end up with the bad practice of directly editing your source code for non-permanent changes. With the second approach, you end up spending extra time up front writing code, and it can make concise scripts more messy by adding in this extra code.

clicake is a bunch of convenience methods that solve these problems, making it super quick and easy to transform your functions into fully-featured CLI-callable scripts.
## Installing

## Getting Started
clicake is really easy to use! Try creating the file 'echo.py' and add the following code:
```python
import clicake

@clicake.runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

if __name__ == '__main__':
    echo()
```
OR
```python
import clicake

def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

if __name__ == '__main__':
    clicake.run(echo)
```
And in your terminal
```bash
$ python echo.py hello world --capitalize
HELLO WORLD
```

## Documentation

### Decorators
 - runnable

### Methods
 - run