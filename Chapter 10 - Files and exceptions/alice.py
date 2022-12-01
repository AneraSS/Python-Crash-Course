# handling the FileNotFound exception

# let's try to read a file that doesn't exist
def first_task():
    filename = 'alice.txt'

    with open(filename, encoding='utf-8') as f:
        contents = f.read()

    # f => instead of fileobject or file_object; f is by convention
    # encoding argumnent => pp. 197 => ne kuzim

#first_task()
# Python >> FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
# Py cannot find the file


def second_task():
    filename = 'alice.txt'
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' doesn't exist.")

#second_task()


# Analyzing text
# gutenberg.org
# let's pull in the text of Alice in Wonderland and try to count the number of words in the text.
# We'll use the string method "split()"
# "split()" can build a list of words from a string
# test it in Console; write:
    # title = "My name is Anera#
    # title.split()

#ATTTN! No file added due to no internet!
def third_task():
    filename = 'alice.txt'

    try:
        with open(filename, encoding='utf-8') as f: # ne znam sto znaci ovaj utf-8 ali se odnosi na ovaj folder u kojem jesam
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' doesn't exist.")
    else:
        # count the approx. number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")

#third_task()


# working with multiple files
# let's add more books to analyze
# move bulk of the program to a function called count_words() to easier run analysis for more books

#VER.1
def count_words(filename):
    """Count approximate number of words in the file."""
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print (f"The file {filename} has {num_words} words.")

# THIS IS FIRST VERSION OF CALLING:
#filename = 'alice.txt'
#count_words(filename)

# THIS IS SECOND VERSION CALLING:
# filenames = ['alice.txt', 'sidharta.txt', 'moby_dick.txt']
# for filename in filenames:
#     count_words(filename)



# * falling silently *
# to continue as nothing happened
def count_words_two(filename):
    """Count approximate number of words in the file."""
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass #print(f"Sorry, the file '{filename}' doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print (f"The file {filename} has {num_words} words.")


filenames = ['alice.txt', 'sidharta.txt', 'moby_dick.txt']
for filename in filenames:
    count_words_two(filename)