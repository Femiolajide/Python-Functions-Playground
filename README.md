# **Python Functions Playground**

Welcome! 👋  

This is my personal coding space where I practise writing python functions  just for fun, learning, and skill-building.  Each function here represents a small problem I decided to solve or an idea I wanted to try out from scratch.  

## **Table of Contents**
1. [INTRODUCTIN](#python-functions-playground)
2. [NUMBER_TO_WORDS](#1-num_to_words)
---

## 🧩 What You’ll Find Here

- Simple, well-documented python functions that perform useful or interesting tasks.  
- A growing collection of code snippets that reflect how I think through problems.  
- Example usages to make it easy for anyone to understand and try them out.  

---

## 💡 Why This Project?

I created this project to keep sharpening my problem-solving skills in python and hopefully inspires others to do the same. I believe that the best way to learn is by creating something, even if it's just small random ideas. 

---

## ⚙️ How to Use

1. Clone or download this repository.  
2. Open any Python file in your preferred editor or Jupyter notebook.  
3. Explore the examples or try the functions with your own data.  

```bash
git clone https://github.com/Femiolajide/python-functions-playground.git
```

---

## 🚀 Future Plans

- Add new functions regularly, covering different areas like:
  - Math and logic
  - String and text manipulation
  - Date and time utilities
  - Data handling and processing  
- Group functions by category for easier access.  
- Write unit tests to ensure accuracy and reliability.
- Possibly turn this into a small python package in the future.


## **1. num_to_words()**

**Description:**

`num_to_words(a)` converts an integer into its full English word  from 1 up to 999,999,999,999,999,999,999,999,999,999,999 (nonillion). This function was built purely with python’s basic features (no external libraries), using string manipulation, nested functions, and conditional logic. The logic works by splitting the number into groups of three digits (hundreds, thousands, millions, etc.), then converting each group recursively and combining them with the correct scale names.


**Features:**

- Accepts one positional argument, an integer between `1` and `999,999,999,999,999,999,999,999,999,999,999 `.
- Converts numbers to proper English text
- Supports large numbers up to `nonillion`.
- Raises `TypeError` when a non-integer is passed in.
- Easy to extend for even larger scales in the future.


**Source Code:**  
Click [here](variety.py#L1-L302) to view the sourse code

**View Notebook Demo:**  

Click [here](https://github.com/Femiolajide/Python-Functions-Playground/blob/main/demo_notebook.ipynb) to view the notebook demo



**Run Notebook Demo:**  
Click [here](https://mybinder.org/v2/gh/Femiolajide/Python-Functions-Playground/HEAD?filepath=demo_notebook.ipynb
) to **run** the usage example in the demo notebook