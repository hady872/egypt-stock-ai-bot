import pandas as pd


def analyze_stock(df):

    df["MA20"] = df["Close"].rolling(20).mean()
    df["Diff"] = df["Close"] - df["MA20"]

    df["CrossSignal"] = "No Signal"

    df.loc[(df["Diff"] > 0) & (df["Diff"].shift(1) <= 0), "CrossSignal"] = "Buy"
    df.loc[(df["Diff"] < 0) & (df["Diff"].shift(1) >= 0), "CrossSignal"] = "Sell"

    latest_price = df["Close"].iloc[-1]
    latest_ma = df["MA20"].iloc[-1]
    latest_signal = df["CrossSignal"].iloc[-1]

    if latest_signal == "Buy":
        comment = "Trend turned bullish. Consider watching for entry."
    elif latest_signal == "Sell":
        comment = "Trend turned bearish. Caution or possible exit zone."
    else:
        if latest_price > latest_ma:
            comment = "Price above MA20. Uptrend still active."
        else:
            comment = "Price below MA20. Downtrend still active."

    message = f"""
Stock Analysis: SKPC

Latest Price: {latest_price:.2f}
MA20: {latest_ma:.2f}
Signal: {latest_signal}

Comment:
{comment}
"""

    return message