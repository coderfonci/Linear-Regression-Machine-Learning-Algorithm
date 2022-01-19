# in this code we use sklearn LinearRegression  or Linear Regression Using Python with scratch

# -*- coding: utf-8 -*-
"""Linear_Rigerssion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XmyAlPFIVcpAoiYB5QsCd-0djBohHYdl

# Business Problem - Predict the Price of Bangalore House
Using Linear Regression - Supervised Machine Learning Algorithm with Sklear

### Load Libraries
"""

import  pandas as pd

"""###Load Data"""

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB" 
df = pd.read_csv(path)

df.head()

"""### Split Data"""

X = df.drop('price', axis=1)
y = df['price']

print('Shape of X =', X.shape)
print('Shape of y =', y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
 
print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

"""##Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)

X_train_sc

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train_sc, y_train)

lr.coef_

lr.intercept_

"""## Predict the value of Home and Test"""

X_test_sc[0, :]

"""#let's predict single house price"""

lr.predict([X_test_sc[0, :]])

"""##Multiple house price predict"""

lr.predict(X_test_sc)

"""#check our model prediction with y_test data """

y_test

"""#Check x_test_sc data with y_test"""

lr.score(X_test_sc, y_test)

"""#Business Problem - Predict the Price of Bangalore House

*Linear Regression Using Python with scratch*
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB" 
df = pd.read_csv(path)

df.head( )

X= df['total_sqft_int']
y= df['price']

"""To estimate the intercept 𝜷0, we can use the following formula:
y = β0 + β1x![1_FHxzIyZEgc3zI0erQub_-w.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAAAoCAYAAABdNX5YAAAEu0lEQVR42uxd3W3jOBCe5PJwj8xdBacSFFwHSgcOroJzOtAiFQTaDrQlrNKB0sGCedw3uYTEHXjhYLgYEPohqbGjaOYDBAe2tKI43/xyqP0D4lEDwJ8A8BMUijSI4lAFAC0AdABQqOwVyqFxbAGgwb8NAFgAyJUDCuVQPzboUikMWoxMuaCQxKGLgHOOD3QPAF96fjPobu+VE++wEec+D8zpGrE0DqmcFIpz4lKnQKFQpVEoVGkUis+sNC5pa7xDWgWtBYADALz1HAdSVp2CO//gXV+teO7OyaG++aXzvB24rh64Lka279gMlAcL/Mc2Ao1OQSb3eJRIihQF7FCIZsXz9VEc2npyagLmuSTntzg2E/uw9cjvNWqiEag41CptE67vJuZ2TQrzkRxqiZyKwPEmK3KGNwzRZOnexkZeWwlRmCVwqPA8x9R4Z7X5hKzYSlYaP3bOIkKGRlAOuAQOdQFyMnhePsellgHnNTgQqb1olZfXhFg9K2RulsQhmqcMFVvs3EbSUMG6RFYqMiKMLtD1S8n/lsQh41XF+jzidi4RmohEWPpWAUsEko8ITVJ3+BI51BA5bbzvS46QowiMQ7egoGXNeiS2L4SFrUvjUN5TuKm51sasF4O3qI0t/mbRnerWgDDXz2LJPnFotiQOWW/NJqogM9YR8Er+3uFh8LPGlulM6NpMH/Y4J06BCi8BPc7nV2FzslQOPXqe5y7m4ouR6k4eIOQGz/0HSXOOGNkwE33HXClyVusJhbHBvSK3whRmqRxyoAup1xz3rgKT1SKizMohhAPz8XaCcR68lWcr1BsvkUNDXGK5dxsZx9uBgdU4ILfyLYE8frOf1JyPg0PUg1vGQkDnKU5UqfuKMWzyH/IBAG68wVr8bi8k+f2fOfwbs5ycBunlTOMe49DR+PyFeVHBeI8GQ+Ud5lQFfl+QnDRJAGWE1vphjhmpuTcCWkeopzlnfM4ZttYMSjyHQ32GaO7CZ197zCaiH40lFqU3pdbV1d3NyPlrRschBCH5zBCHTqE0Q+0x1OCY1PAsj3j7xn/4Sd3aHYZffSHYjkzUU6J7XXL1zJAw40Ww0szl0Cnyq8eBezyShc2H1DfP2IRKUeZpbjdC+tSdifknqJ4VkXs2JOR1KRzi9DRTi8omlg+XMxJKN5BvnrU2gRY5JTm9YD6umclC12KehSoMB4c488upReU9iXpMytaEKlDbMlKqMz2Ww05odbNiC3sQ1PZ/Kg5xeJo6gmf5jI2Ev11ZOfGwbyOLdiFKs8Yk2QTs1ZAADg7NVZomoeDUBXSpD94MyIsEfFI4K1JNxKhTOU2zQoWpVGnYOJSiNBlWbruEXbSFV0WzY9deeS7qB4nNyx6P0Ab0CIUsXL6uiCAb8tx7Eqs7S3sjqJLGxaFYuD6yvee5uoD5pz1oe6KATknvMecaTMo4Nke1I66x0P03q0Z5og12dkk7gy+9ys8Lo3secqGSK0trx60Er3qK19J+x8++0t0dKsxO+aVYQyzKmbxue9xpLuyFEsohPnQn2saRhCuSa3CWgd1iVYOJ4d+oLGvvcJYMbg4d86N/MaTPiPK4DuwP/4+WWpW5QjkUl9Oo9VfMhRgO/QoAAP//sikKamu9R2UAAAAASUVORK5CYII=)
"""

def linear_regression(X, y): 
  N = len(X)
  X_mean = X.mean()
  y_mean = y.mean()
  
  B1_num = ((X - X_mean) * (y - y_mean)).sum()
  B1_den = ((X - X_mean)**2).sum()
  B1 = B1_num / B1_den 
  
  BO = y_mean - (B1*X_mean)

  reg_line = 'y = {} + {}β'.format(BO, round(B1, 3))
  return (BO, B1, reg_line)

from google.colab import drive
drive.mount('/content/drive')

print(linear_regression(X, y))

"""Below is the formula for Pearson’s correlation coefficient:![1_EKTdjU5ls19Jr2KNyCAp1w.png](data:image/png;base64,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)"""

def corr_coef(X, y):
    N = len(X)
    
    num = (N * (X*y).sum()) - (X.sum() * y.sum())
    den = np.sqrt((N * (X**2).sum() - X.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    return R

B0, B1, reg_line = linear_regression(X, y)
print("Regression Line", reg_line)
R = corr_coef(X, y)
print('Correlation Coefe. :', R)
print('"Good of score" : ', R**2)

