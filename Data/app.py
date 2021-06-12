import pandas as pd

a = pd.read_csv("cities.csv")

a.head
a.to_html("Data.html")
