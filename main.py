
def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = list(text)
    count_by_char = {}

    for char in chars:
        default_char = char.lower()
        if (default_char in count_by_char):
            count_by_char[default_char]+=1
        else:
            count_by_char[default_char]=1

    return count_by_char

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(count_words(file_contents))
        print(count_chars(file_contents))

main()