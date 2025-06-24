import pandas as pd
import torch
from torch.utils.data import DataLoader, TensorDataset
from brain import MicroBrain

df = pd.read_csv("data/local_decisions.csv")
X = torch.tensor(df.iloc[:, :4].values, dtype=torch.float32)
Y = torch.tensor(df.iloc[:, 4:].values, dtype=torch.float32)

dataset = TensorDataset(X, Y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)
model = MicroBrain()
optim = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(20):
    for xb, yb in loader:
        preds = model(xb)
        loss = loss_fn(preds, yb.argmax(dim=1))
        loss.backward()
        optim.step()
        optim.zero_grad()
    print(f"Epoch {epoch}, loss = {loss.item():.4f}")

torch.save(model.state_dict(), "weights/brain.pth")
