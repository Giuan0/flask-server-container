import flask
from flask import Flask
from torchvision import models, transforms
from torch.autograd import Variable

import requests
from PIL import Image
import io

app = Flask(__name__)

LABELS_URL = 'https://s3.amazonaws.com/outcome-blog/imagenet/labels.json'

cnn_model = models.resnet152(pretrained=True)
cnn_model.eval()

normalize = transforms.Normalize(
   mean=[0.485, 0.456, 0.406],
   std=[0.229, 0.224, 0.225]
)
preprocess = transforms.Compose([
   transforms.Scale(256),
   transforms.CenterCrop(224),
   transforms.ToTensor(),
   normalize
])

@app.route('/classification', methods=['POST'])
def predict():
      
    image = flask.request.files["image"].read()
    img_pil = Image.open(io.BytesIO(image))

    #pre-process image: resize,normalization and etc
    img_tensor = preprocess(img_pil)
    img_tensor.unsqueeze_(0)

    #image to tensor
    img_variable = Variable(img_tensor)
    fc_out = cnn_model(img_variable)

    #all possible results
    labels = {int(key):value for (key, value)
        in requests.get(LABELS_URL).json().items()}

    #get the most actived neuron and return
    label = labels[fc_out.data.numpy().argmax()]
    return flask.jsonify(label)
