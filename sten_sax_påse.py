import random

val1 = 0
val2 = 0
runda = 1
loop = True
point1 = 0
point2 = 0
pc = 0


while loop: 
    if input("Vill du köra?: y/N") == "y":
        pc = input("Vem vill du spela mot?: pc/player")    
        #spelare 1
         val1 = input("Välj din hand: sten, sax, påse")
            if val1 == "sten": 
                val1 = 1
            elif val1 == "sax":
                val1 = 2
            else val1 == "påse":
                val1 = 3        
        #spelare
        if pc == "pc":  
            val1 = random.randint(1,3)
            else:
            val2 = input("Välj din hand: sten, sax, påse")
            if val2 == "sten": 
                val2 = 1
            elif val2 == "sax":
                val2 = 2
            else val2 == "påse":
                val2 = 3
            if val1 == val2:
                pass
            elif val1 == 1 and val2 == 2:
                point1 += 1
            elif val1 == 2 and val2 == 3:
                point1 += 1
            elif val1 == 3 and val2 == 1:
                point1 += 1
            else:
                point2 += 1
   




    

