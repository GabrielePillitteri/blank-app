import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# @title Scrape prezzi Metalli
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

class ScrapySoup:
    def __init__(self, site):
        self.site = site

    def exploit_table(self):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(self.site, headers=hdr)
        res = urlopen(req)
        rawpage = res.read().decode("utf-8")
        page = rawpage.replace('<!-->', '')

        # Use BeautifulSoup to exploit the table
        soup = BeautifulSoup(page, "html.parser")

        table = soup.find("table")

        # Preparazione delle liste per raccogliere i dati
        rows = []

        # Estrazione delle righe della tabella, skipping the first row (header)
        for row in table.find_all('tr')[1:3]:
            cells = row.find_all('td')
            if len(cells) > 0:
                rows.append([cell.get_text().strip() for cell in cells])

        # Creazione di un DataFrame di pandas
        df = pd.DataFrame(rows)
        return df.iloc[0]



# @title Scraping WestMetal
# Prezzo del copper IERI
siteCopper = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash'
table = ScrapySoup(siteCopper).exploit_table()
print(table)
CopperCash = table[2] #Se inserisco 2 prendo il dato a 3mesi, se metto 1 prendo il dato Csh
prezzoCopper = float(CopperCash.replace(',', ''))
#Prezzo del Nickel ieri
siteNickel = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Ni_cash'
table = ScrapySoup(siteNickel).exploit_table()
NickelCash = table[2]
prezzoNickel = float(NickelCash.replace(',', ''))

#Prezzo dell'Alluminio ieri
siteAlum = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Al_cash'
table = ScrapySoup(siteAlum).exploit_table()
AlumCash = table[2]
prezzoAluminium = float(AlumCash.replace(',', ''))

#Prezzo dello Zinco ieri
siteZinc = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Zn_cash'
table = ScrapySoup(siteZinc).exploit_table()
ZincCash = table[2]
prezzoZinc= float(ZincCash.replace(',', ''))


siteLead = 'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Pb_cash'
table = ScrapySoup(siteLead).exploit_table()
LeadCash = table[2]
prezzoLead= float(LeadCash.replace(',', ''))
prezzoCopper
