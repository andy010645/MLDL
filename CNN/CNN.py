import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.losses import categorical_crossentropy
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
from keras.datasets import mnist

def load_data():
    (x_train,y_train),(x_test,y_test) = mnist.load_data()
    number=10000
    x_train=x_train[0:number]
    y_train=y_train[0:number]
    x_train=x_train.reshape(number,28*28)
    x_test=x_test.reshape(x_test.shape[0],28*28)
    x_train=x_train.astype('float32')
    x_test=x_test.astype('float32')

    y_train=np_utils.to_categorical(y_train,10)
    y_test=np_utils.to_categorical(y_test,10)

    x_train=x_train/255
    x_test=x_test/255

    return (x_train,y_train),(x_test,y_test)

(x_train,y_train),(x_test,y_test)=load_data()

model = Sequential()
model.add(Conv2D(25,(3,3),input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(50,(3,3)))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())

model.add(Dense(input_dim=1250*1,units=100,activation='relu'))
model.add(Dense(units=10,activation='softmax'))

model.compile(loss=categorical_crossentropy,optimizer='Adam',metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=100,epochs=30)
result=model.evaluate(x_test,y_test)
test=model.evaluate(x_train,y_train)
print("\nTrain Loss",test[0],"\nTrain ACC",test[1])
print("\nLoss:",result[0],"\nTest ACC",result[1])