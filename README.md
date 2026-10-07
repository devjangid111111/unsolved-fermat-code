# The Python Code That No Computer Can Solve (Fermat's Style) 🧮

This repository contains a Python script designed based on **Fermat's Last Theorem**. Mathematically, it is structured to search for a counterexample to the theorem, meaning it will run in an infinite loop forever because no such solution exists!

## 🧠 The Mathematical Concept

Fermat's Last Theorem states that no three positive integers \(x\), \(y\), and \(z\) can satisfy the equation:
\[x^n + y^n = z^n\]
for any integer value of \(n\) greater than 2 (\(n > 2\)).

Since Andrew Wiles proved this theorem in 1994, we know for a fact that this equation has **zero** solutions. This Python script systematically checks all possible combinations of \(x\), \(y\), \(z\), and \(n\). Because it will never find a match, **no computer on Earth can ever finish executing this program successfully.**

## 🚀 How to Run (If you dare to try)

To run this infinite mathematical search engine on your local machine, make sure you have Python installed, then follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory:
   ```bash
   cd unsolved-fermat-code
   ```
3. Run the code:
   ```bash
   python main.py
   ```

## ⚠️ Warning
This program will utilize CPU cycles indefinitely as it keeps searching deeper into infinite numbers. You will need to manually stop it using `Ctrl + C`.
