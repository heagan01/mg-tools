# get_key_pressed.py #
Get pressed (released) key in Python.
Similar to the built-in *input()* function, but without hitting *ENTER (RETURN)*

## Prerequisites ##
None! No need to install any external package

## Supported platforms ##
1. Windows
2. Linux
3. MacOS (Tested on 10.14 Mojave)

## Supported Python version ##
Python 3.3 and above

## Usage ##
1. Download *get_key_pressed.py* and put it in your app's project directory
2. Import *get_key* function, which receives optional arguments: string *msg*, int/float *time_to_sleep*
    - If *msg* is not provided then it's "Press any key ..."
    - If *msg* is empty '', then no message will be printed
    - Default time to wait for keypress is *3 sec*

## Example  ##
```
from get_key_pressed import get_key
my_key = None
while not c:
        my_key = get_key("Choose your weapon ... ", 2)
print(my_key)
```

[get_key_pressed example](examples/get_key_pressed.py) - import from project package

## Caveats ##
The terminal window must remain active, you cannot switch to other windows while waiting for keypress.
To overcome this caveat, focus on the terminal window and hit CTRL+C
