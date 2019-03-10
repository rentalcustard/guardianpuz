import puz
from bs4 import BeautifulSoup
import urllib2

page = urllib2.urlopen("https://www.theguardian.com/crosswords/accessible/cryptic/27763").read()
soup = BeautifulSoup(page)
clue_page = urllib2.urlopen("https://www.theguardian.com/crosswords/cryptic/27763").read()
clue_soup = BeautifulSoup(clue_page)
p = puz.Puzzle()
p.height = 15
p.width = 15
p.title = "test"
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

for clue in clue_soup.find_all(attrs={"class": "crossword__clue"}):
    #get clue number and text, need to do this for all across
    # then we need to build a list which is e.g. 1A - 1D - 2A - 3A - 4D - 5A
    print clue.get_text()
    clues.append(clue.get_text().split(")"))

clues = sorted(clues, key=lambda c: c[0].replace('(', ''))
print clues

fill = []
for row in soup.find_all(attrs={"class": "crossword__accessible-row-data"}):
    row_text = ["-"] * 15
    for gap in row.get_text().split(": ")[1].split(" "):
        row_text[letter_to_number[gap] - 1] = "."
    fill.append(''.join(row_text))

fill = ''.join(fill)
print fill
print len(fill)
        
p.fill = fill
p.clues = clues

p.solution = fill.replace("-", "A")

p.save('output.puz')
