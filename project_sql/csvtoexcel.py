import pandas as pd

df = pd.read_csv("top_paying_jobs.csv")  
df.to_excel("top_paying_jobs.xlsx", index=False)