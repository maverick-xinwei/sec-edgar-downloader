import sys
##sys.path.append("./../.")
sys.path.insert(1, "./../.")
from sec_edgar_downloader import Downloader


download_path = './download_files'
dl = Downloader(download_path);

dl.get(None,"", include_amends=True, query = "\"opportunities doctrine\"", dry_run=False )
#dl.get(None,"", include_amends=True, query = "\"business opportunity\" \"conflict of interest\" \"is not prohibited\"", dry_run=True)
