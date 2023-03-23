#### Extra space for random housekeeping stuff
import json
import pandas as pd
from utilities import Utilities


meta = pd.read_csv("/Users/rahulsharma/Desktop/Semester 4/Project/MyProject/voice-recognition-speak-sing/data/metdata.csv")
header = list(meta)[1:]
data = []
for columnName in header:
    data.append(list(meta[columnName]))


h, d = Utilities.createMarkdownTable(header, data)
print(h)


