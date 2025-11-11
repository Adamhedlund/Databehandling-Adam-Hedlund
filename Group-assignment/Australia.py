import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r".\Data\athlete_events.csv")

#A)
print(len(df["Team"].unique()))

#B)
print(df["NOC"].unique())

#C)
print(df["Sport"].unique())

#D)
print(df["Medal"].unique())

#E)
