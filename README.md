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
import cake

@cake.runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

echo.runCLI()
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
import cake

@cake.runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

if __name__ == '__main__':
    echo()
```
OR
```python
import cake

def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

if __name__ == '__main__':
    cake.run(echo)
```
And in your terminal
```bash
$ python echo.py hello world --capitalize
HELLO WORLD
```

## Documentation

### Decorators
 ```python
 def runnable(callback, args, print_output):
     pass
 ```

### Methods
 ```python
 def run(callback):
     pass
 ```
### Objects
```python
class Cake():
    def runnable(callback, args, print_output):
        pass
    def run(callback):
        pass
````
## Examples
A simple example:
```python
import cake

@cake.runnable
def echo(*args, capitalize = False):
    if capitalize:
        args = [a.upper() for a in args]
    print(' '.join(args))

echo.runCLI()
```
```bash
$ python echo.py hello world --capitalize
HELLO WORLD
```

### Multiple Methods
Using the Cake() object allows you to build runners that can handle multiple functions from the command line. The 'first' argument the script recieves (argv[1]) is interpreted as the name of the function, which can be set explicitly through the `name` parameter, or defaults to the method name.

Take the following code as `example.py`:
```python
import cake

cli = cake.Cake()

@cli.runnable
def echo(*args):
    return (' '.join([str(a) for a in args]))

@cli.runnable(name="add")
def sum(*args):
    _sum = 0
    for arg in args:
        _sum += arg
    return _sum

cli.run()
```
```bash
$ python example.py echo hello world
hello world

$ python example.py add 1 2 3 4 5
15
```

Defining a method as runnable also doesn't modify the `__call__` method for the decorated function, the only change with the wrapped function is it adds a callable `runCLI` attribute to the function that can be used to tell the program to parse the CLI args and execute the function based on those args. This lets us use @runnable decorated functions without having to modify dependent code
```python
import cake

cli = cake.Cake()

@cli.runnable
def sum(*args):
    _sum = 0
    for arg in args:
        _sum += arg
    return _sum

@cli.runnable
def doublesum(*args):
    return sum(*args) * 2 # sum function can be called like normal!

cli.run()
```
```bash
$ python example.py sum 1 2 3 4 5
15

$ python example.py doublesum 1 2 3 4 5
30
```
## Testing
From root, you can run the tests with
```bash
python -m cake.tests
```

## Build / Deploy
Install build dependencies locally:
```
pip install --user --upgrade twine setuptools wheel
```
Build source and distribution files:
```
python setup.py sdist bdist_wheel
```
upload to PyPi with Twine:
```
python -m twine upload dist/*
```
You'll be prompted to use `__token__` as the username, and you'll need to use an API token from PyPi as the password.

## Planned Features (todo)
- Add support for specifying explicit types, and code hydration for passing in lambdas
- Add support for input() based text interfaces in addition to just CLI args? (This is already decently well supported by just running the python interactively and importing the desired functions... will evaluate to see if there's actually a need here)
- Add option to wrap errors with 'pretty' printed output
- Add option to specify printed output stream
- Add more extensive testing / unit tests
- improved documentation
 ## Advanced Topics
 ### pyinstaller
 I'd recommend using `pyinstaller` if you want to generate standalone executable script builds in addition to cli-cake. Read more on there site [here]().