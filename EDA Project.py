import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 10

# data = pd.read_csv("C:\\Users\\priya\\Desktop\\DATA SCIENCE\\DATASET\\WorldHospitalRankings2023.csv")
# print(data)

data = pd.read_csv("WorldHospitalRankings2023.csv")
print(data)

print("==============================================================================")

df = data

print("Head of the data :\n",df.head())

print("==============================================================================")

print("Tail of the data:\n",df.tail())

print("==============================================================================")

print("Shape of the data:\n",df.shape)

print("==============================================================================")

print("Size of the data: ",df.size)

print("==============================================================================")

print("Columns Lists:\n",df.columns)

print("==============================================================================")

print("Columns datatype:\n",df.dtypes)

print("==============================================================================")

print("Informations about data:\n",df.info())

print("==============================================================================")

print("Number of unique values_per_column:\n\n",df.nunique())

print("==============================================================================")

print("Check if there is any null values:\n\n", df.isnull().sum())

print("==============================================================================")


print("Getting the Duplicates from the data")

print(df.head())

print("==============================================================================")

print(df.shape)
print("==============================================================================")

print("Nummber of Duplicates available\n")

print(df[(df.duplicated())])

print("==============================================================================")

print("Removes the Duplicated values\n")

df.drop_duplicates(inplace = True) # To make the changes permenently
print(df)
#
print("==============================================================================")
#
print("To check the Duplicates again after Removing\n")

print(df[(df.duplicated())])
print(df.shape)

print("==============================================================================")

print("Total number of Countries\n")

columns = df.columns

# Normalize to get relative frequencies (percentages)

Column = df["Country Name"].value_counts().index
print(Column)

print("==============================================================================")

print("Occurrences of each unique value in the 'Country Name' column\n")

Column1 = df["Country Name"].value_counts()
print(Column1)

print("==============================================================================")

print("To show all the record of this column\n")

Country_Name = df[df['Country Name'].isin(['Sri Lanka'])]
print(Country_Name)

print("==============================================================================")


from numpy import genfromtxt
arr_data = genfromtxt('WorldHospitalRankings2023.csv',dtype=str,delimiter=",",encoding='UTF-8')
print(arr_data)

print("==============================================================================")
print("Shape of an NumPy array\n")

print(arr_data.shape)

print("==============================================================================")
print("Size of the elements")
print(arr_data.size)
print("==============================================================================")
print("Memory size of items")
print(arr_data.itemsize)

print("==============================================================================")
print("No of Bytes = item * itemsize")
print(arr_data.nbytes)

print(arr_data.dtype)
print(arr_data.ndim)
print(arr_data.dtype)

print("==============================================================================")
print("Getting only the Global Ranking column\n")

GlobalRanking_data_str = arr_data[...,2]
print(GlobalRanking_data_str)

print("==============================================================================")

print(" Removing the first row (column headers)\n")

print(GlobalRanking_data_str[1:])

print("==============================================================================")

print("Convert the array from string to int, replacing non-numeric values with 0")

GlobalRanking_data_int = np.where(np.char.isnumeric(GlobalRanking_data_str), GlobalRanking_data_str, '0').astype(int)
print(GlobalRanking_data_int)
print("Size:",GlobalRanking_data_int.size)

print("==============================================================================")

print("Removing all Non-Numeric Values:")

GlobalRanking_data_int = np.array(GlobalRanking_data_str[np.char.isnumeric(GlobalRanking_data_str)], dtype=int)
print(GlobalRanking_data_int)
print("Size:",GlobalRanking_data_int.size)

print("==============================================================================")

GlobalRanking_Mean = np.mean(GlobalRanking_data_int)
print("GlobalRanking_Mean:",GlobalRanking_Mean)

print("==============================================================================")
GlobalRanking_Median = np.median(GlobalRanking_data_int)
print("GlobalRanking.Median:",GlobalRanking_Median)

print("==============================================================================")

GlobalRanking_mode = stats.mode(GlobalRanking_data_int, axis = 0)
print(GlobalRanking_mode)

print("==============================================================================")

GlobalRanking_Std = np.std(GlobalRanking_data_int)
print("GlobalRanking_Std:",GlobalRanking_Std)

print("==============================================================================")

GlobalRanking_Average = np.average(GlobalRanking_data_int)
print("GlobalRanking_Average:",GlobalRanking_Average)

print("==============================================================================")
# GlobalRanking_Quantile = np.quantile(GlobalRanking_data_int)
# print("GlobalRanking.Quantile:",GlobalRanking_Quantile)

# unique_countries = np.unique(df['Country Name'])
# print(unique_countries)

print("==============================================================================")

print("Getting only the Hospital_size column\n")

HospitalSize_data_str =  arr_data[...,3]
print(HospitalSize_data_str)

print("==============================================================================")

print(" Removing the first row (column headers)\n")

print(HospitalSize_data_str[1:])

print("==============================================================================")

print("Convert the array from string to int, replacing non-numeric values with 0")

HospitalSize_data_int = np.where(np.char.isnumeric(HospitalSize_data_str),HospitalSize_data_str, '0').astype(int)
print(HospitalSize_data_int)
print("Size:",HospitalSize_data_int.size)
print("Size:",HospitalSize_data_int.dtype)

print("==============================================================================")

print("Removing all Non-Numeric Values:")

HospitalSize_data_int = np.array(HospitalSize_data_str[np.char.isnumeric(HospitalSize_data_str)], dtype=int)
print(HospitalSize_data_int)
print("Size:",HospitalSize_data_int.size)

print("==============================================================================")

HospitalSize_Mean = np.mean(HospitalSize_data_int)
print("Visibility_Mean:",HospitalSize_Mean)

print("==============================================================================")
HospitalSize_Median = np.median(HospitalSize_data_int)
print("Visibility_Median:",HospitalSize_Median)

print("==============================================================================")

HospitalSize_Mode = stats.mode(HospitalSize_data_int, axis = 0)
print("Visibility_Mode:",HospitalSize_Mode)

print("==============================================================================")

HospitalSize_std = np.std(HospitalSize_data_int)
print("Visibility_std:",HospitalSize_std)

print("==============================================================================")

HospitalSize_Average= np.average(HospitalSize_data_int)
print("Visibility_Average:",HospitalSize_Average)

print("==============================================================================")

Visibility_data_str =  arr_data[...,4]
print(Visibility_data_str)

print("==============================================================================")

print(" Removing the first row (column headers)\n")

print(Visibility_data_str[1:])

print("==============================================================================")

print("Convert the array from string to int, replacing non-numeric values with 0")

Visibility_data_int = np.where(np.char.isnumeric(Visibility_data_str),Visibility_data_str, '0').astype(int)
print(Visibility_data_int)
print("Size:",Visibility_data_int.size)
print("Size:",Visibility_data_int.dtype)

print("==============================================================================")

print("Removing all Non-Numeric Values:")

Visibility_data_int = np.array(Visibility_data_str[np.char.isnumeric(Visibility_data_str)], dtype=int)
print(Visibility_data_int)
print("Size:",Visibility_data_int.size)

print("==============================================================================")

Visibility_Mean = np.mean(Visibility_data_int)
print("Visibility_Mean:",Visibility_Mean)

print("==============================================================================")
Visibility_Median = np.median(Visibility_data_int)
print("Visibility_Median:",Visibility_Median)

print("==============================================================================")

Visibility_Mode = stats.mode(Visibility_data_int, axis = 0)
print("Visibility_Mode:",Visibility_Mode)

print("==============================================================================")

Visibility_std = np.std(Visibility_data_int)
print("Visibility_std:",Visibility_std)

print("==============================================================================")

Visibility_Average= np.average(Visibility_data_int)
print("Visibility_Average:",Visibility_Average)

print("==============================================================================")

Richfiles_data_Float = arr_data[...,5]
print(Richfiles_data_Float)

print("==============================================================================")

print(" Removing the first row (column headers)\n")

print(Richfiles_data_Float[1:])

print("==============================================================================")

print("Convert the array from string to int, replacing non-numeric values with 0")

Richfiles_data_int = np.where(np.char.isnumeric(Richfiles_data_Float),Richfiles_data_Float, '0').astype(int)
print(Richfiles_data_int)
print("Size:",Richfiles_data_int.size)

print("==============================================================================")

print("Removing all Non-Numeric Values:")

Richfiles_data_int = np.array(Richfiles_data_Float[np.char.isnumeric(Richfiles_data_Float)], dtype=int)
print(Richfiles_data_int)
print("Size:",Richfiles_data_int.size)

print("==============================================================================")

Richfiles_Mean = np.mean(Richfiles_data_int)
print("Richfiles_Mean:",Richfiles_Mean)

print("==============================================================================")
Richfiles_Median = np.median(Richfiles_data_int)
print("Richfiles_Median:",Richfiles_Median)

print("==============================================================================")

Richfiles_Mode = stats.mode(Richfiles_data_int, axis = 0)
print("Richfiles_Mode:",Richfiles_Mode)

print("==============================================================================")

Richfiles_std = np.std(Richfiles_data_int)
print("Richfiles_std:",Richfiles_std)

print("==============================================================================")

Richfiles_Average= np.average(Richfiles_data_int)
print("Richfiles_Average:",Richfiles_Average)

print("==============================================================================")


ScholarshipScore_data_Float = arr_data[...,6]
print(ScholarshipScore_data_Float)

print("==============================================================================")

print(" Removing the first row (column headers)\n")

print(ScholarshipScore_data_Float[1:])

print("==============================================================================")

print("Convert the array from string to int, replacing non-numeric values with 0")

ScholarshipScore_data_int = np.where(np.char.isnumeric(ScholarshipScore_data_Float),ScholarshipScore_data_Float, '0').astype(int)
print(ScholarshipScore_data_int)
print("Size:",ScholarshipScore_data_int.size)

print("==============================================================================")

print("Removing all Non-Numeric Values:")

ScholarshipScore_data_int = np.array(ScholarshipScore_data_Float[np.char.isnumeric(ScholarshipScore_data_Float)], dtype=int)
print(ScholarshipScore_data_int)
print("Size:",ScholarshipScore_data_int.size)

print("==============================================================================")

ScholarshipScore_Mean = np.mean(ScholarshipScore_data_int)
print("ScholarshipScore_Mean:",ScholarshipScore_Mean)

print("==============================================================================")
ScholarshipScore_Median = np.median(ScholarshipScore_data_int)
print("ScholarshipScore_Median:",ScholarshipScore_Median)

print("==============================================================================")

ScholarshipScore_Mode = stats.mode(ScholarshipScore_data_int, axis = 0)
print("ScholarshipScore_Mode:",ScholarshipScore_Mode)

print("==============================================================================")

ScholarshipScore_std = np.std(ScholarshipScore_data_int)
print("ScholarshipScore_std:",ScholarshipScore_std)

print("==============================================================================")

ScholarshipScore_Average= np.average(ScholarshipScore_data_int)
print("ScholarshipScore_Average:",ScholarshipScore_Average)

print("==============================================================================")


df_Top50hospitals = df[0:50]
print(df_Top50hospitals)

print("==============================================================================")


fig = plt.figure(figsize=(100,30))
sns.countplot(y = 'Country Name', data = df_Top50hospitals,color="red", saturation=.75, legend="auto",
              stat="count", width=.8)
plt.title("HOSPITAL COUNT")
plt.xscale("log")
plt.xlabel("Count")
plt.ylabel("Country Names")
# plt.xticks(rotation=270)
# plt.xlim(0,5*1e3)
plt.savefig('CountplotCountry&HospitalTop50.png')
plt.show()

print("==============================================================================")

histplot = sns.histplot(data=df_Top50hospitals,x='Visibility',hue = 'Country Name',multiple='stack', kde=True,bins=10)
plt.title("Histogram of Scholarship Score by Country")
plt.xticks(rotation=270)
# plt.ylim(0,10)
plt.savefig('HistplotCountryVisibilityTop50.png')
plt.show()

print("==============================================================================")

print("Relationships and Potential insights")

pairplot1= sns.pairplot(data = df_Top50hospitals,hue = 'Country Name', height=2.5)
plt.suptitle("Relationships and Potential insights")
plt.xlabel('Hospital Names')
plt.ylabel('Count')
plt.savefig('PairplotTop50.png')
plt.show()

print("==============================================================================")

print("Hospital Size - (Hospital: Global Ranking_Top50)")

Boxplot = sns.boxplot(data=df_Top50hospitals,x='Country Name',y='Hospital Size')
plt.title("Hospital Size - (Hospital: Global Ranking_Top50)", fontdict={"size":16})
plt.xticks(rotation=270)
plt.yticks(rotation=0,ticks=None)
plt.tight_layout()
plt.xlabel('Hospital Names')
plt.ylabel('Count')
plt.savefig('BoxplotCountryHospitalSizeTop50.png')
plt.show()

print("==============================================================================")

print("Scholarship Score - (Hospital: Global Ranking_Top50)")

fig = plt.figure(figsize=(40,100))
ax = fig.add_subplot(4,1,1)
sns.barplot(df_Top50hospitals, x="Hospital Name", y='Scholarship Score',hue="Country Name", palette=sns.hls_palette(8, l=0.5, s=1), ax=ax)
plt.title("Scholarship Score - (Hospital: Global Ranking_Top50)", fontdict={"size":16})
plt.xticks(rotation=270)
plt.xlabel('Hospital Names')
plt.ylabel('Count')
plt.savefig('BarplotHospitalScholarshipScoreTop50.png')
plt.show()

print("==============================================================================")

print("Rich Files - (Hospital: Global Ranking_Top50)")

custom_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]

fig = plt.figure(figsize=(40,100))
sns.barplot(df_Top50hospitals, x="Hospital Name", y='Rich Files',hue='Country Name', palette=custom_colors)
plt.title("Rich Files - (Hospital: Global Ranking_Top50)", fontdict={"size":20})
plt.grid()
plt.xticks(rotation=270)
plt.xlabel('Hospital Names')
plt.ylabel('Count')
# plt.legend(df_Top50hospitals['Country Name'], loc='upper left')
plt.savefig('BarplotHospitalRichFilesTop50.png')
plt.show()

print("==============================================================================")

print("Visibility - (Hospital: Global Ranking_Top50)")

custom_colors1 = ['#A52A2A', '#FFC0CB','#800080','#FFA500']

fig = plt.figure(figsize=(40,100))
ax = fig.add_subplot(4,1,1)
sns.barplot(df_Top50hospitals, x="Hospital Name", y='Visibility',hue='Country Name', palette=custom_colors1, ax=ax)
plt.title("Visibility - (Hospital: Global Ranking_Top50)", fontdict={"size":20})
plt.grid()
plt.xticks(rotation=270)
plt.xlabel('Hospital Names')
plt.ylabel('Count')
plt.savefig('BarplotHospitalVisibilityTop50.png')
plt.show()

print("==============================================================================")

print("Hospital Size - (Hospital: Global Ranking_Top50)")

fig = plt.figure(figsize=(40,100))
ax = fig.add_subplot(4,1,1)
sns.barplot(df_Top50hospitals, x="Hospital Name", y='Hospital Size',hue="Country Name", palette=sns.hls_palette(12, l=0.5, s=1), ax=ax)
plt.title("Hospital Size - (Hospital: Global Ranking_Top50)", fontdict={"size":20})
plt.grid()
plt.xticks(rotation=270)
plt.xlabel('Hospital Names')
plt.ylabel('Count')
plt.legend(loc="upper right", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('BarplotHospitalHospitalSizeTop50.png')
plt.show()

print("==============================================================================")












