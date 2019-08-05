import numpy as np
import matplotlib.pyplot as plt


# 激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))


# 激活函数的导数
def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx*(1-fx)


# 损失函数
def loss(y_true, y_pred):
    return((y_pred-y_true)**2).mean()


# 神经网络搭建，一个隐藏层（两个神经元），一个输出，两个输入
class NeuralNetwork:
    def __init__(self):
        # 隐藏层神经元个数
        self.lay = 2
        # 权重和偏置
        self.w = np.empty((self.lay, 2), dtype=np.float)
        self.b = np.empty(self.lay+1, dtype=np.float)
        self.ow=np.empty(self.lay,dtype=np.float)
        #  随机自然数作为初始权重和偏置
        for i in range(self.w.shape[0]):
            for j in range(self.w.shape[1]):
                self.w[i][j] = np.random.normal()
        for i in range(self.b.size):
            self.b[i]=np.random.normal()
        for i in range(self.ow.size):
            self.ow[i]=np.random.normal()

    #前向传播
    def feedforward(self,x):
        h = np.empty(self.lay, dtype=np.float)
        for i in range(h.shape[0]):
            h[i]=sigmoid(self.w[i][0]*x[0]+self.w[i][1]*x[1]+self.b[i])
        o1=sigmoid(np.dot(h,self.ow)+self.b[self.lay])
        return o1


    x=[]
    y=[]
    # 开始训练
    def train(self,data,all_y_true):
        learn_rate=0.1 # 学习率
        epoch=-1  #训练的次数
        y_preds = np.apply_along_axis(self.feedforward, 1, data)
        mse_loss = loss(all_y_true, y_preds)
        while(mse_loss>0.001):
            epoch+=1
            for(x,y_true) in zip(data,all_y_true):
                sum_h = np.empty(self.lay, dtype=np.float)
                h = np.empty(self.lay, dtype=np.float)
                for i in range(h.shape[0]):
                    sum_h[i] = self.w[i][0] * x[0] + self.w[i][1] * x[1] + self.b[i]
                    h[i]=sigmoid(sum_h[i])
                sum_o1=np.dot(self.ow,h)
                o1=sigmoid(sum_o1+self.b[self.lay])
                y_pred=o1

                #损失函数对y偏导
                d_l_d_ypred=-2*(y_true-y_pred)
                #激活函数对输出元权重的偏导数
                d_ypred_d_ow=np.empty(self.ow.size,dtype=np.float)
                for i in range(self.ow.size):
                    d_ypred_d_ow[i]=h[i]*deriv_sigmoid(sum_o1)

                #激活函数对输出元偏置的偏导数
                d_ypred_d_ob=deriv_sigmoid(sum_o1)
                #激活函数对隐藏层返回值的偏导数
                d_ypred_d_h=np.empty(h.size,dtype=np.float)
                for i in range(h.size):
                    d_ypred_d_h[i]=self.ow[i]*deriv_sigmoid(sum_o1)
                #隐藏层返回值对权重的偏导数
                d_h_d_w=np.empty((self.w.shape[0],self.w.shape[1]),dtype=np.float)
                for i in range(self.w.shape[0]):
                    for j in range(self.w.shape[1]):
                        d_h_d_w[i][j]=x[j]*deriv_sigmoid(sum_h[i])
                #隐藏层返回值对偏置的偏导数
                d_h_d_b=np.empty(h.size,dtype=float)
                for i in range(h.size):
                    d_h_d_b[i]=deriv_sigmoid(sum_h[i])

                #更新权重及偏置
                for i in range(self.w.shape[0]):
                    for j in range(self.w.shape[1]):
                        self.w[i][j]-=learn_rate*d_l_d_ypred*d_ypred_d_h[i]*d_h_d_w[i][j]
                for i in range(self.ow.size):
                    self.ow[i]-=learn_rate*d_l_d_ypred*d_ypred_d_ow[i]
                for i in range(self.lay):
                    self.b[i]-=learn_rate*d_l_d_ypred*d_ypred_d_h[i]*d_h_d_b[i]
                self.b[self.lay]-=learn_rate*d_l_d_ypred*d_ypred_d_ob
            if epoch%10==0:
                y_preds=np.apply_along_axis(self.feedforward,1,data)
                mse_loss=loss(all_y_true,y_preds)
                print("Epoch %d loss: %.6f" % (epoch, mse_loss))

            NeuralNetwork.x.append(epoch)
            NeuralNetwork.y.append(mse_loss)
        print(y_preds)
        plt.plot(NeuralNetwork.x,NeuralNetwork.y)
        plt.show()

# Define dataset
data = np.array([
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])
all_y_trues = np.array([
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])
# Train our neural network!
network = NeuralNetwork()
network.train(data, all_y_trues)
