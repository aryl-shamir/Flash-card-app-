
# 🧠 Flash Card App for Learning English

This is a simple **Flash Card App** built using Python and Tkinter. It helps users (especially kids or beginners) to improve their English vocabulary by translating French words into English. This project was made with love for my junior brother to make language learning interactive and fun ❤️.

## 📸 Demo

![Flash Card Demo] (./assets/app_demo.gif)
---

## 🚀 Features

- Flip-card mechanism with a timer  
- Learn French-to-English vocabulary interactively  
- "I know this word" button removes known words from future sessions  
- Tracks and displays the user's score  
- Saves your progress so you don't repeat already learned words  

---

## 🗂 Folder Structure

```
project/
│
├── assets/                 # contains card_front.png, card_back.png, right.png, wrong.png, app_demo.gif
├── data/
│   ├── french_words.csv    # original dataset of words
│   ├── words_to_learn.csv  # dynamically updated based on known words
│   └── score_data.txt      # keeps track of score between sessions
│
├── main.py       # main app script, which is the main flash card app.py
├── README.md               # you're here!
```

---

## 🛠 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/flash-card-app.git
cd flash-card-app
```

2. **Install dependencies**:

```bash
pip install pandas pillow
```

3. **Run the app**:

```bash
python flash_card_app.py
```

---

## 📁 Data Format

Your `french_words.csv` should look like this:

```csv
French,English
partie,part
pomme,apple
livre,book
...
```

---

## 📌 Requirements

- Python 3.6 or above  
- `pandas`  
- `Pillow` (for image handling)  
- Tkinter (usually comes with Python)  

---

## 🧒 Why I Built This

I created this app to help my little brother build his English vocabulary in a more visual and interactive way. Instead of using paper flashcards, this app makes the learning process digital and fun!, and whenever i see a score of more than 60, he obtain a bottle of juice.

---

## 👨‍💻 Author

**Aryl Shamir**  
📍 Cameroon  
🎯 Aspiring Data Scientist & Builder of Fun Learning Tools  

---

## 🪪 License

This project is open source and free to use under the MIT License.

---

## 🙌 Acknowledgements

- Inspired by the 100 Days of Code course project from Angela Yu (Python Bootcamp)  
- Built with 💙 using Python and Tkinter

