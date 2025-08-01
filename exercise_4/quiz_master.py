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
         "hard": [{
                "question": " What is the most abundant gas in Earth’s atmosphere?", 
                "options": ["A.Oxygen","B. Nitrogen","C. Carbon","D. Helium"], 
                "answer": 1
             },
             {
                 "question": "Which element has the highest melting point?",
                 "options": ["A. Iron", "B. Tungsten", "C. Platinium", "D. Titanium"],
                 "answer": 1
             },
             {
                 "question": "What part of the cell is responsible for energy production?",
                 "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondrion", "D. Lysosome"],
                 "answer": 2
             },
             {
                 "question": " Which planet rotates the slowest on its axis?",
                 "options": ["A. Mercury", "B. Venus", "C. Earth", "D. Kumba"],
                 "answer": 1
             },
             {
                 "question": " What type of bond involves the sharing of electron pairs?",
                 "options": ["A. Ionic", "B. Metallic", "C. Hydrogen", "D. Covalent"],
                 "answer": 3
             }]
     },
     "history": {
         "easy": [
             {
        "question": "Who was the first President of the United States?",
        "options": ["A. Jefferson", "B. Washington", "C. Lincoln", "D. Adams"],
        "answer": 1
    },
    {
        "question": "Which ancient civilization built the pyramids?",
        "options": ["A. Romans", "B. Greeks", "C. Egyptians", "D. Persians"],
        "answer": 2
    },
    {
        "question": "What year did World War II end?",
        "options": ["A. 1945", "B. 1940", "C. 1939", "D. 1950"],
        "answer": 0
    },
    {
        "question": "Which explorer discovered America in 1492?",
        "options": ["A. Columbus", "B. Magellan", "C. da Gama", "D. Cook"],
        "answer": 0
    },
    {
        "question": "Which wall divided Berlin during the Cold War?",
        "options": ["A. Great Wall", "B. Iron Wall", "C. Berlin Wall", "D. Soviet Wall"],
        "answer": 2
    }
         ],
         "hard": [
             {
        "question": "Who was the British Prime Minister at the start of World War I?",
        "options": ["A. Churchill", "B. Lloyd George", "C. Asquith", "D. Chamberlain"],
        "answer": 2
    },
    {
        "question": "Which treaty ended the Thirty Years’ War?",
        "options": ["A. Versailles", "B. Utrecht", "C. Westphalia", "D. Tordesillas"],
        "answer": 2
    },
    {
        "question": "What year did the French Revolution begin?",
        "options": ["A. 1776", "B. 1789", "C. 1804", "D. 1812"],
        "answer": 1
    },
    {
        "question": "Who led the Haitian Revolution?",
        "options": ["A. Toussaint", "B. Dessalines", "C. Bolivar", "D. L’Ouverture"],
        "answer": 3
    },
    {
        "question": "Which empire was ruled by Emperor Ashoka?",
        "options": ["A. Gupta", "B. Mughal", "C. Maurya", "D. Chola"],
        "answer": 2
    }
         ]
     },
     "sports": {
         "easy": [{
        "question": "Which sport uses a bat and ball on a field with wickets?",
        "options": ["A. Baseball", "B. Cricket", "C. Golf", "D. Tennis"],
        "answer": 1
    },
    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": ["A. Germany", "B. Italy", "C. Brazil", "D. Argentina"],
        "answer": 2
    },
    {
        "question": "What sport does Serena Williams play?",
        "options": ["A. Tennis", "B. Basketball", "C. Swimming", "D. Cycling"],
        "answer": 0
    },
    {
        "question": "In which sport do players shoot hoops?",
        "options": ["A. Football", "B. Rugby", "C. Basketball", "D. Hockey"],
        "answer": 2
    },
    {
        "question": "Which sport is known for the Tour de France?",
        "options": ["A. Cycling", "B. Running", "C. Skiing", "D. Boxing"],
        "answer": 0
    }],
         "hard": [
             {
        "question": "Which country hosted the first modern Olympic Games in 1896?",
        "options": ["A. France", "B. Greece", "C. England", "D. Germany"],
        "answer": 1
    },
    {
        "question": "Which tennis player has won the most Grand Slam titles (singles) as of 2025?",
        "options": ["A. Nadal", "B. Federer", "C. Djokovic", "D. Sampras"],
        "answer": 2
    },
    {
        "question": "What is the national sport of Canada?",
        "options": ["A. Ice Hockey", "B. Lacrosse", "C. Baseball", "D. Basketball"],
        "answer": 1
    },
    {
        "question": "Which country won the ICC Cricket World Cup in 1992?",
        "options": ["A. India", "B. Australia", "C. England", "D. Pakistan"],
        "answer": 3
    },
    {
        "question": "In which sport would you perform a 'Triple Axel'?",
        "options": ["A. Diving", "B. Gymnastics", "C. Figure Skating", "D. Snowboarding"],
        "answer": 2
    }
         ]
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