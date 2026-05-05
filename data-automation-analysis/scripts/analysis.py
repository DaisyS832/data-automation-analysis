
"""
Analyze cleaned flight delay data and export summary results.
"""

import pandas as pd


def analyze_flight_data():
    df = pd.read_csv("../data/processed/cleaned_data.csv")

    df["ROUTE"] = df["ORIGIN"] + " → " + df["DEST"]

    avg_delay = df.groupby("AIRLINE")["ARR_DELAY"].mean().sort_values(ascending=False)

    route_counts = df["ROUTE"].value_counts()
    valid_routes = route_counts[route_counts > 50].index
    filtered_df = df[df["ROUTE"].isin(valid_routes)]

    route_delay = (
        filtered_df.groupby("ROUTE")["ARR_DELAY"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    avg_delay.to_csv("../outputs/avg_delay_by_airline.csv")
    route_delay.to_csv("../outputs/top_delayed_routes.csv")

    print("Analysis outputs saved to outputs folder.")
    print("\nAverage delay by airline:")
    print(avg_delay.head())

    print("\nTop delayed routes:")
    print(route_delay.head())


if __name__ == "__main__":
    analyze_flight_data()
