# Alex Lewis / Assignment 2A
# Determines the likelyhood an email is spam

# creates email and splits the email into a list
print("Please Input Your Email Below:")
email = input(" ")
words = email.split(" ")

# defines the spam words to check for
badWords = ("invoice new scam action free winner won"
            "hacked urgent verification required alert"
            "bank social refund danger help cheap"
            "deal spam watch savings save member"
            "membership hot sale cart account message")
bWords = badWords.split(" ")

# marks words is email to be spam or fine
def word_check():
    global spamWords
    num = 0
    x = len(words)
    rep = 0
    warn = 0
    fine = 0

    spamWords = []

    # checks each word
    while x != rep:
        rep += 1

        bNum = 0
        y = len(bWords)
        rep2 = 0

        # compares each word to spam words
        while y != rep2:
            rep2 += 1
            warnWord = bWords[bNum]

            if words[num].lower() == warnWord:
                warn += 1

                spamWords.append(warnWord)

                print(" ")
            else:
                fine += 1

            bNum += 1

        num += 1
    print(f"Spam Score: {warn}")

    print(f"Warn words: {spamWords}")

    # determines if an email is spam using spam score
    if warn == 0:
        print("Message is not spam")
    elif warn <= 1:
        print("Message is likely not spam")
    elif warn <= 3:
        print("Message may be spam")
    elif warn >= 4:
        print("Message is likely spam")
    else:
        print("Error: Unable to determine if message is spam")


word_check()