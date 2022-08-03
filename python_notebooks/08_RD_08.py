
import numpy as np, pandas as pd, matplotlib.pyplot as plt

## DAta

data = pd.read_stata("https://github.com/worldbank/r-econ-visual-library/raw/master/Library/Data/RDD_data.dta")

cutoff = 58

data_w = data[data.treatment_locality == 1]
data_w["treatment"] = data_w.treatment_locality <= cutoff

print(dataw.head(3))



