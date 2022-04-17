import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

# Read file
dataFrame=pd.read_csv('StudentsPerformance.csv')
readinglist=dataFrame["reading score"].tolist()
# Finding mean
reading_mean=statistics.mean(readinglist)
# Finding median
reading_median=statistics.median(readinglist)
# Finding mode
reading_mode=statistics.mode(readinglist)
# Finding standard deviation
reading_sd=statistics.stdev(readinglist)
# Printing the values
print("The mean, median, mode of reading score is {}, {} and {} respectively".format(reading_mean,reading_median,reading_mode))

# Finding the first, second and third sd for reading score
reading_fsds,reading_fsde=reading_mean-reading_sd,reading_mean+reading_sd
reading_ssds,reading_ssde=reading_mean-(2*reading_sd),reading_mean+(2*reading_sd)
reading_tsds,reading_tsde=reading_mean-(3*reading_sd),reading_mean+(3*reading_sd)

# Ploting the normal distribution graph for reading
graph=ff.create_distplot([readinglist],['Reading Score'],show_hist=False)
graph.add_trace(go.Scatter(x=[reading_mean,reading_mean],y=[0,0.17],mode='lines',name='Reading Mean'))
graph.add_trace(go.Scatter(x=[reading_fsds,reading_fsde],y=[0,0.17],mode='lines',name='First Standard Deviation of Reading Score'))
graph.add_trace(go.Scatter(x=[reading_fsde,reading_fsds],y=[0,0.17],mode='lines',name='First Standard Deviation of Reading Score'))
graph.add_trace(go.Scatter(x=[reading_ssds,reading_ssde],y=[0,0.17],mode='lines',name='Second Standard Deviation of Reading Score'))
graph.add_trace(go.Scatter(x=[reading_ssde,reading_ssds],y=[0,0.17],mode='lines',name='Second Standard Deviation of Reading Score'))
graph.add_trace(go.Scatter(x=[reading_tsds,reading_tsde],y=[0,0.17],mode='lines',name='Third Standard Deviation of Reading Score'))
graph.add_trace(go.Scatter(x=[reading_tsde,reading_tsds],y=[0,0.17],mode='lines',name='Third Standard Deviation of Reading Score'))
graph.show()

# List of data within fist sd, second sd, third sd of reading
listofdata_fsd_reading=[result for result in readinglist if result>reading_fsds and result<reading_fsde]
listofdata_ssd_reading=[result for result in readinglist if result>reading_ssds and result<reading_ssde]
listofdata_tsd_reading=[result for result in readinglist if result>reading_tsds and result<reading_tsde]

# Printing the first, second, third standard deviation of reading
print("{}% Percentage of data lies within first sd".format(len(listofdata_fsd_reading)*100.0/len(readinglist)))
print("{}% Percentage of data lies within second sd".format(len(listofdata_fsd_reading)*100.0/len(readinglist)))
print("{}% Percentage of data lies within third sd".format(len(listofdata_fsd_reading)*100.0/len(readinglist)))