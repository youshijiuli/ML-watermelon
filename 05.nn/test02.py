import numpy as np


def sigmoid(x):
    # S1gnold actiwatlon funct1on: f(x)  1 / (1 + e“(-X]]
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # s1gmo1d面数的导数: f'(x) = f(X]  [1 . f[X])
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    # Y_true and y-pred are numpy arrays of the same length
    return ((y_true - y_pred) ** 2).mean()


class QurNeuralNetwork:
    # A neural netnork with;
    # - 2 inputs
    # - a hidden loyer with 2 neurons (hl, h2)
    # - an output layer with i neuron (o1]
    # 由大小 DISCLAIMER 大公山
    # The code below is intend to be simple and educationol, NoT optinal.
    # Real neural net code looks nothing like this. Do NoT use this code.
    # Instead, reod/run it to understand how this specific network works.

    # 设置权重和偏执

    def __init__(self) -> None:
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

        self.lr = 1e-2
        self.epoch = 1000

    def forward(self, x: np.array):
        self.h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        self.h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        self.o1 = sigmoid(self.w5 * self.h1 + self.w6 * self.h2 + self.b3)
        return self.o1

    def train(self, data, all_true_features):
        # 开始训练
        epochs = 1000
        for epoch in range(epochs):
            for x, y_true in zip(data, all_true_features):
                # 前向传播
                h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                sum_h1 = sigmoid(h1)
                h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                sum_h2 = sigmoid(h2)
                o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                sum_o1 = sigmoid(o1)
                y_pred = o1

                d_L_d_pred = -2 * (y_true - y_pred)

                # 反向传播
                # o1
                d_y_pred_d_w5 = deriv_sigmoid(sum_o1) * h1
                d_y_pred_d_w6 = deriv_sigmoid(sum_o1) * h2
                d_y_pred_d_b3 = deriv_sigmoid(sum_o1)

                d_y_pred_d_h1 = deriv_sigmoid(sum_o1) * self.w5
                d_y_pred_d_h2 = deriv_sigmoid(sum_o1) * self.w6

                # h1
                d_h1_d_w1 = deriv_sigmoid(sum_h1) * x[0]
                d_h1_d_w2 = deriv_sigmoid(sum_h1) * x[1]
                d_h1_d_b1 = deriv_sigmoid(sum_h1)

                # h2
                d_h1_d_w3 = deriv_sigmoid(sum_h2) * x[0]
                d_h1_d_w4 = deriv_sigmoid(sum_h2) * x[1]
                d_h1_d_b2 = deriv_sigmoid(sum_h2)

                # 权重更新
                self.w5 -= self.lr * d_y_pred_d_w5 * d_L_d_pred
                self.w6 -= self.lr * d_y_pred_d_w6 * d_L_d_pred
                self.b3 -= self.lr * d_y_pred_d_b3 * d_L_d_pred

                self.w1 -= self.lr * d_L_d_pred * d_y_pred_d_h1 * d_h1_d_w1
                self.w2 -= self.lr * d_L_d_pred * d_y_pred_d_h1 * d_h1_d_w2
                self.b1 -= self.lr * d_L_d_pred * d_y_pred_d_h1 * d_h1_d_b1

                self.w3 -= self.lr * d_L_d_pred * d_y_pred_d_h2 * d_h1_d_w3
                self.w4 -= self.lr * d_L_d_pred * d_y_pred_d_h2 * d_h1_d_w4
                self.b2 -= self.lr * d_L_d_pred * d_y_pred_d_h2 * d_h1_d_b2

            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.forward, 1, data)
                loss = mse_loss(all_true_features, y_preds)
                print(f"第{epoch}轮次,loss:{loss}")


data = np.array(
    [[-8, -0.5], [19, 6.5],[11,4.5], [-21, -5.5]]  # Alice  # Bob[11,4.5], # Charlie
)  # diana
# 训练样本标签
all_y_trues = np.array([1, 0, 0, 1])  # ALice  # Bob  # Charlie  # diana
# 训练我们的神经网络
network = QurNeuralNetwork()
# 初始化我们的权重和偏置
network.train(data, all_y_trues)

# 进行预测
emily = np.array([-13, -2.5])  # 128 pounds,63 inches
frank = np.array([14, 2.5])  # 155 pounds, 68 inches
print("Emily: %.3f" % network.forward(emily))  # 0.961 -F
print("Frank: %.3f" % network.forward(frank))  # .056 - M


# loss下降的部署很明显

# 第0轮次,loss:0.4429933504085486

# 第990轮次,loss:0.2641334183722174


# 但是它的那个下降到了0.0023  ?