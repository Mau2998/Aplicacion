import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_mldata 

#leemos la base de datos 
b=pd.read_csv('USvideos.csv',header=0)
print (b.shape)
ba=pd.DataFrame(b)
x=ba.drop(['description','ratings_disabled','video_error_or_removed','thumbnail_link','comments_disabled','tags','publish_time','channel_title','title','video_id','trending_date'],axis=1)
print (x)
X_embedded  =  TSNE ( n_components = 2 ) .fit_transform ( x ) 
X_embedded . forma 

