import sys
sys.path.append("./../.")
from sec_edgar_downloader import Downloader


download_path = './download_files'
dl = Downloader(download_path);

dl.get(None,"", include_amends=True, query = "\"opportunities doctrine\"" )
#dl.get(None,"", include_amends=True, query = "\"business opportunity\" \"conflict of interest\" \"is not prohibited\"", dry_run=True)
