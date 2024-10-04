from datetime import datetime

imieo = input("Podaj imie solenizanta: ")
while True:
    rok=input("Podaj rok urodzenia solenizanta: ")
    try:
        rok=int(rok)
        break
    except ValueError:
        print("Bład! Rok urodzenia musi być liczbą całkowitą!")

imien = input("Podaj swoje imie: ")

wiek = datetime.now().year - rok

separator=("-"*100)

szablon_urodzinowy ="""
W tym wyjątkowym dniu, życzę Ci, aby każdy kolejny dzień przynosił Ci wiele radości i spełnienia. 
Niech Twoje marzenia, nawet te najskrytsze, stają się rzeczywistością. 
Niech każdy krok na Twojej drodze będzie pełen sukcesów, a otaczający Cię ludzie niech zawsze wspierają Cię w Twoich dążeniach. 
Dużo zdrowia, uśmiechu i niekończącej się energii do podejmowania nowych wyzwań!\n\nWszystkiego najlepszego!"""

print(f"{separator}\n\n{imieo} Wszystkiego najlepszego z okazji {wiek} urodzin!\n\n {szablon_urodzinowy}\n\n{imien}")
