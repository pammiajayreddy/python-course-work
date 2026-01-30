def run_quiz():
    print("🧪 Welcome to the Python Interview Prep Quiz Game!\n")

    questions = [
        {
            "question": "What is the output of: print(2 ** 3)?",
            "options": {
                "a": "6",
                "b": "8",
                "c": "9",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "Which data type is used to store True or False values?",
            "options": {
                "a": "int",
                "b": "str",
                "c": "bool",
                "d": "float"
            },
            "answer": "c"
        },
        {
            "question": "What keyword is used to handle exceptions in Python?",
            "options": {
                "a": "catch",
                "b": "try",
                "c": "handle",
                "d": "error"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of: print(10 // 3)?",
            "options": {
                "a": "3.33",
                "b": "3",
                "c": "4",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "Which collection allows duplicate values?",
            "options": {
                "a": "set",
                "b": "tuple",
                "c": "dictionary",
                "d": "list"
            },
            "answer": "d"
        },
        {
            "question": "Which keyword is used to create a class in Python?",
            "options": {
                "a": "function",
                "b": "define",
                "c": "class",
                "d": "object"
            },
            "answer": "c"
        },
        {
            "question": "What is the output of: print(type(10.5))?",
            "options": {
                "a": "<class 'int'>",
                "b": "<class 'float'>",
                "c": "<class 'double'>",
                "d": "<class 'decimal'>"
            },
            "answer": "b"
        },
        {
            "question": "Which loop is best when the number of iterations is known?",
            "options": {
                "a": "while",
                "b": "do-while",
                "c": "for",
                "d": "infinite"
            },
            "answer": "c"
        },
        {
            "question": "What does the break statement do?",
            "options": {
                "a": "Skips one iteration",
                "b": "Stops the loop",
                "c": "Ends the program",
                "d": "Restarts the loop"
            },
            "answer": "b"
        },
        {
            "question": "Which operator is used for logical AND?",
            "options": {
                "a": "&",
                "b": "&&",
                "c": "and",
                "d": "AND"
            },
            "answer": "c"
        },
        {
            "question": "What is the output of: print(len('Python'))?",
            "options": {
                "a": "5",
                "b": "6",
                "c": "7",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "Which function converts a string to an integer?",
            "options": {
                "a": "str()",
                "b": "int()",
                "c": "float()",
                "d": "bool()"
            },
            "answer": "b"
        },
        {
            "question": "Which symbol is used for membership testing?",
            "options": {
                "a": "in",
                "b": "is",
                "c": "==",
                "d": "!="
            },
            "answer": "a"
        },
        {
            "question": "What is the output of: print(bool(''))?",
            "options": {
                "a": "True",
                "b": "False",
                "c": "None",
                "d": "Error"
            },
            "answer": "b"
        },
        {
            "question": "Which keyword is used to return a value from a function?",
            "options": {
                "a": "break",
                "b": "stop",
                "c": "return",
                "d": "yield"
            },
            "answer": "c"
        },
        {
            "question": "What does the continue statement do?",
            "options": {
                "a": "Stops the loop",
                "b": "Ends the program",
                "c": "Skips current iteration",
                "d": "Repeats the loop"
            },
            "answer": "c"
        },
        {
            "question": "Which of the following is a valid variable name?",
            "options": {
                "a": "2value",
                "b": "value_2",
                "c": "value-2",
                "d": "value 2"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of: print(5 == 5.0)?",
            "options": {
                "a": "False",
                "b": "Error",
                "c": "True",
                "d": "None"
            },
            "answer": "c"
        },
        {
            "question": "Which function is used to get user input?",
            "options": {
                "a": "scan()",
                "b": "input()",
                "c": "read()",
                "d": "get()"
            },
            "answer": "b"
        },
        {
            "question": "What is the output of: print(type(None))?",
            "options": {
                "a": "<class 'null'>",
                "b": "<class 'None'>",
                "c": "<class 'NoneType'>",
                "d": "<class 'void'>"
            },
            "answer": "c"
        }
    ]

    score = 0

    for i in range(len(questions)):
        q = questions[i]
        print(f"Question {i + 1}: {q['question']}")
        for option in q["options"]:
            print(f"{option}) {q['options'][option]}")
        user_answer = input("Your answer (a/b/c/d): ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")

    print(f"🎯 Your Final Score: {score}/{len(questions)}")

    if score >= 15:
        print("🎉 Excellent! You're interview-ready!")
    elif score >= 10:
        print("👍 Good job! Keep practicing!")
    else:
        print("📘 Keep learning! Practice makes perfect.")


run_quiz()
