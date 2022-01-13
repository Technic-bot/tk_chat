#from utils.utils import process_opt
#import utils.utils 
import utils.loader
from tklogs.log_collector import logScrapper

if __name__=="__main__":
  cache = None
  args = utils.loader.process_opt()
  if args.cache:
    cache = utils.loader.read_cache(args.cache)

  #  page = utils.loader.load_page("debug.html")

  ls = logScrapper(cache,args.outdir)
  
  ls.get_all_logs()

#  ls.parse_log_page(page)
#  ls.get_all_logs()


