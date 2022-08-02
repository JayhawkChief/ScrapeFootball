import urllib.request
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlopen("https://www.pro-football-reference.com/years/2021/passing.htm")
    # print(r.status)
    # print(r)

    url = "https://www.pro-football-reference.com/years/2021/passing.htm"

    html = urlopen(url)
    stats_page = BeautifulSoup(html, "html.parser")

    # Collect table headers
    column_headers = stats_page.findAll('tr')[0]
    column_headers = [i.getText() for i in column_headers.findAll('th')]
    print(column_headers)

if __name__ == '__main__':
    main()



