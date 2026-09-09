import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

df=pd.read_csv("Week8_Classfication/Breast_Cancer.csv")
feature=["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
X=df[feature]
y_raw=df['diagnosis']

le=LabelEncoder()
Y=le.fit_transform(y_raw)

X_train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
print(f"Train result : {round((len(X_train)/len(X))*100)}%")
print(f"Test result : {round((len(Y_Test)/len(X))*100)}%")

Scaler=StandardScaler()
X_Train_scaler=Scaler.fit_transform(X_train)
X_Test_scaler=Scaler.transform(X_Test)

svm=SVC()
tree=DecisionTreeClassifier()
linear_model=LogisticRegression()

svm.fit(X_Train_scaler,Y_Train)
tree.fit(X_Train_scaler,Y_Train)
linear_model.fit(X_Train_scaler,Y_Train)

svm_predict=svm.predict(X_Test_scaler)
tree_predict=tree.predict(X_Test_scaler)
linear_model_predict=linear_model.predict(X_Test_scaler)

model_preds ={
    "logistic regression":linear_model_predict,
    "Decision Tree":tree_predict,
    "Support Vector Machine":svm_predict
}
for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(Y_Test, preds)}", sep="\n\n")