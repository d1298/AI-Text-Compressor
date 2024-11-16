# import dependencies
# numpy for dealing with matrices
import cupy as np

#pandas for retrieving the data
import pandas as pd

# matplotlib for displaying the data
from matplotlib import pyplot as plt

#open the training data
data = pd.read_csv("train.csv")
# convert the data to a numpy array
data = np.array(data)

# get the number of number of images (rows) m, and the number of pixels per image (columns) n
m, n = data.shape

#shuffle the data
np.random.shuffle(data)

#set values for the testing data (dev) which won't be used to train the model only to test it, this avoids generalisation of the model
# .T at the end transposes the data so the data for an image is now in a column instead of a row
data_dev = data[0:1000].T
# gets the labels for the dev data
Y_dev = data_dev[0]
# gets the actual data for the dev data 
X_dev = data_dev[1:n]  

X_dev = X_dev / 255.0

#set values for the training data which is the set of data that is used to train the model
data_train = data[1000:m].T
# gets the labels for the dev data
Y_train = data_train[0]
# gets the actual data for the dev data 
X_train = data_train[1:n]
X_train = X_train / 255.0

# def init_params():
#     W1 = np.load("W1.npy")
#     b1 = np.load("b1.npy")
#     W2 = np.load("W2.npy")
#     b2 = np.load("b2.npy")
#     return W1, b1, W2, b2

def init_params():
    #set random values for the weights and biuses to go into the hidden layer
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5

    #set random values for the weights and biuses to go into the output layer
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5

    return W1, b1, W2, b2

#create a function to apply the ReLU activation function which sets the value to 0 if it is less than 0 and x if it is greater than 0
def ReLU(Z):
    return np.maximum(0, Z)

# function to return the derivative of the ReLU function at x = Z
def deriv_ReLU(Z):
    return Z > 0

#The softmax function is used to convert the output of the model into a value between 0 and 1 which can be used to determine the probability of the output being the correct result.
def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A

def forward_prop(W1, b1, W2, b2, X):
    #multiply the input data by the weights and add the biases
    Z1 = W1.dot(X) + b1

    #apply the ReLU activation function to Z1 (hidden layer)
    A1 = ReLU(Z1)

    #multiply the input data by the weights and add the biases
    Z2 = W2.dot(A1) + b2

    #apply the softmax function to the output layer
    A2 = softmax(Z2)

    return Z1, A1, Z2, A2


# need more understanding



# creates an array where all values are 0 except for the one at index y
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    # set the value of the one-hot vector at the index of the correct output to 1
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def back_prop(Z1, A1, Z2, A2, W2, X, Y):
    m = Y.size
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = (1 / m) * dZ2.dot(A1.T) 
    db2 = (1 / m) * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * deriv_ReLU(Z1)
    dW1 = (1 / m) * dZ1.dot(X.T)
    db1 = (1 / m) * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2

    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, iterations, alpha):
    W1, b1, W2, b2 = init_params()
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = back_prop(Z1, A1, Z2, A2, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 50 == 0:
            print("Iteration: ", i)
            print("Accuracy: ", (get_accuracy(get_predictions(A2), Y)) * 100)
    return W1, b1, W2, b2

W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 100, 0.1)

np.save("W1.npy", W1)
np.save("b1.npy", b1)
np.save("W2.npy", W2)
np.save("b2.npy", b2)


def make_predictions(X, W1, b1, W2, b2):
    _,_,_, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def test_prediction(index,W1,b1,W2,b2):
    current_image = X_train[:,index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)

    current_image = current_image.reshape((28, 28)) *255
    plt.gray()
    plt.imshow(current_image, interpolation="nearest")
    plt.show()

# while True:
#     index = int(input("Enter the index of the image you want to test: "))
#     test_prediction(index, W1, b1, W2, b2)