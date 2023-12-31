import torch
import torch.nn as nn

def forward(x,w1,w2):
    net1=nn.Linear(2,2)
    net1.weight.data=w1
    net1.bias.data=torch.Tensor([0])
    h=net1(x)
    #print(h)
    h=torch.sigmoid(h)
    
    net2=nn.Linear(2,2)
    net2.weight.data=w2
    net2.bias.data=torch.Tensor([0])
    o=net2.forward(x)
    o=torch.sigmoid(o)
    return o

if __name__=='__main__':
    x = torch.tensor([0.5, 0.3])
    w1 = torch.tensor([[0.2, 0.5], [-0.4, 0.6]])
    w2 = torch.tensor([[0.1, -0.3], [-0.5, 0.8]])
    output = forward(x,w1,w2)
    print('最终的输出值是：',output)
