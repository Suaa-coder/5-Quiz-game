# Python quiz game

questions = (" Which country is home to the official language of Swahili?: ",
           "Which of the following is a widely spoken language in Switzerland?:",
           "Which country is the setting for Gabriel Garcia Marquez's famous novel One Hundred Years of Solitude?:",
           "Which language is spoken by the most people worldwide as their first language? ",
           "Who is the author of the novel Pride and Predjudice?:")

options = (("A. Kenya", "B. India", "C. Argentina","D. Spain"),
           ("A. Dutch","B. French","C. Portoguese","D. finnish"),
           ("A. Peru","B. Brazi","C. Colombia","D. Mexico"),
           ("A. English","B. Hindi","C.Spanish","D. Mandarin Chinese"),
           ("A. Emily Bronte","B. Louisa May Alcott","C. jane Austen ","D. Mary Shelley"))

answers = ("A", "B", "C","D","C")
guesses = []
score = 0
question_num = 0
          
for question in questions:
    print("----------------------")
    print(question)

   guess = input ("Enter (A,B,C,D): ").upper()
   guesses.append(guess)
   if guess == answers[question_num]:
      score += 1
      print ("CORRECT!")
   else:
       print("INCORRECT!")
       print(f"{answers[question_num]} is the correct answer")
   question_num += 1

print("----------------------")
print("        RESULT        ")
print("----------------------")

print("answers:, end="")
for answer in answers:
    print(answer, end= "")
print()

print("guesses: ", end= "")
for guess in guesses:
    print (guess, end="")
print()


score = score/ len(questions) *100)
print (f"your score is : {score%"})

      
          
