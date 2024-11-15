import tkinter as tk
from tkinter import messagebox

def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    while not age.isdigit():
        print("Please enter a valid age.")
        age = input("Enter your age: ")
    
    python_knowledge = input("Enter your Python knowledge level (beginner, intermediate, advanced): ").lower()

    while python_knowledge not in ['beginner', 'intermediate', 'advanced']:
        print("Please enter a valid Python knowledge level (beginner, intermediate, advanced).")
        python_knowledge = input("Enter your Python knowledge level (beginner, intermediate, advanced): ").lower()

    return name, age, python_knowledge

user_name, user_age, user_python_level = get_user_info()

print(f"\nHello {user_name}, Age: {user_age}, Python Knowledge Level: {user_python_level.capitalize()}")

quiz_questions = [
    {
        "question": "Which of the following is used to define a block of code in Python language?",
        "options": ["Indentation", "Key", "Brackets", "All of the mentioned"],
        "answer": "a"
    },
    {
        "question": "All keywords in Python are in _________",
        "options": ["Capitalised", "Lower Case", "Upper Case", "None of the mentioned"],
        "answer": "d"
    },
    {
        "question": "Which of the following is the correct extension of the Python file?",
        "options": [".python", ".pl", ".py", ".p"],
        "answer": "c"
    },
    {
        "question": "Which of the following is used to define a block of code in Python language?",
        "options": ["Indentation", "Key", "Brackets", "All of the mentioned"],
        "answer": "a"
    },
    {
        "question": "Which of the following is the truncation division operator in Python?",
        "options": ["|", "//", "/", "%"],
        "answer": "b"
    },
    {
        "question": "What does the expression `'Python' * 3` evaluate to?",
        "options": ["PythonPythonPython", "Python3", "Python,Python,Python", "TypeError"],
        "answer": "a"
    },
    {
        "question": "Which of the following functions is a built-in function in Python?",
        "options": ["factorial()", "print()", "seed()", "sqrt()"],
        "answer": "b"
    },
    {
        "question": "What will be the output of the following Python function? min(max(False,-3,-4), 2,7)",
        "options": ["-4", "-3", "2", "False"],
        "answer": "d"
    },
    {
        "question": "Which of the following is not a core data type in Python programming?",
        "options": ["Tuples", "List", "Dictionary", "Class"],
        "answer": "d"
    },
    {
        "question": "Which one of the following is not a keyword in Python language?",
        "options": ["pass", "eval", "assert", "nonlocal"],
        "answer": "b"
    },
    {
        "question": "What will be the output of the following Python program?\n z=set('abc') \nz.add('san') \nz.update(set(['p', 'q'])) \nprint(z)",
        "options": ["{‘a’, ‘c’, ‘c’, ‘p’, ‘q’, ‘s’, ‘a’, ‘n’}", "{‘abc’, ‘p’, ‘q’, ‘san’}", "{‘a’, ‘b’, ‘c’, ‘p’, ‘q’, ‘san’}", "{‘a’, ‘b’, ‘c’, [‘p’, ‘q’], ‘san}"],
        "answer": "c"
    },
    {
        "question": "Which of the following statements is used to create an empty set in Python?",
        "options": ["( )", "[ ]", "{ }", "set()"],
        "answer": "d"
    },
    {
        "question": "To add a new element to a list we use which Python command?",
        "options": ["element1.addEnd(5)", "element1.addLast(5)", "element1.append(5)", "element1.add(5)"],
        "answer": "c"
    },
    {
        "question": "Which of the following is a Python tuple?",
        "options": ["{1, 2, 3} ", "{}", "[1, 2, 3]", "(1, 2, 3)"],
        "answer": "d"
    },
    {
        "question": "Which of the following statements create a dictionary?",
        "options": ["d = {}", "d = {“john”:40, “peter”:45}", "d = {40:”john”, 45:”peter”}", "All of the mentioned"],
        "answer": "d"
    },
    {
        "question": "Suppose d = {“john”:40, “peter”:45}, to delete the entry for “john” what command do we use?",
        "options": ["d.delete(“john”:40)", "d.delete(“john”)", "del d[“john”]", "del d(“john”:40)"],
        "answer": "c"
    },
    {
        "question": "What will be the output of the following Python code snippet? x = [i**+1 for i in range(3)]; print(x);",
        "options": [" [0, 1, 2]", "[1, 2, 5]", "error, **+ is not a valid operator", "error, ‘;’ is not allowed"],
        "answer": "a"
    },
    {
        "question": "Which of the following functions accepts only integers as arguments?",
        "options": ["ord()", "chr()", "min()", "any()"],
        "answer": "b"
    },
    {
        "question": "Which of the following functions does not throw an error?",
        "options": ["ord()", "ord(‘ ‘)", "ord(”)", "ord(“”)"],
        "answer": "b"
    },
    {
        "question": "To open a file c:\scores.txt for reading, we use _____________",
        "options": ["infile = open(“c:\scores.txt”, “r”)", "infile = open(“c:\\scores.txt”, “r”)", "infile = open(file = “c:\scores.txt”, “r”)", "infile = open(file = “c:\\scores.txt”, “r”)"],
        "answer": "b"
    },
    {
        "question": "Which of the following statements are true?",
        "options": ["When you open a file for reading, if the file does not exist, an error occurs", "When you open a file for writing, if the file does not exist, a new file is created", "When you open a file for writing, if the file exists, the existing file is overwritten with the new file", "All of the mentioned"],
        "answer": "d"
    },
    {
        "question": "What is the correct way to create a variable in Python?",
        "options": ["x = 10", "int x = 10", "var x = 10", "declare x = 10"],
        "answer": "a"
    },
    {
        "question": "What data type is the result of 5 / 2 in Python?",
        "options": ["Integer", "Float", "String", "Boolean"],
        "answer": "b"
    },
    {
        "question": "What will print(type(3.0)) output?",
        "options": [" <class 'int'>", "<class 'float'>", "<class 'string'>", "Error"],
        "answer": "b"
    },
    {
        "question": "Which of the following loops is used to iterate over a range of numbers?",
        "options": ["while", "do-while", "for", "if"],
        "answer": "c"
    },
    {
        "question": "What is the output of the following code? x = 10 if x > 5: print('Hello')",
        "options": ["10", "Hello", "Error", "Nothing"],
        "answer": "b"
    },
    {
        "question": "Which of the following statements will stop a loop in Python?",
        "options": ["break", "stop", "exit", "terminate"],
        "answer": "a"
    },
    {
        "question": "How do you define a function in Python?",
        "options": ["function myFunction():", "def myFunction():", "define myFunction():", "myFunction()"],
        "answer": "b"
    },
    {
        "question": "What will be the output of len('Python')?",
        "options": ["5", "6", "7", "Error"],
        "answer": "b"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to the PyQuiz!")
        self.root.geometry("1000x1000")
        self.root.config(bg="#5e5566")

        self.score = 0
        self.current_question = 0
        self.user_answers = []

        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 40),
            wraplength=700,
            justify="center",
            bg="#5e5566",      
            fg="#FFFFFF"       
        )
        self.question_label.pack(pady=60)

    
        self.answer_var = tk.StringVar()

        self.option_buttons = []
        for i in range(4): 
            button = tk.Radiobutton(root, text="Option", variable=self.answer_var, value="a", font=("Arial", 40), bg = "#5e5566", fg= "#FFFFFF", pady=10)
            button.pack(anchor="w")
            self.option_buttons.append(button)

     
        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font= ("Arial", 40), bg="#5e5566")
        self.next_button.pack(pady=30)

     
        self.load_question()

    def load_question(self):
        question_data = quiz_questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=chr(97 + i))

        self.answer_var.set("")

    def next_question(self):

        selected_answer = self.answer_var.get()
        correct_answer = quiz_questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(quiz_questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        if self.score >= 15 and self.score <= 29: 
            messagebox.showinfo("Quiz Result", f"Great attempt! You scored {self.score} out of {len(quiz_questions)}.")
        elif self.score >= 10 and self.score < 15: 
            messagebox.showinfo("Quiz Result", f"Good try! You scored {self.score} out of {len(quiz_questions)}.")
        elif self.score >= 0 and self.score < 10: 
            messagebox.showinfo("Quiz Result", f"Better luck next time! You scored {self.score} out of {len(quiz_questions)}.")
        
        self.root.quit()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()