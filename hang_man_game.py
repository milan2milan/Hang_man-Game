from random import randint
def random_word():
    ls = ["Iron", "thar", "spider", "hulk", "doctor Strange",
      "black panther", "marvel", "captain america"]
    l = len(ls)
    k = randint(0, l-1)
    s = ""
    var=ls[k]
    return(var)
