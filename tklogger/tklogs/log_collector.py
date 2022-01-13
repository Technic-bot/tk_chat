import requests 
import random 
import time
import csv 

from bs4 import BeautifulSoup

from utils.loader import save_cache

base_url="https://twokinds.gallery/"

class logScrapper():
  def __init__(self,cache,directory="."):
    if cache:
      self.cache = set(cache)
    else: 
      self.cache = set()

    self.base_sleep = 1
    self.out_dir = directory
    return 

  def get_all_logs(self,limit=10):
      """Get all logs up to limit"""
      log_html=self.get_log()
      self.save_html(log_html,"debug.html")
      chat,link = self.parse_log_page(log_html)
      self.save_chat_page(chat,self.out_dir+"log.csv")
      for i in range(limit):
        log_html=self.get_log(link)
        chat,link = self.parse_log_page(log_html)
        fname = self.format_filename(link)
        self.save_chat_page(chat,fname) 
    
      return 

  def format_filename(self,link):
    """Formats links into filenames"""
    filename = link.replace(".","-")
    filename = filename.replace("/","_")
    filename = filename.rstrip("_")
    filename = self.out_dir + "/" + filename + ".csv"
    return filename
    

  def get_log(self,entry="log"):
    """Gets logs from date entry"""
    # Add some jitter 
    base_sleep = 1
    jitter = random.uniform(0,2)
    time.sleep(base_sleep + jitter)

    log_url = base_url+entry
    r = requests.get(log_url)
    log_html = r.text
    return log_html

  def parse_log_page(self,page):
    soup = BeautifulSoup(page,'html.parser')
    title = soup.find("h1").text
    title = " ".join(title.split())
    link = soup.find("h1").a['href']
    print(title)
    chat_area = soup.find(id="resultsArea")
    chat_entries = chat_area.find_all("div")
    # fmt = "{}, {}: {}"
    chat = []
    for msg in chat_entries:
      spans = msg.find_all("span")
      time = msg['id']
      user = spans[1].text
      txt = spans[2].text
     # print(fmt.format(time,user,txt))
      chat.append([time,user,txt])
    return chat, link

  def save_chat_page(self,chat,filename):
    """Save page to csv file"""
    with open(filename,'w') as page_csv:
      page_writer = csv.writer(page_csv)
      page_writer.writerow(('date','user','comment'))
      page_writer.writerows(chat)
    return

  def save_html(self,html,filename):
    with open(filename,'w') as html_file:
      html_file.write(html)

    return
      
  def persist_cache(self):
    save_cache(self.cache)
    return
    

