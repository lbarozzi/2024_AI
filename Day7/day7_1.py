import torch
import torch.utils
import torchvision
import torchvision.transforms as transforms

''' Workaround SSL problems
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# ''' 
# Step 1 
transform= transforms.Compose([transforms.ToTensor(),
                               transforms.Normalize( (0.5, 0.5, 0.5), (0.5, 0.5,0.5) )])

trainset=torchvision.datasets.CIFAR10(root="./data/", train=True,
                                       download= True, transform=transform )

testset=torchvision.datasets.CIFAR10(root="./data/", train=False,
                                      download= True,  transform=transform)

trainloader= torch.utils.data.DataLoader( trainset, batch_size=4, shuffle=False)
testloader= torch.utils.data.DataLoader( testset, batch_size=4, shuffle=False)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# Step 2
import matplotlib.pyplot as plt 
import numpy as np

def convert_to_imshow_format(image):
    # CHW => HWC
    image= image/2+0.5   # from [-1:1] to [0:1]
    image= image.numpy()
    return image.transpose(1,2,0)

dataiter = iter(trainloader)
images, labels = next(dataiter)

fig,ax = plt.subplots(1, len(images),figsize=(12,2.5) )

for idx, image in enumerate(images):
    ax[idx].imshow(convert_to_imshow_format(image))
    ax[idx].set_title(classes[labels[idx]])
    ax[idx].set_xticks([])
    ax[idx].set_yticks([])

plt.show()

# Step 3
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        # img 3x32x32
        self.s_conv1 = nn.Conv2d(3, 6, 5)   #456 hyparams    
        # 6x28x28 (32-5)+1
        self.pool = nn.MaxPool2d(2, 2) # split 6x14x14
        #(5x5x6 )+1 x 16 (14-5)+1
        self.s_conv2 = nn.Conv2d(6, 16, 5)  #2416 hyperparams
        self.f_layer1 = nn.Linear(16*5*5,120)
        self.f_layer2 = nn.Linear(120,84)
        self.out= nn.Linear(84,10)  # CIFAR10
        # TOT 62K hyperparams 
   
    def forward(self,x):
        x= self.s_conv1(x)
        x= F.relu(x)
        x= self.pool(x)
        # second net
        x= self.pool(F.relu(self.s_conv2(x)))
        #
        x= x.view(-1,16*5*5)
        #
        x=F.relu(self.f_layer1(x))
        x=F.relu(self.f_layer2(x))
        x= self.out(x)
        return x

net=Net()

import torch.optim as optim
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD( net.parameters(), lr=0.001, momentum=0.9)

# Train
import os
epochs = 2 #

model_dir_path="model/"
model_path= f"{model_dir_path}cifar-10-cnn-model.pt"

if not os.path.exists(model_dir_path):
    os.mkdir(model_dir_path)

if os.path.isfile(model_path):
    net.load_state_dict(torch.load(model_path))
else:
    # Let's do it 
    for epoch in range(epochs):
        r_loss= 0.0
        for i, data in enumerate(trainloader,0):
            inputs, labels = data
            
            optimizer.zero_grad()

            outputs = net(inputs)
            loss= criterion(outputs,labels)
            loss.backward()
            optimizer.step()

            r_loss += loss.item()

            if i%2000==1999:
                print(f"{epoch}:{i} => {r_loss}/2000")
                r_loss=0.0
    print("done...")
    torch.save(net.state_dict(),model_path)
    print(f"model saved to: {model_path}")

# Step 4 
dataiter = iter(testloader)
images, labels = next(dataiter)

fix, ax = plt.subplots(1,len(images), figsize=(12,2.5)) 

for idx, image in enumerate(images):
    ax[idx].imshow(convert_to_imshow_format(image))
    ax[idx].set_title(classes[labels[idx]])
    ax[idx].set_xticks([])
    ax[idx].set_yticks([])


outputs = net(images)
sm=nn.Softmax(dim=1)
sm_outputs = sm(outputs)

prob, idx = torch.max(sm_outputs,dim=1)
for p,i in zip(prob,idx):
    print(f"{classes[i]}: {p}")



plt.show()

