"""cheks valid words and count number of times
   every char appears in it"""
import enchant
from sys import argv

stria = argv[1:]

def wrapper(fuc):
    """Decorator separate valid words

    function use Enchant to separate valid words
    from spellwrong words got as atguments from command line.
    """
    def checkword(words):
        che = enchant.Dict("en_US")
        wrong = []
        for i in words:
            #if True then word is in dictionary enchant
            if che.check(i) == True:
                continue
            else:
                #if False separate word in two lists
                wrong.append(i)
                words.remove(i)
        if wrong:
            print ", ".join(wrong) + ": %d words got wrong" % len(wrong)
        ret = fuc(words)
        return ret
    return checkword


@wrapper
def stri(words):
    lenwords = len(words)
    words = " ".join(words)
    result = []
    [result.append({x: words.count(x)})
    for x in words if {x: words.count(x)} not in result]
    if result:
        print "words:", lenwords, "\nCharacters:", len(words), "\n", result
        return result

stri(stria)
