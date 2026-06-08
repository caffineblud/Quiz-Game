import tkinter as tk

root = tk.Tk()

root.title("Modern Quiz Game")
root.geometry("700x500")
root.config(bg="#121212")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="QUIZ GAME",
    font=("Arial", 28, "bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=20)

# ---------------- SCORE ---------------- #

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14),
    bg="#121212",
    fg="#00ff99"
)

score_label.pack()

# ---------------- QUESTION ---------------- #

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    wraplength=600,
    bg="#121212",
    fg="white"
)

question_label.pack(pady=40)

# ---------------- OPTIONS ---------------- #

selected_option = tk.StringVar()

buttons = []

for i in range(4):

    btn = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 14),
        bg="#1e1e1e",
        fg="white",
        activebackground="#1e1e1e",
        activeforeground="#00ff99",
        selectcolor="#121212",
        padx=10,
        pady=10
    )

    btn.pack(fill="x", padx=120, pady=8)

    buttons.append(btn)

# ---------------- NEXT BUTTON ---------------- #

next_btn = tk.Button(
    root,
    text="Next",
    font=("Arial", 14, "bold"),
    bg="#00ff99",
    fg="black",
    padx=20,
    pady=10,
    borderwidth=0
)

next_btn.pack(pady=30)