import numpy as np
from scipy import signal
from LoadMnistData import *
from Softmax import *
from ReLU import *
from Conv import *
from Pool import *
from MnistConv import *


# Learn
#
Images, Labels = LoadMnistData('MNIST\\t10k-images-idx3-ubyte.gz', 'MNIST\\t10k-labels-idx1-ubyte.gz')
image_x = Images.shape[1]
image_y = Images.shape[2]
num_of_label = 10

Images = np.divide(Images, 255)

W1 = 1e-2 * np.random.randn(9, 9, 20)
W5 = np.random.uniform(-1, 1, (100, int((image_x-9+1)/2)*int((image_y-9+1)/2)*20)) * np.sqrt(6) / np.sqrt(360 + int((image_x-9+1)/2)*int((image_y/-9+1)/2)*20)
Wo = np.random.uniform(-1, 1, ( num_of_label,  100)) * np.sqrt(6) / np.sqrt( num_of_label +  100)

X = Images[0:8000, :, :]
D = Labels[0:8000]
    
for _epoch in range(3):
    print(_epoch)
    W1, W5, Wo = MnistConv(W1, W5, Wo, X, D, num_of_label)

    
# Test
#
X = Images[8000:10000, :, :]
D = Labels[8000:10000]

acc = 0
N   = len(D)
for k  in range(N):
    x  = X[k, :, :]

    y1 = Conv(x, W1)
    y2 = ReLU(y1)
    y3 = Pool(y2)
    y4 = np.reshape(y3, (-1, 1))
    v5 = np.matmul(W5, y4)
    y5 = ReLU(v5)
    v  = np.matmul(Wo, y5)
    y  = Softmax(v)
    
    i = np.argmax(y)
    if i == D[k][0]:
        acc = acc + 1
        
acc = acc / N
print("Accuracy is : ", acc)


