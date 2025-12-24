# 📊 Stock Portfolio Tracker
A simple console-based Stock Portfolio Tracker built in Python. This program calculates the total investment value based on user-entered stock names and quantities using manually defined stock prices. It allows users to interactively build a portfolio, view individual and total investment values, and optionally save the results to a .txt or .csv file. The project focuses on core Python fundamentals such as dictionaries, input/output operations, arithmetic calculations, and basic file handling.

## 🎯 Goal
Build a simple stock portfolio tracker in Python that calculates the total investment value based on user-selected stocks and quantities using predefined stock prices.

## ⭐ Features
- Hardcoded dictionary of stock prices for quick lookup
- User input for stock names and share quantities
- Validation for unavailable stocks and invalid quantities
- Real-time calculation of individual stock value
- Displays total investment amount
- Option to save portfolio data as .txt or .csv file

## 🧠 Key Concepts Used
- Dictionaries for storing stock prices
- User input and output handling
- Basic arithmetic calculations
- File handling for saving results

## 🛠 Tech Stack
**Language :** Python

**Environment :** Terminal/Command Line

## 📂 Project Structure
``` bash
CodeAlpha_StockPortfolioTracker/
│
├── StockPortfolioTracker.py   # Main program file
└── README.md                  # Documentation
```

## 📥  Installation
Clone the repository using Git : 
```bash
  git clone https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker
cd CodeAlpha_StockPortfolioTracker
```

## 🖥 Run Locally
Navigate to the location of your file :
```bash
  cd CodeAlpha_StockPortfolioTracker
```
Run the script :
```bash
 python StockPortfolioTracker.py
```

## 🎥 Demo
*A video demonstration of the Stock Portfolio Tracker showing the complete working of the program, including user input, investment calculation, and file saving functionality.*

 [ ▶ click here to view the demo video of the stock portfolio tracker ](https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker/releases/tag/v1.0)

## 📝 Usage / Example
When the program runs, it prompts the user to enter stock names and quantities as shown below :
``` bash
Enter stock name (or 'done' to finish): AAPL
Enter quantity for AAPL: 2
Enter stock name (or 'done' to finish): TSLA
Enter quantity for TSLA: 1
Enter stock name (or 'done' to finish): done
```
*After completing the stock entries, the program calculates the total investment value and prompts the user to optionally save the results. The output can be saved as a .txt or .csv file, which is created in the same project directory.*
```bash
Added: AAPL - 2 shares at $180 each = $360
Added: TSLA - 1 shares at $250 each = $250

Total Investment: $610
Save results to a file? (y/n): y
Enter filename (without extension): portfolio
Save as .txt or .csv? txt
Results saved to portfolio.txt
```

## 📊 Data Handling Logic
- Stock prices are stored in a Python dictionary for fast access
- User inputs are validated to ensure stock availability and positive quantities
- Investment value is calculated using basic arithmetic (price × quantity)
- Portfolio data is stored in a list and optionally written to a file using file handling techniques

## 🚀 Deployment
This is a local, console-based Python script and does not require deployment. It can be run on any system with Python installed.

## ⚙ Optimisations
- Uses a dictionary for fast stock price lookup
- Simple calculation logic for efficient execution
- Optional file saving without affecting core functionality

## 🎓 Lessons Learned
- Working on this project helped reinforce
- Effective use of dictionaries for structured data
- Handling user input and validation
- Performing arithmetic calculations in real time
- Writing data to text and CSV files
- Building a complete loop-based console application

## 🔮 Future Improvements  
- Allow dynamic stock price input  
- Add portfolio percentage distribution
- Support reading stock prices from a file
- Add a simple menu-based interface  
- Include currency selection support

## 📄 Documentation
The project is documented using this README.md, which explains the project goal, input format, execution steps, and sample output.
The code is written in a clear and beginner-friendly manner for easy understanding and modification.

## 👤 Author
- [@shreyakantha](https://github.com/shreyakantha)

## 🙌 Acknowledgements
- Inspired by basic stock-tracking concepts
- Python documentation for dictionary and file handling
- Open-source README formatting guidelines

## 📜 License
This project is open for educational and personal use. Feel free to modify, improve, and expand it as needed.

## 💬 Feedback
If you have any feedback or suggestions, feel free to reach out at 📧 shreyakantha348@gmail.com

##❓ FAQ
#### Q1. Are real-time stock prices used?
No. The program uses manually defined stock prices for simplicity.
#### Q2. Can I add more stocks?
Yes. You can add more entries to the stock_prices dictionary.
#### Q3. Where are the output files saved?
The .txt or .csv file is saved in the same directory where the program is executed.

## 🧩 Appendix
This project was completed as ***The second task Stock Portfolio Tracker*** under the CodeAlpha Python Programming Internship, with a focus on practicing data handling, user input processing, and basic investment calculations using Python.

## 📌 Related Projects
*The following projects were completed as part of the same **CodeAlpha internship** program and focus on strengthening core Python programming concepts.*

-  🔗 [Hangman Game – Python fundamentals and control flow](https://github.com/shreyakantha/CodeAlpha_HangmanGame)
-  🔗 [Email Extraction Automation – File handling and regular expressions in Python](https://github.com/shreyakantha/CodeAlpha_EmailExtractor)
-  🔗 [Basic Chatbot – Rule-based conversation using conditional logic](https://github.com/shreyakantha/CodeAlpha_BasicChatbot)
