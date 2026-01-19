import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent   # <-- THIS is the datasets folder

class Loader:
    def load(self, filename: str):
        return pd.read_csv(DATA_DIR / filename)

    def load_irisDataset(self):
        return self.load("iris.csv")

    def load_housingDataset(self):
        return self.load("housing.csv")

    def load_diamondsDataset(self):
        return self.load("diamonds.csv")

    def load_mpgDataset(self):
        return self.load("mpg.csv")

    def load_titanicDataset(self):
        return self.load("titanic.csv")


def main():
    loader = Loader()
    df = loader.load_housingDataset()
    print(df.head())

if __name__ == "__main__":
    main()
