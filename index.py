import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as sts
import random
from pandas import read_csv as rc

data = rc("data.csv")["Math_score"].tolist()
dataMean = sts.mean(data)
dataStd = sts.stdev(data)

def rsm(x):
    return sts.mean([data[random.randint(0, len(data)-1)] for i in range(x)])

mL = [rsm(100) for i in range(1000)]
mLStd = sts.stdev(mL)
mML = sts.mean(mL)

stdev1S, stdev1E = mML - mLStd, mML + mLStd
stdev2S, stdev2E = mML - (mLStd*2), mML + (mLStd*2)
stdev3S, stdev3E = mML - (mLStd*3), mML + (mLStd*3)

fig = ff.create_distplot([mL], ["Student Marks"], show_hist=False)

fig.add_trace(go.Scatter(x=[stdev1S, stdev1S], y=[0, 0.17], mode="lines", name="stdev1S"))
fig.add_trace(go.Scatter(x=[stdev1E, stdev1E], y=[0, 0.17], mode="lines", name="stdev1e"))

fig.add_trace(go.Scatter(x=[stdev2S, stdev2S], y=[0, 0.17], mode="lines", name="stdev2S"))
fig.add_trace(go.Scatter(x=[stdev2E, stdev2E], y=[0, 0.17], mode="lines", name="stdev2E"))

fig.add_trace(go.Scatter(x=[stdev3S, stdev3S], y=[0, 0.17], mode="lines", name="stdev3S"))
fig.add_trace(go.Scatter(x=[stdev3E, stdev3E], y=[0, 0.17], mode="lines", name="stdev3E"))

fig.show()

print("Z Score:",(sts.mean(rc("data2.csv")["Math_score"].tolist()) - dataMean)/dataStd)
