from pathlib import Path
import pandas as pd

Data_path = Path(__file__).parent/ "data"
print(Data_path / "Prog_book.csv")

df = pd.read_csv(Data_path / "Prog_book.csv")
print(df.head())