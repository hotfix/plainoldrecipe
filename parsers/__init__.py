from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.lovingitvegan import Lovingitvegan
from parsers.minimalistbaker import Minimalistbaker
from parsers.bowlofdelicious import Bowlofdelicious
from parsers.chefkoch import Chefkoch
from parsers.hostthetoast import Hostthetoast

PARSERS = {
    'gimmesomeoven.com': Gimmesomeoven,
    'smittenkitchen.com': Smittenkitchen,
    'letsdishrecipes.com': Letsdishrecipes,
    'lovingitvegan.com': Lovingitvegan,
    'minimalistbaker.com': Minimalistbaker,
    'www.chefkoch.de': Chefkoch,
    'www.bowlofdelicious.com': Bowlofdelicious,
    'bowlofdelicious.com': Bowlofdelicious,
    'hostthetoast.com': Hostthetoast,
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser()
