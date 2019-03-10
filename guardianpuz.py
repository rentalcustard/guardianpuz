import puz
from bs4 import BeautifulSoup
import urllib2
import sys

crossword_number = sys.argv[1]

accessible_url = "https://www.theguardian.com/crosswords/accessible/cryptic/" + crossword_number
standard_url = "https://www.theguardian.com/crosswords/cryptic/" + crossword_number

page = urllib2.urlopen(accessible_url).read()
soup = BeautifulSoup(page, features='html.parser')
clue_page = urllib2.urlopen(standard_url).read()

clue_soup = BeautifulSoup(clue_page, features='html.parser')
p = puz.Puzzle()
p.height = 15
p.width = 15
p.title = "Guardian Cryptic Crossword No " + crossword_number
p.author = clue_soup.find(attrs={"itemprop": "author"}).find(attrs={"itemprop": "name"}).get_text()
clues = []

letter_to_number = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15
        }

class Clue:
    def __init__(self, number, direction, text):
        self.number = number
        self.direction = direction
        self.text = text

    def __lt__(self, other):
        if self.number == other.number:
            if self.direction == 'D':
                return False
            else:
                return True
        else:
            return self.number < other.number

clues = []
for clue in clue_soup.find(attrs={"class": "crossword__clues--across"}).find_all(attrs={"class": "crossword__clue"}):
    #get clue number and text, need to do this for all across
    # then we need to build a list which is e.g. 1A - 1D - 2A - 3A - 4D - 5A
    clue_number = int(clue.find(attrs={"class": "crossword__clue__number"}).get_text())
    clue_direction = "A"
    clue_text = clue.find(attrs={"class": "crossword__clue__text"}).get_text()
    clues.append(Clue(clue_number, clue_direction, clue_text))

for clue in clue_soup.find(attrs={"class": "crossword__clues--down"}).find_all(attrs={"class": "crossword__clue"}):
    #get clue number and text, need to do this for all across
    # then we need to build a list which is e.g. 1A - 1D - 2A - 3A - 4D - 5A
    clue_number = int(clue.find(attrs={"class": "crossword__clue__number"}).get_text())
    clue_direction = "D"
    clue_text = clue.find(attrs={"class": "crossword__clue__text"}).get_text()
    clues.append(Clue(clue_number, clue_direction, clue_text))

sorted_clue_texts = map(lambda c: c.text, sorted(clues))

fill = []
for row in soup.find_all(attrs={"class": "crossword__accessible-row-data"}):
    row_text = ["-"] * 15
    for gap in row.get_text().split(": ")[1].split(" "):
        row_text[letter_to_number[gap] - 1] = "."
    fill.append(''.join(row_text))

fill = ''.join(fill)

p.fill = fill
p.clues = sorted_clue_texts

p.solution = fill.replace("-", "A")

p.save('output.puz')
