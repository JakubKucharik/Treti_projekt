"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jakub Kuchařík
email: jakub.kucharik@gmail.com
discord: Jakub Kuchařík#8660
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests
import argparse


def ziskat_nuts(url_okres):
    raw_html = requests.get(url_okres)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    nuts_list = list()
    nuts = soup.find("div",{"class":"topline"})
    nuts2 = nuts.find_all("td",{"class":"cislo"})
    nuts3 = list()
    for i in nuts2:
        i = i.find("a")
        nuts3.append(i.text)
    return nuts3


def volici_obalky_platne_hlasy(url_obec):
    raw_html = requests.get(url_obec)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    volici_obalky_platne_hlasy_list = list()
    registered = soup.find("td", headers="sa2").text
    envelopes = soup.find("td", headers="sa3").text
    valid = soup.find("td", headers="sa6").text
    volici_obalky_platne_hlasy_list.append(registered)
    volici_obalky_platne_hlasy_list.append(envelopes)
    volici_obalky_platne_hlasy_list.append(valid)
    volici_obalky_platne_hlasy_list = [znak.replace(r"\xa0", " ") for znak in volici_obalky_platne_hlasy_list]
    return volici_obalky_platne_hlasy_list


def ziskat_hlasy(url):
    raw_html = requests.get(url)
    soup = BeautifulSoup(raw_html.text,"html.parser")
    hlasy = list()
    for i in soup.find_all("td", headers = "t1sa2 t1sb3"):
        hlasy.append(i.text)
    for i in soup.find_all("td",headers="t2sa2 t2sb3"):
        if i.text == "-":
            continue
        hlasy.append(i.text)
    return hlasy


def ziskat_strany(url_obec):
    raw_html = requests.get(url_obec)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    strany = list()
    for i in soup.find_all("td", class_="overflow_name"):
        if i.text == "-":
            continue
        strany.append(i.text)
    return strany


def nazev_obce(url_obec):
    raw_html = requests.get(url_obec)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    obec = soup.find("div",{"class":"topline"})
    obec2 = obec.find_all("h3")[2].text
    obec_list = list()
    obec_list.append(obec2[7:])
    obec_list2 = list()
    for i in obec_list:
        obec_list2.append(i.replace("\n", ""))
    return obec_list2


def ziskej_url_obci(url_okres):
    raw_html = requests.get(url_okres)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    odkazy_resultset = soup.find_all(href=True)
    odkazy_resultset = odkazy_resultset[6:-2]
    odkazy_resultset_list = list()
    for odkaz in odkazy_resultset:
        if odkaz.text.isdigit():
            odkazy_resultset_list.append(odkaz["href"])
    return odkazy_resultset_list


def main() -> list:
    try:
        while True:
            parser = argparse.ArgumentParser(description=
                                             "Vložte odkaz na vybraný okres a název csv souboru "
                                             "včetně přípony .csv")
            parser.add_argument('url_okres', help="Vložte odkaz na vybraný okres obalený uvozovkami", type=str)
            parser.add_argument('nazev_csv', help="Vložte jméno csv souboru včetně přípony .csv", type=str)
            args = parser.parse_args()
            if args.url_okres[0:52] == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" \
                    and args.nazev_csv[-4:] == ".csv":
                break
            else:
                print("Špatně zadaný odkaz nebo název csv souboru, zkuste vložení provést znovu")
                exit()

        url_okres = args.url_okres
        nazev_csv = args.nazev_csv

        url_obec = f"https://volby.cz/pls/ps2017nss/{ziskej_url_obci(url_okres)[0]}"
        nuts = ziskat_nuts(url_okres) #list s nutsy
        strany = ziskat_strany(url_obec)
        vysledky = list()
        for url in ziskej_url_obci(url_okres):
            url_obec = f"https://volby.cz/pls/ps2017nss/{url}"
            vysledky2 = list()
            vysledky2 = nazev_obce(url_obec) +\
                        volici_obalky_platne_hlasy(url_obec) + ziskat_hlasy(url_obec)
            vysledky.append(vysledky2)
        df = pd.DataFrame(vysledky,columns=(["location", "registered", "envelopes", "valid"] + strany))
        df.insert(0,"code",nuts)
        df.to_csv(nazev_csv, index=False)
    except IndexError:
        print("Špatně zadaný odkaz, zkuste odkaz vložit znovu")

if __name__ == "__main__":
    main()




