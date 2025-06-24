import torch
import torch.nn as nn

class MicroBrain(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 3),  # [shoot_prob, pass_prob, dribble_prob]
            nn.Softmax(dim=0)
        )

    def forward(self, x):
        return self.net(x)

def load_model(path=None):
    model = MicroBrain()
    if path:
        model.load_state_dict(torch.load(path))
    model.eval()
    return model
