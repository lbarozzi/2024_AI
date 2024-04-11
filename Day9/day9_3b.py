import os
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# Set device (GPU if available, else CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Number of flower types
NUM_CLASSES = 6

# Image size
IMG_SIZE = 224

# Batch size
BATCH_SIZE = 32

# Number of epochs
EPOCHS = 10

# Learning rate
LR = 0.001

def load_dataset(data_dir):
    transform = transforms.Compose([
        transforms.Resize((IMG_SIZE, IMG_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    dataset = torchvision.datasets.ImageFolder(data_dir, transform=transform)
    return dataset

def load_model():
    #model = torchvision.models.resnet50(pretrained=True)
    model = torchvision.models.resnet50(weights=torchvision.models.ResNet50_Weights.DEFAULT);
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
    #model=FlowerCNN()
    return model


class FlowerCNN(nn.Module):
    def __init__(self):
        super(FlowerCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * (IMG_SIZE // 2) * (IMG_SIZE // 2), 128)
        self.fc2 = nn.Linear(128, NUM_CLASSES)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 64 * (IMG_SIZE // 2) * (IMG_SIZE // 2))
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def train(model, train_loader, optimizer, criterion, writer):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            writer.add_scalar("Training Loss", loss.item(), batch_idx * len(data))
            print(f"Training Loss { loss.item(), batch_idx * len(data) }")


def evaluate(model, test_loader, criterion, writer):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = criterion(output, target)
            test_loss += loss.item()
            _, predicted = torch.max(output.data, 1)
            correct += (predicted == target).sum().item()
    test_loss /= len(test_loader.dataset)
    writer.add_scalar("Test Loss", test_loss) #, writer.iter)
    writer.add_scalar("Accuracy", 100. * correct / len(test_loader.dataset) ) # , writer.iter)
    print(f"Test Loss: {test_loss}")
    print(f"Accuracy { 100. * correct / len(test_loader.dataset) } ") # , writer.iter)


def save_model(model, save_dir):
    torch.save(model.state_dict(), os.path.join(save_dir, "flower_cnn.pth"))


# Load dataset
data_dir = "flowers"
dataset = load_dataset(data_dir)

# Create data loaders
train_loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
test_loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=2)

# Load model
model = load_model()
model.to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# Create TensorBoard writer
writer = SummaryWriter()

print("Train")
#Train
for epoch in range(EPOCHS):
    train(model, train_loader, optimizer, criterion, writer)
    evaluate(model, test_loader, criterion, writer)
    if (epoch + 1) % 5 == 0:
        save_model(model, "model")

print("Test")
evaluate(model,test_loader,criterion,writer)


print("Done...")