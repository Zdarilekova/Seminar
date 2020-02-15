##Výskumy prezradili jednu zaujímavú vec.
##Človek dokáže prečítať slová aj bez toho, aby jednotlivé písmená dávali zmysel.
##Je to spôsobené tým, že mozog číta slová ako celok, nie po jednotlivých písmenách.
##Stačí, aby bolo prvé a posledné písmeno na tom istom mieste, tak ako v klasickom slove.
##Po anglicky sa to volá Scrambled text, čiže poprehadzovaný text
##V textovom súbore poprehadzovany_text1_vstup.txt je pripravený vstupný súbor.
##Vytvorte program, ktorý:
##   
##    prečíta a vypíše textový súbor,
##    v texte identifikuje jednotlivé slová
##        (predpokladajme, že text obsahuje iba slová a medzery,
##         a žiadne iné znaky neobsahuje),
##    v slove náhodne poprehadzuje písmená, okrem prvého a posledného písmena,
##    takto transformovaný text vypíše na obrazovku,
##    takto transformovaný text uloží do textového súboru poprehadzovany_text1.txt.
##    
##Ukážka vstupného textového súboru:
##    Výskumy prezradili jednu zaujímavú vec
##    Tou je že človek môže prečítať slová aj bez toho aby jednotlivé písmená dávali zmysel
##    Je to spôsobené tým že mozog číta slová ako celok
##    
##Ukážka výstupného textového súboru:
##    Vsuýmky pdrirlazei jdenu zvjaauímú vec
##    Tou je že čevlok môže pčíertať svolá aj bez toho aby jvtdoeliné písmneá dalávi zymsel
##    Je to spôbeonsé tým že mzoog číta svloá ako cloek

import random
subor1 = open('poprehadzovany_text1_vstup.txt', 'r')
subor2 = open('poprehadzovany_text1.txt', 'w')     



subor1.close()
subor2.close()
    


    
