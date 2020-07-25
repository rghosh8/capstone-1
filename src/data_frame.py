import pandas as pd
from parameters import *  

class data_frame(object):
    # parse basic statistical properties of data
    def __init__(self, filepath:str, reference_date:str, current_date:str, moveback_date:str, stat_date=start_date):
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        
        self.df = self.df.set_index(pd.to_datetime(self.df['Date']))
        
        self.start_date = pd.to_datetime(start_date)
        # self.start_value = self.df.loc[self.start_date,'Close']

        self.reference_date = pd.to_datetime(reference_date)
        self.reference_value = self.df.loc[self.reference_date,'Close']
        
        self.current_date = pd.to_datetime(current_date)
        self.current_value = self.df.loc[self.current_date,'Close']
        
        self.moveback_date = pd.to_datetime(moveback_date)
        self.moveback_value = self.df.loc[self.moveback_date,'Close']
        
        self.df['Noramlized_Close'] = self.df['Close'].divide(self.reference_value)
        self.df['Diff'] = self.df['Close'].diff()
        self.df['Pct_Diff'] = self.df['Close'].pct_change()
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

    @property
    def chunk(self):
        self.part = self.df[(pd.to_datetime(self.df.index) >= self.moveback_date) & (pd.to_datetime(self.df.index) <= self.current_date) ]
    
        return self



