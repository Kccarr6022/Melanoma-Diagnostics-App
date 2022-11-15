###############################################
# TASK
# --------------------
#
# 1. import JPG file into python
# 2. pass the JPG into function testimage as an argument(final line)
# 3. Add model from kaggle to testimage function so that it returns a prediction
# 4. If model is working it shall return a number that is greater than 0

############################################################################################################
# Code is basically the same process as the test_model function in kaggle. Any errors that arise will probably be from saving the 
# model or working with one image, should be  relatively easy to resolve
#  https://pytorch.org/tutorials/beginner/saving_loading_models.html ----> this site explains how to save and load a model
# model must be defined, it is defined in this file

import base64
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torchvision
from torchvision import models, transforms
from torchvision.datasets import ImageFolder
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # code is necessary for calculating masks and labels

############
# Model
############

class ResNetBlock(nn.Module):
    def __init__(self, layers, dimension_increase=False):
        super(ResNetBlock, self).__init__()
        self.dimension_increase = dimension_increase
        self.layers = layers
        if self.dimension_increase:
            self.downsample = nn.Sequential(
                OrderedDict([
                    ("conv1", nn.Conv2d(layers[0], layers[1], kernel_size=(1, 1), stride=(2, 2))),
                    ("batchnorm", nn.BatchNorm2d(layers[1]))
                ])
            )

            self.block = nn.Sequential(
                OrderedDict([
                    ("convx_1",
                     nn.Conv2d(layers[0], layers[1], kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)),
                    ("batch_norm", nn.BatchNorm2d(layers[1])),
                    ("relu", nn.ReLU(inplace=True)),
                    ("convx_2",
                     nn.Conv2d(layers[1], layers[2], kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)),
                    ("batch_norm", nn.BatchNorm2d(layers[2]))
                ])
            )
        else:
            self.block = nn.Sequential(
                OrderedDict([
                    ("convx_1",
                     nn.Conv2d(layers[0], layers[1], kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)),
                    ("batch_norm", nn.BatchNorm2d(layers[1])),
                    ("relu", nn.ReLU(inplace=True)),
                    ("convx_2",
                     nn.Conv2d(layers[1], layers[2], kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)),
                    ("batch_norm", nn.BatchNorm2d(layers[2]))
                ])
            )

    def forward(self, x):
        identity = x
        if self.dimension_increase:
            identity = self.downsample(identity)

        x = self.block(x)
        return F.relu(identity + x)


class ResNet18(nn.Module):
    def __init__(self):
        super(ResNet18, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True)
        )

        self.conv2 = nn.Sequential(
            nn.MaxPool2d(kernel_size=(3, 3), stride=2, padding=1),
            ResNetBlock(layers=[64, 64, 64], dimension_increase=False),
            ResNetBlock(layers=[64, 64, 64], dimension_increase=False)
        )

        self.conv3 = nn.Sequential(
            ResNetBlock(layers=[64, 128, 128], dimension_increase=True),
            ResNetBlock(layers=[128, 128, 128], dimension_increase=False)
        )

        self.conv4 = nn.Sequential(
            ResNetBlock(layers=[128, 256, 256], dimension_increase=True),
            ResNetBlock(layers=[256, 256, 256], dimension_increase=False)
        )

        self.conv5 = nn.Sequential(
            ResNetBlock(layers=[256, 512, 512], dimension_increase=True),
            ResNetBlock(layers=[512, 512, 512], dimension_increase=False)
        )

        self.fc = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(512, 3)
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.fc(x)

        return x


model = ResNet18()
LEARNING_RATE = 0.001
EPOCHS = 100
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=0.001)
criterion = nn.CrossEntropyLoss()
file = torch.load("../input/pytorch-model-file/Melanoma - Prediction ResNet 18 from Scratch/melanoma_model.pt")
# min_loss = np.inf
min_loss = file["min_loss"]
model.load_state_dict(file['model'])

model.to(device)

###########
# Function
###########

image = ""
imgdata = base64.b64decode(image)


def testimage(imgdata) -> float:  # argument is the image: base64image (str, optional): JPG image of mole
    total_correct = 0
    test_result: float = 0

    # Add model from kaggle to testimage function so that it returns a prediction
    # loading model
    file = torch.load("path\model.pt")  # file = torch.load("/kaggle/working/melanoma_model.pt") 
    model.load_state_dict(file['model'])  # model.load_state_dict(torch.load(PATH))
    model.eval()

    # Calculations, eq is needed for calculating total_correctness (line 166)
    with torch.no_grad():
        for images, labels in imgdata:
            images, labels = images.to(device), labels.to(device)
            ps = model(imgdata)  # applying model to image

            ps = nn.Softmax(dim=1)(ps)

            top_p, top_class = ps.topk(1, dim=1)
            eq = top_class == labels.view(-1, 1)
            total_correct += eq.sum().item()

    # If model is working it shall return a number that is greater than 0
    total_correct += eq.sum().item()
    test_result = ((total_correct / len(imgdata)) * 100) # calculating percentage

    return float(test_result)

# test function
print(f" This image has a {testimage(image)}% chance of being melanoma")