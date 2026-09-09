import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

df=pd.read_csv("Week8_Classfication/winequality-red.csv")
feature = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
X=df[feature]
Y = (df['quality'] >= 6).astype(int)

X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train Size: {round((len(X_Train)/len(X)) * 100)}%")
print(f"Test Size: {round((len(Y_Test)/len(Y)) * 100)}%")

scaler=StandardScaler()
X_Train_Scaler=scaler.fit_transform(X_Train)
X_Test_Scaler=scaler.transform(X_Test)

svm = SVC(kernel='rbf', C=10, gamma='scale')
Tree = DecisionTreeClassifier(random_state=42)
linear_model = LogisticRegression()
rdc = RandomForestClassifier(n_estimators=300, max_features='sqrt', random_state=42)

svm.fit(X_Train_Scaler,Y_Train)
Tree.fit(X_Train_Scaler,Y_Train)
linear_model.fit(X_Train_Scaler,Y_Train)
rdc.fit(X_Train_Scaler,Y_Train)

svm_predict=svm.predict(X_Test_Scaler)
Tree_predict=Tree.predict(X_Test_Scaler)
logistic_regression_predict=linear_model.predict(X_Test_Scaler)
rdc_predict=rdc.predict(X_Test_Scaler)

model_preds={
    "Support Vector Machine":svm_predict,
    "Decision Tree":Tree_predict,
    "Logistic regression":logistic_regression_predict,
    "Random Forest classifier":rdc_predict
}
for model,preds in model_preds.items():
    print(f"{model} results:\n{classification_report(Y_Test,preds)}",sep="\n\n")

