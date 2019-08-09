from artiq.experiment import *

from imported_exp import ImportedExp

import typing


class Exp1(EnvExperiment):

    def build(self):
        self.clock_cycle = ImportedExp(self)
