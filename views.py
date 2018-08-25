from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse 
# Create your views here.
def index(request):
	return render(request,'index.html')
def new(request):
    import numpy as np
    import matplotlib.pyplot as pt
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    data=pd.read_csv("C:/Users/Welcome/Desktop/per/dataset/train.csv").as_matrix()
    clf=DecisionTreeClassifier()
    #training dataset
    xtrain=data[0:21000,1:]
    train_label=data[0:21000,0]
    clf.fit(xtrain,train_label)
    #testing dataset
    xtest=data[0:,1:]
    actual_label=data[0:,0]
    n=request.GET["userI"]
    n=int(n)
    d=xtest[n]
    d.shape=(28,28)
    pt.imshow(255-d,cmap='gray')
    response= str(clf.predict([xtest[n]]))
    #pt.show()
    
    
    return HttpResponse(response)

