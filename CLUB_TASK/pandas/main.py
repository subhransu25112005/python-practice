import pandas as pd

data = {
    "Arpita": {"roll": 101, "branch": "CSE", "marks": 95},
    "Bharti": {"roll": 102, "branch": "CSE", "marks": 98},
    "Neha": {"roll": 102, "branch": "ECE", "marks": 90},
    "sai": {"roll": 103, "branch": "ME", "marks": 78}
}

df = pd.DataFrame(data).T  # Transpose to make student names rows
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
