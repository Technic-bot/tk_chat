import pandas as pd 

def filter_chat_user(df,user):
  filtered_df = df[df['user']==user]
  return filtered_df
