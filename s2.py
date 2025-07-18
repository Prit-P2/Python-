import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,mean_squared_error 
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
#a=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
df=pd.read_csv("sort_housing.csv")

print(df.head())

set_train,set_test=train_test_split(df,test_size=0.2,random_state=42)

#print(set_train.shape)
#print(set_test.shape)
print(df['3'].value_counts())

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(df,df['3']):
    strat_train_set=df.loc[train_index]
    strat_test_set=df.loc[test_index]
train=strat_train_set.drop("13",axis=1)   

train_label=strat_train_set["13"].copy()

print(strat_test_set['3'].value_counts())
my_pipline=Pipeline([('std_scaler',StandardScaler()),])

train_1=my_pipline.fit_transform(train)
#model=LinearRegression()
model=DecisionTreeRegressor()
model.fit(train_1,train_label)
model_p=model.predict(train_1)
mse=mean_squared_error(train_label,model_p)
rmse=np.sqrt(mse)
print(rmse)
score=cross_val_score(model,train,train_label,scoring="neg_mean_squared_error",cv=10)
rmse=np.sqrt(-score)
print(rmse)
test=strat_test_set.drop("13",axis=1)   

test_label=strat_test_set["13"].copy()
test_1=my_pipline.transform(test)

model_p=model.predict(test_1)
mse=mean_squared_error(test_label,model_p)
rmse=np.sqrt(mse)
print(rmse)