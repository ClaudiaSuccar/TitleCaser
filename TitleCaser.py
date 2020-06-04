myStr = input("Enter the string to be formalized:\n")
no_cap = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet", "a", "an", "the", "at", "in", "around", "by",
          "after", "along", "from", "of", "on", "to", "with", "without"]

def joinIt(joined):
    converted = " ".join(joined)
    print(converted)

def capsIt(capitalized):
    new_ar = []
    for n in capitalized:
        n = n.capitalize()
        new_ar.append(n)
    joinIt(new_ar)


def cleanUp(ar):
    ar = ar.lower()
    ar = ar.split(' ')
    capsIt(ar)


cleanUp(myStr)
