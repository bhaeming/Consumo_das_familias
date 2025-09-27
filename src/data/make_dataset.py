import pandas as pd
import numpy as np
import sidrapy as sd
from bcb import sgs
import sidrapy as sidra
from sidrapy import get_table
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf


consumo_familias=sidra.get_table(
    table_code = "1620",
    territorial_level = "1",
    ibge_territorial_code = "all",
    variable = "583",
    classifications = {"11255":"93404"},
    period = "all"
    )

consumo_familias



bc_br= sgs.get({'ibc_br' : '24363'},
               start = '2000-03-31')
bc_br

saldo_cred_pf = sgs.get({'crédito_pf' : '20541'},
               start = '2000-03-31')
saldo_cred_pf