## Python3 Preprocessor
This is a basic preprocessor addon for python3. It allows for C-like preprocessor directives to be added to a program. You can add preprocessor directives at the start of a program like this:
```
#def fun def
#def word "str"
#def num 6
```
Included in this repository is `setup.sh`, a bash script that sets up a permanent location and alias for the preprocessor script called `piethon` (a probably temporary alias name for now). Also included is an example python file with preprocessor directives in it, `test.py`, which has C-like syntax rather than pythonic syntax for demonstration purposes.
## Usage Syntax
```
$ piethon file.py [--proc] [--show] [--orig]
	--proc: shows the registered preprocessor directives at runtime
	--show: show the program file after the preprocessor directives have been applied
	--orig: show the original program file before any preprocessing
```


I'm not sure how much time I'll be putting into this, but if there are any issue requests I'll do my best to tackle them!

Much love,

R3IXY (https://r3ixy.com)
