import tkinter as tk
from tkinter import messagebox

questions = []
i = 0
score = 0

def add_question():
    if len(questions) < 5:
        questions.append([
            q.get(),
            a.get(),
            b.get(),
            c.get(),
            d.get(),
            ans.get().upper()
        ])
        q.delete(0, tk.END)
        a.delete(0, tk.END)
        b.delete(0, tk.END)
        c.delete(0, tk.END)
        d.delete(0, tk.END)
        ans.delete(0, tk.END)
        status.config(text=f"Added {len(questions)}/5 questions")
    else:
        messagebox.showinfo("Done", "Only 5 questions allowed")

def start_quiz():
    if len(questions) < 5:
        messagebox.showerror("Error", "Please add 5 questions first")
        return
    entry_frame.pack_forget()
    quiz_frame.pack()
    load_question()

def load_question():
    ques.config(text=questions[i][0])
    var.set(None)
    r1.config(text=questions[i][1], value="A")
    r2.config(text=questions[i][2], value="B")
    r3.config(text=questions[i][3], value="C")
    r4.config(text=questions[i][4], value="D")

def next_question():
    global i, score
    if var.get() == questions[i][5]:
        score += 1

    i += 1
    if i < 5:
        load_question()
    else:
        messagebox.showinfo("Result", f"Score: {score}/5")
        root.destroy()

root = tk.Tk()
root.title("Simple Online Quiz System")
root.geometry("400x400")

entry_frame = tk.Frame(root)
entry_frame.pack()

q = tk.Entry(entry_frame, width=40)
q.pack()
q.insert(0, "Question")

a = tk.Entry(entry_frame, width=40)
a.pack()
a.insert(0, "Option A")

b = tk.Entry(entry_frame, width=40)
b.pack()
b.insert(0, "Option B")

c = tk.Entry(entry_frame, width=40)
c.pack()
c.insert(0, "Option C")

d = tk.Entry(entry_frame, width=40)
d.pack()
d.insert(0, "Option D")

ans = tk.Entry(entry_frame, width=40)
ans.pack()
ans.insert(0, "Correct (A/B/C/D)")

tk.Button(entry_frame, text="Add Question", command=add_question).pack(pady=5)
tk.Button(entry_frame, text="Start Quiz", command=start_quiz).pack(pady=5)

status = tk.Label(entry_frame, text="Added 0/5 questions")
status.pack()

quiz_frame = tk.Frame(root)

ques = tk.Label(quiz_frame, text="", wraplength=300)
ques.pack()

var = tk.StringVar()

r1 = tk.Radiobutton(quiz_frame, variable=var)
r2 = tk.Radiobutton(quiz_frame, variable=var)
r3 = tk.Radiobutton(quiz_frame, variable=var)
r4 = tk.Radiobutton(quiz_frame, variable=var)

r1.pack(anchor="w")
r2.pack(anchor="w")
r3.pack(anchor="w")
r4.pack(anchor="w")

tk.Button(quiz_frame, text="Next", command=next_question).pack(pady=10)

root.mainloop()
