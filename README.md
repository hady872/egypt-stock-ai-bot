# Egypt Stock AI Bot

this project is a personal AI learning journey.

## Day 1 – Data Setup & Git Basics

**Tasks Completed:**
- Created SKPC.csv file in `data/` folder
- Added sample stock data (Date, Open, High, Low, Close, Volume)
- Learned about Git add, commit, push
- Fixed `.gitignore` issue to track data files
**Learning Points:**
- How to create and save CSV files for analysis
- Basic Git workflow: add → commit → push
- How `.gitignore` affects tracked files



## Day 2 – Load SKPC Data with Pandas

**Tasks Completed:**
- Loaded `SKPC.csv` using pandas
- Converted `Date` column to datetime
- Set `Date` column as index
- Displayed data before and after changes to understand effect
**Learning Points:**
- Difference between normal column and index
- Importance of Date as index for time series analysis
- How to read CSV files and inspect data with `df` and `dtypes`



## Day 3 – Data Analysis Basics

**Tasks Completed:**
- Calculated Daily Return for SKPC stock
- Calculated 2-day Moving Average (MA_2)
- Learned the difference between pct_change() and rolling()
**Learning Points:**
- `Daily_Return` shows % change in Close price day by day
- `MA_2` smooths prices using the last 2 days




## Day 5 - Trend Logic & Trading Signals

**Tasks Completed:**
- Created Trend column based on Close vs MA20
- Generated basic Buy/Sell signals
- Improved logic using price crossover detection
- Used shift(1) to compare current vs previous day
- Created Cross Signal column (Buy / Sell / No Signal)
**Learning Points:**
- Difference between simple signal and crossover signal
- Importance of avoiding repeated signals
- How shift() works in time series
- How to convert analysis into rule-based logic
- Basic structure of trading signal generation