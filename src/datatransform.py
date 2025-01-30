from .datacleaning import cleaning
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
le = LabelEncoder()
Cleaning = cleaning()
df = Cleaning.df_cleaning()

class Transform:
    def __init__ (self):
        pass
    def transform(self):
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = le.fit_transform(df[col])

        x = df.drop('Price', axis=1)
        y = df['Price']        

        x = sc.fit_transform(x)

        return x,y