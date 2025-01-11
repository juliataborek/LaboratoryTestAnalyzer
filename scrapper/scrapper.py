#Import bibliotek
import random
from time import sleep
from playwright.sync_api import sync_playwright, TimeoutError

#Import klasy TestNorm
from test_norm import TestNorm

#Klasa zajmująca się scrapowaniem
class LeksykonScrapper:

    url = "http://bazalekow.leksykon.com.pl/normy-i-skale.html"

    def __init__(self):
        """
            Inicjalizacja obiektu klasy LeksykonScrapper z domyślnymi wartościami atrybutów.
            """
        self.pr = None
        self.browser = None
        self.context = None
        self.test_norms = []
        self.page = None

    def random_wait(self):
        """
            Wstrzymuje wykonywanie programu na losowy czas pomiędzy 0.3 a 0.8 sekundy.
            """
        random_number = random.uniform(0.3, 0.8)
        sleep(random_number)

    def initialize(self):
        """
            Inicjalizacja i konfiguracja środowiska Playwright.
            """
        self.pr = sync_playwright().start() #uruchamia playwright w trybie synchronicznym
        self.browser = self.pr.firefox.launch() #uruchamia przeglądarkę
        self.context = self.browser.new_context(record_video_dir="records",
                                                record_video_size={"width": 3840, "height": 2160}, viewport={
                'width': 3840,
                'height': 2160
            }) #tworzy nowy kontekst (profil) przeglądarki (ustawienia dotyczące nagrywania, wyświetlania strony)
        self.page = self.context.new_page() #tworzy nową stronę w ramach kontekstu przeglądarki
        self.page.goto(self.url) #wchodzi na stronę pod adresem zapisanym w `self.url`
        self.page.wait_for_load_state("load") #czeka na załadowanie strony
        self.random_wait() #symuluje losowe opóźnienia między akcjami

    def close(self):
        """

            """
        self.page.close() #zamyka stronę
        self.browser.close() #zamyka przeglądarkę
        self.pr.stop() #kończy sesję playwright


    def input_declaration(self):
        """
            Wstępna deklaracja o byciu pacjentem.
            """
        sleep(5) #symuluje czytanie deklaracji
        self.random_wait()
        self.page.query_selector("#btn-patient").click() #klika opcję "Jestem pacjentem"

    def scrap_kind(self, name, kind_name, div):
        """

            """
        select_element = div.query_selector('select')
        units = []
        self.random_wait()
        options = select_element.query_selector_all('option') #wszystkie opcje z selektora
        for option in options:
            units.append(option.text_content()) #dodanie jednostki do listy
        norm = div.query_selector("input").get_attribute('placeholder')
        return self.test_norms.append(TestNorm(norm=norm, name=name, kind=kind_name, units=units))

    def scrape_test_norm(self, selector):
        """

            """
        self.random_wait()
        selector.click() #klikanie w nazwe badania
        div = self.page.query_selector(".info3")
        name = div.query_selector(".name").text_content() #nazwa badania
        kind_element = div.query_selector(".kinds") #w jednym badaniu kilka podbadń
        self.random_wait()
        table_element = kind_element.query_selector('table') #obiekt htmlowy - tabela
        kinds = table_element.query_selector_all("td") #wiersze z tabeli
        if len(kinds) == 1: #jeden wiersz w tabeli (nie ma podbadania)
                kind = kinds[0]
                kind_name = kind.text_content()
                return self.scrap_kind(name, kind_name, div) #scrapowanie norm podbadania
        for kind in kinds: #jeżeli więcej podbadań
            kind_name = kind.text_content()
            kind.click()
            self.scrap_kind(name, kind_name, div)


    def scrape_norms(self):
        """

            """
        try:
            norms_selectors = self.page.query_selector_all(".col_0")
            counter = 0 #numer badania
            for norm_selector in norms_selectors:
                counter +=1
                print(counter) #kontrolowanie scrappowania kolejnych norm
                if counter in [38,39,40,43,50,53,54,55,56,57,58,59,60,61,62,63,78,79,165,163,162,158,157,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135,134,133,132,131,130,129,128,127,126125,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,97,93,91,90,89,88,86,167]: # nie ma sensu skrapowac
                    continue #przejście do kolejnego badania
                self.scrape_test_norm(norm_selector) #jeżeli nie jest w liście to scrapujemy normy
        except Exception as e:
            print(e)#drukuje błedy

    def scrape(self):
        """
            Główna metoda inicjująca, która wywołuje kolejne metody niezbędne w procesie scrapowania.
            """
        self.initialize()
        self.input_declaration()
        self.scrape_norms()
        self.close()




