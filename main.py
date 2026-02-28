import pandas as pd
from analysis import analyze_stock


def main():

    df = pd.read_csv("data/SKPC.csv")

    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    result = analyze_stock(df)

    print(result)


if __name__ == "__main__":
    main()