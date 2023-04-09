import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

data = pd.read_csv('medium_data.csv')

datan = data['reading_time'].to_list()

population_mean = statistics.mean(datan)
stdev = statistics.stdev(datan)

def display(list):
    mean = statistics.mean(list)
    graph = ff.create_distplot([datan],['Medium Data'],show_hist = False)
    graph.add_trace(go.Scatter(x=[mean,mean], y=[0,0], mode='lines', name='Mean'))
    graph.show()

def randomData(count):
    dataset = []
    for i in range(count):
        integer = random.randint(0,len(datan)-1)
        value = datan[integer]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

st_list = []
for i in range(100):
    count = randomData(30)
    st_list.append(count)
mean = statistics.mean(st_list)

print("Mean of sample data 100 times is {}".format(mean))
print("population mean is {}".format(population_mean))
display(st_list)

stdev_1_start, stdev_1_end = population_mean - stdev, population_mean + stdev
stdev_2_start, stdev_2_end = population_mean - (2*stdev), population_mean + (2*stdev)
stdev_3_start, stdev_3_end = population_mean - (3*stdev), population_mean + (3*stdev)

'''print('{} and {} is the 1st stdev range'.format(stdev_1_start,stdev_1_end))
print('{} and {} is the 2nd stdev range'.format(stdev_2_start,stdev_2_end))
print('{} and {} is the 3rd stdev range'.format(stdev_3_start,stdev_3_end))'''

fig = ff.create_distplot([st_list],['Sample Mean 100 times'], show_hist = False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],name='Sample Mean', mode = 'lines'))

fig.add_trace(go.Scatter(x=[stdev_1_start,stdev_1_start],y=[0,0.17],name='1st stdev start', mode = 'lines'))
fig.add_trace(go.Scatter(x=[stdev_1_end,stdev_1_end],y=[0,0.17],name='1st stdev end', mode = 'lines'))

fig.add_trace(go.Scatter(x=[stdev_2_start,stdev_2_start],y=[0,0.17],name='2nd stdev start', mode = 'lines'))
fig.add_trace(go.Scatter(x=[stdev_2_end,stdev_2_end],y=[0,0.17],name='2nd stdev end', mode = 'lines'))

fig.add_trace(go.Scatter(x=[stdev_3_start,stdev_3_start],y=[0,0.17],name='3rd stdev start', mode = 'lines'))
fig.add_trace(go.Scatter(x=[stdev_3_end,stdev_3_end],y=[0,0.17],name='3rd stdev end', mode = 'lines'))

fig.show()

z_score = (mean - population_mean)/stdev

if(z_score <= 2):
    comment = 'insignificant'
else:
    comment = 'significant'

print('{} is the z-score of the data and is {}'.format(z_score, comment))
print('{} is the stdev of the sample mean'.format(statistics.stdev(st_list)))
print('{} is the stdev of the total mean'.format(statistics.stdev(datan)))