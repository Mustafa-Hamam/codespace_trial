from nlp_logic.nlp import get_wiki, sum_wiki, get_txtblob,get_phrases

def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors")