# Word Counter
Word counter is a simple python script for counting words,
 lines or characters in a file or in standard input stream
 (which if a file is not specified is chosen as default)
## Installation
To be able to use this program simply download the [WordCounter.py](WordCounter.py) file. To work properly this program
requires that you have the [python interpreter](https://www.python.org/downloads/) installed too.
Next put the WordCounter.py file in a directory you would like to use it in.
## Usage
Assuming you have python installed and WordCounter.py where you would like to use it, open the terminal
 on your computer no specific shell required. Next type
 `python3` or `python2`(on linux systems `python` on windows) and then `WordCounter.py` to run the program. So an example use would look something like this:
 `python3 WordCounter.py -f examplefile.txt -cc -cw -cl`
 
 WordCounter allows you to use various options when using it, such as:
*  `-cc` or `--COUNTCHARS`
   This option makes the program count each alphabetic character appearing in your input
   (which can be a file or lines entered through your terminal)
*  `-cw` or `--COUNTWORDS`
   This option makes the program count each word in the input stream. The word is defined as a string
   of alphabetic characters separated by white spaces from other strings in the input.
*  `-cl` or `--COUNTLINES`
    This option makes the program count the amount of lines in the specified file(or standard input).
*   `-f`
    This option is used to specify a file on which you would like to use this program on.
*   `-h` or `--help`
    This option lists above options and quick descriptions about each of them.