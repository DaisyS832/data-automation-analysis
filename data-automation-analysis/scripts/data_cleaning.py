
"""
Clean raw flight delay data and save a processed dataset.
"""

import pandas as pd


def clean_flight_data():
    df = pd.read_csv("../data/raw/raw_data.csv")

    columns_to_drop = [
        "AIRLINE_DOT", "DOT_CODE", "FL_NUMBER", "CANCELLATION_CODE",
        "TAXI_OUT", "WHEELS_OFF", "WHEELS_ON", "TAXI_IN", "AIR_TIME",
        "CRS_ELAPSED_TIME", "ELAPSED_TIME", "CRS_DEP_TIME", "CRS_ARR_TIME",
        "DEP_TIME", "ARR_TIME", "DELAY_DUE_CARRIER", "DELAY_DUE_WEATHER",
        "DELAY_DUE_NAS", "DELAY_DUE_SECURITY", "DELAY_DUE_LATE_AIRCRAFT",
        "AIRLINE_CODE"
    ]

    df = df.drop(columns=columns_to_drop, errors="ignore")
    df = df.dropna(subset=["DEP_DELAY", "ARR_DELAY"])
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"])

    df = df[["FL_DATE", "AIRLINE", "ORIGIN", "DEST", "DEP_DELAY", "ARR_DELAY", "DISTANCE"]]

    df = df[(df["DEP_DELAY"] > -100) & (df["DEP_DELAY"] < 500)]
    df = df[(df["ARR_DELAY"] > -100) & (df["ARR_DELAY"] < 500)]

    df["AIRLINE"] = df["AIRLINE"].str.replace("Inc.", "", regex=False)
    df["AIRLINE"] = df["AIRLINE"].str.replace("LLC", "", regex=False)
    df["AIRLINE"] = df["AIRLINE"].str.replace("d/b/a aha!", "", regex=False)
    df["AIRLINE"] = df["AIRLINE"].str.strip()

    df.to_csv("../data/processed/cleaned_data.csv", index=False)

    print("Cleaned data saved to data/processed/cleaned_data.csv")


if __name__ == "__main__":
    clean_flight_data()
