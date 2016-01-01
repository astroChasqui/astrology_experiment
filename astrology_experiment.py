#!/usr/bin/env python

from bs4 import BeautifulSoup
from random import shuffle
import requests, argparse


def main(file_out="astrology_experiment.txt", today=True):

    signs = {1 : "Aries",
             2 : "Taurus",
             3 : "Gemini",
             4 : "Cancer",
             5 : "Leo",
             6 : "Virgo",
             7 : "Libra",
             8 : "Scorpio",
             9 : "Sagittarius",
             10: "Capricorn",
             11: "Aquarius",
             12: "Pisces"}

    base = "http://www.horoscope.com/us/horoscopes/general/"
    if today:
        base += "horoscope-general-daily-today.aspx?sign="
    else:
        base += "horoscope-general-daily-yesterday.aspx?sign="

    horoscope = {}
    for idx in range(1, 13):
        url = base + str(idx)
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
        horoscope[signs[idx]] = \
          soup.find_all("div", {"class": "block-horoscope-text"})\
          [0].text.strip().replace(signs[idx], '---')

    date = soup.find_all("div", {"class": "block-horoscope-date"})\
           [0].text.strip()

    letters = "A B C D E F G H I J K L".split()
    signs_letters = {}
    x = range(1, 13)
    shuffle(x)
    with open(file_out, 'w') as f:
        f.write("Source: www.horoscope.com, {0}\n\n".format(date))
        for idx, idx_shuffled in zip(range(1,13), x):
            signs_letters[letters[idx-1]] = signs[idx_shuffled]
            f.write("{0}: {1}\n\n".\
                    format(letters[idx-1], horoscope[signs[idx_shuffled]]))
        f.write("\nKey:\n\n")
        for sign in signs_letters:
            f.write("{0} {1}\n".format(sign, signs_letters[sign]))

    print "Success! Horoscope date: {0}".format(date)
    
    return horoscope


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
               description='Scrapes a daily horoscope from www.horoscope.com '+\
                           'and creates a shuffled version of it with letter '+\
                           'labels to run the astrology experiment. A key is '+\
                           'also provided.')
    parser.add_argument('-f', '--file_out', default='astrology_experiment.txt',
                        help='output file (default="astrology_experiment.txt")')
    parser.add_argument('-t', '--today', action="store_true",\
                        help='Use today\'s horoscope, not yesterday\'s')
    args = parser.parse_args()
    main(args.file_out, args.today)
