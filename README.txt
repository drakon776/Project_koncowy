repo na githubie

Django/Flask

Klient:
Panel Klienta:
    --Imie
    --Nazwisko
    --Telefon
    --Adres [ul./os.] [nr. bloku/domu] [nr.mieszkania]
    --email (Opcjonalnie)
- Klient wybiera co chce zareklamowac
- Klient wybiera jak objawia sie usterka
    --kilka opcji do wybrania
    --tekst wlasny
- Klient wybiera date/godzine pasującą dla klienta z DOSTĘPNYCH terminów
- Klient wybiera jak chce dostac informacje zwrotna co do umowionego terminu
    --email
    --SMS
    --Rozmowa Telefoniczna

Serwis:
Panel Serwisu:
    --Imie
    --Nazwisko
    --Specjalizacja
    --Historia wykonanych Napraw
- oznacza odebrane zlecenia
    --wysyla maila lub SMS do klienta ze zlecenie zosało odebrane
- Informuje klienta (SMS/Email/Rozmowa Telefoniczna) o dacie pojawienia sie serwisanta
    --data
    --godzina
    --adres
    --Który Serwisant się pojawi
-odznacza wykonane zleceie
    --wypisuje użyty materiał
    --dopisuje wykonany adres do montera
    --wysyla SMS/Email o wykonanej usterce do klienta(szablon)

