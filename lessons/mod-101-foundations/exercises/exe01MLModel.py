import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import requests
from io import BytesIO

# Load pre-trained ResNet
model = models.resnet18(pretrained=True)
model.eval()

# Download a sample image
url = "https://github.com/pytorch/hub/raw/master/images/dog.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Prepare image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

input_tensor = preprocess(img)
input_batch = input_tensor.unsqueeze(0)

# Inference
with torch.no_grad():
    output = model(input_batch)

# Get prediction
_, predicted = torch.max(output, 1)
print(f"Predicted class: {predicted.item()}")