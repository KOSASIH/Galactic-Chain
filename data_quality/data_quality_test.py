import unittest
from galactic_chain.data_quality import DataQuality

class TestDataQuality(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6], 'C': ['a', 'b', 'c', 'd', 'e']})

    def test_clean_data(self):
        data_quality = DataQuality(self.data)
        cleaned_data = data_quality.clean_data()
        self.assertEqual(cleaned_data.shape[0], 5)

    def test_validate_data(self):
        data_quality = DataQuality(self.data)
        validated_data = data_quality.validate_data()
        self.assertEqual(validated_data['C'].iloc[0], 'a')

    def test_normalize_data(self):
        data_quality = DataQuality(self.data)
        normalized_data = data_quality.normalize_data()
        self.assertAlmostEqual(normalized_data['A'].mean(), 0)

if __name__ == '__main__':
    unittest.main()
