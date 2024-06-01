import unittest
from multi_modal_data import MultiModalData

class TestMultiModalData(unittest.TestCase):
    def test_get_image(self):
        data = MultiModalData("image.jpg", "This is a test image")
        image = data.get_image()
        self.assertIsInstance(image, torch.Tensor)
        self.assertEqual(image.shape, (3, 224, 224))

    def test_get_text(self):
        data = MultiModalData("image.jpg", "This is a test image")
        text = data.get_text()
        self.assertIsInstance(text, str)
        self.assertEqual(text, "This is a test image")

    def test_get_embedding(self):
        data = MultiModalData("image.jpg", "This is a test image")
        embedding = data.get_embedding()
        self.assertIsInstance(embedding, torch.Tensor)
        self.assertEqual(embedding.shape, (1, 512))

if __name__ == "__main__":
    unittest.main()
