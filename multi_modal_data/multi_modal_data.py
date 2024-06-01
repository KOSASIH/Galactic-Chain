import numpy as np
import torch
from PIL import Image
import torchvision.transforms as transforms

class MultiModalData:
    def __init__(self, image_path, text):
        self.image_path = image_path
        self.text = text

    def get_image(self):
        image = Image.open(self.image_path)
        transform = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor()])
        image = transform(image)
        return image

    def get_text(self):
        return self.text

    def get_embedding(self):
        # Implement a method to get the embedding of the multi-modal data
        # For example, using a pre-trained model like CLIP
        from clip import clip
        model, preprocess = clip.load("ViT-B/32", device="cuda")
        image_embedding = model.encode_image(self.get_image().unsqueeze(0))
        text_embedding = model.encode_text(self.get_text())
        return torch.cat((image_embedding, text_embedding), dim=1)

if __name__ == "__main__":
    pass
