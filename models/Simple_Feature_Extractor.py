import torch
import torch.nn as nn

class SimpleFeatureExtractor(nn.Module):
    def __init__(self, ft_in, ft_hidden):
        super(SimpleFeatureExtractor, self).__init__()
        self.fc = nn.Linear(ft_in, ft_hidden)
        self.act = nn.PReLU()
        for m in self.modules():
            self.weights_init(m)

    def weights_init(self, m):
        if isinstance(m, nn.Linear):
            torch.nn.init.xavier_uniform_(m.weight.data)
            if m.bias is not None:
                m.bias.data.fill_(0.0)

    def forward(self, seq):
        ret = self.fc(seq)
        return self.act(ret)