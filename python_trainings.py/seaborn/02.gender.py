#Imports libaries seaborn and matplotlib.pyplot
import seaborn as sns
import matplotlib.pyplot as plt

#Here we have a list of genders for each individual in the dataset.
gender = ["Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male"]

sns.countplot(x=gender)
plt.show()