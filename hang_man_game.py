from random import randint
def random_word():
    ls = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby"]
    l = len(ls)
    k = randint(0, l-1)
    s = ""
    var=ls[k]
    return(var)
