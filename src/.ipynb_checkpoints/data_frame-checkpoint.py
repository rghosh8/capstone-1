import pandas as pd

class data_frame(object):
    # parse basic statistical properties of data
    def __init__(self, filepath:str, reference_date:str='2020-03-16', current_date:str='2020-07-20', moveback_date:str='2019-10-15'):
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        
        self.df = self.df.set_index(pd.to_datetime(self.df['Date']))
        
        self.reference_date = pd.to_datetime(reference_date)
        self.reference_value = self.df.loc[self.reference_date,'Close']
        
        self.current_date = pd.to_datetime(current_date)
        self.current_value = self.df.loc[self.current_date,'Close']
        
        self.moveback_date = pd.to_datetime(moveback_date)
        self.moveback_value = self.df.loc[self.moveback_date,'Close']
        
        self.df['Noramlized_Close'] = self.df['Close'].divide(self.reference_value)
        self.df['Diff'] = self.df['Close'].diff()
        self.df['Normalized_Diff'] = self.df['Close'].divide(self.reference_value).diff()
        self.df.dropna(inplace=True)
        
    @property
    def data_info(self):
        return self.df.info()
    
    @property
    def before_after(self):
        self.before = self.df[(pd.to_datetime(self.df.index) >= self.moveback_date) & (pd.to_datetime(self.df.index) <= self.reference_date) ]
        self.after = self.df[(pd.to_datetime(self.df.index) > self.reference_date) & (pd.to_datetime(self.df.index) <= self.current_date) ]
    
        return self