#import streamlit as st
import pandas as pd
import numpy as np
#import plotly_express as px
#import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Create a heading for the subscription
#st. title("Exploring Indian General Elections 2019")
#st.divider()

filepath = "LS_2.0.csv"
df = pd.read_csv(filepath)

#Showing the dataframe
st.dataframe(df)

#df.head()
df.tail()

#import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

#Create a heading for the subscription
#st. title("Exploring Indian General Elections 2019")
#st.divider()

filepath = "LS_2.0.csv"
df = pd.read_csv(filepath)

#Showing the dataframe
st.dataframe(df)

#df.head()
df.tail()

df.describe().T

df.duplicated().sum()
df.info()
df.isnull().sum().sort_values()
df["ASSETS"].value_counts()
df["ASSETS"].value_counts()
df["SYMBOL"].value_counts()
df.drop(['ASSETS', 'LIABILITIES', 'SYMBOL'], axis=1, inplace=True) 
df["EDUCATION"].value_counts()
df["GENDER"].value_counts()
df["CATEGORY"].value_counts()
df["WINNER"].value_counts()

#Filter out rows where WINNER is 0 (numeric) or '0' (string)
df_win = df[df["WINNER"] != 0]

#Shape of the new cleaned data
df_win.shape

#Drop the "WINNER" column from the cleaned data to ensure the dataset 
df_win.drop(['WINNER'], axis=1, inplace=True) 

#Shape of the new cleaned data
df_win.shape

# Getting the null value counts along each rows.
df_win.isnull().sum().sort_values()

df_win["AGE"].value_counts().sort_values()

df_win["EDUCATION"].value_counts()

df_win["GENDER"].value_counts()
df_win["PARTY"].value_counts()
df_win.info()


EDA

# 1. GENDER-AGE SPREAD AMONG WINNING ELECTORS.
gender_age = df_win.groupby("GENDER")["AGE"].mean().sort_values().head(10)
plt.barh(y= gender_age.index, width = gender_age.values)
plt.xlabel("Age")
plt.ylabel("Gender")
plt.title("Male vs Female (Winning) Electors");

# 2. TOTAL WINNING VOTES ACROSS THE STATES
party_state = df_win.groupby("STATE")["TOTAL\nVOTES"].mean().sort_values().head(20)
plt.barh(y= party_state.index, width = party_state.values)
plt.xlabel("Winning Votes")
plt.ylabel("State")
plt.title("Spread of Total Winning Votes across the States");
