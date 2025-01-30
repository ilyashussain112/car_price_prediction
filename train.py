from pipeline.model import Model
from src.dataspliting import Spliting
import joblib as j
models = Model()
spltr = Spliting()

grid = models.model()
x_train, x_test, y_train, y_test = spltr.spliting()
print ("Training start .. .")

grid.fit(x_train, y_train)
print ("Model train")


model = grid.best_estimator_
j.dump(model , "model/model.pkl")
print ("Model save.")