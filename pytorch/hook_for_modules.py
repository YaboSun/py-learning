#!/usr/bin/env python
# encoding: utf-8
# @Author: sunyabo
# @Date: 2020/11/11 上午10:28
import torch
from torch import nn

"""
神经网络module一般被封装在神经网络中间，通常只能获得网络整体的输入和输出
对于夹在网络中间的模块，很难得知输入输出的梯度，甚至连输入输出的数值都无法获得
除非在设计网络时，在forward函数的返回值中包含中间module的输出

为了解决这个麻烦，PyTorch设计了两种hook：register_forward_hook和
register_backward_hook，分别用来获取正/反向传播时，中间层模块输入和输出的
feature和gradient，从而降低获取模型内部信息流的难度
"""


class Model(nn.Module):
    """
    定义一个模型
    """

    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(3, 4)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(4, 1)
        self.initialize()

    def initialize(self):
        """
        为方便验证，指定特殊的weight和bias
        :return:
        """
        with torch.no_grad():
            self.fc1.weight = torch.nn.Parameter(torch.tensor([[1., 2., 3.],
                                                               [-4., -5., -6.],
                                                               [7., 8., 9.],
                                                               [-10., -11., -12.]]))
            self.fc1.bias = torch.nn.Parameter(torch.tensor([1.0, 2.0, 3.0, 4.0]))
            self.fc2.weight = torch.nn.Parameter(torch.tensor([[1.0, 2.0, 3.0, 4.0]]))
            self.fc2.bias = torch.nn.Parameter(torch.tensor([1.0]))

    def forward(self, x):
        o = self.fc1(x)
        o = self.relu1(o)
        o = self.fc2(o)
        return o


# 全局变量，用于存储中间层的feature
total_feature_out = []
total_feature_in = []


# 定义forward hook function
def hook_fn_forward(module, input, output):
    # 用于区分模块
    print(module)
    print('input', input)
    print('output', output)
    total_feature_out.append(output)
    total_feature_in.append(input)


total_grad_out = []
total_grad_in = []


# 定义backward hook function
def hook_fn_backward(module, grad_input, grad_output):
    # 为了区分模块
    print(module)
    # 为了符合反向传播顺序，先打印grad_output
    print('grad_output', grad_output)
    print('grad_input', grad_input)
    total_grad_in.append(grad_input)
    total_grad_out.append(grad_output)


model = Model()
modules = model.named_children()
for name, module in modules:
    module.register_forward_hook(hook_fn_forward)
    module.register_backward_hook(hook_fn_backward)

x = torch.Tensor([[1.0, 1.0, 1.0]]).requires_grad_()
o = model(x)
o.backward()

print("================saved inputs and outputs===========================")
for idx in range(len(total_feature_in)):
    print('input:', total_feature_in[idx])
    print('output:', total_feature_out[idx])
