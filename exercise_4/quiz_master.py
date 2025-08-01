from datetime import datetime

quiz_questions = {
     "science": {
         "easy": [{
                "question": "How old is the earth?", 
                "options": ["A. 5 billion years","B. 100 years","C. 2 million years","D. 2000 years"], 
                "answer": 0
             },
             {
                 "question": "What is the mass number of carbon?",
                 "options": ["A. 17", "B. 19", "C. 14", "D. 12"],
                 "answer": 3
             },
             {
                 "question": "What is the SI unit of time",
                 "options": ["A. the minute", "B. the hour", "C. 2 weeks", "D. second"],
                 "answer": 3
             },
             {
                 "question": "Who discovered electrons?",
                 "options": ["A. Sir. Gita", "B. Michael Faraday", "C. J.J. Thompson ", "D. Neils Bohr"],
                 "answer": 2
             },
             {
                 "question": "Planets originated from small particles called",
                 "options": ["A. Ions", "B. Fragments", "C. Planet fragments", "D. Planetismals"],
                 "answer": 3
             }],
         "hard": [...]
     },
     "history": {
         "easy": [{"question": "Q?", "options": ["A","B","C","D"], "answer": 0}],
         "hard": [...]
     },
     "sports": {
         "easy": [{"question": "Q?", "options": ["A","B","C","D"], "answer": 0}],
         "hard": [...]
     }
}

def take_quiz():
    print("\n=== QUIZ MASTER ===\n")
    
    categories = [category for category in quiz_questions]

    category = input(f"Select category from: {", ".join(categories)}: ").strip().lower()
    difficulty = input("Preferred difficulty(easy or hard): ").strip().lower()
    if (category not in categories) or (difficulty not in 'easyhard'):
        print("Please select from the provided options")
        return
    
    questions = quiz_questions[category][difficulty]
    num_quesions = len(questions)
    gotten_right = 0

    progress_bar = ['..','..','..','..','..']

    print(f"{"".join(progress_bar)} 00.0% complete")
    for i in range(num_quesions):
        start_time = datetime.now()

        is_correct = False
        question = questions[i]
        options = question["options"]
        correct_index = question["answer"]

        

        # prints the question number, question and options respectively
        print(f"\nQuestion {i+1}/{num_quesions}:\n  {question["question"]}\n    {"  ".join(options)}")

        answer = input("\nAnswer:  ")
        if answer.lower() not in "abcd":
            print(f"\nPlease enter just the letter corresponding to the correct answer.\nYou just lost the mark for question {i+1}!\n")
            continue
        for option in options:
            #checks if the answer entered matches the correct answer
            if options[correct_index].startswith(answer.strip().upper()):
                gotten_right += 1
                is_correct = True
                break
        
        duration = datetime.now() - start_time

        if not is_correct:
            print(f"❌ Wrong\n  Correct answer is: {options[correct_index]}")
        else:
            print(f"✅ Correct (+20 points)")
        print(f"Time: {duration.seconds:.1f} seconds")

        progress_bar[i] = '=='
        print(f"{"".join(progress_bar)} {((i+1)/5) * 100}% complete")

    final_score = gotten_right * 20
    print(f"\nFINAL SCORE: {final_score}/{num_quesions*20}  ({gotten_right}/{num_quesions} correct!)")
        



take_quiz()