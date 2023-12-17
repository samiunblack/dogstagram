import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from IPython.display import Image, display


def path_to_tensor(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    return np.expand_dims(x, axis=0)



def dog_detector(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    prediction = np.argmax(ResNet50_model.predict(img))
    return ((prediction <= 268) & (prediction >= 151)) 



ResNet50_model = ResNet50(weights='imagenet')


def ResNet50_predict_labels(img_path):
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))



def predictWhat(img_path):    
    display(Image(img_path, height=224, width=224)) 
       
    if(dog_detector(img_path)):
        return True   
           
    else:
        return False