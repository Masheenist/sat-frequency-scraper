import pandas as pd
import requests
import re
import numpy as np



def Scraper():
    ucs_url = "https://www.ucsusa.org/media/11492"

    ucs_xl = pd.read_excel(ucs_url, storage_options={'User-Agent': 'Chrome/51.0.2704.103'}) 
    ucs_df = pd.DataFrame(ucs_xl)



    return myDict

if __name__ == "__main__":
    myFrame = pd.DataFrame.from_dict(Scraper())
    print(myFrame)
