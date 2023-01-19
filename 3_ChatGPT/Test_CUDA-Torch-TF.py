import torch
import tensorflow as tf

print("TF Version: " + str(tf.__version__))
print("CUDA Available: " + str(torch.cuda.is_available()))