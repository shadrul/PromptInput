# PromptInput
## Take command line input using Prompt


PromptInput is a python library built on top of "argparse".It allows you to ask for inputs from user with the relevant help text whenever you miss to pass that input with command.


## Features

- You don't need to worry about remembering the order of input anymore.
- PromptInput will ask for any input that you miss.
- By passing the default value you can also make an argument optional.


## Tech

PromptInput just uses built in argparse module of python and do not have any other dependency. 

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Python](https://python.org/) v3.6+ to run.

Install the library using pip.

```sh
pip install PromptInput
```

## Usage

Import PromptInput in your script.
```sh
from PromptInput import PromptInput
```

Make an object of PromptInput class.
```sh
parser = PromptInput()
```

Call add_argument method  and pass all these arguments accoring to usage.
```sh
parser.add_argument('var1',  type=str, nargs='?',
help='Enter var 1',default = "demo",count = 1,required = True)
```
## count 
It is passed with every argument to specify the position of a particular argument. It is used to later prompt the help for the correct input.

## required
It is only passed if the argument is required and there is no default value present and you want the user to input it in case it is left blank with command.

Calling parse_args method to get a namespace containing all the arguments
```sh
args = parser.parse_args()
print(args.var1)
```
## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/shadrul/PromptInput>
   [git-repo-url]: <https://github.com/shadrul/PromptInput>
   