#Vi importerar random modulen
import random
#Vi definerar variablerna
val1 = 0
val2 = 0
runda = 1
loop = True
point1 = 0
point2 = 0
pc = 0

#Vi gör en loop som loopar så länge det är sant annars så stänger vi av programet
while loop: 
    if input("Vill du köra?: y/N") == "y":
        pc = input("Vem vill du spela mot?: pc/player") 
        while runda < 4:   
        #spelare 1 val av hand
            val1 = input("Välj din hand: sten, sax, påse")
            if val1 == "sten": 
                val1 = 1
            elif val1 == "sax":
                val1 = 2
            else:
                val1 = 3

            #spelare 2 val av hand
            if pc == "pc":
                val2 = random.randint(1,3)

            else:
                val2 = input("Välj din hand: sten, sax, påse")
                if val2 == "sten": 
                    val2 = 1
                elif val2 == "sax":
                    val2 = 2
                else:
                    val2 = 3

            if val1 == val2:
                pass 
                print("Det blev lika")
            elif val1 == 1 and val2 == 2:
                point1 += 1
                print("poäng till spelare 1")
            elif val1 == 2 and val2 == 3:
                point1 += 1
                print("poäng till spelare 1")
            elif val1 == 3 and val2 == 1:
                point1 += 1
                print("poäng till spelare 1")
            else:
                point2 += 1
                print("poäng till spelare 2")
            runda += 1
            print("Nästa runda. Poängen är: " + str(point1) + "-" + str(point2))





    

