# 🧠 Quiz Game

> A clean, dark-themed desktop quiz application built with Python & Tkinter.

---

## ✨ Features

- Multiple-choice questions with radio button selection
- Real-time score tracking
- Warning on unanswered questions
- Final score summary on completion
- Sleek dark UI (`#121212` background, `#00ff99` accents)

---

## 📁 Project Structure

```
quiz-game/
├── main.py          # App entry point & event logic
├── ui.py            # Tkinter UI layout & widgets
├── logic.py         # Quiz state management
├── questions.py     # Question bank
└── requirements.txt # Dependencies (none external)
```

---

## 🚀 Getting Started

**Requirements:** Python 3.x (Tkinter is included in the standard library)

```bash
# Clone or download the project, then run:
python main.py
```

---

## 🎮 How to Play

1. Read the question displayed on screen
2. Select one of the four options
3. Click **Next** to confirm your answer
4. Your score updates live after each question
5. A final score popup appears when the quiz ends

---

## 🛠️ Adding Questions

Open `questions.py` and add entries to the `questions` list:

```python
{
    "question": "Your question here?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option A"
}
```

---

## 📸 UI Preview

| Element        | Style                          |
|----------------|-------------------------------|
| Background     | Dark `#121212`                |
| Accent Color   | Neon green `#00ff99`          |
| Font           | Arial, Bold                   |
| Window Size    | 700 × 500 px                  |

---
## Author:
***yash kumar singh***

---
*Built with ❤️ using Python & Tkinter — no external dependencies required.*
