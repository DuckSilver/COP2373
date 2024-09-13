# Alex Lewis / Assignment 1B
# The system simulates a magic 8 ball. Giving the user a random yes/no answer
import random
def main():

    def eightball():
        # creating/opening the txt file
        file1 = open("8ball_responses.txt", "w")

        # writes the possible outputs of the program to the txt file
        file1.write("Yes, of course! \n")
        file1.write("Without a doubt, yes. \n")
        file1.write("You can count on it. \n")
        file1.write("For sure! \n")
        file1.write("Ask me later! \n")
        file1.write("I'm not sure. \n")
        file1.write("I can't tell you right now. \n")
        file1.write("I'll tell you after my nap. \n")
        file1.write("No way! \n")
        file1.write("I don't think so. \n")
        file1.write("Without a doubt, no. \n")
        file1.write("The answer is clearly NO! \n")

        file1.close()


        # reads the txt file onto a list: ball
        file1 = open("8ball_responses.txt", "r+")

        data = file1.read()
        ball = data.split("\n")

        # function which selects then prints a random response from the list
        def answer():
            num = random.randint(0,11)
            print("........")
            print(ball[num])
            print()

        # prompts the user to use the 8 ball
        cont = input('Ask the magic 8 ball a question... ("n" to end): ')
        while cont != "n":
            answer()
            cont = input("Continue? (y/n): ")




    eightball()

main()

