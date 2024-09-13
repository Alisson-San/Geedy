from copy import deepcopy
import math
from tracemalloc import stop
import pandas as pd
from sqlalchemy import false


class Greepy():
    def __init__(self, df_pandas):
        self.df = df_pandas
        self.columns_name = self.df.columns.to_list()
        self.machines = deepcopy(self.columns_name[2:])
        self.df_times = None
        self.__count = 0

        self.__preparation_df()



    def __preparation_df(self):
        numeric_columns = self.df.columns.to_list()[1:]
        self.df[numeric_columns] = self.df[numeric_columns].apply(pd.to_numeric)
        for machine in self.machines:
            self.df[f'{machine}_time'] = self.df.apply(lambda row: self.__calculate_machine_times(row, machine), axis=1)
        self.df_times = self.df.copy().drop(self.machines, axis=1)


    def __calculate_machine_times(self, row, machine):
        return (
                row['Demanda'] / row[machine] if  row[machine] > 0 else 0
            )


    def ehValido(self, n):
        if n != 0:
            return True
        return False

    def solve(self):
        if self.__count == 0:
            print('sequence...')
            return False
        