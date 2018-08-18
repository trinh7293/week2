import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
# scatter_plot = plt.figure()
# axes1 = scatter_plot.add_subplot(1, 1, 1)
# axes1.scatter(tips['total_bill'], tips['tip'])
# axes1.set_title('Scatterplot of Total Bill vs Tip')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')

# boxplot = plt.figure()
# axes1 = boxplot.add_subplot(1, 1, 1)
# axes1.boxplot(
#     # first argument of boxplot is the data
#     # since we are plotting multiple pieces of data
#     # we have to put each piece of data into a list
#     [tips[tips['sex'] == 'Female']['tip'],
#      tips[tips['sex'] == 'Male']['tip']],
#     # We can then pass in an optional labels parameter
#     # to label the data we passed
#     labels=['Female', 'Male'])
# axes1.set_xlabel('Sex')
# axes1.set_ylabel('Tip')
# axes1.set_title('Boxplot of Tips by Sex')

# create a color variable based on the sex


# def recode_sex(sex):
#     if sex == 'Female':
#         return 0
#     else:
#         return 1
# tips['sex_color'] = tips['sex'].apply(recode_sex)
# scatter_plot = plt.figure()
# axes1 = scatter_plot.add_subplot(1, 1, 1)
# axes1.scatter(x=tips['total_bill'], y=tips['tip'],
#               # set the size of the dots based on party size
#               # we multiply the values by 10 to make the points bigger
#               # and also to emphasize the difference
#               s=tips['size'] * 10,
#               # set the color for the sex
#               c=tips['sex_color'],
#               # set the alpha so points are more transparent
#               # this helps with overlapping points
#               alpha=0.5)
# axes1.set_title('Total Bill vs Tip colored by Sex and sized by Size')
# axes1.set_xlabel('Total Bill')
# axes1.set_ylabel('Tip')
# scatter_plot.show()

# hist = sns.distplot(tips['total_bill'])
# hist.set_title('Total Bill Histogram with Density Plot')

# scatter = sns.regplot(x='total_bill', y='tip', data=tips)
# scatter.set_title('Total Bill Histogram')
# scatter.set_xlabel('Total Bill')
# scatter.set_ylabel('Frequency')

# scatter = sns.jointplot(x='total_bill', y='tip', data=tips)
# scatter.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
# # add a title, set font size, and move the text above the total bill axes
# scatter.fig.suptitle('Joint plot of Total Bill and Tip', fontsize=20, y=1.03)

# bar = sns.barplot(x='time', y='total_bill', data=tips)
# bar.set_title('Barplot of average total bill for time of day')
# bar.set_xlabel('Time of day')
# bar.set_ylabel('Average total bill')


# sns.pairplot(tips,
#              hue='sex')

tips['total_bill'].plot.kde()
plt.show()
