
def countWords(words):
    return len(words.split())

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(countWords(file_contents))

main()