econtalk-ngrams
===============

This repository computes [n-grams](https://en.wikipedia.org/wiki/N-gram) from transcripts of the [EconTalk](http://www.econtalk.org) podcast.

How to use
----------

First, scrape the transcripts 

    python scrape.py

this populates the transcripts folder with text files for each episode. To compute ngrams from transcripts in the transcripts folder, run

    python ngrams.py
    
The script will generate output in the ngrams folder, with one file for ngrams consisting of a fixed number of words. For example, the file ngrams03.csv contains a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) of n-grams of three words in the transcripts. The first few lines of this file read as follows

    3883,a lot of
    1581,are going to
    1554,one of the
    1368,the united states
    1261,going to be
    ....

This means that the phrase "a lot of" occurs 3883 times across all transcripts.
