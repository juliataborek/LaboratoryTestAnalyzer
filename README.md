# NormaDlaNiej – narzędzie analizy wyników badań krwi dla kobiet w wieku 18-26 lat
Dokumentacja oprogramowania

**Strona internetowa aplikacji:** https://normadlaniej.streamlit.app/
  
---

## 1. Charakterystyka oprogramowania

### a. Nazwa skrócona
NormaDlaNiej

### b. Nazwa pełna
NormaDlaNiej – narzędzie analizy wyników badań krwi dla kobiet w wieku 18-26 lat.

### c. Krótki opis ze wskazaniem celów
Nasze oprogramowanie jest narzędziem wspierającym analizę wyników badań krwi u kobiet w wieku 18–26 lat. Głównym celem projektu było dostarczenie użytkowniczkom szybkiej i intuicyjnej informacji zwrotnej o stanie ich zdrowia w kontekście obszarów takich jak prokreacja, endokrynologia oraz stosowanie antykoncepcji, które często dotyczą kobiet w tym wieku.

Strona internetowa umożliwia wprowadzenie wieku oraz płci, a po spełnieniu założeń programu także wybór wybranych badań krwi oraz ich analizę. Na tej podstawie system porównuje dostarczone dane z normami pobranymi ze strony Leksykon.pl i wskazuje, czy wyniki mieszczą się w granicach normy lub czy są poniżej lub powyżej normy. W przypadku wyników odbiegających od normy użytkowniczka otrzymuje rekomendację, do jakiego specjalisty powinna się zgłosić oraz sugestie dotyczące dodatkowych badań krwi, które mogą być związane z uzyskanym wynikiem. Oprogramowanie wspiera samodzielne monitorowanie zdrowia i ułatwia diagnostykę w istotnych dla młodych kobiet obszarach medycznych.

---

## 2. Prawa autorskie

### a. Autorzy
Autorzy oprogramowania: **Natalia Machlus, Julia Taborek**.  
**Podział pracy:**

#### Natalia Machlus
1. **Wywiad z lekarzem**:  
   - Przeprowadzenie rozmowy na temat możliwych problemów z interpretacją wyników badań krwi, które mogą się różnić w zależności od źródła danych, wieku, płci, stylu życia, kraju oraz rasy pacjenta.  
   - Omówienie rozwiązania polegającego na ograniczeniu grupy docelowej aplikacji do kobiet w wieku 18-26 lat oraz skupieniu się na najczęstszych obszarach zdrowotnych, które je dotyczą: prokreacja, chęć rozpoczęcia antykoncepcji i endokrynologia.  
   - Dyskusja na temat wiarygodnych źródeł dostarczających informacji o interpretacji wyników krwi oraz o specjalistach, do których należy udać się w przypadku uzyskania nieprawidłowych wyników.  

2. **Pobieranie danych o normach wyników krwi**:  
   - Napisanie kodu do scrapowania danych z normami wyników krwi ze strony Leksykon.pl.  

3. **Zapis danych do pliku CSV**:  
   - Zapisanie pobranych danych, zawierających nazwę badania, nazwę podbadania, możliwe jednostki oraz normę badania lub podbadania do pliku CSV.  

4. **Uzupełnianie informacji o specjalistach oraz powiązanych badaniach**:  
   - Dodanie do aplikacji informacji o specjalistach, do których można udać się w celu dalszej diagnostyki po uzyskaniu nieprawidłowego wyniku badania oraz o innych badaniach powiązanych z nieprawidłowymi wynikami.  

5. **Przeprowadzenie testów funkcjonalnych scrapera.**  
6. **Przygotowanie dokumentacji projektu.**  

#### Julia Taborek
1. **Przygotowanie interfejsu aplikacji**:  
   - Stworzenie strony startowej aplikacji oraz bocznego menu, które umożliwia nawigację pomiędzy stronami.  
   - Wgranie danych – pliku zawierającego normy badań oraz pliku zawierającego informacje o powiązanych badaniach i specjalistach oraz przygotowanie danych do dalszego użycia:  
     - Ograniczenie się jedynie do wybranych do zaimplementowania badań.  
     - Usunięcie niepotrzebnych wyrazów z rodzajów badań (np. określeń wskazujących, że norma dotyczy kobiet, ponieważ aplikacja skierowana jest wyłącznie do kobiet).
   - 	Stworzenie formularza umożliwiającego podanie płci i wieku użytkownika oraz zaimplementowanie walidacji tych cech w celu sprawdzenia, czy użytkownik jest docelowym odbiorcą aplikacji.
   - 	Utworzenie listy rozwijalnej pozwalającej wybrać badania, których wyniki użytkownik chce wprowadzić oraz zaimplementowanie logiki dla wyboru „Zaznacz wszystkie”, która pozwala na wprowadzenie wyników badań dla wszystkich dostępnych badań.
   - 	Stworzenie funkcji sprawdzającej, czy wyniki badań są w normie oraz pomocniczych funkcji zwracających górną i dolną granicę normy badania.
   - 	Zaimplementowanie tabeli przedstawiającej wyniki pacjenta oraz informacji, czy podany wynik jest w normie.
   - 	Przygotowanie informacji zwrotnej o ogólnym rezultacie wyników, podsumowującej dane w czytelny sposób dla użytkownika.
   - 	Opublikowanie aplikacji za pomocą Streamlit Community Cloud.  
2. **Uzupełnianie informacji o specjalistach oraz powiązanych badaniach**:  
   - Dodanie do aplikacji informacji o specjalistach, do których można udać się w celu dalszej diagnostyki po uzyskaniu nieprawidłowego wyniku badania oraz o innych badaniach powiązanych z nieprawidłowymi wynikami. 
3.	**Przeprowadzenie testów funkcjonalnych interfejsu użytkownika.**
4.	**Przygotowanie dokumentacji projektu.**

---

### b. Warunki licencyjne do oprogramowania
Licencja: **CC BY-NC 4.0 (Uznanie autorstwa – Użycie niekomercyjne).**

---

## 3. Specyfikacja wymagań

| Identyfikator | Nazwa                           | Opis                                                                                                                                                   | Priorytet | Kategoria      |
|---------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|
| W-001         | Pobieranie norm wyników badań    | Pobranie norm badań ze strony internetowej Leksykon.pl za pomocą scrapera.                                                                            | 1         | Funkcjonalne   |
| W-002         | Ograniczenie grupy użytkowników | System przeznaczony dla kobiet w wieku 18–26 lat, co weryfikowane jest po przejściu na stronę. W przypadku niespełnienia przez użytkownika wymagań odnośnie płci i wieku wyświetla się informacja o możliwych błędach w interpretacji wyników badań. | 1         | Funkcjonalne   |
| W-003         | Wybór badań                      | System uwzględnia tylko określone wyniki badań, np. hormonów, morfologii czy prób wątrobowych.                                                           | 2         | Funkcjonalne   |
| W-004         | Wprowadzanie wyników badań       | Użytkownik wprowadza wybrane wyniki badań, które są szczególnie ważne dla kobiet w wieku 18-26 lat.                                                     | 1         | Funkcjonalne   |
| W-005         | Analiza wyników                  | System sprawdza, czy wprowadzone wyniki są w normie na podstawie norm pobranych ze strony internetowej.                                                | 1         | Funkcjonalne   |
| W-006         | Wskazanie specjalisty            | W przypadku nieprawidłowych wyników, które nie mieszczą się w ustalonych normach system zaleca wizytę u odpowiedniego specjalisty (np. endokrynolog). | 1         | Funkcjonalne   |
| W-007         | Stworzenie powiązań              | Do każdego badania zostały przypisane powiązane badania oraz specjaliści, na podstawie wywiadu z lekarzem oraz źródeł medycznych.                        | 1         | Funkcjonalne   |
| W-008         | Interfejs graficzny              | Łatwa obsługa i przejrzystość procesu wprowadzania danych.                                                                                              | 1         | Niefunkcjonalne|
| W-009         | Interfejs użytkownika           | Dostosowanie interfejsu do komputerów.                                                                                                                 | 2         | Niefunkcjonalne|
| W-010         | Wydajność                        | Szybka analiza wyników niezależnie od liczby wprowadzonych badań.                                                                                      | 2         | Niefunkcjonalne|

## 4. Architektura systemu/oprogramowania

### a. Architektura rozwoju

Stos technologiczny wykorzystany podczas tworzenia oprogramowania:

#### i. Scraper

| Nazwa                | Przeznaczenie                                                                          | Numer wersji                |
|----------------------|----------------------------------------------------------------------------------------|-----------------------------|
| PyCharm              | Środowisko programistyczne (IDE)                                                      | 2020.2.3                    |
| Środowisko wirtualne (venv) | Utworzenie izolowanego środowiska, w którym instalowane są biblioteki i ich odpowiednie wersje wymagane do działania projektu. | -                           |
| Python               | Główny język programowania                                                             | 3.12                        |
| playwright           | Interakcja z przeglądarką oraz scrapowanie danych ze strony internetowej: <br>• sync_playwright (do uruchamiania playwright w trybie synchronicznym) <br>• TimeoutError (do obsługi wyjątków związanych z czasem oczekiwania) | 1.49.1                      |
| random               | Generowanie liczb losowych                                                             | Wbudowana w Python 3.12     |
| time                 | Wstrzymywanie działania programu                                                       | Wbudowana w Python 3.12     |
| dataclasses          | Użycie dataclass do uproszczenia definicji klasy, która definiuje strukturę pojedynczego badania. | Wbudowana w Python 3.12     |

#### ii. Interfejs użytkownika

| Nazwa                | Przeznaczenie                                                                          | Numer wersji                |
|----------------------|----------------------------------------------------------------------------------------|-----------------------------|
| PyCharm              | Środowisko programistyczne (IDE)                                                      | 2020.2.3                    |
| Python               | Główny język programowania                                                             | 3.12                        |
| streamlit            | Framework aplikacji                                                                    | 1.40.1                      |
| pandas               | Wczytanie, przygotowanie danych oraz przechowywanie wyników badań użytkownika w DataFrame | 2.0.3                       |
| Image                | Obsługa obrazu                                                                         | 10.4.0                      |
| openpyxl             | Obsługa plików Excel (.xlsx)                                                           | 3.1.5                       |

#### iii. Uzupełnianie informacji o specjalistach oraz powiązanych badaniach

| Nazwa                | Przeznaczenie                                                                          | Numer wersji                |
|----------------------|----------------------------------------------------------------------------------------|-----------------------------|
| Microsoft Excel      | Uzupełnianie informacji o specjalistach oraz powiązanych badaniach                     | Microsoft® Excel® dla Microsoft 365 MSO (wersja 2410 kompilacji 16.0.18129.20158) 64-bitowa |

### b. Architektura uruchomieniowa

Stos technologiczny wykorzystany do uruchomienia systemu:

| Nazwa                | Przeznaczenie                                                                          | Numer wersji                |
|----------------------|----------------------------------------------------------------------------------------|-----------------------------|
| PyCharm              | Środowisko programistyczne (IDE)                                                      | 2020.2.3                    |
| Python               | Główny język programowania                                                             | 3.12                        |
| streamlit            | Framework aplikacji                                                                    | 1.40.1                      |
| pandas               | Wczytanie, przygotowanie danych oraz przechowywanie wyników badań użytkownika w DataFrame | 2.0.3                       |
| Image                | Obsługa obrazu                                                                         | 10.4.0                      |
| openpyxl             | Obsługa plików Excel (.xlsx)                                                           | 3.1.5                       |
| Streamlit Cloud      | Platforma do hostowania i uruchamiania aplikacji Streamlit. Kod aplikacji pobierany z repozytorium na GitHub. | -                           |
| Github               | Repozytorium kodu źródłowego oraz zarządzanie wersjami projektu                         | -                           |
| Przeglądarka internetowa | Wyświetlanie i obsługa interfejsu aplikacji                                           | -                           |

## 5. Testy

### a.	Scenariusze testów 

## W-001 Pobranie danych
| Nr kroku | Krok                                          | Format | Oczekiwany rezultat | Wprowadzane dane |
|----------|-----------------------------------------------|--------|---------------------|------------------|
| 1        | Uruchomienie programu i zapis wyników do pliku CSV | plik CSV | Poprawne pobranie danych (nazwy badania, nazwy podbadania, możliwych jednostek, norm) i zapis do pliku CSV. |  |

## W-002 Ograniczenie grupy użytkowników
| Nr kroku | Krok                                                    | Format         | Oczekiwany rezultat                                         | Wprowadzane dane |
|----------|---------------------------------------------------------|----------------|-------------------------------------------------------------|------------------|
| 1        | Otworzenie strony z aplikacją                          |                | Wyświetlana jest informacja o dedykowanej grupie odbiorców systemu oraz pola służące do weryfikacji wieku oraz płci użytkowników. |  |
| 2        | Podaj nam swój wiek                                    | Numeryczny     | Pole pozwalające użytkownikowi wpisać wiek                  |  |
| 3        | Wybierz swoją płeć:                                    | Checkbox       | Pole pozwalające użytkownikowi podać płeć                  | Kobieta; Mężczyzna |
| 4        | Podanie wieku mniejszego lub równego 0                 |                | Wyświetlenie informacji "Wartość musi być większa lub równa 1" | -1; -123 |
| 5        | Podanie wieku większego od 100                         |                | Wyświetlenie informacji "Wartość musi być mniejsza lub równa 100" | 123; 400 |
| 6        | Użytkownik jest mężczyzną oraz podał wiek spoza przedziału 18-26 |                | Wyświetlony komunikat o tym, że aplikacja skierowana jest do innych użytkowników oraz odnośnik do norm badań. | 10, Mężczyzna |
| 7        | Użytkownik jest mężczyzną oraz podał wiek z przedziału 18-26 |                | Wyświetlony komunikat o tym, że aplikacja skierowana jest do innych użytkowników oraz odnośnik do norm badań. | 20, Mężczyzna |
| 8        | Użytkownik jest kobietą oraz podał wiek spoza przedziału 18-26 |                | Wyświetlony komunikat o tym, że aplikacja skierowana jest do innych użytkowników oraz odnośnik do norm badań. | 16, Kobieta |
| 9        | Użytkownik jest kobietą oraz podał wiek z przedziału 18-26 |                | Pojawia się widok umożliwiający wybór badań.                | 23, Kobieta |

## W-003 Wybór badań
| Nr kroku | Krok                                                       | Format                          | Oczekiwany rezultat                                                       | Wprowadzane dane |
|----------|------------------------------------------------------------|---------------------------------|---------------------------------------------------------------------------|------------------|
| 1        | Otworzenie strony z aplikacją                             |                                 | Wyświetlana jest informacja o dedykowanej grupie odbiorców systemu oraz pola służące do weryfikacji wieku oraz płci użytkowników. |  |
| 2        | Spełnienie wymagań odnośnie płci i wieku użytkownika (kobieta, wiek z zakresu 18-26 lat) |                                 | Wyświetlenie się widoku umożliwiającego wybór badań, których wyniki chce się wprowadzić | 19, Kobieta |
| 3        | Pole pod napisem "Wybierz badania, których wyniki chcesz wprowadzić:" | Lista rozwijalna wielokrotnego wyboru | Naciśnięcie na pole powoduje wyświetlenie listy rozwijalnej z badaniami możliwymi do wprowadzenia. |  |
| 4        | Pisanie w polu pod napisem "Wybierz badania, których wyniki chcesz wprowadzić:" |                                 | Pole umożliwia wyszukania wszystkich badań, które spełniają podany warunek. Wyszukania możliwe jest po pełnej nazwie badania jak i fragmencie nazwy (%like%) | 'Że', 'Trójglicerydy' |
| 5        | Wpisanie w polu "Wybierz badania, których wyniki chcesz wprowadzić:" tekstu, który nie znajduje się wśród nazw badań w systemie. |                                 | System nie zapisuje wpisanej wartości jako wybranego badania, a użytkownik nie może przejść dalej, dopóki nie wybierze poprawnego badania z listy. | Samochód' |
| 6        | Wybór badania                                            |                                 | Powoduje wyświetlenie się pola, w którym można wprowadzić wynik badania. | Androgeny (Testosteron) |
| 7        | Wybranie z listy rozwijalnej opcji 'Zaznacz wszystko'     |                                 | Powoduje wyświetlenie się pól, który umożliwiają wprowadzenie wyników dla wszystkich możliwych badań zawartych w systemie. | Zaznacz wszystko |

## W-004 Wprowadzenie wyników badań
| Nr kroku | Krok                                                    | Format   | Oczekiwany rezultat                                                       | Wprowadzane dane |
|----------|---------------------------------------------------------|----------|---------------------------------------------------------------------------|------------------|
| 1        | Otworzenie strony z aplikacją                          |          | Wyświetlana jest informacja o dedykowanej grupie odbiorców systemu oraz pola służące do weryfikacji wieku oraz płci użytkowników. |  |
| 2        | Spełnienie wymagań odnośnie płci i wieku użytkownika (kobieta, wiek z zakresu 18-26 lat) |          | Wyświetlenie się widoku umożliwiającego wybór badań, których wyniki chce się wprowadzić | 19, Kobieta |
| 3        | Wybór co najmniej jednego badania z listy               |          | Pojawienie się pola umożliwiającego wprowadzenie wyniku badania, które zostało wybrane z listy badań | 'Hormony (TSH)' |
| 4        | Wpisanie wartości ujemnej                               | Numeryczny | Wyświetlenie komunikatu "Wartość musi być większa lub równa 0".         | -123 |
| 5        | Wpisanie wartości większej niż 500                      | Numeryczny | Wyświetlenie komunikatu "Wartość musi być mniejsza lub równa 500".      | 9999 |

## W-005, W-006 Analiza wyników
| Nr kroku | Krok                                                    | Format   | Oczekiwany rezultat                                                       | Wprowadzane dane |
|----------|---------------------------------------------------------|----------|---------------------------------------------------------------------------|------------------|
| 1        | Otworzenie strony z aplikacją                          |          | Wyświetlana jest informacja o dedykowanej grupie odbiorców systemu oraz pola służące do weryfikacji wieku oraz płci użytkowników. |  |
| 2        | Spełnienie wymagań odnośnie płci i wieku użytkownika (kobieta, wiek z zakresu 18-26 lat) |          | Wyświetlenie się widoku umożliwiającego wybór badań, których wyniki chce się wprowadzić | 18, Kobieta |
| 3        | Wybór co najmniej jednego badania z listy               |          | Pojawienie się pola umożliwiającego wprowadzenie wyniku badania, które zostało wybrane z listy badań |  |
| 4        | Naciśnięcie przycisku "Przejdź do analizy wyników"      |          | Wyświetlenie się widoku "Analiza Twoich wyników badań" zawierającego tabelę. |  |
| 5        | Naciśnięcie przycisku "Przejdź do analizy wyników" bez wyników |          | Brak działania. Widok "Analiza Twoich wyników badań" nie zostaje wyświetlony dopóki nie zostanie podany co najmniej jeden wynik badania. |  |
| 6        | Tabela z analizą wyników                                |          | Zawiera jedynie badania, których wyniki zostały uzupełnione w poprzednim kroku. |  |
| 7        | Podany wynik badania okazał się poza normą              |          | Wyświetlana jest informacja o powiązanych badaniach oraz specjaliście, do którego warto się udać. |  |
| 8        | Podany wynik badania jest w normie                      |          | Wyświetla się jedynie zakres normy i informacje, że badany wynik jest w normie. |  |
| 9        | Informacja podsumowująca wyniki badań                   |          | W przypadku, gdy wszystkie wyniki są w normie wyświetlana jest

### b. Sprawozdanie z wykonania scenariuszy testów

#### Scraper

Podczas tworzenia scrapera korzystano z możliwości nagrywania działania programu oferowanych przez bibliotekę Playwright. Nagrania umożliwiały identyfikację ewentualnych błędów oraz weryfikację poprawności poruszania się scrapera po stronie, w tym akceptację wstępnej deklaracji, wybieranie badań i podbadań oraz pomijanie niepotrzebnych badań. Napotkano dwa główne wyzwania, które wymagały dostosowania kodu. Wprowadzono następujące zmiany:

1. **Zmiana deklaracji użytkownika na stronie** – podczas tworzenia programu, strona została zaktualizowana i wprowadzono dodatkową opcję wyboru „Jestem pacjentem”. Początkowo scraper zakładał, że zawsze dostępna jest jedynie opcja „Jestem lekarzem”. Aby program działał poprawnie, konieczne było dostosowanie odpowiedniego fragmentu kodu, tak aby wybierał nową opcję „Jestem pacjentem” i kontynuował działanie.
2. **Dodanie listy wykluczeń** – część badań na stronie nie dotyczyła badań krwi, których normy były nam potrzebne do projektu. W związku z tym zdecydowano się wprowadzić listę wykluczeń, która pomijała niepotrzebne pozycje.

Po wprowadzeniu zmian scraper działał poprawnie i pobierał dane w pożądanym formacie. W tym czasie nagrano działanie programu, co stanowi potwierdzenie, że program wówczas funkcjonował zgodnie z założeniami.

Jednak obecnie scraper nie działa już prawidłowo, ponieważ struktura strony internetowej ponownie się zmieniła. Program zatrzymuje się po wybraniu opcji „Jestem pacjentem”, ponieważ struktura strony po wybraniu tej opcji jest teraz zupełnie inna. Realizacja projektu wymagała jednorazowego pobrania danych, dlatego kod nie został do niej dostosowany.

---

#### Interfejs aplikacji

W trakcie testów funkcjonalnych interfejsu aplikacji znaleziono oraz poprawiono następujące błędy:

1. **Błędne jednostki** – dane dotyczące jednostek były pobierane z kolumny ‘units’, która zawiera więcej niż jedną jednostkę, zamiast z kolumny ‘norm’, gdzie jednostki normy były poprawnie oraz jednoznacznie określone. Problem został naprawiony poprzez poprawne powiązanie norm z odpowiednimi jednostkami.
2. **Niepoprawny format pola** – pole umożliwiające wprowadzanie wyników badań akceptowało wyłącznie wartości całkowite. W zaktualizowanej wersji aplikacji wprowadzono możliwość podawania wyników z dokładnością do 0,01, co pozwala na większą precyzję.
3. **Wyświetlanie pustej tabeli** – program pierwotnie umożliwiał wyświetlenie widoku „Analiza Twoich wyników badań” w sytuacji, gdy użytkownik nie podał żadnych wyników. Postanowiono, że przejście do widoku analizy (po naciśnięciu przycisku „Przejdź do analizy”) jest możliwe jedynie po wpisaniu co najmniej jednego wyniku badań.
4. **Brak walidacji** – wcześniejsza wersja aplikacji umożliwiała wpisanie ujemnego wyniku badania, co jest błędne z medycznego punktu widzenia. W aktualizacji wprowadzono walidację, która ogranicza możliwe wartości wprowadzanych wyników do zakresu od 0 do 500.

Wszystkie błędy zostały naprawione, a następnie przeprowadzono ponowne testy aplikacji. Ostatecznie wszystkie scenariusze zakończyły się pozytywnym wynikiem, a w aktualnej wersji aplikacji nie zidentyfikowano żadnych błędów.

---

## 7. Źródła

Źródła wykorzystane do uzupełnienia powiązanych badań oraz specjalistów:

1. Diagnostyka (https://diag.pl/pacjent/)
2. DOZ.pl (https://www.doz.pl/)
3. Jakubowski Z., Kabata J., Kalinowski L., Szczepańska-Konkel M., Angielski S. (1996). *Badania laboratoryjne w codziennej praktyce*. Wydawnictwo Medyczne MAKmed.
