from nlp_logic.nlp import get_phrases

def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors")