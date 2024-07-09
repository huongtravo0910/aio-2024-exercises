import torch
import torch.nn as nn


class CustomedSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp/x_exp.sum(0, True)


class CustomedSoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        ele_max = torch.max(x, 0, True)
        x_exp = torch.exp(x-ele_max)
        return x_exp/x_exp.sum(0, True)


data = torch.Tensor([1, 2, 3])
softmax = CustomedSoftmax()
output = softmax(data)

print(f'sofmax result : ${output}')

data2 = torch.Tensor([1, 2, 3])
softmax2 = CustomedSoftmaxStable()
output2 = softmax2(data2)

print(f'sofmax stable result : ${output2}')
