import pandas as pd

# Load data
df = pd.read_parquet("data/stock_market_regimes_2000_2026.parquet")

print("Initial Shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort properly
df = df.sort_values(["ticker", "date"])

# Merge small class
df["regime_label"] = df["regime_label"].replace(
    {"High-volatility": "Crisis"}
)

# Create yield spread
df["yield_spread"] = df["10y_treasury"] - df["2y_treasury"]

# Drop missing values
df = df.dropna()

print("After Cleaning Shape:", df.shape)

# Save cleaned file
df.to_parquet("data/cleaned_market_data.parquet")

print("Cleaning completed.")
