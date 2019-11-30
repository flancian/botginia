#!/usr/bin/env python3

import glob
import os
import random
import tweepy

import secret

DEBUG = True

auth = tweepy.OAuthHandler("pagwyePax8TSOveeGYveRZ153", secret.CONSUMER_SECRET)
auth.set_access_token("1200715929707044865-6ZpORfGjD8rs3qBgwOofpNYj3ztS9j", secret.ACCESS_TOKEN_SECRET)

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
            next
        l = line.split("\n")
        output.append(" ".join(l).strip())
    return output

def score(string):
    # Right now this defaults to 0 and has some ad-hoc heuristics for favouring (-1) 
    # and deprioritizing (1) phrases. "nice".
    if len(string) < 20:
        return 1
    if len(string) > 270:
        return 1
    return 0

def main():
    # Choose a book.
    clean_books = [clean_book(book) for book in get_books()]
    book = random.choice(clean_books)

    # Choose k phrases from that book.
    phrases = random.choices(book, k=10)

    # Score them and pick the first.
    phrase = sorted(phrases, key=score)[0]

    # Score them and pick the first.
    if DEBUG:
        print("Would tweet:", phrase)
    else:
        api.update_status(phrase)


if __name__ == "__main__": # how is this still a thing?
    main()
