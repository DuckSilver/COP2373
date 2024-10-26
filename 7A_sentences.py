import re

# scans and outputs the results of the analysis
def sentence_scan(paragraph):

    # pattern to identify sentences
    check = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    resultCount = re.findall(check, paragraph, flags=re.DOTALL | re.MULTILINE)

    # prints sentence count
    sentenceNum = len(resultCount)
    print(f"{sentenceNum} sentence(s) detected: ")
    print(" ")

    # prints all sentences
    for i in resultCount:
        print("->", i)

# main function
def main():

    # prompts user for paragraph
    paragraph = input("Please enter a paragraph: ")
    sentence_scan(paragraph)


main()



