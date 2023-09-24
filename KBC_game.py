# KBC game on console

questions = [
    "What is the capital of Bangladesh?",
    "When is the next world cup starting?",
    "How many years usually turtles live for?",
    "How does we measure water level?",
    "What is the purpose of learning coding?",
]

answers = [
    ["Dhaka", "Chittagong", "Khulna", "Rajshahi"],
    ["2022","2023","2024","2025"],
    ["100","105","110","115"],
    ["stethoscope","microscope","caloscope","barometer"],
    ["fun","joy","living","exitement"]

]

right = [ "a", "c", "d", "b", "c"]

prize = [500, 1000, 5000, 10000, 20000]

print("Lets start the game:\n")

for i in range(len(prize)):
    print( f"{i + 1}th question for taka {prize[i]} is: {questions[i]}\n")
    print(f"a. {answers[i][0]}    b.{answers[i][1]}\nc.{answers[i][2]}    d.{answers[i][3]}\n\n")
    ans = input("type your answer: ")
    if(ans == right[i]):
        print("Congratulations! You've won taka: ",prize[i])
        if(i<len(prize)-1):
            print("Do you wish to continue?\n")
            con = int(input("1:Yes   2:No\n"))
            if(con==1):
                continue
            else:
                print("You're going with taka: ",prize[i])
                break
    else:
        if(i>2):
            print("sorry, wrong answer. You're going with taka: ", prize[0])
        else:
            print("sorry, wrong answer. You're not recieving any money")
        break