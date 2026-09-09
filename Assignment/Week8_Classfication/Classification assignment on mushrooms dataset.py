import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.metrics import classification_report

df=pd.read_csv("Week8_Classfication/mushrooms.csv")
feature=["cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring","stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color","ring-number", "ring-type", "spore-print-color","population", "habitat"]
raw_X=df[feature]
raw_Y=df["class"]

on=OrdinalEncoder()
X=on.fit_transform(raw_X)
le=LabelEncoder()
Y=le.fit_transform(raw_Y)

X_train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train Size: {round((len(X_train)/len(X)) * 100)}%")
print(f"Test Size: {round((len(Y_Test)/len(Y)) * 100)}%")

scaler=StandardScaler()
X_Train_scaler=scaler.fit_transform(X_train)
X_Test_Scaler=scaler.transform(X_Test)

svm=SVC()
tree=DecisionTreeClassifier()
linear_model=LogisticRegression()

svm.fit(X_Train_scaler,Y_Train)
tree.fit(X_Train_scaler,Y_Train)
linear_model.fit(X_Train_scaler,Y_Train)

svm_predict=svm.predict(X_Test_Scaler)
tree_predict=tree.predict(X_Test_Scaler)
linear_predict=linear_model.predict(X_Test_Scaler)

model_preds={
    "Support Vector Machine":svm_predict,
    "Decision Tree":tree_predict,
    "Logistic regression":linear_predict
}
for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(Y_Test,preds)}",sep="\n\n")