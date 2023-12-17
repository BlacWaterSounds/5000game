import tkinter as tk
from tkinter import messagebox

def check_answers():
    sscore = 0
    answer = "Power over Ethernet"
    sscore = 0
    b = entry1.get()
    if b == answer:
        sscore += 1
    answer = "Voice over IP"
    b = entry2.get()
    if b == answer:
        sscore += 1
    answer = "crossover cable"
    b = entry3.get()
    if b == answer:
        sscore += 1
    if sscore == 3:
        messagebox.showinfo("Congratulations!", "You answered all questions correctly! 🎉🎉🎉")
    else:
        messagebox.showinfo("Results", "Thank you for playing the game! Your score is " + str(sscore) + " out of 3.")

root = tk.Tk()
root.title("Quiz Game")

label1 = tk.Label(root, text="What is your name?")
label1.pack()

entry0 = tk.Entry(root)
entry0.pack()

label6 = tk.Label(root, text=" ")
label6.pack()

label7 = tk.Label(root, text="Answer the following questions:")
label7.pack()

label8 = tk.Label(root, text=" ")
label8.pack()

label9 = tk.Label(root, text="What does PoE stand for?")
label9.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text=" ")
label2.pack()

label10 = tk.Label(root, text="What does VoIP stand for?")
label10.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text=" ")
label3.pack()

label11 = tk.Label(root, text="A cable used to connect two like devices without a distribution device?")
label11.pack()

entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text=" ")
label4.pack()

button1 = tk.Button(root, text="Submit", command=check_answers)
button1.pack()

label5 = tk.Label(root, text=" ")
label5.pack()

root.mainloop()
