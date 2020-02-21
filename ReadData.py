import pandas as pd
import os

class ReadData:
    def __init__(self,filepath):
        self.filepath = filepath
        self.filetype()
        if self.file_extension == '.csv':
            self.read_csv()
        elif self.file_extension == '.xlsx':
            self.read_excel()

    def filetype(self):
        filename,file_extension = os.path.splitext(self.filepath)
        self.filename = filename
        self.file_extension = file_extension

    @classmethod
    def stack_df(cls=None,data_list=None):
        # stack a few dataframe store in a list
        for nd in range(len(data_list)):
            if nd == 0:
                combined_data = data_list[nd]
            else:
                combined_data = combined_data.append(data_list[nd],ignore_index=True)

        return combined_data

    
    def read_csv(self,sep=None):
        df = pd.read_csv(self.filepath,sep=sep,skiprows=0)
        self.data = df

    def read_excel(self,sheet_name=None,header=0,usecol=None):
        df = pd.read_excel(self.filepath,sheet_name,header,usecols=None)
        self.data = df