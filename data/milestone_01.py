import pandas as pd

try:
    df = pd.read_csv("data/finflow_users.csv")
except FileNotFoundError:
    print("Error: data/finflow_users.csv not found.")
    exit()

print("Dataset loaded successfully.")
