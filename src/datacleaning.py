from dataloading import loader
import pandas as pd 
PATH = r"model\car_price_prediction.csv"
loader = loader()
df = loader.df_loader(PATH)

class cleaning:
    def __init__ (self):
        pass
    def df_cleaning(self ,df=df):
        df.drop(['Doors', 'ID'], axis= 1, inplace=True)
        df.drop_duplicates(inplace=True)
        df.dropna(inplace = True)
        df["zscore"] = (df["Price"] - df["Price"].mean())/df["Price"].std()
        df.drop(df[df['zscore']>3].index, inplace=True)
        df.drop(df[df['zscore']<-3].index, inplace=True)
        print (df.shape)

        return df