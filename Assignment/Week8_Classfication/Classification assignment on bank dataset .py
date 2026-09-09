import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder

df=pd.read_csv("Week8_Classfication/bank.csv")

cat_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
num_cols = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

oe = OrdinalEncoder()
df[cat_cols] = oe.fit_transform(df[cat_cols])
X = df[cat_cols + num_cols]

raw_y=df["deposit"]
le=LabelEncoder()
Y = le.fit_transform(raw_y)

X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train Size: {round((len(X_Train)/len(X)) * 100)}%")
print(f"Test Size: {round((len(Y_Test)/len(Y)) * 100)}%")

scaler=StandardScaler()
X_train_scaler=scaler.fit_transform(X_Train)
X_Test_Scaler=scaler.transform(X_Test)

svm=SVC()
tree=DecisionTreeClassifier()
linear_model=LogisticRegression()

svm.fit(X_train_scaler,Y_Train)
tree.fit(X_train_scaler,Y_Train)
linear_model.fit(X_train_scaler,Y_Train)

svm_predict=svm.predict(X_Test_Scaler)
tree_predict=tree.predict(X_Test_Scaler)
logisctic_predict=linear_model.predict(X_Test_Scaler)

model_preds={
    "Support Vector Machine":svm_predict,
    "Decision Tree":tree_predict,
    "Logistic regression":logisctic_predict
}
for model,preds in model_preds.items():
    print(f"{model} Results: \n{classification_report(Y_Test,preds)}",sep="\n\n")