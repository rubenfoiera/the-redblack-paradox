import random

new_list2 = []

def number_creator():
    #counter_number_creator = 0
    random_numb = random.randint(0, 1)
    #if random_numb == 1:
    #    new_list2.append(random_numb)
    #    counter_number_creator += 1
    #else:
    #    new_list2.append(random_numb)
    return random_numb

def lenght_of_ones(x):
    c = 0
    win_counter = 0
    lose_counter = 0

    while c < x:
        a = number_creator()
        if a == 1:
            print(a)
        else:
            print("zero came")
            break
        c += 1

    if a == 0:
        win_counter += 1
    else:
        lose_counter += 1

    print("Wins:",win_counter)
    print("Loses:",lose_counter)



lenght_of_ones(5)



#b= 0
#while b < 20:
#    random_numb = random.randint(0,1)
#    new_list2.append(random_numb)
#    b += 1
#
#print(new_list2)
#counter_ONES = 0
#
#for number in new_list2:
#    if number == 1:
#        counter_ONES += 1
#        print(number)
#
#    else:
#        break
#
#    if new_list2[counter_ONES+1] == 0:
#        print("WON")
#
#    else:
#        print("NOPE")
#
#
#
#


#a=0
#kopf=0.000
#zahl=0.000
#while a < 9:
#    zufallszahl = random.randint(0,1)
#    if zufallszahl == 0:
#        kopf+=1
#        print("Kopf")
#    else:
#        zahl+=1
#        print("Zahl")
#
#    a += 1
#
#print("Anzahl Kopf = " + str(kopf), "Anzahl Zahl = " + str(zahl))
#
#prozentsatz_kopf = (kopf / (kopf+zahl)) * 100
#prozentsatz_zahl = (zahl / (kopf+zahl)) * 100
#
#print("Prozentsatz Kopf = " + str(prozentsatz_kopf))
#print("Prozentsatz Zahl = " + str(prozentsatz_zahl))
#
#print("Das ist eine Nummer: %s Und das ist ein String: %s" %(123.1,"Hello"))
#print("Das ist ebenfalls einen String: {}".format("Hello"))
#
#list = [1,2,3]
#a=5
#new_list = list + [a]
#new_list.append(6)
#print(new_list)