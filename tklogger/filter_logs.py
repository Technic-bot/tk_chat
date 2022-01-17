import argparse
import pandas as pd

import analysis.coalesce 
 
def process_opt():
  parser = argparse.ArgumentParser()
  parser.add_argument("dir",help="Input csv files directory")
  parser.add_argument("out", help="Output directory or file")
  parser.add_argument("--coalesced-filename",help="Full coalesced filename")
  parser.add_argument("user", help="User to filter chat messages from")

  return parser.parse_args()


if __name__=="__main__":
  args = process_opt()
  chat_df = analysis.coalesce.coalesce_csvs(args.dir)
  filtered_df = analysis.coalesce.filter_chat_user(chat_df,args.user)
  filtered_df.to_csv(args.out)
  if args.coalesced_filename:
   chat_df.to_csv(args.coalesced_filename)
  
  
