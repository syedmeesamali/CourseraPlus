import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Use the seaborn regplot function to create the plot
sns.regplot(x=x, y=y)
# Use the plt.show() function to keep the plot persistent in the view
plt.show()
