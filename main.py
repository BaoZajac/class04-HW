#   TREŚĆ ZADANIA
# Napisz program do obsługi ładowarki paczek.
# Każda paczka może maksymalnie zmieścić 20 kg towaru.
# Do paczki dodawane są elementy. Każdy z nich może ważyć od 1 do 10 kg.
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg,\
#   paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), a bieżący element powinien zostać dodany do nowej paczki.
# Wszystkie elementy powinny zostać wysłane.
# Program powinien pobierać maksymalną liczbę elementów do wysyłki.
# Jeśli podano element o wadze 0, program powinien zakończyć działanie, tak jakby maksymalna liczba paczek została osiągnięta.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#  1. Liczbę paczek wysłanych
#  2. Liczbę kilogramów wysłanych
#  3. Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
#  4. Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.
None
# paczka <= 20kg  #max 20kg     +
# paczka = a + b + c + ...      +
# element = a, b, c, ...        +
# 10kg >= element >= 1kg
# wysłanie paczki -> max_elementow and a + b + c + ... <= 20kg
# element = 0kg -> koniec programu
# wyswietlić podsumowania
# element > 10kg or 1kg > element > 0kg -> błąd programu

waga_elementu = int(input())
waga_paczki = 0
waga_paczki += waga_elementu
paczki_wyslane = 0
pierwszy_element = 1

if waga_paczki > 20:
    print("Twój pierwszy element jest za ciężki! Nie możemy wysłać Twojej paczki.")
    pierwszy_element = 0

while waga_elementu and pierwszy_element == 1:
    if waga_elementu == 0:
        break
    elif waga_paczki <= 20:
        print(f"Waga dodanego elementu: [{waga_elementu}kg]")
        print(f"Waga paczki: [{waga_paczki}kg]\n")
        waga_elementu = int(input())
        waga_paczki += waga_elementu
    else:
        waga_paczki -= waga_elementu
        print(f"Wyślij paczkę! Twoj paczka waży: {waga_paczki}.\n ------------------")
        waga_paczki = 0
        waga_paczki += waga_elementu



        #
        # if waga_paczki >= 20:
        #     paczki_wyslane += 1
        #     print("Wyślij paczkę!\nIlość wysłanych paczek to: " + str(paczki_wyslane) + ".")
        #     waga_elementu = int(input())
        #     waga_paczki = waga_elementu
        #     print(f"\ntest - waga nast paczki to: {waga_paczki}")
        # else:
        #     waga_elementu = int(input())
        #     waga_paczki += waga_elementu


    # else:
    #     paczki_wyslane += 1
    #     print("Wyślij paczkę!\nIlość wysłanych paczek to: " + str(paczki_wyslane) + ".")
    #     print(f"Waga paczki to: {waga_paczki}")
    #     break
else:
    print("nic")

print(f"RAPORT: \nIlość wysłanych paczek to: [{paczki_wyslane}]")


# DZIAŁA 4 - ALE PĘTLA NIESKOŃCZONA

# waga_elementu = int(input())
# waga_paczki = 0
# waga_paczki += waga_elementu
# paczki_wyslane = 0
# I_element = 0
#
#
# if waga_paczki > 20:
#     print("Twój pierwszy element jest za ciężki! Nie możemy wysłać Twojej paczki.")
#     I_element = 1
#
# while waga_elementu and I_element == 0:
#     if waga_paczki <= 20:
#         print(f"Waga dodanego elementu: [{waga_elementu}kg]")
#         print(f"Waga paczki: [{waga_paczki}kg]\n")
#         waga_elementu = int(input())
#         waga_paczki += waga_elementu
#     else:
#         paczki_wyslane += 1
#         print("Wyślij paczkę!\nIlość wysłanych paczek to: " + str(paczki_wyslane) + ".")
#         print(f"Waga paczki to: {waga_paczki}")
#         break
# else:
#     print("nic")
#
# print(f"RAPORT: \nIlość wysłanych paczek to: [{paczki_wyslane}]")

None
# DZIAŁA 3 - ALE PĘTLA NIESKOŃCZONA
# if waga_paczki > 20:
#     print("Twój pierwszy element jest za ciężki! Nie możemy wysłać Twojej paczki.")
#     I_element = 1
#
# while waga_elementu and I_element == 0:
#     if waga_paczki <= 20:
#         print(f"Waga dodanego elementu: [{waga_elementu}kg]")
#         print(f"Waga paczki: [{waga_paczki}kg]\n")
#         waga_elementu = int(input())
#         waga_paczki += waga_elementu
#     else:
#         paczki_wyslane += 1
#         print("Wyślij paczkę!\nIlość wysłanych paczek to: " + str(paczki_wyslane) + ".")
#         break
# else:
#     print("nic")
#
# print(f"RAPORT: \nIlość wysłanych paczek to: [{paczki_wyslane}]")
None
# DZIAŁA 2!
# if waga_paczki > 20:
#     print("Twój pierwszy element jest za ciężki! Nie możemy wysłać Twojej paczki.")
#     error = 1
# else:
#     while waga_elementu:
#         if waga_paczki <= 20:
#             print(f"Waga dodanego elementu: [{waga_elementu}kg]")
#             print(f"Waga paczki: [{waga_paczki}kg]\n")
#             waga_elementu = int(input())
#             waga_paczki += waga_elementu
#         else:
#             print("Wyślij paczkę!")
#             paczki_wyslane += 1
#             break
#     # else:
#     #     print("Nic")
#
# print(f"RAPORT: \nIlość wysłanych paczek to: [{paczki_wyslane}]")
None
#DZIAŁA!
# while waga_elementu:
#     if waga_paczki > 20:
#         print("Twój pierwszy element jest za ciężki! Nie możemy wysłać Twojej paczki.")
#         break
#     if waga_paczki <= 20:
#         waga_elementu = int(input())
#         waga_paczki += waga_elementu
#         if waga_paczki <= 20:
#             print(f"Waga dodanego elementu: [{waga_elementu}kg]")
#             print(f"Waga paczki: [{waga_paczki}kg]\n")
#         else:
#             print("Wyślij paczkę!")
#     else:
#         print("Nic")



# while waga_paczki <= 20:
#     waga_elementu = int(input())
#     waga_paczki += waga_elementu
#     if waga_paczki <= 20:
#         print(f"Waga ost.dod.elementu: [{waga_elementu}kg]")
#         print(f"Waga paczki: [{waga_paczki}kg]\n")
#     else:
#         print("Wyślij paczkę!")

# while waga_elementu:
#     if waga_paczki >= 20:
#         print("Wyslij paczkę!")
#     else:
#         print("Opcja 2")

# while waga_paczki >= 20:
#     print("Wyślij paczkę!")


# while waga_paczki <= 20:
#     if waga_paczki > 20:
#         print("Wyslij paczkę!")
#     else:
#         waga_elementu = int(input())
#         waga_paczki += waga_elementu
#         print(f"Waga ost.dod.elementu: [{waga_elementu}kg]")
#         print(f"Waga paczki: [{waga_paczki}kg]\n")
