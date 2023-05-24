import torch

print(torch.__version__)  # 查看torch当前版本号

print(torch.version.cuda)  # 编译当前版本的torch使用的cuda版本号

print(torch.cuda.is_available())  # 查看当前cuda是否可用于当前版本的Torch，如果输出True，则表示可用

print(torch.cuda.device_count())   #返回gpu数量；

print(torch.cuda.get_device_name())   #返回gpu名字，设备索引默认从0开始；

print(torch.cuda.current_device())    #返回当前设备索引；