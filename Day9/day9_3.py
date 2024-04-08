import numpy as np
import pandas as pd
import os
import torch
import torch.nn as nn
import torch.nn.functional as F 
import torch.utils
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available")
else:
    device = torch.device("cpu")
    print("GPU is not available")

print(f"Device: {device}")

# Read DataSet
transform = transforms.Compose([ transforms.Resize(128), 
                                transforms.RandomCrop(128),
                                transforms.ToTensor()
                                ])

dataset = torchvision.datasets.ImageFolder("flowers",transform=transform)

dataloader= torch.utils.data.DataLoader(dataset,batch_size=1, shuffle=False) # TODO: set a True

class CNNFlower(nn.Module):
    def __init__(self):
        super(CNNFlower,self).__init__()

        self.Conv1 = nn.Conv2d(3,64,kernel_size=3,stride=1,padding=1)
        self.Conv2 = nn.Conv2d(64,64,kernel_size=3,stride=1,padding=1)
        self.pool = nn.MaxPool2d(2) # half 
        # Let's do some test
        self.Conv3 = nn.Conv2d(64,128,kernel_size=3,stride=1,padding=1)
        self.Conv4 = nn.Conv2d(128,128,kernel_size=3,stride=1,padding=1)
        # self.pool = nn.MaxPool2d(2) # half 

        self.Conv5 = nn.Conv2d(128,256,kernel_size=3,stride=1,padding=1)
        self.Conv6 = nn.Conv2d(256,256,kernel_size=3,stride=1,padding=1)
        # self.pool = nn.MaxPool2d(2) # half 
        # self.pool = nn.MaxPool2d(2) # half 
        

        self.Conv7 = nn.Conv2d(256,512,kernel_size=3,stride=1,padding=1)
        self.Conv8 = nn.Conv2d(512,512,kernel_size=3,stride=1,padding=1)

        # uhm... may need some additional layer

        # linear layers
        self.lin_size= 131072
        self.f_lin1 = nn.Linear(self.lin_size,4096)
        self.f_lin2 = nn.Linear(4096,4096)
        self.f_lin3 = nn.Linear(4096,1024)
        self.f_lin4 = nn.Linear(1024,100)
        self.out = nn.Linear(100,6)

    def forward(self,x):
        x= F.relu(self.Conv1(x))
        x= F.relu(self.Conv2(x))
        x= self.pool(x)
        x= F.relu(self.Conv3(x))
        x= F.relu(self.Conv4(x))
        x= self.pool(x)
        x= F.relu(self.Conv5(x))
        x= F.relu(self.Conv6(x))
        x= self.pool(x)
        x= F.relu(self.Conv7(x))
        x= F.relu(self.Conv8(x))

        #
        x= x.view(-1,self.lin_size) #GetError on size
        x = F.relu(self.f_lin1(x))
        x = F.relu(self.f_lin2(x))
        x = F.relu(self.f_lin3(x))
        x = F.relu(self.f_lin4(x))
        x = F.relu(self.out(x))

        return x
    
Net=CNNFlower().to(device)

criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.SGD(Net.parameters(),lr=0.001, momentum=0.9)

model_dir_path="model/"
if not os.path.exists(model_dir_path):
    os.makedirs(model_dir_path)

modelname=f"{model_dir_path}flower_model.pth"

if os.path.exists(modelname):
    Net.load_state_dict(torch.load(modelname))
    print(f"Model loaded from file: {modelname}")
else:
    for epoch in range(10):
        losses=0.0
        for i,data in enumerate(dataloader,0):
            inputs, labels = data[0], data[1]

            optimizer.zero_grad()
            outputs = Net(inputs)

            loss= criterion(outputs,labels)
            optimizer.step()

            losses += loss.item()

            if i%100==99:
                print(f"Epoch {epoch}: loss: {losses/100}")
    
    torch.save(Net.state_dict(),modelname)


#OK: test 

