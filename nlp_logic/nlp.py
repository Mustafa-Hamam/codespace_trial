from textblob import TextBlob
import wikipedia


def get_wiki(name):
    print(f"searching for: {name}")
    return wikipedia.search(name)


def sum_wiki(name):
    print(f"Summarizing: {name}")
    return wikipedia.summary(name)


def get_txtblob(text):
    """creates a text blob object for supplied text"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    text = sum_wiki(name)
    blob = get_txtblob(text)
    phrases = blob.noun_phrases
    return phrases
