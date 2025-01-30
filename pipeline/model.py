from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


rf = RandomForestRegressor()

class Model:
    def __init__(self):
        pass

    def model(self):

        pramas = {
        'n_estimators' : [10,20],
        'min_samples_split' : [2,3,4,],
        'min_samples_leaf' : [1,2,3],
        'max_features' : [ 'sqrt', 'log2']

        }

        grid = GridSearchCV(rf, pramas, cv=5)

        return grid