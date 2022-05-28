# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("C:/Users/HP/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt","r") as filename:
        readfile = filename.read()
        return readfile
read_file_content("C:/Users/HP/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt")


def count_words():
    text = read_file_content("C:/Users/HP/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    x = text.split()
    count = {}
    for i in x:
        if i in count:
            count[i]
        else:
            count[i] = 1
    return count
print(count_words())