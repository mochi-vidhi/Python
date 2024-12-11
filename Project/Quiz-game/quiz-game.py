# Quiz application using python 

name = enNum = className = score  = None
questions = []

def askDetail():
    global name,enNum,className,score
    print("************** QUIZ GAME ****************")
    name = input("Enter Your Full Name: ")
    enNum = int(input("Enter Your enrollment number: "))
    className = input("Enter Your class: ")
    startQuiz = input("Enter Yes for start: ")
    startQuiz = startQuiz.capitalize()
    if(startQuiz=='Yes'):
        print("\nAll the best \U0001F44D \U0001F44D \U0001F44D...\n")
        print("Your Quiz is start Now.....\n ")
        quizStart()
        showDetails()
    
    else:
        print("\t\tExit...\U0001F60F \U0001F60F")

  
def quizStart():
    global questions,score
    questions = [
        {
          'prompt': "1.What does HTML stand for ?",
          'options': ["A. HyperText Markup Language","B. Home Tool Markup Language","C. Hyperlinks and Text Markup Language","D. HighText Machine Language"],
          'Answer': "A"
        },
        {
          'prompt': "2.Which HTML tag is used to create a hyperlink",
          'options': ["A. <link>","B. <a>" ,"C. <href>","D. <url>"],
          'Answer': "B" 
        },
        {
          'prompt': "3.What does CSS stand for?",
          'options':["A. Colorful Style Sheets","B. Cascading Style Sheets","C. Computer Style Sheets ","D. Creative Style Sheets "],
          'Answer': "B"
        },
        {
          'prompt':"4.Which is the correct way to comment in HTML?",
          'options':["A. // 'This is a comment","B. <!-- This is a comment -->","C. # This is a comment","D. /* This is a comment */"],
          'Answer': "B"
        },
        {
          'prompt':"5.Which CSS property is used to control the text size?",
          'options':["A. font-size","B. text-style","C. text-size","D. font-style"],
          'Answer': "A"
        },
        {
          'prompt':"6.Which is the correct CSS syntax to select an element with the class 'container' ?",
          'options':["A. #container {}","B. .container {}","C. container {}","D. *container {}"],
          'Answer':"B"
        }
    ]
    score = 0
    for question in questions:
        print(question['prompt'])
        print("\n")
        for options in question['options']:
            print(options)
        ans = input("\nEnter Your Answer (A,B,C or D): ").upper()
        if(ans == question['Answer']):
            print(f"{ans} is correct..\U0001F38A \U0001F38A \n")
            score+=1
        else:
            print(f"Your answer {ans} is  wrong \U0001F44E \U0001F44E \n")
            
             
def showDetails():
    global score
    print("\n\t\t****************************************")
    print(f"\t\tStudent name is: {name}")
    print(f"\t\tStudent Enrollment Number is: {enNum}")
    print(f"\t\tStudent class is: {className}")
    if score == len(questions):
        print(f"\t\tStudent score is {score} out of {len(questions)}")
        print("\n\t\tcongratulation \U0001F389 You pass with full marks \U0001F3C6 \U0001F389 \U0001F38A \U0001F38A	")
    elif score == 0:
        print("\n\t\tYou not attend quiz....\U0001F60F \U0001F60F")
    else:
        print(f"\t\tStudent score is {score} out of {len(questions)}")
    print("\n\t\t***************************************")
    


askDetail() 
