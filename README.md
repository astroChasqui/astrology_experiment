# The Astrology Experiment

A daily horoscope is scraped from the web, shuffled, and the signs removed so that you do not know which horoscope is for which sign. A key is provided at the end.

## Code

Written for Python2. Requires the BeautifulSoup library. Examples to run from the terminal are provided below.

The default:

```
./astrology_experiment.py 
```

creates a file astrology_experiment.txt with yesterday's text from [horoscope.com](http://www.horoscope.com). If you want today's horoscope instead, try the -t (--today) flag:

```
./astrology_experiment.py -t -f horoscope_today.txt
```

Here the -f (--file\_out) flag was used to specify the output file name (horoscope_today.txt). You can also try the shorter horoscope from [sfgate.com](http://www.sfgate.com/horoscope), which downloads a lot quicker, by using the -s (--source) flag:

```
./astrology_experiment.py -s sfgate -t -f sfgate_today.txt
```

Again, we specified the output file name here (sfgate_today.txt).

## Implementation

Make a group of people read the entire horoscope and ask them to tell you which one best matches their day **yesterday**. Then, show them the key and ask who got their horoscope "right". Go on to discuss how accurate are the predictions of astrology.

An implementation file is included in this repo. This activity was created by the [Astronomical Society of the Pacific](http://astrosociety.org/edu/astro/act3/astrologyprint.html).

I run this experiment on the first day of my introductory astronomy classes for non-majors. So far all my results have been around 8% "accurate", a suspicious 1/12 chance ... hmmm ...

Have fun!
