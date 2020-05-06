from sklearn.metrics import accuracy_score

y_true  = [1,0,1]
y_pred = [1,1,1]

print(confusion_matrix(y_true, y_pred))
