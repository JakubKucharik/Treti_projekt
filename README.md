# Treti_projekt
Vítejte v programu Webscraper voleb 2017. Tento program scrapuje data z voleb do Poslanecké sněmovny Parlamentu České republiky v roce 2017 (po usnesení NSS) libovolného okresu z webu volby.cz a vytváří z nich přehlednou tabulku ve formátu csv.
Knihovny, které je potřeba nainstalovat pro spuštění programu najdete v souboru requirements.txt.
K instalaci knihoven dojde zadáním příkazu do terminálu ve formě: pip install a název příslušné knihovny, např. pip install pandas.
Program je navržen pro spouštění přes terminál pomocí dvou argumentů. Prvním argumentem je URL odkaz na okres, pro který chcete vytvořit tabulku s výsledky. Tento argument je potřeba napsat v uvozovkách. Druhým argumentem je název CSV souboru včetně přípony .csv. 
Pro zobrazení nápovědy (help) napište příkaz python Webscraping.py -h nebo python Webscraping.py --help. 
Pro nalezení správného URL odkazu otevřete následující odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ, poté vyberte okres, pro který chcete vytvořit tabulku. Klikněte na X ve sloupci Výběr obce pravým tlačítkem myši a poté klikněte na „Kopírovat adresu odkazu“.
Příklad zadání argumentů při spuštění programu v terminálu:
python Webscraping.py ´https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103´ Prostejov.csv

Seznam funkcí:
    1) Získat nuts – parametrem funkce je url odkaz na okres, vrátí seznam čísel nuts pro všechny obce v okresu.
    2) Voliči, obálky, platné hlasy –  parametrem funkce je url odkaz na obec, funkce vrátí seznam s počtem voličů, počtem vydaných obálek a počtem platných hlasů v obci
    3) Získat hlasy –  parametrem funkce je url odkaz na obec, funkce vrátí seznam s hlasy
    4) Získat strany -  parametrem funkce je url odkaz na obec, funkce vrátí seznam s názvy stran
    5) Název obce -  parametrem funkce je url odkaz na obec, funkce vrátí seznam s názvem obce
    6) Získej URL obcí, parametrem funkce je url odkaz na okres, funkce vrátí seznam s měnícími se koncovkami URL
