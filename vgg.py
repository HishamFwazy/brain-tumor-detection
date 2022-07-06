import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os

#import firebase_admin
#import sseclient
#from tensorflow.keras.engine.saving import load_model
from keras.models import Model, load_model


print(os.listdir(r"D:\2NAAAAAA\new dataset"))


os.listdir("../")


# import shutil
# from tqdm import tqdm
#
#
# for i in tqdm(os.listdir(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set")):
# #     print(i)
#     if i.split(".")[0] == "no":
#         shutil.copy2(os.path.join(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set",i),os.path.join(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set\no",i))
#     elif i.split(".")[0] == "yes":
#         shutil.copy2(os.path.join(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set",i),os.path.join(r"D:\2NAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set\yes",i))
#


import keras
from keras.models import Model
from keras.layers import Dense
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image


os.listdir(r"D:\2NAAAAAA\gradution project\New folder (2)\brain_tumor_dataset\training_set")

trdata = ImageDataGenerator()
traindata = trdata.flow_from_directory(directory=r"D:\2NAAAAAA\new dataset\Training",target_size=(224,224))


tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory=r"D:\2NAAAAAA\new dataset\Testing", target_size=(224,224))



from keras.applications.vgg16 import VGG16

vggmodel = VGG16(weights='imagenet', include_top=True)

vggmodel.summary()


for layers in (vggmodel.layers)[:19]:
    print(layers)
    layers.trainable = False



X= vggmodel.layers[-2].output


predictions = Dense(2, activation="softmax")(X)


model_final = Model(input = vggmodel.input, output = predictions)


model_final.compile(loss = "categorical_crossentropy", optimizer = optimizers.SGD(lr=0.0001, momentum=0.9), metrics=["accuracy"])


#model_final.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



model_final.summary()



from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping

os.listdir("../")


filepath="cnn-parameters-improvement-{epoch:02d}-{val_accuracy:.2f}"
#save the model with the best validation (development) accuracy till now
checkpoint = ModelCheckpoint(r"D:\2NAAAAAA\gradution project\brain\Brain-Tumor-Detection-master\New folder\new data setttt\new activation function/{}.model".format(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max'))


#checkpoint = ModelCheckpoint("vgg16_1.h5", monitor='val_acc', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
#early = EarlyStopping(monitor='val_acc', min_delta=0, patience=40, verbose=1, mode='auto')

#hist = model_final.fit_generator(generator= traindata, steps_per_epoch= 2, epochs= 15, validation_data= testdata, validation_steps=1, callbacks=[checkpoint])



####### model_final.save_weights("vgg16_1.h5")

#best_model = load_model(r'D:\2NAAAAA\gradution project\brain\Brain-Tumor-Detection-master\New folder\new data setttt\cnn-parameters-improvement-11-0.97.model')





# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
#
# # Fetch the service account key JSON file contents
# cred = credentials.Certificate(r'C:\Users\hisha\Downloads/brain-tumor-classificati-305af-firebase-adminsdk-zuf47-30c18dc580 (1).json')
# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "https://brain-tumor-classificati-305af-default-rtdb.firebaseio.com"
# })
#
# ref = db.reference('Database reference')
# print(ref.get())
#







best_model =load_model(r'D:\2NAAAAAA\gradution project\effiecientNET/cnn-parameters-improvement-05-1.00.model')

best_model.metrics_names
#loss, acc = best_model.evaluate(x=X_test, y=y_test)

import pandas as pd
#from keras.applications.efficientnet import preprocess_input

df=pd.read_csv(r"D:\New folder\submission.csv")

countNo=0
countYes=0

print(df["label"][0])
pd.options.mode.chained_assignment = None  # default='warn'

for e,i in enumerate(os.listdir(r"D:\2NAAAAAA\wierd dataset\Dataset\3")):
    print(i)
    output=[]
    img = image.load_img(os.path.join(r"D:\2NAAAAAA\wierd dataset\Dataset\3",i),target_size=(224,224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    output = best_model.predict(img)
    if output[0][0] > output[0][1]:
        output[0][0]
        df["id"][e]=i
        df["label"][e]="--------->no"
        countNo+=1
    else:
        output[0][1]
        df["id"][e]=i
        df["label"][e]="--------->yes"
        countYes+=1

df
print("Yes-> ",countYes ,"     NO->",countNo)
df.to_csv("submission.csv",index=False)




# img = image.load_img(os.path.join(r"D:\2NAAAAAA\gradution project\New folder (2)\brain_tumor_dataset\single_prediction/Y33.jpg"),target_size=(224,224))
# img = np.asarray(img)
# img = np.expand_dims(img, axis=0)
# output = best_model.predict(img)
# if output[0][0] > output[0][1]:
#  print(output[0][0])
#  print("no")
# else:
#  print(output[0][1])
#  print('yes')
