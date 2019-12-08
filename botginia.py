#!/usr/bin/env python3

import glob
import itertools
import os
import random
import tweepy

import config
# config.py Must export:
# - CONSUMER_SECRET
# - ACCESS_TOKEN_SECRET
# - DEBUG
DEBUG = config.DEBUG
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler("pagwyePax8TSOveeGYveRZ153", CONSUMER_SECRET)
auth.set_access_token("1200715929707044865-6ZpORfGjD8rs3qBgwOofpNYj3ztS9j", ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_books():
    # Read all books (keep them separate in a list) to get things started.
    books_glob = "books/*.txt"
    books = []
    for book in glob.glob(books_glob):
        books.append(open(book, "r").read())
    return books

def clean_book(book):
    # Ugly but, you know, it works for now.
    lines = book.split("\n\n")
    output = []
    for line in lines:
        if line.startswith('#'):
            continue
        l = line.split("\n")
        output.append(" ".join(l).strip())
    return output

def score(string):
    # Right now this defaults to 0 and has some ad-hoc heuristics for favouring (-1) 
    # and deprioritizing (1) phrases. Unix-nice-like.
    if len(string) > 270:
        return 1
    if len(string) < 80:
        return 1
    if string[-1] in ['.', '\'', '\"', '!', '?']:
        return -1
    if len(string) > 150:
        return -1
    return 0

def main():
    # Clean up books.
    clean_books = [clean_book(book) for book in get_books()]

    # Define a corpus: either all books ("flatten") or one chosen at random.
    corpus = [phrase for book in clean_books for phrase in book]
    # corpus = random.choice(clean_books)

    # Note to self: I want to write the following but it doesn't work.
    # corpus = [phrase for phrase in book for book in clean_books]

    # Choose k phrases from the corpus and score them.
    phrases = sorted(random.choices(corpus, k=20), key=score)

    # Pick the highest scoring.
    phrase = phrases[0]

    # Print or tweet.
    if DEBUG:
        # import pdb; pdb.set_trace()
        from pprint import pprint
        print("Phrases considered:")
        pprint(phrases)
        print("Would tweet:", phrase)
    else:
        api.update_status(phrase)


if __name__ == "__main__": # how is this still a thing?
    main()
