# GuardianPuz

Given a [Guardian](https://www.guardian.co.uk/crosswords) cryptic crossword number, spits out a puz file suitable for use with [cursewords](https://parkerhiggins.net/2019/03/cursewords-crossword-puzzle-solving-interface-terminal/)

## Requirements
* Python 2.something
* [puzpy](https://github.com/alexdej/puzpy) - `pip install puzpy`
* [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - `pip install bs4`

## Usage

`python guardianpuz.py <NUMBER>`

NUMBER is the number of the crossword you want to load, for example 27763. You can find it in the URL, e.g. https://www.theguardian.com/crosswords/cryptic/27763.

This creates a file named output.puz with your crossword, to open in the puz-reading program of your choice. I only test with cursewords because I'm lazy.

## Example screenshot

![cursewords running with a file created by GuardianPuz](doc/example.png)

## Things I'd love for this to do but haven't yet implemented

* For non-prize crosswords, get the solution (i.e. press 'reveal all', read all the solution text. Does BS4 know how to javascript?)
* Be able to fetch prize, quiptic, everyman, etc. crosswords
* Have code that is not godawful and hacked together when I was too lazy to solve the Prize crossword, but not too lazy to do _something_.
* Be distributed via pip
* Have any kind of error handling at all
* Not to be written in python 2 (but I think puzpy only works in 2, so not my fault, guv)
* Have the ability to find the latest crossword in a category. I can't see a good way to do this looking at the structure of the Guardian's listing pages.

## Other notes
* Since we're crawling a web page to do this and rely on specific structures, things might break at any time. I probably would have been better off using my time to send the Guardian a nice message asking them to provide puz files daily.

## Contributing

Let's be honest, you're probably better at programming than I am. Just hack on it and send me patches.
