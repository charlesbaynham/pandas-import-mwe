
from artiq.experiment import *

import pandas as pd


class EndExperiment(Exception):
    pass


class ImportedExp(HasEnvironment):

    def build(self):
        self.make_dataframe()

    def make_dataframe(self) :

        arr = pd.DataFrame([123])

        return arr
