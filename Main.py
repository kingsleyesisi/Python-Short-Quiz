import json

 with open("data.json", 'r') as file:
     content = file.read()

 data = json.loads(content)



 score = 1



 for question in data:

     print(question['questions_text'])

     for index, alternative in enumerate(question['alternatives']):

         print(index + 1, "-", alternative)

     user_choice = int(input('Enter your answer: '))

     question['user_choice'] = user_choice

     if question["user_choice"] == question["correct_answer"]:

         print('Correct')

         score = score + 1



 for index, question in enumerate(data):

     message = (f" your your answer: {question['user_choice']}, "

                f"Correct Answer: {question['correct_answer']}")

     print(index +1, '-', message)

 print(f"Your score is {score}/{len(data)}")

