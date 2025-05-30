# Authors: Maya Edlund

import pytest
from unittest.mock import patch
from src.util.detector import detect_duplicates
from src.util.parser import Article

pytestmark = pytest.mark.unit


# Example articles with DOI
article_doi_1 = Article(key="key1", doi="10.1111/aaa")
article_doi_2 = Article(key="key1", doi="10.1111/aaa")
article_doi_3 = Article(key="key2", doi="10.2222/aaa")
# Example articles without DOI
article_4 = Article(key="key1", doi=None)
article_5 = Article(key="key1", doi=None)
article_6 = Article(key="key1", doi=None)


# Test cases

# Testcase 1: Only one article
def test_one_article():
    """ 
    Testcase when there is only one article
    Should throw ValueError
    """
    with patch('src.util.detector.parse', return_value=[article_doi_1]):
        with pytest.raises(ValueError):
            detect_duplicates("")

# Testcase 2: 2 matching articles 
def test_mathing_doi_articles():
    """ 
    Testcase when two articles with the same DOI number
    Should return list of articles
    """
    with patch('src.util.detector.parse', return_value=[article_doi_1, article_doi_2]):
        result = detect_duplicates("")
        assert len(result) == 1

# Testcase 3: 2 unmatching articles
def test_doi_unmatching():
    """ 
    Testcase when 2 articles have DOI but not matching
    Return empty list
    """
     with patch('src.util.detector.parse', return_value=[article_doi_1, article_doi_3]):
        result = detect_duplicates("")
        assert result == []

# Testcase 4: 2 articles without DOI but have mathing key
def test_mathing_key_articles():
    """ 
    Testcase when 2 articles dont have DOI but matching key
    Should return list of articles
    """
    with patch('src.util.detector.parse', return_value=[article_4, article_4]):
        result = detect_duplicates("")
        assert len(result) == 1

# Testcase 5: No DOI and not mathing keys
def test_unmatching_keys(controller, invalid_email):
    """
    Testcase when 2 articles dont have DOI and dont have mathing key
    Should return empty list
    """
    with patch('src.util.detector.parse', return_value=[article_4, article_5]):
        result = detect_duplicates("")
        assert result == []
