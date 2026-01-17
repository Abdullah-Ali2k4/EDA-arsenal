import pandas as pd

number_of_dataset=0
datasets = {
    'titanic': 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
    'housing': 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv',
    'iris': 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv',
    'mpg': 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv',
    'diamonds': 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv',
    'tips': 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv',

}

print("📥 Downloading datasets...")
for name, url in datasets.items():
    try:
        df = pd.read_csv(url)
        path = f'{name}.csv'
        df.to_csv(path, index=False)
        print(f"✅ {name}: {len(df)} rows, {df.shape[1]} columns")
        number_of_dataset+=1
    except Exception as e:
        print(f"❌ {name}: Failed - {str(e)[:50]}...")

print(f"\n📊 Total datasets: {number_of_dataset}")
