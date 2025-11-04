import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



def plot_missing_values (df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    
    missing_df = pd.DataFrame({
        "Kolumn" : missing.index,
        "Antal saknade värden" : missing.values
    })

    plt.figure(figsize=(10,5))
    sns.barplot(data = missing_df, x="Kolumn", y="Antal saknade värden", palette="magma")
    plt.title("Antal Null värden")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
