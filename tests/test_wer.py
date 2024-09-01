import unittest
from devnagari_wer.normalizer import normalize
from devnagari_wer.wer import calculate_wer

class TestDevnagariWER(unittest.TestCase):

    def test_normalization(self):
        self.assertEqual(normalize('यह एक परीक्षण है।'), 'यह एक परीक्षण है')
    
    def test_wer(self):
        reference = normalize('यह एक परीक्षण है')
        hypothesis = normalize('यह एक परिक्षण है')
        self.assertAlmostEqual(calculate_wer(reference, hypothesis), 0.25, places=2)

if __name__ == '__main__':
    unittest.main()
