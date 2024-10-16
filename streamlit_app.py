import streamlit as st
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

# Define the ScrapySoup class to scrape data
class ScrapySoup:
    def __init__(self, site):
        self.site = site

    def exploit_table(self):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(self.site, headers=hdr)
        res = urlopen(req)
        rawpage = res.read().decode("utf-8")
        page = rawpage.replace('<!-->', '')

        soup = BeautifulSoup(page, "html.parser")
        table = soup.find("table")
        rows = []

        for row in table.find_all('tr')[1:3]:
            cells = row.find_all('td')
            if len(cells) > 0:
                rows.append([cell.get_text().strip() for cell in cells])

        df = pd.DataFrame(rows)
        return df.iloc[0]

# App title
st.title("🎈 Metal Prices Scraper")

# Scrape copper price
siteCopper = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash'
table = ScrapySoup(siteCopper).exploit_table()
CopperCash = table[2]
prezzoCopper = float(CopperCash.replace(',', ''))
st.write(f"Copper price: {prezzoCopper}")

# Scrape nickel price
siteNickel = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Ni_cash'
table = ScrapySoup(siteNickel).exploit_table()
NickelCash = table[2]
prezzoNickel = float(NickelCash.replace(',', ''))
st.write(f"Nickel price: {prezzoNickel}")

# Scrape aluminum price
siteAlum = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash'
table = ScrapySoup(siteAlum).exploit_table()
AlumCash = table[2]
prezzoAluminium = float(AlumCash.replace(',', ''))
st.write(f"Aluminium price: {prezzoAluminium}")

# Scrape zinc price
siteZinc = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Zn_cash'
table = ScrapySoup(siteZinc).exploit_table()
ZincCash = table[2]
prezzoZinc = float(ZincCash.replace(',', ''))
st.write(f"Zinc price: {prezzoZinc}")

# Scrape lead price
siteLead = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Pb_cash'
table = ScrapySoup(siteLead).exploit_table()
LeadCash = table[2]
prezzoLead = float(LeadCash.replace(',', ''))
st.write(f"Lead price: {prezzoLead}")
