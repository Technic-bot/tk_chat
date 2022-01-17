import argparse

def process_opt():
  parser = argparse.ArgumentParser()
  parser.add_argument("--limit",help="Max date to scrape", type=int,default=5)
  parser.add_argument("--start",help="Date to start ", default="")
  parser.add_argument("--cache",help="Cache filename")
  parser.add_argument("--out-cache",help="Cache filename",default="cache.txt")
  parser.add_argument("outdir",help="directory to store results")
  return parser.parse_args()

def read_cache(filename):
  cache = []
  with open(filename,'r') as cache_file:
    for entry in cache_file:
      # Process line 
      cache.append(entry.strip())
       
  return cache

def save_cache(filename,cache):
  with open(filename, 'w') as cache_file:
    for c in cache:
      cache_file.write(c)
      cache_file.write('\n')

  return

def load_page(filename):
  with open(filename,'r') as page:
    page_html = page.read()
  return page_html
