#About this project:


#What are all libraries used: 

#Approach:

#References:
##Datasets:

#Code:

#Output:

##Console Output:

"C:\Users\priya\Desktop\DATA SCIENCE\venv\Scripts\python.exe" "C:\Users\priya\Desktop\DATA SCIENCE\Projects\EDA\EDA Project.py" 
                                       Hospital Name  ... Scholarship Score
0                                   Cleveland Clinic  ...              11.0
1               St Jude Children's Research Hospital  ...              37.0
2                             Johns Hopkins Medicine  ...              61.0
3                          Mayo Clinic Scottsdale AZ  ...              94.0
4              University of Maryland Medical Center  ...              34.0
...                                              ...  ...               ...
11997                       Polyclinique Santa Maria  ...            2394.0
11998                              Sanatorio Mautone  ...            2394.0
11999  Zentrum für Orthopadische Chirurgie Pfaffikon  ...            2394.0
12000              Marienkrankenhaus Wickede Wimbern  ...            2394.0
12001                       Volga City Hospital nr 1  ...            2394.0

[12002 rows x 7 columns]
==============================================================================
Head of the data :
                            Hospital Name  ... Scholarship Score
0                       Cleveland Clinic  ...              11.0
1   St Jude Children's Research Hospital  ...              37.0
2                 Johns Hopkins Medicine  ...              61.0
3              Mayo Clinic Scottsdale AZ  ...              94.0
4  University of Maryland Medical Center  ...              34.0

[5 rows x 7 columns]
==============================================================================
Tail of the data:
                                        Hospital Name  ... Scholarship Score
11997                       Polyclinique Santa Maria  ...            2394.0
11998                              Sanatorio Mautone  ...            2394.0
11999  Zentrum für Orthopadische Chirurgie Pfaffikon  ...            2394.0
12000              Marienkrankenhaus Wickede Wimbern  ...            2394.0
12001                       Volga City Hospital nr 1  ...            2394.0

[5 rows x 7 columns]
==============================================================================
Shape of the data:
 (12002, 7)
==============================================================================
Size of the data:  84014
==============================================================================
Columns Lists:
 Index(['Hospital Name', 'Country Name', 'Global Ranking', 'Hospital Size',
       'Visibility', 'Rich Files', 'Scholarship Score'],
      dtype='object')
==============================================================================
Columns datatype:
 Hospital Name         object
Country Name          object
Global Ranking        object
Hospital Size         object
Visibility            object
Rich Files           float64
Scholarship Score    float64
dtype: object
==============================================================================
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 12002 entries, 0 to 12001
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Hospital Name      12002 non-null  object 
 1   Country Name       12002 non-null  object 
 2   Global Ranking     12002 non-null  object 
 3   Hospital Size      12002 non-null  object 
 4   Visibility         12002 non-null  object 
 5   Rich Files         12000 non-null  float64
 6   Scholarship Score  12000 non-null  float64
dtypes: float64(2), object(5)
memory usage: 656.5+ KB
Informations about data:
 None
==============================================================================
Number of unique values_per_column:

 Hospital Name        11994
Country Name           135
Global Ranking        4006
Hospital Size         4666
Visibility           11008
Rich Files            1670
Scholarship Score      451
dtype: int64
==============================================================================
==============================================================================
Check if there is any null values:

 Hospital Name        0
Country Name         0
Global Ranking       0
Hospital Size        0
Visibility           0
Rich Files           2
Scholarship Score    2
dtype: int64
==============================================================================
Getting the Duplicates from the data
                           Hospital Name  ... Scholarship Score
0                       Cleveland Clinic  ...              11.0
1   St Jude Children's Research Hospital  ...              37.0
2                 Johns Hopkins Medicine  ...              61.0
3              Mayo Clinic Scottsdale AZ  ...              94.0
4  University of Maryland Medical Center  ...              34.0

[5 rows x 7 columns]
==============================================================================
(12002, 7)
==============================================================================
     Hospital Name    Country Name  ... Rich Files Scholarship Score
9901             N  Norfolk Island  ...        NaN               NaN

[1 rows x 7 columns]
==============================================================================
Removes the Duplicated values


                                       Hospital Name  ... Scholarship Score
0                                   Cleveland Clinic  ...              11.0
1               St Jude Children's Research Hospital  ...              37.0
2                             Johns Hopkins Medicine  ...              61.0
3                          Mayo Clinic Scottsdale AZ  ...              94.0
4              University of Maryland Medical Center  ...              34.0
...                                              ...  ...               ...
11997                       Polyclinique Santa Maria  ...            2394.0
11998                              Sanatorio Mautone  ...            2394.0
11999  Zentrum für Orthopadische Chirurgie Pfaffikon  ...            2394.0
12000              Marienkrankenhaus Wickede Wimbern  ...            2394.0
12001                       Volga City Hospital nr 1  ...            2394.0

[12001 rows x 7 columns]
==============================================================================

Process finished with exit code 0


##Interpretation
