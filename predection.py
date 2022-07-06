


import os

import numpy as np
from keras.models import load_model
# from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image

best_model =load_model(r'D:\2NAAAAAA\gradution project\brain\Brain-Tumor-Detection-master\New folder\with augmanted/cnn-parameters-improvement-15-1.00.model')

best_model.metrics_names
#loss, acc = best_model.evaluate(x=X_test, y=y_test)


import pandas as pd
from keras.applications.efficientnet import preprocess_input
df=pd.read_csv(r"D:\New folder\submission.csv")



print(df["label"][0])
pd.options.mode.chained_assignment = None  # default='warn'

for e,i in enumerate(os.listdir(r"D:\YES AND NO\unknown")):
    print(i)
    output=[]
    img = image.load_img(os.path.join(r"D:\YES AND NO\unknown",i),target_size=(224,224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
#    img= preprocess_input(img)
    output = best_model.predict(img)
    if output[0][0] > output[0][1]:
#         print("cat")
        df["id"][e]=i
        df["label"][e]="--------->no"
    else:
#         print('dog')
        df["id"][e]=i
        df["label"][e]="--------->yes"

df

df.to_csv("submission.csv",index=False)
