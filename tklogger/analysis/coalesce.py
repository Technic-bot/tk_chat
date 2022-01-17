import pandas as pd 
import os 
import glob

def coalesce_csvs(input_dir):
  """ Load several csvs into a single data frame"""
  path = os.path.abspath(input_dir)
  filenames = glob.glob(os.path.join(path,"*.csv"))
  dfs = []
  for f in filenames:
    day =  os.path.basename(f).split('.')[0]
    tmp_df = pd.read_csv(f)
    if not tmp_df.empty:
      add_date(tmp_df,day)
      dfs.append(tmp_df) 
    else:
      print("{} has not rows".format(f))

  all_df = pd.concat(dfs)
    
  if not len(all_df):
    print("No files read")
    return None

  print("Read {} csvs into  {} records".format(len(filenames),len(all_df)))
  all_df.sort_values('date',inplace=True)
  print(all_df.info())

  return all_df

def add_date(df,day):
  """ Add date from title """
  # Format dd-mm-yy
  #df['date'] = day + 'T' + df['date'] 
  df['date'] = pd.to_datetime(df['date'],format='%d-%m-%YT%H:%M:%S')
  return 
  
def filter_chat_user(df,user):
  print("Filtering for {}".format(user))
  filtered_df = df[df['user']==user]
  print("Filtered down to {} entries".format(len(filtered_df)))
  return filtered_df
