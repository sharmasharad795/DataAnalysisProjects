import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


###Juve_stats sheet begins###
juve_stats=pd.read_csv('C:/Users/sharad/Documents/crime/Juve_Stats.csv')
#print(juve_stats.head(5))
#sheet1 BEGINS
year_grped=juve_stats.groupby('Year')
print("Total crimes committed by boys of all age froups across all years:",juve_stats['Total for boys all Age Groups'].sum())
print("\n")
print("Total crimes committed by girls of all age froups across all years:",juve_stats['Total for girls all Age Groups'].sum())
print("\n")
sns.lmplot(x='Total for boys all Age Groups', y='Total for girls all Age Groups', data=juve_stats,
          # fit_reg=False, # No regression line
          # hue='Year') 
t12=year_grped['Total for boys all Age Groups'].agg(np.sum)
t13=year_grped['Total for girls all Age Groups'].agg(np.sum)
t12.plot.line(marker='D',color='red',label='Boys')
t13.plot.line(marker='^',color='green',label='Girls')
plt.ylabel('no of crimes')
------------------------------------
OUTPUT :
Total crimes committed by boys of all age froups across all years: 319013


Total crimes committed by girls of all age froups across all years: 18873

Graph 1: in crimes.docx
----------------------------------------------------

year_grped=juve_stats.groupby('Year')
print("Year wise total crime comparison:")
print(year_grped['Grand total'].aggregate(np.sum))
print("\n")
t1=year_grped['Grand total'].aggregate(np.sum)
t1.plot.line(marker='D')
plt.ylabel('Crimes committed')
-----------------------------------------
OUPUT:
  Year wise total crime comparison:
Year
2001    28717
2002    30395
2003    30217
2004    31551
2005    32618
2006    34498
2007    38441
2008    39524
2009    36864
2010    35061
Name: Grand total, dtype: int64
           
Graph 2: In crimes.docx
-----------------------------------------
print("Age group for boys/girls/both most engaged in crime:")
print(juve_stats['Boys 7-12 Years'].sum())
print(juve_stats['Girls 7-12 Years'].sum())
print(juve_stats['Boys 12-16 Years'].sum())
print(juve_stats['Girls 12-16 Years'].sum())
print(juve_stats['Boys 16-18 Years'].sum())
print(juve_stats['Girls 16-18 Years'].sum())
print("\n")
----------------------------------
 OUTPUT:
 Age group for boys/girls/both most engaged in crime:
14684
1158
123092
6596
181237
11119


---------------------------------

t2=[juve_stats['Boys 7-12 Years'].sum(),juve_stats['Girls 7-12 Years'].sum(),juve_stats['Boys 12-16 Years'].sum(),juve_stats['Girls 12-16 Years'].sum(),juve_stats['Boys 16-18 Years'].sum(),juve_stats['Girls 16-18 Years'].sum()]
#print(t2)
t3=['Boys 7-12','Girls 7-12','Boys 12-16','Girls 12-16','Boys 16-18','Girls 16-18']
#print(t3)
sns.barplot(x=t3, y=t2)
plt.ylabel('Crimes committed')
plt.xlabel('Age groups')
plt.xticks(rotation='vertical')
-----------------
           Graph 3: in crimes.docx
-------------------------

print("state/ut wise comparison of young minds gone down the wrong road:")
state_grp=juve_stats.groupby('STATE/UT')

juve_stats['young_guns']=juve_stats['Boys 7-12 Years'] + juve_stats['Girls 7-12 Years']

print(state_grp)
max_young_crime=state_grp['young_guns'].agg(np.sum)
temp1=max_young_crime.sort_values(ascending=False)
temp1=temp1.head(10)
print(max_young_crime)
print(np.max(max_young_crime))
print("\n")
plt.pie(temp1,labels=temp1.index, shadow=True, startangle=180)
plt.axis('equal')
           
---------------------------
A&N Islands             5
Andhra Pradesh       1111
Arunachal Pradesh      80
Assam                 860
Bihar                  84
Chandigarh            124
Chhattisgarh         1097
D&N Haveli              3
Daman & Diu             0
Delhi UT              443
Goa                    91
Gujarat               994
Haryana               210
Himachal Pradesh       44
Jammu & Kashmir        22
Jharkhand             900
Karnataka             518
Kerala                 69
Lakshadweep             0
Madhya Pradesh       3343
Maharashtra          3174
Manipur                 0
Meghalaya              65
Mizoram               272
Nagaland               19
Odisha                576
Puducherry              2
Punjab                163
Rajasthan             653
Sikkim                 20
Tamil Nadu            563
Tripura                45
Uttar Pradesh          49
Uttarakhand            86
West Bengal           157
Name: young_guns, dtype: int64
3343
           
graph 4: in crimes.docx
--------------------------------------
           

##MP has max no of young children committing crimes..we now do a year by analysis of MP's situation regarding this
juve_stats['young_guns']=juve_stats['Boys 7-12 Years'] + juve_stats['Girls 7-12 Years']

MP_crime=juve_stats[juve_stats['STATE/UT'] == "Madhya Pradesh"]
MP_crime_yr=MP_crime.groupby('Year')
print(MP_crime_yr['young_guns'].aggregate(np.sum))
ab=MP_crime_yr['young_guns'].aggregate(np.sum)
print("\n")
ab.plot.line(marker='^',color='red')
plt.ylabel('Crimes committed')
 ------------------------------------
 Year
2001    388
2002    409
2003    427
2004    305
2005    306
2006    326
2007    362
2008    316
2009    276
2010    228
Name: young_guns, dtype: int64
 
graph 5: in crimes.docx
-------------------------------------------
juve_stats['boys']=juve_stats['Boys 7-12 Years'] + juve_stats['Boys 12-16 Years'] + juve_stats['Boys 16-18 Years']
juve_stats['girls']=juve_stats['Girls 7-12 Years'] + juve_stats['Girls 12-16 Years'] + juve_stats['Girls 16-18 Years']



crime_grp=juve_stats.groupby('CRIME')
print(crime_grp['boys'].agg(np.sum))
print(np.max(crime_grp['boys'].agg(np.sum)))
print("\n")
#theft tops in boys if we exclude other ipc crimes
print(crime_grp['girls'].agg(np.sum))
print(np.max(crime_grp['girls'].agg(np.sum)))
#hurt?grevious hurt tops for girls if we exclude other ipc crimes
print("\n")
print(crime_grp['Grand total'].agg(np.sum))
print(np.max(crime_grp['Grand total'].agg(np.sum)))
print("\n") 
           
           
------------------------------------
  OUTPUT :
 CRIME
Arson                                         748
Assault on Women wih intent to outrage h     5838
Attempt to Commit Murder                     5968
Auto Theft                                  12504
Burglary                                    30998
C H Not amounting to Murder                   302
Causing death by negligence                  1137
Cheating                                     1319
Counterfeiting                                 90
Criminal Breach of Trust                      389
Cruelty by Husband or Relatives              1833
Custodial Rape                                  0
Dacoity                                      1709
Dowry Deaths                                  486
Hurt/Grevious Hurt                          41778
Importation of girls from Foreign Countr        0
Insult to Modesty of Women                   1966
K & A of Women and Girls                     2114
K & A of others                               875
Kidnapping & Abduction                       2989
Murder                                       6857
Other IPC Crimes                            60170
Other Rape                                   6993
Other Theft                                 44928
Preparation & Assembly for Dacoity            806
Rape                                         6993
Riots                                       17461
Robbery                                      4330
Theft                                       57432
Name: boys, dtype: int64
60170


CRIME
Arson                                         17
Assault on Women wih intent to outrage h      67
Attempt to Commit Murder                     257
Auto Theft                                    43
Burglary                                     577
C H Not amounting to Murder                   24
Causing death by negligence                   45
Cheating                                      93
Counterfeiting                                13
Criminal Breach of Trust                      25
Cruelty by Husband or Relatives             1533
Custodial Rape                                 0
Dacoity                                       47
Dowry Deaths                                 342
Hurt/Grevious Hurt                          3272
Importation of girls from Foreign Countr       3
Insult to Modesty of Women                    18
K & A of Women and Girls                     235
K & A of others                               71
Kidnapping & Abduction                       306
Murder                                       500
Other IPC Crimes                            4735
Other Rape                                   136
Other Theft                                 2466
Preparation & Assembly for Dacoity             2
Rape                                         136
Riots                                       1341
Robbery                                       60
Theft                                       2509
Name: girls, dtype: int64
4735


CRIME
Arson                                         765
Assault on Women wih intent to outrage h     5905
Attempt to Commit Murder                     6225
Auto Theft                                  12547
Burglary                                    31575
C H Not amounting to Murder                   326
Causing death by negligence                  1182
Cheating                                     1412
Counterfeiting                                103
Criminal Breach of Trust                      414
Cruelty by Husband or Relatives              3366
Custodial Rape                                  0
Dacoity                                      1756
Dowry Deaths                                  828
Hurt/Grevious Hurt                          45050
Importation of girls from Foreign Countr        3
Insult to Modesty of Women                   1984
K & A of Women and Girls                     2349
K & A of others                               946
Kidnapping & Abduction                       3295
Murder                                       7357
Other IPC Crimes                            64905
Other Rape                                   7129
Other Theft                                 47394
Preparation & Assembly for Dacoity            808
Rape                                         7129
Riots                                       18802
Robbery                                      4390
Theft                                       59941
Name: Grand total, dtype: int64
64905
----------------------------------
#theft tops for both combined 
###Juve_Stats sheet ENDS#################

###Sheet 2 Begins ###Juve_arrests
juve_arst=pd.read_csv('C:/Users/sharad/Documents/crime/Juve_arrests.csv')
arst_yr_grp=juve_arst.groupby('Year')
print("Has cases against children be solved, can't ruin their future with tain against their name")
print(arst_yr_grp['Juveniles_whose_Cases_Pending_Disposal'].agg(np.sum))
t4=arst_yr_grp['Juveniles_whose_Cases_Pending_Disposal'].agg(np.sum)
print("\n")
---------------------------
 OUTPUT:
 Has cases against children be solved, can't ruin their future with tain against their name
Year
2001    14296
2002    13977
2003    12049
2004    12140
2005    13778
2006    13792
2007    14297
2008    14497
2009    14553
2010    10810
Name: Juveniles_whose_Cases_Pending_Disposal, dtype: int64
----------------------------------------
#t4.plot.line(marker='D',color='green')
#plt.ylabel('Crimes committed')
t5=juve_arst[['Year','Juveniles_whose_Cases_Pending_Disposal']]
sns.violinplot(x='Year', y='Juveniles_whose_Cases_Pending_Disposal', data=t5)
sns.swarmplot(x='Year', y='Juveniles_whose_Cases_Pending_Disposal', data=t5)
------------------------------------
Graph 6 : In crimes.docx
--------------------------------------
print("Has mental state of childen committing crime changed")
juve_arst['Mental_state']=juve_arst['Juveniles_Released_on_Probation_and_placed_under_the_Care_of_Fit_Institutions'] + juve_arst['Juveniles_Sent_to_Special_Home']
print(arst_yr_grp['Mental_state'].agg(np.sum))
print("\n")
t5=arst_yr_grp['Mental_state'].agg(np.sum)
t5.plot.line(marker='D',color='green',ls='--')
plt.ylabel('Crimes committed')
---------------------------------------
 OUTPUT:
Has mental state of childen committing crime changed
Year
2001    5040
2002    4600
2003    5462
2004    6080
2005    6356
2006    5992
2007    6413
2008    6907
2009    6661
2010    6845
Name: Mental_state, dtype: int64
           
Graph 7 : In imdb.docx
-----------------------------------
           
#region with most juvenile arrests
print("Region/state wise juvs arrested")
arst_st_grp=juve_arst.groupby('Area_Name')
print(arst_st_grp['Juveniles_Arrested'].agg(np.sum))

temp2=arst_st_grp['Juveniles_Arrested'].agg(np.sum).sort_values(ascending=False)
temp2=temp2.head(10)
plt.pie(temp2,labels=temp2.index,shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
#MP Contributes to 24.7 % of juvenile arrests
----------------------------
 OUTPUT:
 OUTPUT:
Region/state wise juvs arrested
Area_Name
Andaman & Nicobar Islands      339
Andhra Pradesh               19914
Arunachal Pradesh             1193
Assam                         4953
Bihar                         6871
Chandigarh                    1177
Chhattisgarh                 22104
Dadra & Nagar Haveli           114
Daman & Diu                     48
Delhi                         9230
Goa                            753
Gujarat                      28830
Haryana                      17484
Himachal Pradesh              1522
Jammu & Kashmir                114
Jharkhand                     6559
Karnataka                     4437
Kerala                        5404
Lakshadweep                      2
Madhya Pradesh               71254
Maharashtra                  61111
Manipur                          0
Meghalaya                      840
Mizoram                       1748
Nagaland                       123
Odisha                        4816
Puducherry                     440
Punjab                        1428
Rajasthan                    22273
Sikkim                         381
Tamil Nadu                   29906
Tripura                        209
Uttar Pradesh                 2936
Uttarakhand                    996
West Bengal                   1906
Name: Juveniles_Arrested, dtype: int64
graph 8 : in crimes.docx
---------------------------------------------
#comparing two higher to two lower states in the juveniles arrested category
t6=juve_arst[(juve_arst['Area_Name']=="Madhya Pradesh")|(juve_arst['Area_Name']=="Maharashtra")|(juve_arst['Area_Name']=="Goa")|(juve_arst['Area_Name']=="Nagaland")]

t6=t6[['Area_Name','Juveniles_Arrested']]

sns.swarmplot(x='Area_Name', y='Juveniles_Arrested', data=t6)
-----------------------
 Graph 9 : in crimes.docx
           
=--------------------
###Sheet ends#######

######prop csv#############
prop_stolen=pd.read_excel('C:/Users/sharad/Documents/crime/Prop.xlsx')
prop=prop_stolen[prop_stolen.Group_Name.str.contains("Total Property") == False]
arst_st_grp=prop.groupby('Area_Name')
recover=arst_st_grp['Value_of_Property_Recovered'].agg(np.sum)
stolen=arst_st_grp['Value_of_Property_Stolen'].agg(np.sum)
print("which state force has acted proactively to get stolen things back:")
print(recover/stolen)
           
-------------------------------
OUTPUT:
which state force has acted proactively to get stolen things back:
Area_Name
Andaman & Nicobar Islands    0.096885
Andhra Pradesh               0.482018
Arunachal Pradesh            0.336051
Assam                        0.285333
Bihar                        0.162083
Chandigarh                   0.356437
Chhattisgarh                 0.368486
Dadra & Nagar Haveli         0.121202
Daman & Diu                  0.246100
Delhi                        0.055126
Goa                          0.118313
Gujarat                      0.130236
Haryana                      0.593244
Himachal Pradesh             0.321490
Jammu & Kashmir              0.442532
Jharkhand                    0.161612
Karnataka                    0.339351
Kerala                       0.146137
Lakshadweep                  0.177742
Madhya Pradesh               0.612154
Maharashtra                  0.147042
Manipur                      0.097598
Meghalaya                    0.125425
Mizoram                      0.416117
Nagaland                     0.076075
Odisha                       0.233041
Puducherry                   0.567890
Punjab                       0.526697
Rajasthan                    0.566189
Sikkim                       0.162850
Tamil Nadu                   0.677086
Tripura                      0.178033
Uttar Pradesh                0.534611
Uttarakhand                  0.325127
West Bengal                  0.233074
dtype: float64
----------------------
t7=recover/stolen

x = t7.index
y = t7.values

plt.bar(x, y)
plt.ylabel('Ratio of recovered/stolen')
plt.xticks(rotation='vertical')

print("\n")
-------------------
graph 10 : in crimes.docx
----------------------------
#state-wise comparison of police force efficiency on basis of property stolen/recovered
t8=prop_stolen[(prop_stolen['Area_Name']=="Tamil Nadu")|(prop_stolen['Area_Name']=="Kerala")|(prop_stolen['Area_Name']=="Karnataka")|(prop_stolen['Area_Name']=="Punjab")|(prop_stolen['Area_Name']=="Madhya Pradesh")|(prop_stolen['Area_Name']=="Uttar Pradesh")|(prop_stolen['Area_Name']=="Gujarat")|(prop_stolen['Area_Name']=="Bihar")|(prop_stolen['Area_Name']=="West Bengal")|(prop_stolen['Area_Name']=="Nagaland")|(prop_stolen['Area_Name']=="Maharashtra")]
sns.lmplot(x='Value_of_Property_Stolen', y='Value_of_Property_Recovered', data=t8,
           fit_reg=True, # No regression line
           hue='Area_Name')   
           
----------------------------------
 graph 11 : in crimes.docx
---------------------------------

#TN has done the best job##'''
###sheet ends######

###Pol strength begins ####
police=pd.read_csv('C:/Users/sharad/Documents/crime/Pol_strength.csv')
police1=police[police.Group_Name.str.contains("Actual Police Strength - Total") == False]
police2=police1[police1.Group_Name.str.contains("Actual Women Police Strength - Total") == False]
police3=police2[police2.Group_Name.str.contains("Sanctioned Police Strength - Total") == False]
police4=police3[police3.Group_Name.str.contains("Sanctioned Women Police Strength - Total") == False]

pol=police4[police4['Group_Name'] == "Actual Police Strength - Armed Police"]
pol_yr_grp=pol.groupby('Year')
print("How total armed force combined across all yrs has changed:")
print(pol_yr_grp['Rank_All_Ranks_Total'].agg(np.sum))
print("\n")
           
----------------------------------------
 OUTPUT:
How total armed force combined across all yrs has changed:
Year
2001    277041
2002    293555
2003    285739
2004    294339
2005    296283
2006    314122
2007    329363
2008    341393
2009    342447
2010    356992
Name: Rank_All_Ranks_Total, dtype: int64
------------------------------
#t5=pol_yr_grp['Rank_All_Ranks_Total'].agg(np.sum)
#t5.plot.line(marker='D',color='green',ls='--')

naxal_st=pol[(pol['Area_Name']=="Jharkhand")|(pol['Area_Name']=="Bihar")|(pol['Area_Name']=="Chhattisgarh")|(pol['Area_Name']=="Odisha")|(pol['Area_Name']=="Maharashtra")|(pol['Area_Name']=="Uttar Pradesh")|(pol['Area_Name']=="Madhya Pradesh")]
nxl_yr_grp=naxal_st.groupby('Year')
print("armed force change yr wise in naxal states:")
print(nxl_yr_grp['Rank_All_Ranks_Total'].agg(np.sum))
print("\n")
#t15=nxl_yr_grp['Rank_All_Ranks_Total'].agg(np.sum)
#t15.plot.line(marker='D',color='purple',ls='--')
----------------------------------
 OUTPUT:
 armed force change yr wise in naxal states:
Year
2001     84586
2002     85651
2003     90434
2004     94561
2005     96227
2006    101819
2007    110354
2008    118935
2009    121886
2010    123510
Name: Rank_All_Ranks_Total, dtype: int64
---------------------------------------

#sns.barplot(x=naxal_st['Area_Name'], y=naxal_st['Rank_All_Ranks_Total'])
#plt.ylabel('Police force for Naxal states')
#plt.xlabel('Naxal States')
#plt.xticks(rotation='vertical')

print("which state has most women employed in police forces:")
w_police=police[police['Group_Name']=="Actual Women Police Strength - Total"]
st_women_grp=w_police.groupby('Area_Name')
print(st_women_grp['Rank_All_Ranks_Total'].agg(np.sum))
t16=st_women_grp['Rank_All_Ranks_Total'].agg(np.sum)
x=t16.index
y=t16.values
plt.bar(x,y)
plt.xticks(rotation='vertical')
#Tamil Nadu tops##
##sheet ends####
----------------------------------------
 graph 12: in crimes.docx
------------------------------------

###pol_killed begins####
##comparing terrorist act death on ind-pak border to ROI
pol_kill=pd.read_csv('C:/Users/sharad/Documents/crime/Pol_killed.csv')
del pol_kill['Sub_Group_Name']
print("Police killed on Ind-Pak border to terrorist related activities:")
pol_killed=pol_kill[pol_kill.Group_Name.str.contains("Police - Total") == False]
pak_bor_sts= pol_killed[(pol_killed['Area_Name'] == "Rajasthan")|(pol_killed['Area_Name'] == "Gujarat")|(pol_killed['Area_Name'] == "Punjab")|(pol_killed['Area_Name'] == "Jammu & Kashmir")]
print(pak_bor_sts['Police_Killed_In_TerroristsExtremists_Operations'].sum())
print("\n")

pol1=pol_killed[pol_killed.Area_Name.str.contains("Rajasthan") == False]
pol2=pol1[pol1.Area_Name.str.contains("Gujarat") == False]
pol3=pol2[pol2.Area_Name.str.contains("Punjab") == False]
pol4=pol3[pol3.Area_Name.str.contains("Jammu & Kashmir") == False]
print("police killed in terrorist activities in ROI:")
print(pol4['Police_Killed_In_TerroristsExtremists_Operations'].sum())
print("\n")
print("the ratio is")
print(pak_bor_sts['Police_Killed_In_TerroristsExtremists_Operations'].sum()/pol4['Police_Killed_In_TerroristsExtremists_Operations'].sum())
print("\n")
###1/3 of ROI...#making it one of the most dangerous borders in the world
           
------------------------------------------
 OUTPUT :
 Police killed on Ind-Pak border to terrorist related activities:
442


police killed in terrorist activities in ROI:
1214


the ratio is
0.3640856672158155
 -------------------------------------------



###most dangerous states year wise###
pol_sts_yr=pol_killed.groupby(['Year','Area_Name'])
print(pol_sts_yr['Police_Killed_Total_Policemen'].agg(np.sum).sort_values())
#2001-JK
#2002- JK
#2003/04/05/06/07/08/09-UP
#2009 -Maharashtra
#2010 - Punjab
-----------------------------------------
OUPUT:
Year  Area_Name                
2001  Andaman & Nicobar Islands      0
2008  Lakshadweep                    0
2003  Daman & Diu                    0
      Dadra & Nagar Haveli           0
2009  Nagaland                       0
2005  Lakshadweep                    0
2009  Puducherry                     0
2003  Arunachal Pradesh              0
      Andaman & Nicobar Islands      0
2005  Mizoram                        0
2002  Uttarakhand                    0
2005  Puducherry                     0
2002  Sikkim                         0
2010  Arunachal Pradesh              0
2008  Goa                            0
2009  Andaman & Nicobar Islands      0
2008  Daman & Diu                    0
2006  Andaman & Nicobar Islands      0
2008  Dadra & Nagar Haveli           0
2010  Chandigarh                     0
2002  Lakshadweep                    0
      Kerala                         0
2003  Goa                            0
2009  Mizoram                        0
      Lakshadweep                    0
2005  Goa                            0
2004  Goa                            0
      Daman & Diu                    0
      Dadra & Nagar Haveli           0
      Lakshadweep                    0

2009  Tamil Nadu                    80
2002  Uttar Pradesh                 80
2007  Chhattisgarh                  80
2003  Maharashtra                   81
2010  Chhattisgarh                  82
2004  Maharashtra                   85
2008  Maharashtra                   87
      Punjab                        89
2004  Punjab                        93
2007  Punjab                        94
2005  Punjab                        94
2001  Punjab                        95
2002  Jammu & Kashmir               96
2010  Maharashtra                   97
2006  Punjab                        99
      Maharashtra                   99
2009  Chhattisgarh                 103
2005  Maharashtra                  105
2010  Uttar Pradesh                105
2003  Uttar Pradesh                106
      Punjab                       109
2010  Punjab                       110
2004  Uttar Pradesh                111
2009  Uttar Pradesh                115
2008  Uttar Pradesh                118
2005  Uttar Pradesh                118
2006  Uttar Pradesh                123
2007  Uttar Pradesh                142
2001  Jammu & Kashmir              150
2009  Maharashtra                  152
Name: Police_Killed_Total_Policemen, Length: 350, dtype: int64
 --------------------------------------

pol_class_grp=pol_killed.groupby('Group_Name')
print(pol_class_grp['Police_Killed_Total_Policemen'].agg(np.sum))
print(pol_class_grp['Police_Injured_Total_Policemen'].agg(np.sum))
t20=pol_class_grp['Police_Killed_Total_Policemen'].agg(np.sum)

t19=pol_class_grp['Police_Injured_Total_Policemen'].agg(np.sum)
x=t19.index
y=t19.values
plt.bar(x,y)
plt.xticks(rotation='vertical')
plt.ylabel('police Injured')

plt.pie(t20,shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
------------------------------------
OUTPUT:
Group_Name
Police - Assistant Sub-Inspectors     670
Police - Constables                  5300
Police - Head Constables             1712
Police - Inspectors                   123
Police - Other Gazetted Officers       96
Police - Sub-Inspectors               476
Name: Police_Killed_Total_Policemen, dtype: int64
Group_Name
Police - Assistant Sub-Inspectors     2473
Police - Constables                  23430
Police - Head Constables              5157
Police - Inspectors                   1310
Police - Other Gazetted Officers       845
Police - Sub-Inspectors               3301
Name: Police_Injured_Total_Policemen, dtype: int64
------------------------------------------
#constables are at high risk commpared to other classes of policemen

####sheet ends#######################################

###Pol_suicide begins###
pol_sui=pd.read_csv('C:/Users/sharad/Documents/crime/Pol_suicide.csv')
pol_suicide=pol_sui[pol_sui['Group_Name'] == "Suicides by Police Personnel"]
sui_sts_grp=pol_suicide.groupby('Area_Name')
print(sui_sts_grp['Age_Total'].agg(np.sum).sort_values())
temp8=sui_sts_grp['Age_Total'].agg(np.sum).sort_values()
#temp8=temp8.tail(10)
plt.pie(temp8,shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
##maharashtra tops police suicide 
--------------------------------------
 OUTPUT:
 Area_Name
Dadra & Nagar Haveli           0
Daman & Diu                    0
Lakshadweep                    0
Arunachal Pradesh              1
Assam                          2
Manipur                        2
Mizoram                        3
Goa                            3
Puducherry                     4
Nagaland                       5
Chandigarh                     6
Meghalaya                      6
Uttarakhand                    8
Sikkim                        10
Andaman & Nicobar Islands     10
Bihar                         12
Odisha                        18
Tripura                       18
Jammu & Kashmir               20
Himachal Pradesh              26
Jharkhand                     36
Rajasthan                     47
Punjab                        50
Uttar Pradesh                 51
Chhattisgarh                  55
Delhi                         58
Haryana                       67
West Bengal                   76
Gujarat                       92
Andhra Pradesh                99
Karnataka                    101
Kerala                       134
Madhya Pradesh               154
Tamil Nadu                   165
Maharashtra                  324
Name: Age_Total, dtype: int64
graph 13: in crimes.docx
---------------------------------------------

#finding the most affected age group
t9=pol_suicide[['Age_18_25_Yrs','Age_25_35_Yrs','Age_35_45_Yrs','Age_45_55_Yrs','Age_Above_55_Yrs']]
sns.boxplot(data=t9)
plt.ylabel('no of suicides')
plt.xticks(rotation='vertical')
-----------------------------
 graph 14: in crimes.docx
 ---------------------------

####Sheet ends######

####Juve_edu starts#####

#is lack of education a major reason to commit crimes?
juve_edu=pd.read_csv('C:/Users/sharad/Documents/crime/Juve_edu.csv')
juve_edu['Lower levels of edu']=juve_edu['Education_Upto_primary'] + juve_edu['Education_Illiterate']
juve_edu_yr=juve_edu.groupby('Year')
print(juve_edu_yr['Lower levels of edu'].agg(np.sum))
t10=juve_edu_yr['Lower levels of edu'].agg(np.sum)

juve_edu['Higher levels of edu']=juve_edu['Education_Matric_or_Higher_Secondary_&_above'] +juve_edu['Education_Above_Primary_but_below_Matric_or_Higher_Secondary']
print(juve_edu_yr['Higher levels of edu'].agg(np.sum))
t11=juve_edu_yr['Higher levels of edu'].agg(np.sum)

x1 = t11.index
y1 = t11.values
x2=t10.index
y2=t10.values

t10.plot.line(marker='D',color='red',label='Lower levels')
t11.plot.line(marker='^',color='green',label='Higher levels')

plt.ylabel('Crimes committed')
plt.legend(loc='upper right')
plt.show()
-------------------------------------
OUTPUT:
Year
2001    23841
2002    24596
2003    23123
2004    20044
2005    21054
2006    20663
2007    20585
2008    21613
2009    19434
2010    17425
Name: Lower levels of edu, dtype: int64
Year
2001     9787
2002    11183
2003    10197
2004    10899
2005    11627
2006    11482
2007    13942
2008    12894
2009    14208
2010    12878
Name: Higher levels of edu, dtype: int64
           
 Graph 15 : In crimes.docx

#if we compare the two bar graphs, we'll see it is increasing for 'higher levels of edu'


##clearly lower levels of education do play a role
####sheet ends###

####Juve_eco starts###
##no need to do this
##sheet ends########

###Juve_fam starts###
juve_fam=pd.read_csv('C:/Users/sharad/Documents/crime/Juve_fam.csv')
fam_yr_grp=juve_fam.groupby('Year')
print(fam_yr_grp['Family_back_ground_Homeless'].agg(np.sum))
print(fam_yr_grp['Family_back_ground_Living_with_guardian'].agg(np.sum))
print(fam_yr_grp['Family_back_ground_Living_with_parents'].agg(np.sum))

t12=fam_yr_grp['Family_back_ground_Homeless'].agg(np.sum)
t13=fam_yr_grp['Family_back_ground_Living_with_guardian'].agg(np.sum)
t14=fam_yr_grp['Family_back_ground_Living_with_parents'].agg(np.sum)

t12.plot.line(marker='D',color='red',label='Homeless')
t13.plot.line(marker='^',color='green',label='Living in guardiun')
t14.plot.line(marker='o',color='blue',label='Living in parents')

plt.ylabel('Family Background')
plt.legend(loc='upper right',bbox_to_anchor=(1.2, 1.2))
plt.show()
##shockingly family has a reverse effect on juv_crimes
---------------------------------------
OUTPUT:
Year
2001    2533
2002    2196
2003    2156
2004    2320
2005    2719
2006    2197
2007    2354
2008    1848
2009    2352
2010    1672
Name: Family_back_ground_Homeless, dtype: int64
Year
2001    4075
2002    5692
2003    4729
2004    4922
2005    4564
2006    4958
2007    5099
2008    4852
2009    4657
2010    4082
Name: Family_back_ground_Living_with_guardian, dtype: int64
Year
2001    27020
2002    27891
2003    26435
2004    23701
2005    25398
2006    24990
2007    27074
2008    27807
2009    26633
2010    24549
Name: Family_back_ground_Living_with_parents, dtype: int64
           
  Graph 16: In crimes.docx
 -------------------------------------------------------

fam_sts_grp=juve_fam.groupby('Area_Name')
print(fam_sts_grp['Family_back_ground_Homeless'].agg(np.sum).sort_values())
t13=fam_sts_grp['Family_back_ground_Homeless'].agg(np.sum).sort_values()
plt.pie(t13,shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')


#AP tops this list followed by Tamil Nadu
--------------------------
OUTPUT:
Area_Name
Andaman & Nicobar Islands       0
Manipur                         0
Himachal Pradesh                0
Dadra & Nagar Haveli            0
Lakshadweep                     0
Arunachal Pradesh               1
Jammu & Kashmir                 1
Daman & Diu                     4
Sikkim                          9
Nagaland                       14
Goa                            21
Punjab                         27
Chandigarh                     35
Meghalaya                      39
Tripura                        43
Puducherry                     47
Uttar Pradesh                  61
Uttarakhand                    86
Mizoram                       117
Kerala                        176
West Bengal                   196
Karnataka                     237
Odisha                        244
Rajasthan                     352
Bihar                         553
Assam                         647
Jharkhand                     702
Delhi                         746
Chhattisgarh                  765
Haryana                       951
Gujarat                      2586
Maharashtra                  2681
Madhya Pradesh               2754
Tamil Nadu                   3018
Andhra Pradesh               5234
Name: Family_back_ground_Homeless, dtype: int64
           
Graph 17 : In crimes.docx
----------------------------------------------
####sheet ends ####


##recid begins ##############
recid=pd.read_csv('C:/Users/sharad/Documents/crime/recid.csv')
recid['repeated crimes/st']=recid['Offenders_Conviction_in_the_past_Twice'] + recid['Offenders_Conviction_in_the_past_Three_times_or_More']
recid_sts_grp=recid.groupby('Area_Name')
print(recid_sts_grp['repeated crimes/st'].agg(np.sum).sort_values())
t14=recid_sts_grp['repeated crimes/st'].agg(np.sum).sort_values()
plt.pie(t14,shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')

#MP is least law fearing state
-------------------------------------------
Area_Name
Daman & Diu                       0
Lakshadweep                       0
Dadra & Nagar Haveli              0
Sikkim                           30
Manipur                          68
Andaman & Nicobar Islands       142
Puducherry                      144
Goa                             149
Arunachal Pradesh               250
Tripura                         294
Meghalaya                       449
Nagaland                        529
Chandigarh                      551
Himachal Pradesh               2007
Jammu & Kashmir                2026
Uttarakhand                    2056
Mizoram                        2342
Kerala                         7380
Karnataka                      9795
Gujarat                       10019
Bihar                         10306
Maharashtra                   11794
Punjab                        13015
Uttar Pradesh                 14951
Haryana                       15202
Odisha                        16635
Rajasthan                     23797
Delhi                         24832
West Bengal                   29417
Jharkhand                     35998
Chhattisgarh                  57510
Andhra Pradesh                57778
Assam                         59426
Tamil Nadu                   108760
Madhya Pradesh               125156
Name: repeated crimes/st, dtype: int64
           
Graph 18 : in crimes.docx
--------------------------------------

recid['repeated crimes/country']=recid['Offenders_Conviction_in_the_past_Twice'] + recid['Offenders_Conviction_in_the_past_Three_times_or_More'] + recid['Offenders_Conviction_in_the_past_Once']
recid_yr_grp=recid.groupby('Year')
print(recid_yr_grp['repeated crimes/country'].agg(np.sum))

--------------------------------
OUTPUT:
Year
2001    242084
2002    200167
2003    194430
2004    278004
2005    234219
2006    232177
2007    238789
2008    222085
2009    256049
2010    240481
Name: repeated crimes/country, dtype: int64
---------------------------
#sns.violinplot(x='Year', y='Offenders_Arrested_for_the_First_time', data=recid ) 



##### sheet ends####

####corrpt sheet starts###
#corrpt=pd.read_csv('C:/Users/sharad/Documents/crime/Corrpt.csv')
#leave it , not necessary
####sheet ends##############

###women_crime begins #####

women=pd.read_csv('C:/Users/sharad/Documents/crime/wom_crimes.csv')
##finding the most common crime against women
print("Rape", np.sum(women['Rape']))
print( "Kidnap" , np.sum(women['Kidnapping and Abduction']))
print("Dowry Deaths" , np.sum(women['Dowry Deaths']))
print("Cruelt by spouse and fam", np.sum(women['Cruelty by Husband or his Relatives']))
print("Assualt" ,np.sum(women['Assault on women with intent to outrage her modesty']))
print("importaton of girls",np.sum(women['Importation of Girls']))
x=['Rape','Kidnap','Dowry Deaths','Cruelt by spouse and fam','Assualt','importation of girls']
y=[np.sum(women['Rape']),np.sum(women['Rape']),np.sum(women['Dowry Deaths']), np.sum(women['Cruelty by Husband or his Relatives']),np.sum(women['Assault on women with intent to outrage her modesty']),np.sum(women['Importation of Girls'])]
plt.bar(x,y,color='yellow')
plt.xticks(rotation='vertical')
plt.ylabel('Crimes')
           
--------------------------------
 OUTPUT:
 Rape 239137
Kidnap 263907
Dowry Deaths 91202
Cruelt by spouse and fam 875201
Assualt 453155
importaton of girls 892
           
Graph 19 : in crimes.docx
----------------------------------------
##have crimes against women decreased?
yr_wcr_grp=women.groupby('Year')
print(yr_wcr_grp['Total'].agg(np.sum))
t20=yr_wcr_grp['Total'].agg(np.sum)

t20.plot.line(marker='D',color='red')
plt.ylabel('Crimes')
-------------------------------------
Year
2001    130725
2002    131112
2003    131364
2004    143615
2005    143523
2006    154158
2007    174921
2008    186616
2009    194835
2010    205009
2011    219142
2012    232528
           
Graph 20 : In crimes.docx
----------------------------

#most unsafe state/district for women
yr_wcr_st=women.groupby('STATE/UT')
print(yr_wcr_st['Total'].agg(np.sum).sort_values())
t21=yr_wcr_st['Total'].agg(np.sum).sort_values()
x=t21.index
y=t21.values
plt.bar(x,y)
plt.xticks(rotation='vertical')
plt.ylabel('Crimes')



yr_wcr_dt=women.groupby('DISTRICT')
print(yr_wcr_dt['Total'].agg(np.sum).sort_values())
           
--------------------------------
 OUTPUT:
STATE/UT
LAKSHADWEEP              20
DAMAN & DIU              90
D & N HAVELI            243
NAGALAND                407
SIKKIM                  547
A & N ISLANDS           570
GOA                    1175
PUDUCHERRY             1226
MIZORAM                1719
MEGHALAYA              2008
ARUNACHAL PRADESH      2029
CHANDIGARH             2121
MANIPUR                2172
HIMACHAL PRADESH      10681
UTTARAKHAND           11825
TRIPURA               12573
JAMMU & KASHMIR       29067
PUNJAB                29199
JHARKHAND             30518
CHHATTISGARH          46078
DELHI                 48089
HARYANA               56292
KARNATAKA             68036
TAMIL NADU            69280
ODISHA                75876
BIHAR                 79983
GUJARAT               87463
KERALA                90514
ASSAM                 93502
MAHARASHTRA          164782
RAJASTHAN            176849
MADHYA PRADESH       183590
WEST BENGAL          202939
UTTAR PRADESH        224301
ANDHRA PRADESH       241784
Name: Total, dtype: int64
DISTRICT
BIEO                       0
CID                        0
CRIME JAMMU                0
CRIME KASHMIR              0
CRIME SRINAGAR             0
RAILWAYS KATRA             0
STF                        0
SPL CELL                   0
RAILWAYS JAMMU             1
CAR                        2
CID CRIME                  2
RAILWAYS KASHMIR           2
RAILWAYS KMR               2
LONGLENG                   2
S.T.F.                     2
UPPER DIBANG VALLEY        2
KIPHIRE                    3
ANJAW                      4
G.R.P. AJMER               4
EOW                        4
TAMENGLONG                 4
G.R.P. JODHPUR             5
CRIME BRANCH               5
W.RLY VADODARA             7
C.I.D.                     8
SUKMA                     10
CHANDEL                   11
NICOBAR                   11
G.R.P.JODHPUR             12
UKHRUL                    13
 
SAGAR                   8956
CHITTORGARH             8964
HOOGHLY                 8984
MALAPPURAM              9002
BANGALORE COMMR.        9010
SOUTH                   9268
MUMBAI COMMR.           9304
AGRA                    9497
EAST GODAVARI           9514
NALGONDA                9744
KOLKATA                 9797
KURNOOL                 9850
NAGAON                 10191
INDORE                 10392
KHAMMAM                10518
KRISHNA                10742
KANPUR NAGAR           10904
WEST                   10971
JALPAIGURI             12073
GUNTUR                 12390
LUCKNOW                12679
WEST GODAVARI          14299
AHMEDABAD COMMR.       14973
CYBERABAD              15411
KARIMNAGAR             16110
NADIA                  17582
HYDERABAD CITY         19685
24 PARGANAS NORTH      24376
24 PARGANAS SOUTH      25115
MURSHIDABAD            27004
Name: Total, Length: 806, dtype: int64
           
 Graph 21: in crimes.docx
---------------------------------------------------

ex=women[women['STATE/UT'] == "ANDHRA PRADESH"]

#contribution of AP to the most committed crime ie cruelty by ....output : 119007
print(np.sum(ex['Cruelty by Husband or his Relatives']))

##most committed crime in the top 3 district(ALL wb)
mex=women[(women['DISTRICT'] == "MURSHIDABAD")|(women['DISTRICT'] == "24 PARGANAS NORTH")|(women['DISTRICT'] == "24 PARGANAS SOUTH")]
print("Rape", np.sum(mex['Rape']))
print( "Kidnap" , np.sum(mex['Kidnapping and Abduction']))
print("Dowry Deaths" , np.sum(mex['Dowry Deaths']))
print("Cruelt by spouse and fam", np.sum(mex['Cruelty by Husband or his Relatives']))
print("Assualt" ,np.sum(mex['Assault on women with intent to outrage her modesty']))
print("importaton of girls",np.sum(mex['Importation of Girls'])) 

----------------------------------
 OUTPUT:
 Rape 7456
Kidnap 7029
Dowry Deaths 1709
Cruelt by spouse and fam 53347
Assualt 6844
importaton of girls 11
--------------------------------

##Sheet ends###
