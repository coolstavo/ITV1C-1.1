def flipside(s):
    """flipside swaps s's sides
       Argument s: a string
    """
    x = len(s) // 2
    return s[x:] + s[:x]

# Tests
assert flipside("zijkant") == "kantzij"
assert flipside("huiswerk") == "werkhuis"
assert flipside("flipside") == "sideflip"
assert flipside("az") == "za"
assert flipside("a") == "a"
assert flipside("") == ""



def mult(n, m):
    """
    moet het de vermenigvuldiging
    van de twee gehele getallen n en m als 
    resultaat teruggeven.
    """
    if n == 0:
      return 0
    elif n == 1:
      return m
    else:
      return m + mult(n-1, m)



def dot(L, k):
    """ Inwendig product van beide lijsten dus L en k moeten lijsten zijn
    """
    if len(L) != len(k):
      return 0.0 
    if len(L) == 0:
      return 0.0
    else:
      return L[0]*k[0] + dot(L[1:],k[1:])



def ind(e, L):
    """
    L kan een string of lijst
    e element
    """
    if e < 0 and e not in L:
      return len(L)
    elif e == L[0]:
      return 0
    else:
      return 1 + ind(e, L[1:])



def letter_score (let):
  """""Geeft een letter en de score wordt bepaald :)"""
  if let in "adeinorst":
    return 1
  elif let in "ghl":
    return 2
  elif let in "bcmp":
    return 3
  elif let in "jkuvw":
    return 4
  elif let == "f":
    return 5
  elif let == "z":
    return 6
  elif let in "xy":
    return 8
  elif let == "q":
    return 10
  else:
    return 0
 

def scrabble_score(score):
  """de functie accepteerd, s die alleen kleine letters (strings) mag bevatten"""
  if score == "":
    return 0
  else:
    return letter_score(score[0]) + scrabble_score(score[1:])


assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0

def one_dna_to_rna(c):
  """Converts a single-character c from DNA nucleotide
  to complementary RNA nucleotide"""
  if c == "A":
    return "U"
  elif c == "C":
    return "G"
  elif c == "G":
    return "C"
  elif c == "T":
    return "A"
  else:
    return ""

def transcribe(s):
  """"accepteerd s als DNA string en transformeert het naar RNA"""
  if len(s) == 0:
    return ""
  else:
    return one_dna_to_rna(s[0]) + transcribe(s[1:])
  

# Tests
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'  # De spatie verdwijnt
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('hanze')    == ''         # Andere tekens verdwijnen
assert transcribe('')         == ''
