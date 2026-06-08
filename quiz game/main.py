from tkinter import messagebox

from ui import (
    root,
    question_label,
    buttons,
    selected_option,
    next_btn,
    score_label
)

import logic


def load_question():

    selected_option.set("")

    current_question = logic.get_question()

    question_label.config(
        text=current_question["question"]
    )

    for i in range(4):

        buttons[i].config(
            text=current_question["options"][i],
            value=current_question["options"][i]
        )


def next_question():

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select an option!"
        )
        return

    logic.check_answer(selected)

    score_label.config(
        text=f"Score: {logic.score}"
    )

    logic.next_question()

    if logic.quiz_finished():

        messagebox.showinfo(
            "Quiz Finished",
            f"Final Score: {logic.score}"
        )

        root.destroy()

    else:
        load_question()


next_btn.config(command=next_question)

load_question()

root.mainloop()