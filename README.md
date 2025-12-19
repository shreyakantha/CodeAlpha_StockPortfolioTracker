
# 📊 Stock Portfolio Tracker


A simple console-based Stock Portfolio Tracker built in Python. This program calculates the total investment value based on user-entered stock names and quantities using manually defined stock prices. It allows users to interactively build a portfolio, view individual and total investment values, and optionally save the results to a .txt or .csv file. The project focuses on core Python fundamentals such as dictionaries, input/output operations, arithmetic calculations, and basic file handling.



## ⭐ Features

- Hardcoded dictionary of stock prices for quick lookup.
- User input for stock names and share quantities.
- Validation for unavailable stocks and invalid quantities.
- Real-time calculation of individual stock value.
- Displays total investment amount.
- Option to save portfolio data as .txt or .csv file.



## 📂 Project Structure

``` bash
project-folder/
│
├── StockPortfolioTracker.py   # Main program file
└── README.md                  # Documentation
```
## 📥  Installation

Install the project locally : 
```bash
git clone https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker
cd CodeAlpha_StockPortfolioTracker
```
    
## 🖥  Run Locally
Navigate to the project directory and run the script :
```bash
python StockPortfolioTracker.py
```



## 🎥 Demo

*A video demonstration of the Stock Portfolio Tracker showing the complete working of the program, including user input, investment calculation, and file saving functionality.*

**Click Here** ▶  [Stock-Portfolio-Tracker-Demo-Video](https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker/releases/tag/v1.0)





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

- Stock prices are stored in a Python dictionary for fast access.

- User inputs are validated to ensure stock availability and positive quantities.

- Investment value is calculated using basic arithmetic (price × quantity).

- Portfolio data is stored in a list and optionally written to a file using file handling techniques.

## 🎓 Lessons Learned

- Working on this project helped reinforce.

- Effective use of dictionaries for structured data.

- Handling user input and validation.

- Performing arithmetic calculations in real time.

- Writing data to text and CSV files.

- Building a complete loop-based console application.


## 🔮 Future Improvements  
- Allow dynamic stock price input.  
- Add portfolio percentage distribution.  
- Support reading stock prices from a file.  
- Add a simple menu-based interface.  
- Include currency selection support.
## 👤 Author

- [@shreyakantha](https://github.com/shreyakantha)


## 🙌 Acknowledgements

- Inspired by basic stock-tracking concepts.

- Python documentation for dictionary and file handling.

- Open-source README formatting guidelines.



## 📜 License

This project is open for educational and personal use.
Feel free to modify, improve, and expand it as needed.



## 💬 Feedback

If you have any feedback or suggestions, feel free to reach out at
📧 shreyakantha348@gmail.com



##❓ FAQ

#### Q1. Are real-time stock prices used?
No. The program uses manually defined stock prices for simplicity.

#### Q2. Can I add more stocks?
Yes. You can add more entries to the stock_prices dictionary.

#### Q3. Where are the output files saved?
The .txt or .csv file is saved in the same directory where the program is executed.


