from trainCNN_multiclassClassifier import *
#from data_multiclassClassifier import *
import numpy as np
import os
import scipy.misc

def load_test_data(self,location):
    npy_path = "npydata"
    print('-'*30)
    print('loading test images...')
    print('-'*30)
    imgs_test_merged = np.load(self.npy_path+"/"+location+"/imgs_test.npy")
    imgs_test = imgs_test_merged[:, :, :, :2]  # first 2 channels, final shape subimg_count x h x w x 2
    labels_test = imgs_test_merged[:, :, :, 2:]  # last 3 channels, final shape subimg_count x h x w x 3
    print('test images loaded.')
    print('-' * 30)
    return imgs_test, labels_test

mydata = dataProcess(128,128)

print("loading data")
imgs_test, labels_test = mydata.load_test_data()
print("loading data done")

mycnn = myCNN(128,128)
model = mycnn.get_CNN()
print("got CNN")

model.load_weights('CNNweights.hdf5')
print("loaded model weights")

imgs_mask_test = model.predict(imgs_test, batch_size=1, verbose=1)
loss, acc = model.evaluate(imgs_test, labels_test, batch_size=1, verbose=1)
print('loss on test data is ', loss)
print('acc on test data is ', acc)
print("saving test masks")
np.save('npydata/imgs_mask_test.npy', imgs_mask_test)

print("array to image")
imgs_true = labels_test
print('loading done, now saving')

import imageio

for i in range(imgs_true.shape[0]):
    img = imgs_test[i,:,:,0]*255
    img_pred = imgs_mask_test[i,:,:,:]*255
    img_true = imgs_true[i,:,:,:]*255
    if not os.path.lexists('results'):
        os.mkdir('results')
    imageio.imwrite("results/{}_img.png".format(i), img)
    imageio.imwrite("results/{}_pred.png".format(i), img_pred)
    imageio.imwrite("results/{}_true.png".format(i), img_true)

os.system('python image2csv.py')
os.system('python csv2json.py location')