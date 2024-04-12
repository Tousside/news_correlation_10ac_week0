from main import tf_idf_similarty
from scikit-learn.feature_extraction.text import TfidfVectorizer
from scikit-learn.metrics.pairwise import cosine_similarity
import unittest
import numpy

class TestMain(unittest.TestCase):
    def test_tf_idf_similarty(self):
        title="superstar chef yannick alléno brings refined french cuisine pavyllon london"
        body= "avyllon london four seasons hotel london park lane one worlds best chefs\
    created new culinary stage london yannick alléno superstar french chef \
    nabbed impressive 15 michelin stars recently made uk debut opening pavyllon\
    london located four seasons hotel london park lane fashionable mayfair\
    new restaurant showcases allénos modern"
        self.assertIsInstance(tf_idf_similarity(title, body), numpy.float64)
        print("Test passed")

if __name__== "__tf_idf_similarty__":
    title="superstar chef yannick alléno brings refined french cuisine pavyllon london"
    body= "avyllon london four seasons hotel london park lane one worlds best chefs\
    created new culinary stage london yannick alléno superstar french chef \
    nabbed impressive 15 michelin stars recently made uk debut opening pavyllon\
    london located four seasons hotel london park lane fashionable mayfair\
    new restaurant showcases allénos modern"
    unittest.tf_idf_similarty(title, body)

