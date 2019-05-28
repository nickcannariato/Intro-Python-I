"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

from os.path import abspath, dirname


def read_and_print(file_path):
    """Open a file print it to the console

    Args:
        file_path: String -- A path-like object pointing to the file you'd like to read
    """
    with open(file_path, 'r') as f:
        for line in f:
            print(line)


def write_lines(file_path, text_to_write):
    """Overwrite a file with either a string or an array of strings

    Args:
        file_path: String -- A path-like object pointing to the file you'd like to write to (will create a new file if not found)
        text_to_write: Array or String -- The text you would like written to the file found at file_path
    """
    if isinstance(text_to_write, list) is False:
        text_to_write = text_to_write.split('\n')

    with open(file_path, 'w') as f:
        for line in text_to_write:
            f.write(f'{line}\n')


def main():
    # Default lines List
    lines = [
        'To be, or not to be, that is the question:',
        "Whether 'tis nobler in the mind to suffer",
        'The slings and arrows of outrageous fortune'
    ]

    # Path to the directory of the module
    base_path = dirname(abspath(__file__))

    # Open up the "foo.txt" file (which already exists) for reading
    # Print all the contents of the file, then close the file
    read_and_print(f'{base_path}/foo.txt')

    # Open up a file called "bar.txt" (which doesn't exist yet) for
    # writing. Write three lines of arbitrary content to that file,
    # then close the file. Open up "bar.txt" and inspect it to make
    # sure that it contains what you expect it to contain
    write_lines(f'{base_path}/bar.txt', lines)
    read_and_print(f'{base_path}/bar.txt')

    # OPTIONAL: see how write_lines() can handle both strings and arrays
    # lines2 = 'this is\njust\na string'
    # write_lines(f'{base_path}/baz.txt', lines2)
    # read_and_print(f'{base_path}/baz.txt')


if __name__ == '__main__':
    main()
