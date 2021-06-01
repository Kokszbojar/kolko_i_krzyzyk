# Kółko i krzyżyk gra w konsoli

# Wstępne utworzenie pustej planszy

PLANSZA = [[" " for x in range(3)] for y in range(3)]

# Wyświetlenie planszy

def wyświetl():
    print("\n  ", PLANSZA[0][0], " | ", PLANSZA[1][0]," | ", PLANSZA[2][0])
    print(" -----------------")
    print("  ", PLANSZA[0][1], " | ", PLANSZA[1][1]," | ", PLANSZA[2][1])
    print(" -----------------")
    print("  ", PLANSZA[0][2], " | ", PLANSZA[1][2]," | ", PLANSZA[2][2],"\n")

# Wybór pola gracza X

def gX():
    print("Wybór gracza X\n")
    x = int(input("Wprowadź numer kolumny wybranego pola:  "))
    y = int(input("Wprowadź numer wiersza wybranego pola:  "))
    x = x - 1
    y = y - 1
    if(PLANSZA[x][y] == " "):
        PLANSZA[x][y] = "X"
    else:
        print("\nTa pozycja jest zajęta! Wybierz inne pole\n")
        wyświetl()
        gX()

# Wybór pola gracza O
    
def gO():
    print("Wybór gracza O\n")
    x = int(input("Wprowadź numer kolumny wybranego pola:  "))
    y = int(input("Wprowadź numer wiersza wybranego pola:  "))
    x = x - 1
    y = y - 1
    if(PLANSZA[x][y] == " "):
        PLANSZA[x][y] = "O"
    else:
        print("\nTa pozycja jest zajęta! Wybierz inne pole\n")
        wyświetl()
        gO()

# Główny program

wyświetl()
i = 0
while(i < 9):
    if (i % 2 == 0):
        gX()
        wyświetl()
    elif (i % 2 == 1):
        gO()
        wyświetl()
    if (i > 3):
        #pozioma wygrana
        for j in range(3):
            if(PLANSZA[0][j] == PLANSZA[1][j] and PLANSZA[0][j] == PLANSZA[2][j] and PLANSZA[0][j] != " "):
                print("\nWygrywa gracz ", PLANSZA[0][j])
                i = 9

        #pionowa wygrana
        for j in range(3):
            if(PLANSZA[j][0] == PLANSZA[j][1] and PLANSZA[j][0] == PLANSZA[j][2] and PLANSZA[j][0] != " "):
                print("\nWygrywa gracz ", PLANSZA[j][0])
                i = 9
                
        #skos Lg-Pd
        if(PLANSZA[0][0] == PLANSZA[1][1] and PLANSZA[0][0] == PLANSZA[2][2] and PLANSZA[1][1] != " "):
            print("\nWygrywa gracz ", PLANSZA[1][1])
            i = 9
                
        #skos Ld-Pg
        if(PLANSZA[2][0] == PLANSZA[1][1] and PLANSZA[2][0] == PLANSZA[0][2] and PLANSZA[1][1] != " "):
            print("\nWygrywa gracz ", PLANSZA[1][1])
            i = 9

    i += 1
    





