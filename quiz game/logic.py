from questions import questions

question_index = 0
score = 0


def get_question():

    return questions[question_index]


def check_answer(selected):

    global score

    correct_answer = questions[question_index]["answer"]

    if selected == correct_answer:
        score += 1


def next_question():

    global question_index

    question_index += 1


def quiz_finished():

    return question_index >= len(questions)