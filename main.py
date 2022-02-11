#   TREŚĆ ZADANIA
# Napisz program do obsługi ładowarki paczek.               +
# Każda paczka może maksymalnie zmieścić 20 kg towaru.      +
# Do paczki dodawane są elementy. Każdy z nich może ważyć od 1 do 10 kg.        +
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg,\
#   paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), a bieżący element powinien zostać dodany do nowej paczki.      +
# Wszystkie elementy powinny zostać wysłane.             +
# Program powinien pobierać maksymalną liczbę elementów do wysyłki.             +
# Jeśli podano element o wadze 0, program powinien zakończyć działanie, tak jakby maksymalna liczba paczek została osiągnięta.      +
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#  1. Liczbę paczek wysłanych           +
#  2. Liczbę kilogramów wysłanych       +
#  3. Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych            +
#  4. Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik      +
# Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.       +
None
# paczka <= 20kg  #max 20kg
# paczka = a + b + c + ...
# element = a, b, c, ...
# 10kg >= element >= 1kg
# wysłanie paczki -> max_elementow and a + b + c + ... <= 20kg
# element = 0kg -> raport
# wyswietlić podsumowania
# element > 10kg or 1kg > element > 0kg -> błąd programu

waga_elementu = input()
waga_paczki = 0
paczki_wyslane = 0
kg_wyslane = 0
najlzejsza_paczka = 20
nr_najlzejszej_paczki = 0

if waga_elementu:
    waga_elementu = float(waga_elementu)
    waga_paczki += waga_elementu

while waga_elementu:
    if (waga_elementu > 10) or (1 > waga_elementu > 0):
        waga_elementu = waga_elementu + input()         # wystąpienie błedu jest celowe
    elif waga_paczki <= 20:
        print(f"Waga dodanego elementu: [{waga_elementu}kg]")
        print(f"Aktualna waga paczki: [{waga_paczki}kg]\n")
        waga_elementu = input()
        if (waga_elementu) and (waga_elementu != "0"):
            waga_elementu = float(waga_elementu)
            waga_paczki += waga_elementu
        else:
            paczki_wyslane += 1
            print(f"Wyślij paczkę! Twoja paczka nr {paczki_wyslane} waży: {waga_paczki}kg.\n ------------------")
            kg_wyslane += waga_paczki

            if (paczki_wyslane == 1) or (najlzejsza_paczka > waga_paczki):
                najlzejsza_paczka = waga_paczki
                nr_najlzejszej_paczki = paczki_wyslane

    else:
        waga_paczki -= waga_elementu
        paczki_wyslane += 1
        print(f"Wyślij paczkę! Twoja paczka nr {paczki_wyslane} waży: {waga_paczki}kg.\n ------------------")
        kg_wyslane += waga_paczki

        if (paczki_wyslane == 1) or (najlzejsza_paczka > waga_paczki):
            najlzejsza_paczka = waga_paczki
            nr_najlzejszej_paczki = paczki_wyslane

        waga_paczki = 0
        waga_paczki += waga_elementu

    if waga_elementu:
        waga_elementu = float(waga_elementu)


if nr_najlzejszej_paczki == 0:
    najlzejsza_paczka = 0

print(f"\nRAPORT: \n\
Ilość wysłanych paczek to: [{paczki_wyslane}]\n\
Ilość wysłanych kg to: [{kg_wyslane}]\n\
Ilość pustych kg to: [{paczki_wyslane * 20 - kg_wyslane}]\n\
Najlżejsza paczka to paczka nr [{nr_najlzejszej_paczki}] i waży kg: [{najlzejsza_paczka}]")

