from random import randint
def random_word():
    ls = ["Aardvark", "Baboon", "Cat", "Dog", "Elephant", "Flamingo", "Giraffe", 
    "Hippopotamus", "Iguana", "Jaguar", "Kangaroo", "Lemur", "Meerkat", 
    "Narwhal", "Octopus", "Penguin", "Quokka", "Rabbit", "Squirrel", 
    "Tiger", "Urchin", "Vulture", "Walrus", "Xerus", "Yak", "Zebra",
    "Amaryllis", "Begonia", "Chrysanthemum", "Daffodil", "Edelweiss", 
    "Foxglove", "Gardenia", "Hibiscus", "Iris", "Jasmine", "Lavender", 
    "Marigold", "Narcissus", "Orchid", "Peony", "Quince", "Rose", 
    "Sunflower", "Tulip", "Uvularia", "Violet", "Wisteria", "Xanthium", 
    "Yarrow", "Zinnia","Albatross", "Bluejay", "Canary", "Dove", "Eagle", "Falcon", "Goose", 
    "Hummingbird", "Ibis", "Jay", "Kingfisher", "Lark", "Magpie", 
    "Nightingale", "Owl", "Parrot", "Quail", "Robin", "Sparrow", "Toucan", 
    "Umbrellabird", "Vireo", "Woodpecker", "Xenops", "Yellowhammer","Alder", "Birch", "Cedar", "Dogwood", "Elm", "Fir", "Gingko", "Hickory", 
    "Ironwood", "Juniper", "Kauri", "Larch", "Maple", "Nutmeg", "Oak", 
    "Pine", "Quercus", "Redwood", "Spruce", "Teak", "Ulmus", "Vine", 
    "Willow", "Xylosma", "Yew"]
    l = len(ls)
    k = randint(0, l-1)
    s = ""
    var=ls[k]
    return(var)
