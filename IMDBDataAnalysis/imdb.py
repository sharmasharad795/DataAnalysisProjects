
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie=pd.read_csv('C:/Users/A609418/Documents/python learnings/exercises/IMDB.csv',delimiter=',')


print(movie.dtypes)

Output:
Rank                    int64
Title                  object
Genre1                 object
Genre2                 object
Genre3                 object
Description            object
Director               object
Actors1                object
Actors2                object
Actors3                object
Actors4                object
Year                    int64
Runtime (Minutes)       int64
Rating                float64
Votes                   int64
Revenue (Millions)    float64
Metascore             float64
dtype: object

#---Movie runtime basic stats
print(movie[movie['Runtime (Minutes)'] == movie['Runtime (Minutes)'].max()])
print(movie[movie['Runtime (Minutes)'] == movie['Runtime (Minutes)'].min()])
print(movie['Runtime (Minutes)'].mean())


OUTPUT:

 Rank       Title  Genre1  Genre2    Genre3  \
828   829  Grindhouse  Action  Horror  Thriller   

                                           Description          Director  \
828  Quentin Tarantino and Robert Rodriguez's homag...  Robert Rodriguez   

          Actors1        Actors2       Actors3    Actors4  Year  \
828  Kurt Russell   Rose McGowan   Danny Trejo   Zoë Bell  2007   

     Runtime (Minutes)  Rating   Votes  Revenue (Millions)  Metascore  
828                191     7.6  160350               25.03        NaN  

--------------------------------
     Rank                Title     Genre1  Genre2 Genre3  \
793   794  Ma vie de Courgette  Animation  Comedy  Drama   

                                           Description       Director  \
793  After losing his mother, a young boy is sent t...  Claude Barras   

               Actors1         Actors2          Actors3            Actors4  \
793  Gaspard Schlatter   Sixtine Murat   Paulin Jaccoud  Michel Vuillermoz   

     Year  Runtime (Minutes)  Rating  Votes  Revenue (Millions)  Metascore  
793  2016                 66     7.8   4370                0.29       85.0  
--------------------------------
113.172
----------------------------------
#---Movie ratings basic stats
print(movie[movie['Rating'] == movie['Rating'].max()])
print(movie[movie['Rating'] == movie['Rating'].min()])
print(movie['Rating'].mean())

OUTPUT:
 Rank            Title  Genre1 Genre2 Genre3  \
54    55  The Dark Knight  Action  Crime  Drama   

                                          Description           Director  \
54  When the menace known as the Joker wreaks havo...  Christopher Nolan   

           Actors1        Actors2         Actors3        Actors4  Year  \
54  Christian Bale   Heath Ledger   Aaron Eckhart  Michael Caine  2008   

    Runtime (Minutes)  Rating    Votes  Revenue (Millions)  Metascore  
54                152     9.0  1791916              533.32       82.0 

--------------------------------------

     Rank           Title  Genre1 Genre2 Genre3  \
829   830  Disaster Movie  Comedy    NaN    NaN   

                                           Description         Director  \
829  Over the course of one evening, an unsuspectin...  Jason Friedberg   

            Actors1          Actors2        Actors3       Actors4  Year  \
829  Carmen Electra   Vanessa Lachey  Nicole Parker   Matt Lanter  2008   

     Runtime (Minutes)  Rating  Votes  Revenue (Millions)  Metascore  
829                 87     1.9  77207               14.17       15.0  
--------------------------------------

6.723200000000003
--------------------------------------

#---Movie Revenue stats
print(movie[movie['Revenue (Millions)'] == movie['Revenue (Millions)'].max()])
print(movie[movie['Revenue (Millions)'] == movie['Revenue (Millions)'].min()])
print(movie['Revenue (Millions)'].mean())

OUTPUT:
  
 Rank                                       Title  Genre1     Genre2  \
50    51  Star Wars: Episode VII - The Force Awakens  Action  Adventure   

     Genre3                                        Description     Director  \
50  Fantasy  Three decades after the defeat of the Galactic...  J.J. Abrams   

         Actors1       Actors2       Actors3            Actors4  Year  \
50  Daisy Ridley   John Boyega   Oscar Isaac   Domhnall Gleeson  2015   

    Runtime (Minutes)  Rating   Votes  Revenue (Millions)  Metascore  
50                136     8.1  661608              936.63       81.0  
----------------------------------------
     Rank             Title Genre1 Genre2    Genre3  \
231   232  A Kind of Murder  Crime  Drama  Thriller   

                                           Description      Director  \
231  In 1960s New York, Walter Stackhouse is a succ...  Andy Goddard   

            Actors1        Actors2         Actors3              Actors4  Year  \
231  Patrick Wilson   Jessica Biel   Haley Bennett   Vincent Kartheiser  2016   

     Runtime (Minutes)  Rating  Votes  Revenue (Millions)  Metascore  
231                 95     5.2   3305                 0.0       50.0  
-------------------------------------------
82.95637614678897
----------------------------------------

#---Movie metascore stats
print(movie[movie['Metascore'] == movie['Metascore'].max()])
print(movie[movie['Metascore'] == movie['Metascore'].min()])
print(movie['Metascore'].mean())

OUTPUT:
Rank    Title Genre1 Genre2 Genre3  \
656   657  Boyhood  Drama    NaN    NaN   

                                           Description           Director  \
656  The life of Mason, from early childhood to his...  Richard Linklater   

            Actors1             Actors2       Actors3       Actors4  Year  \
656  Ellar Coltrane   Patricia Arquette   Ethan Hawke  Elijah Smith  2014   

     Runtime (Minutes)  Rating   Votes  Revenue (Millions)  Metascore  
656                165     7.9  286722               25.36      100.0  
-------------------------------------------------------------------
     Rank       Title  Genre1  Genre2   Genre3  \
999  1000  Nine Lives  Comedy  Family  Fantasy   

                                           Description          Director  \
999  A stuffy businessman finds himself trapped ins...  Barry Sonnenfeld   

          Actors1           Actors2        Actors3       Actors4  Year  \
999  Kevin Spacey   Jennifer Garner   Robbie Amell  Cheryl Hines  2016   

     Runtime (Minutes)  Rating  Votes  Revenue (Millions)  Metascore  
999                 87     5.3  12435               19.64       11.0  
--------------------------------------------
58.98504273504273
------------------------------------------
#---Year wise grouping stats 
yrcount=movie['Year'].value_counts()
print(yrcount)
yrcount.plot(kind='pie', autopct='%1.1f%%',startangle=90, shadow=False, legend = False, fontsize=11)

OUTPUT:
2016    297
2015    127
2014     98
2013     91
2012     64
2011     63
2010     60
2007     53
2008     52
2009     51
2006     44
--------------------------
Graph 1 : In imdb.docx
---------------


mlength=movie.groupby('Year')

yrruntime=mlength['Runtime (Minutes)'].aggregate(np.mean)
print(yrruntime)
yrruntime.plot.line() 
---------------------OUTPUT:
  Year
2006    120.840909
2007    121.622642
2008    110.826923
2009    116.117647
2010    111.133333
2011    114.603175
2012    119.109375
2013    116.065934
2014    114.489796
2015    114.496063
2016    107.373737
Name: Runtime (Minutes), dtype: float64
-----------------------------
GRAPH2 : In imdb.docx
------------------------------
yrrating=mlength['Rating'].aggregate(np.mean)
print(yrrating)
yrrating.plot.line(x='Year',y='Rating')

------------------------------------------
OUTPUT:
Year
2006    7.125000
2007    7.133962
2008    6.784615
2009    6.960784
2010    6.826667
2011    6.838095
2012    6.925000
2013    6.812088
2014    6.837755
2015    6.602362
2016    6.436700
Name: Rating, dtype: float64
----------------------------
GRAPH 3: IN imdb.docx
----------------------------------

yrrevenue=mlength['Revenue (Millions)'].aggregate(np.mean)
print(yrrevenue)
yrrevenue.plot.line(x='Year',y='Revenue (Millions)')

-------------------------
OUTPUT:
Year
2006     86.296667
2007     87.882245
2008     99.082745
2009    112.601277
2010    105.081579
2011     87.612258
2012    107.973281
2013     87.121818
2014     85.078723
2015     78.355044
2016     54.690976
Name: Revenue (Millions), dtype: float64
----------------------
GRAPH 4 :In imdb.docx
-------------------

yrmetascore=mlength['Metascore'].aggregate(np.mean)
print(yrmetascore)
yrmetascore.plot.line(x='Year',y='Metascore')

-------------------------------
OUTPUT:
Year
2006    64.414634
2007    64.500000
2008    57.408163
2009    57.122449
2010    59.389831
2011    61.724138
2012    61.145161
2013    58.534884
2014    57.315789
2015    57.040650
2016    58.283582
Name: Metascore, dtype: float64
    
-----------------------
GRAPH 5 : In imdb.docx




#-----mix graphs
ymix=mlength[['Metascore','Revenue (Millions)']].aggregate(np.mean)
print(ymix)
plt.plot(ymix)
---------------------------
OUTPUT:
 Metascore  Revenue (Millions)
Year                               
2006  64.414634           86.296667
2007  64.500000           87.882245
2008  57.408163           99.082745
2009  57.122449          112.601277
2010  59.389831          105.081579
2011  61.724138           87.612258
2012  61.145161          107.973281
2013  58.534884           87.121818
2014  57.315789           85.078723
2015  57.040650           78.355044
2016  58.283582           54.690976

----------------------------
GRAPH 6 : In imdb.docx
---------------------


ymix2=mlength[['Runtime (Minutes)','Metascore']].aggregate(np.mean)
print(ymix2)
ax2=ymix2.plot.line()
ax2.set_ylim(56,122)

------------------------------------
Output :
Runtime (Minutes)  Metascore
Year                              
2006         120.840909  64.414634
2007         121.622642  64.500000
2008         110.826923  57.408163
2009         116.117647  57.122449
2010         111.133333  59.389831
2011         114.603175  61.724138
2012         119.109375  61.145161
2013         116.065934  58.534884
2014         114.489796  57.315789
2015         114.496063  57.040650
2016         107.373737  58.283582
-----------------------------
Graph 7 : In imdb.docx
---------------------------


ymix3=mlength[['Runtime (Minutes)','Revenue (Millions)']].aggregate(np.mean)
print(ymix3)
ax3=ymix3.plot.line()
ax3.set_ylim(54,122)

----------------------------
OUTPUT:
  Runtime (Minutes)  Revenue (Millions)
Year                                       
2006         120.840909           86.296667
2007         121.622642           87.882245
2008         110.826923           99.082745
2009         116.117647          112.601277
2010         111.133333          105.081579
2011         114.603175           87.612258
2012         119.109375          107.973281
2013         116.065934           87.121818
2014         114.489796           85.078723
2015         114.496063           78.355044
2016         107.373737           54.690976

------------------------
Graph 8 : In imdb.docx
--------------------------

ratingrun=mlength['Runtime (Minutes)','Rating'].aggregate(np.mean)
ratingrun.plot.line(x='Rating',y='Runtime (Minutes)')
---------------------------------
Graph 9 : In imdb.docx
--------------------------------

ratingrev=mlength['Revenue (Millions)','Rating'].aggregate(np.mean)
ratingrev.plot.line(x='Rating',y='Revenue (Millions)')
-------------------------------------
Graph 10 : In imdb.docx
----------------------------------

ratingmeta=mlength['Metascore','Rating'].aggregate(np.mean)
print(ratingmeta)
ratingmeta.plot.line(x='Rating',y='Metascore')

----------------------------------------
     Metascore    Rating
Year                     
2006  64.414634  7.125000
2007  64.500000  7.133962
2008  57.408163  6.784615
2009  57.122449  6.960784
2010  59.389831  6.826667
2011  61.724138  6.838095
2012  61.145161  6.925000
2013  58.534884  6.812088
2014  57.315789  6.837755
2015  57.040650  6.602362
2016  58.283582  6.436700
------------------------------------------------
Graph 11 : In imdb.docx
-----------------------------------





--- Movie category wise grouping stats

mcat=movie.groupby(['Genre1','Genre2','Genre3'])
print(mcat.aggregate(np.size).sort_values(by='Year',ascending=False ))
print(mcat.aggregate({'Rating' : np.mean,'Year' : np.count_nonzero}).sort_values(by=["Year","Rating"]))
print(mcat.aggregate({'Metascore' : np.mean,'Year' : np.count_nonzero}).sort_values(by=["Year","Metascore"]))
print(mcat.aggregate({'Runtime (Minutes)' : np.mean,'Year' : np.count_nonzero}).sort_values(by=["Year","Runtime (Minutes)"]))
print(mcat.aggregate({'Revenue (Millions)' : np.mean,'Year' : np.count_nonzero}).sort_values(by=["Year","Revenue (Millions)"]))


#--- finding out the popular and unpopular genres of each year

pop2016=movie[movie["Year"]==2016]
mcats2016=pop2016.groupby(['Genre1','Genre2','Genre3'])
print(mcats2016.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2015=movie[movie["Year"]==2015]
mcats2015=pop2015.groupby(['Genre1','Genre2','Genre3'])
print(mcats2015.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2014=movie[movie["Year"]==2014]
mcats2014=pop2014.groupby(['Genre1','Genre2','Genre3'])
print(mcats2014.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2013=movie[movie["Year"]==2013]
mcats2013=pop2013.groupby(['Genre1','Genre2','Genre3'])
print(mcats2013.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2012=movie[movie["Year"]==2012]
mcats2012=pop2012.groupby(['Genre1','Genre2','Genre3'])
print(mcats2012.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2011=movie[movie["Year"]==2011]
mcats2011=pop2011.groupby(['Genre1','Genre2','Genre3'])
print(mcats2011.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2010=movie[movie["Year"]==2010]
mcats2010=pop2010.groupby(['Genre1','Genre2','Genre3'])
print(mcats2010.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2009=movie[movie["Year"]==2009]
mcats2009=pop2009.groupby(['Genre1','Genre2','Genre3'])
print(mcats2009.aggregate(np.size).sort_values(by="Year",ascending=False))


pop2008=movie[movie["Year"]==2008]
mcats2008=pop2008.groupby(['Genre1','Genre2','Genre3'])
print(mcats2008.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2007=movie[movie["Year"]==2007]
mcats2007=pop2007.groupby(['Genre1','Genre2','Genre3'])
print(mcats2007.aggregate(np.size).sort_values(by="Year",ascending=False))

pop2006=movie[movie["Year"]==2006]
mcats2006=pop2006.groupby(['Genre1','Genre2','Genre3'])
print(mcats2006.aggregate(np.size).sort_values(by="Year",ascending=False))



#--- Director related stats

print(movie['Director'].value_counts().sort_values(ascending=False))
movie2 = movie[(movie['Genre1'] == "Action") | (movie['Genre2']== "Adventure") |  (movie['Genre3']== "Sci-Fi")]
dircount=movie2['Director'].value_counts()
print(dircount)

----------------------------------
OUTPUT :
Ridley Scott          8
M. Night Shyamalan    6
David Yates           6
Paul W.S. Anderson    6
Michael Bay           6
Justin Lin            5
Danny Boyle           5
J.J. Abrams           5
Antoine Fuqua         5
Christopher Nolan     5
David Fincher         5
Denis Villeneuve      5
Martin Scorsese       5
Zack Snyder           5
Peter Berg            5
Woody Allen           5
Gore Verbinski        4
Peter Jackson         4
James Wan             4
Joe Wright            4
Dennis Dugan          4
Paul Feig             4
D.J. Caruso           4
David O. Russell      4
Tim Burton            4
Louis Leterrier       4
Adam McKay            4
Mike Flanagan         4
Steven Spielberg      4
Clint Eastwood        4
                     ..
Oriol Paulo           1
Ryan Coogler          1
Dan Berk              1
Denzel Washington     1
Akiva Schaffer        1
Tom Gormican          1
John Wells            1
James Mangold         1
Kyle Balda            1
Mark Andrews          1
François Ozon         1
Chris Renaud          1
Colin Trevorrow       1
Lenny Abrahamson      1
Frank Miller          1
Taika Waititi         1
John Stockwell        1
Ben Younger           1
Amber Tamblyn         1
Scott Frank           1
James Lapine          1
Kenneth Lonergan      1
Dennis Gansel         1
Asghar Farhadi        1
Michael Hoffman       1
Drew Goddard          1
Garry Marshall        1
Sergei Bodrov         1
Patricia Rozema       1
Richie Smyth          1
Name: Director, Length: 644, dtype: int64
Paul W.S. Anderson         6
Ridley Scott               5
Zack Snyder                5
Christopher Nolan          5
Justin Lin                 5
Michael Bay                5
J.J. Abrams                4
Francis Lawrence           4
Antoine Fuqua              4
Peter Berg                 4
Guy Ritchie                4
Ron Howard                 3
Matthew Vaughn             3
Neill Blomkamp             3
McG                        3
Gore Verbinski             3
Paul Feig                  3
Andrew Stanton             3
Louis Leterrier            3
Edgar Wright               3
Bryan Singer               3
Roland Emmerich            3
Duncan Jones               3
Andrew Niccol              2
Pierre Coffin              2
Guillermo del Toro         2
James Gunn                 2
D.J. Caruso                2
Brett Ratner               2
Kenneth Branagh            2
                          ..
François Simard            1
Stephen Sommers            1
Mike Judge                 1
Wes Anderson               1
James Wan                  1
Olivier Megaton            1
Frank Miller               1
Paco Cabezas               1
Ruben Fleischer            1
Christopher Landon         1
J.D. Dillard               1
Greg Tiernan               1
Tyler Shields              1
Robert Stromberg           1
Chris Renaud               1
David O. Russell           1
Rupert Sanders             1
David Yates                1
Spike Jonze                1
Clint Eastwood             1
Richie Smyth               1
Rawson Marshall Thurber    1
Rich Moore                 1
Tim Miller                 1
Colin Trevorrow            1
Rob Cohen                  1
Dan Bradley                1
Dennis Gansel              1
Joe Wright                 1
Ben Wheatley               1
Name: Director, Length: 235, dtype: int64
------------------------------------------


mdir=movie.groupby('Director')
print(mdir.aggregate({'Year':np.count_nonzero,'Runtime (Minutes)':np.mean}).sort_values(by='Year',ascending=False))
----------------------------------
OUTPUT:
Director                                   
Ridley Scott           8         134.625000
M. Night Shyamalan     6         102.500000
David Yates            6         135.000000
Michael Bay            6         147.666667
Paul W.S. Anderson     6         103.333333
Danny Boyle            5         108.800000
Christopher Nolan      5         152.600000
Justin Lin             5         118.800000
Martin Scorsese        5         151.200000
Peter Berg             5         116.800000
Antoine Fuqua          5         126.200000
Woody Allen            5          99.200000
Denis Villeneuve       5         122.400000
J.J. Abrams            5         126.600000
Zack Snyder            5         136.600000
David Fincher          5         150.000000
Mike Flanagan          4          95.250000
Gore Verbinski         4         154.000000
Francis Lawrence       4         126.750000
Steven Spielberg       4         132.750000
Clint Eastwood         4         121.500000
Tim Burton             4         116.000000
David O. Russell       4         125.000000
Dennis Dugan           4         108.250000
Ron Howard             4         128.750000
Robert Zemeckis        4         125.000000
Quentin Tarantino      4         154.500000
Peter Jackson          4         152.250000
Joe Wright             4         118.500000
D.J. Caruso            4         104.250000
                 ...                ...
Jason Friedberg        1          87.000000
Jared Hess             1          95.000000
Jamie Linden           1         100.000000
James Wong             1          85.000000
James Watkins          1          92.000000
James Ward Byrkit      1          89.000000
James Schamus          1         110.000000
James Ponsoldt         1          95.000000
James Marsh            1         123.000000
James Mangold          1         126.000000
James Lapine           1         104.000000
James Gray             1         141.000000
James Franco           1         110.000000
James Cameron          1         162.000000
James Bobin            1         113.000000
Jamal Hill             1          87.000000
Jalil Lespert          1          99.000000
Jake Szymanski         1          98.000000
Jake Schreier          1         109.000000
Jake Kasdan            1          94.000000
Jaco Van Dormael       1         141.000000
Jackson Stewart        1          84.000000
J.D. Dillard           1          89.000000
J Blakeson             1         112.000000
Ivan Reitman           1         108.000000
Ilya Naishuller        1          96.000000
Ido Fluk               1          97.000000
Hugo Gélin             1         118.000000
Hope Dickson Leach     1          83.000000
Zackary Adler          1         110.000000

------------------------------------------------------------
print(mdir.aggregate({'Year':np.count_nonzero,'Rating':np.mean}).sort_values(by='Year',ascending=False))
---------------------------------
OUTPUT:
                      Year    Rating
Director                          
Ridley Scott           8  6.850000
M. Night Shyamalan     6  5.533333
David Yates            6  7.433333
Michael Bay            6  6.483333
Paul W.S. Anderson     6  5.766667
Danny Boyle            5  7.420000
Christopher Nolan      5  8.680000
Justin Lin             5  6.820000
Martin Scorsese        5  7.920000
Peter Berg             5  6.860000
Antoine Fuqua          5  7.040000
Woody Allen            5  7.020000
Denis Villeneuve       5  7.760000
J.J. Abrams            5  7.580000
Zack Snyder            5  7.040000
David Fincher          5  7.820000
Mike Flanagan          4  6.325000
Gore Verbinski         4  6.850000
Francis Lawrence       4  7.025000
Steven Spielberg       4  6.900000
Clint Eastwood         4  7.700000
Tim Burton             4  6.700000
David O. Russell       4  7.375000
Dennis Dugan           4  5.825000
Ron Howard             4  6.950000
Robert Zemeckis        4  6.975000
Quentin Tarantino      4  7.900000
Peter Jackson          4  7.475000
Joe Wright             4  6.750000
D.J. Caruso            4  5.875000
                 ...       ...
Jason Friedberg        1  1.900000
Jared Hess             1  5.800000
Jamie Linden           1  6.100000
James Wong             1  2.700000
James Watkins          1  6.300000
James Ward Byrkit      1  7.200000
James Schamus          1  6.900000
James Ponsoldt         1  7.100000
James Marsh            1  7.700000
James Mangold          1  6.700000
James Lapine           1  6.900000
James Gray             1  7.100000
James Franco           1  6.200000
James Cameron          1  7.800000
James Bobin            1  6.200000
Jamal Hill             1  6.600000
Jalil Lespert          1  6.100000
Jake Szymanski         1  6.000000
Jake Schreier          1  6.300000
Jake Kasdan            1  5.100000
Jaco Van Dormael       1  7.900000
Jackson Stewart        1  5.200000
J.D. Dillard           1  6.000000
J Blakeson             1  5.200000
Ivan Reitman           1  6.200000
Ilya Naishuller        1  6.700000
Ido Fluk               1  5.400000
Hugo Gélin             1  7.400000
Hope Dickson Leach     1  6.400000
Zackary Adler          1  5.100000
---------------------------------------------
print(mdir.aggregate({'Year':np.count_nonzero,'Revenue (Millions)':np.mean}).sort_values(by='Year',ascending=False))
------------------------------------
OUTPUT:
                    Year  Revenue (Millions)
Director                                    
Ridley Scott           8           89.882500
M. Night Shyamalan     6           74.098000
David Yates            6          271.751667
Michael Bay            6          236.886667
Paul W.S. Anderson     6           34.820000
Danny Boyle            5           36.680000
Christopher Nolan      5          303.018000
Justin Lin             5          164.958000
Martin Scorsese        5           91.622000
Peter Berg             5          102.266000
Antoine Fuqua          5           78.642000
Woody Allen            5           28.238000
Denis Villeneuve       5           43.242000
J.J. Abrams            5          336.690000
Zack Snyder            5          195.148000
David Fincher          5          105.544000
Mike Flanagan          4           31.295000
Gore Verbinski         4          207.455000
Francis Lawrence       4          324.952500
Steven Spielberg       4          156.747500
Clint Eastwood         4          164.747500
Tim Burton             4          138.505000
David O. Russell       4          108.055000
Dennis Dugan           4          124.680000
Ron Howard             4           75.922500
Robert Zemeckis        4           56.530000
Quentin Tarantino      4          112.480000
Peter Jackson          4          215.112500
Joe Wright             4           34.732500
D.J. Caruso            4           59.665000
                 ...                 ...
Jason Friedberg        1           14.170000
Jared Hess             1           17.360000
Jamie Linden           1            0.200000
James Wong             1            9.350000
James Watkins          1            0.040000
James Ward Byrkit      1            0.070000
James Schamus          1            3.400000
James Ponsoldt         1            6.850000
James Marsh            1           35.890000
James Mangold          1          132.550000
James Lapine           1                 NaN
James Gray             1            8.010000
James Franco           1                 NaN
James Cameron          1          760.510000
James Bobin            1           77.040000
Jamal Hill             1                 NaN
Jalil Lespert          1                 NaN
Jake Szymanski         1           46.010000
Jake Schreier          1           31.990000
Jake Kasdan            1           38.540000
Jaco Van Dormael       1                 NaN
Jackson Stewart        1                 NaN
J.D. Dillard           1            3.850000
J Blakeson             1           34.910000
Ivan Reitman           1           70.630000
Ilya Naishuller        1            9.240000
Ido Fluk               1                 NaN
Hugo Gélin             1                 NaN
Hope Dickson Leach     1                 NaN
Zackary Adler          1            6.530000
-----------------------------

print(movie[movie['Director']=="David Yates"])
---------------------------------
OUTPUT:
  Rank                                         Title     Genre1     Genre2  \
10     11       Fantastic Beasts and Where to Find Them  Adventure     Family   
107   108                          The Legend of Tarzan     Action  Adventure   
114   115  Harry Potter and the Deathly Hallows: Part 2  Adventure      Drama   
314   315     Harry Potter and the Order of the Phoenix  Adventure     Family   
418   419  Harry Potter and the Deathly Hallows: Part 1  Adventure     Family   
473   474        Harry Potter and the Half-Blood Prince  Adventure     Family   

      Genre3                                        Description     Director  \
10   Fantasy  The adventures of writer Newt Scamander in New...  David Yates   
107    Drama  Tarzan, having acclimated to life in London, i...  David Yates   
114  Fantasy  Harry, Ron and Hermione search for Voldemort's...  David Yates   
314  Fantasy  With their warning about Lord Voldemort's retu...  David Yates   
418  Fantasy  As Harry races against time and evil to destro...  David Yates   
473  Fantasy  As Harry Potter begins his sixth year at Hogwa...  David Yates   

                 Actors1               Actors2             Actors3  \
10        Eddie Redmayne   Katherine Waterston        Alison Sudol   
107  Alexander Skarsgård         Rory J. Saper   Christian Stevens   
114     Daniel Radcliffe           Emma Watson        Rupert Grint   
314     Daniel Radcliffe           Emma Watson        Rupert Grint   
418     Daniel Radcliffe           Emma Watson        Rupert Grint   
473     Daniel Radcliffe           Emma Watson        Rupert Grint   

              Actors4  Year  Runtime (Minutes)  Rating   Votes  \
10         Dan Fogler  2016                133     7.5  232072   
107   Christoph Waltz  2016                110     6.3  117590   
114    Michael Gambon  2011                130     8.1  590595   
314   Brendan Gleeson  2007                138     7.5  385325   
418        Bill Nighy  2010                146     7.7  357213   
473    Michael Gambon  2009                153     7.5  351059   

     Revenue (Millions)  Metascore  
10               234.02       66.0  
107              126.59       44.0  
114              380.96       87.0  
314              292.00       71.0  
418              294.98       65.0  
473              301.96       78.0  
------------------------------------------
print(mdir.aggregate({'Year':np.count_nonzero,'Metascore':np.mean}).sort_values(by='Year',ascending=False))
--------------------------------------------
OUTPUT:
                     Year  Metascore
Director                           
Ridley Scott           8  59.750000
M. Night Shyamalan     6  40.000000
David Yates            6  68.500000
Michael Bay            6  43.833333
Paul W.S. Anderson     6  40.333333
Danny Boyle            5  75.000000
Christopher Nolan      5  74.800000
Justin Lin             5  57.200000
Martin Scorsese        5  77.000000
Peter Berg             5  57.400000
Antoine Fuqua          5  52.400000
Woody Allen            5  69.400000
Denis Villeneuve       5  75.600000
J.J. Abrams            5  74.600000
Zack Snyder            5  48.000000
David Fincher          5  78.600000
Mike Flanagan          4  64.333333
Gore Verbinski         4  50.000000
Francis Lawrence       4  67.500000
Steven Spielberg       4  74.500000
Clint Eastwood         4  69.666667
Tim Burton             4  62.000000
David O. Russell       4  76.500000
Dennis Dugan           4  34.000000
Ron Howard             4  52.500000
Robert Zemeckis        4  65.000000
Quentin Tarantino      4  72.666667
Peter Jackson          4  56.250000
Joe Wright             4  54.666667
D.J. Caruso            4  36.666667
                 ...        ...
Jason Friedberg        1  15.000000
Jared Hess             1  47.000000
Jamie Linden           1        NaN
James Wong             1  45.000000
James Watkins          1  48.000000
James Ward Byrkit      1  65.000000
James Schamus          1  78.000000
James Ponsoldt         1  82.000000
James Marsh            1  72.000000
James Mangold          1  60.000000
James Lapine           1  72.000000
James Gray             1  78.000000
James Franco           1  43.000000
James Cameron          1  83.000000
James Bobin            1  34.000000
Jamal Hill             1  36.000000
Jalil Lespert          1        NaN
Jake Szymanski         1  51.000000
Jake Schreier          1  56.000000
Jake Kasdan            1  36.000000
Jaco Van Dormael       1  63.000000
Jackson Stewart        1  59.000000
J.D. Dillard           1  62.000000
J Blakeson             1  33.000000
Ivan Reitman           1  50.000000
Ilya Naishuller        1  51.000000
Ido Fluk               1  52.000000
Hugo Gélin             1        NaN
Hope Dickson Leach     1  82.000000
Zackary Adler          1  90.000000
--------------------------------


#---Actor related stats(protagnist--Actors1)

mact=movie.groupby('Actors1')
print(mact.agg(np.size).sort_values(by="Year",ascending=False))
print(mact.agg({'Year':np.size,'Rating':np.mean}).sort_values(by="Year",ascending=False))
print(mact.agg({'Year':np.size,'Revenue (Millions)':np.mean}).sort_values(by="Year",ascending=False))
print(mact.agg({'Year':np.size,'Metascore':np.mean}).sort_values(by="Year",ascending=False))
-----------------------------------------
OUTPUT:
                     Rank  Title  Genre1  Genre2  Genre3  Description  \
Actors1                                                                 
Christian Bale         11     11      11      11      11           11   
Mark Wahlberg          11     11      11      11      11           11   
Denzel Washington       9      9       9       9       9            9   
Jake Gyllenhaal         9      9       9       9       9            9   
Leonardo DiCaprio       9      9       9       9       9            9   
Brad Pitt               9      9       9       9       9            9   
Adam Sandler            9      9       9       9       9            9   
Will Smith              9      9       9       9       9            9   
Tom Hardy               8      8       8       8       8            8   
Johnny Depp             8      8       8       8       8            8   
Daniel Radcliffe        8      8       8       8       8            8   
Robert Downey Jr.       8      8       8       8       8            8   
Tom Hanks               8      8       8       8       8            8   
Jennifer Lawrence       7      7       7       7       7            7   
Matt Damon              7      7       7       7       7            7   
Matthew McConaughey     7      7       7       7       7            7   
Michael Fassbender      7      7       7       7       7            7   
Tom Cruise              7      7       7       7       7            7   
Channing Tatum          7      7       7       7       7            7   
George Clooney          6      6       6       6       6            6   
Hugh Jackman            6      6       6       6       6            6   
Seth Rogen              6      6       6       6       6            6   
Ben Affleck             6      6       6       6       6            6   
Jesse Eisenberg         6      6       6       6       6            6   
Vin Diesel              6      6       6       6       6            6   
Chris Pine              6      6       6       6       6            6   
Kristen Stewart         6      6       6       6       6            6   
Will Ferrell            6      6       6       6       6            6   
Sylvester Stallone      6      6       6       6       6            6   
Chris Hemsworth         6      6       6       6       6            6   
                  ...    ...     ...     ...     ...          ...   
Florence Pugh           1      1       1       1       1            1   
Fionn O'Shea            1      1       1       1       1            1   
Fiona Gordon            1      1       1       1       1            1   
Ferdia Walsh-Peelo      1      1       1       1       1            1   
Hiroki Hasegawa         1      1       1       1       1            1   
Ice Cube                1      1       1       1       1            1   
Ivana Baquero           1      1       1       1       1            1   
Jack Huston             1      1       1       1       1            1   
Jennifer Garner         1      1       1       1       1            1   
Jemaine Clement         1      1       1       1       1            1   
Jason Segel             1      1       1       1       1            1   
Jason Momoa             1      1       1       1       1            1   
Jason Clarke            1      1       1       1       1            1   
Jared Padalecki         1      1       1       1       1            1   
Jared Leto              1      1       1       1       1            1   
Jared Gilman            1      1       1       1       1            1   
Jane Levy               1      1       1       1       1            1   
Jamie Foxx              1      1       1       1       1            1   
James Marsden           1      1       1       1       1            1   
James Badge Dale        1      1       1       1       1            1   
James Allen McCune      1      1       1       1       1            1   
Jamal Woolard           1      1       1       1       1            1   
Jake Johnson            1      1       1       1       1            1   
Jahking Guillory        1      1       1       1       1            1   
Jaden Smith             1      1       1       1       1            1   
Jacob Latimore          1      1       1       1       1            1   
Jackie Earle Haley      1      1       1       1       1            1   
Jackie Chan             1      1       1       1       1            1   
Jack O'Connell          1      1       1       1       1            1   
Zooey Deschanel         1      1       1       1       1            1   

                     Director  Actors2  Actors3  Actors4  Year  \
Actors1                                                          
Christian Bale             11       11       11       11    11   
Mark Wahlberg              11       11       11       11    11   
Denzel Washington           9        9        9        9     9   
Jake Gyllenhaal             9        9        9        9     9   
Leonardo DiCaprio           9        9        9        9     9   
Brad Pitt                   9        9        9        9     9   
Adam Sandler                9        9        9        9     9   
Will Smith                  9        9        9        9     9   
Tom Hardy                   8        8        8        8     8   
Johnny Depp                 8        8        8        8     8   
Daniel Radcliffe            8        8        8        8     8   
Robert Downey Jr.           8        8        8        8     8   
Tom Hanks                   8        8        8        8     8   
Jennifer Lawrence           7        7        7        7     7   
Matt Damon                  7        7        7        7     7   
Matthew McConaughey         7        7        7        7     7   
Michael Fassbender          7        7        7        7     7   
Tom Cruise                  7        7        7        7     7   
Channing Tatum              7        7        7        7     7   
George Clooney              6        6        6        6     6   
Hugh Jackman                6        6        6        6     6   
Seth Rogen                  6        6        6        6     6   
Ben Affleck                 6        6        6        6     6   
Jesse Eisenberg             6        6        6        6     6   
Vin Diesel                  6        6        6        6     6   
Chris Pine                  6        6        6        6     6   
Kristen Stewart             6        6        6        6     6   
Will Ferrell                6        6        6        6     6   
Sylvester Stallone          6        6        6        6     6   
Chris Hemsworth             6        6        6        6     6   
                      ...      ...      ...      ...   ...   
Florence Pugh               1        1        1        1     1   
Fionn O'Shea                1        1        1        1     1   
Fiona Gordon                1        1        1        1     1   
Ferdia Walsh-Peelo          1        1        1        1     1   
Hiroki Hasegawa             1        1        1        1     1   
Ice Cube                    1        1        1        1     1   
Ivana Baquero               1        1        1        1     1   
Jack Huston                 1        1        1        1     1   
Jennifer Garner             1        1        1        1     1   
Jemaine Clement             1        1        1        1     1   
Jason Segel                 1        1        1        1     1   
Jason Momoa                 1        1        1        1     1   
Jason Clarke                1        1        1        1     1   
Jared Padalecki             1        1        1        1     1   
Jared Leto                  1        1        1        1     1   
Jared Gilman                1        1        1        1     1   
Jane Levy                   1        1        1        1     1   
Jamie Foxx                  1        1        1        1     1   
James Marsden               1        1        1        1     1   
James Badge Dale            1        1        1        1     1   
James Allen McCune          1        1        1        1     1   
Jamal Woolard               1        1        1        1     1   
Jake Johnson                1        1        1        1     1   
Jahking Guillory            1        1        1        1     1   
Jaden Smith                 1        1        1        1     1   
Jacob Latimore              1        1        1        1     1   
Jackie Earle Haley          1        1        1        1     1   
Jackie Chan                 1        1        1        1     1   
Jack O'Connell              1        1        1        1     1   
Zooey Deschanel             1        1        1        1     1   

                     Runtime (Minutes)  Rating  Votes  Revenue (Millions)  \
Actors1                                                                     
Christian Bale                      11    11.0     11                11.0   
Mark Wahlberg                       11    11.0     11                11.0   
Denzel Washington                    9     9.0      9                 9.0   
Jake Gyllenhaal                      9     9.0      9                 9.0   
Leonardo DiCaprio                    9     9.0      9                 9.0   
Brad Pitt                            9     9.0      9                 9.0   
Adam Sandler                         9     9.0      9                 9.0   
Will Smith                           9     9.0      9                 9.0   
Tom Hardy                            8     8.0      8                 8.0   
Johnny Depp                          8     8.0      8                 8.0   
Daniel Radcliffe                     8     8.0      8                 8.0   
Robert Downey Jr.                    8     8.0      8                 8.0   
Tom Hanks                            8     8.0      8                 8.0   
Jennifer Lawrence                    7     7.0      7                 7.0   
Matt Damon                           7     7.0      7                 7.0   
Matthew McConaughey                  7     7.0      7                 7.0   
Michael Fassbender                   7     7.0      7                 7.0   
Tom Cruise                           7     7.0      7                 7.0   
Channing Tatum                       7     7.0      7                 7.0   
George Clooney                       6     6.0      6                 6.0   
Hugh Jackman                         6     6.0      6                 6.0   
Seth Rogen                           6     6.0      6                 6.0   
Ben Affleck                          6     6.0      6                 6.0   
Jesse Eisenberg                      6     6.0      6                 6.0   
Vin Diesel                           6     6.0      6                 6.0   
Chris Pine                           6     6.0      6                 6.0   
Kristen Stewart                      6     6.0      6                 6.0   
Will Ferrell                         6     6.0      6                 6.0   
Sylvester Stallone                   6     6.0      6                 6.0   
Chris Hemsworth                      6     6.0      6                 6.0   
                               ...     ...    ...                 ...   
Florence Pugh                        1     1.0      1                 1.0   
Fionn O'Shea                         1     1.0      1                 1.0   
Fiona Gordon                         1     1.0      1                 1.0   
Ferdia Walsh-Peelo                   1     1.0      1                 1.0   
Hiroki Hasegawa                      1     1.0      1                 1.0   
Ice Cube                             1     1.0      1                 1.0   
Ivana Baquero                        1     1.0      1                 1.0   
Jack Huston                          1     1.0      1                 1.0   
Jennifer Garner                      1     1.0      1                 1.0   
Jemaine Clement                      1     1.0      1                 1.0   
Jason Segel                          1     1.0      1                 1.0   
Jason Momoa                          1     1.0      1                 1.0   
Jason Clarke                         1     1.0      1                 1.0   
Jared Padalecki                      1     1.0      1                 1.0   
Jared Leto                           1     1.0      1                 1.0   
Jared Gilman                         1     1.0      1                 1.0   
Jane Levy                            1     1.0      1                 1.0   
Jamie Foxx                           1     1.0      1                 1.0   
James Marsden                        1     1.0      1                 1.0   
James Badge Dale                     1     1.0      1                 1.0   
James Allen McCune                   1     1.0      1                 1.0   
Jamal Woolard                        1     1.0      1                 1.0   
Jake Johnson                         1     1.0      1                 1.0   
Jahking Guillory                     1     1.0      1                 1.0   
Jaden Smith                          1     1.0      1                 1.0   
Jacob Latimore                       1     1.0      1                 1.0   
Jackie Earle Haley                   1     1.0      1                 1.0   
Jackie Chan                          1     1.0      1                 1.0   
Jack O'Connell                       1     1.0      1                 1.0   
Zooey Deschanel                      1     1.0      1                 1.0   

                     Metascore  
Actors1                         
Christian Bale            11.0  
Mark Wahlberg             11.0  
Denzel Washington          9.0  
Jake Gyllenhaal            9.0  
Leonardo DiCaprio          9.0  
Brad Pitt                  9.0  
Adam Sandler               9.0  
Will Smith                 9.0  
Tom Hardy                  8.0  
Johnny Depp                8.0  
Daniel Radcliffe           8.0  
Robert Downey Jr.          8.0  
Tom Hanks                  8.0  
Jennifer Lawrence          7.0  
Matt Damon                 7.0  
Matthew McConaughey        7.0  
Michael Fassbender         7.0  
Tom Cruise                 7.0  
Channing Tatum             7.0  
George Clooney             6.0  
Hugh Jackman               6.0  
Seth Rogen                 6.0  
Ben Affleck                6.0  
Jesse Eisenberg            6.0  
Vin Diesel                 6.0  
Chris Pine                 6.0  
Kristen Stewart            6.0  
Will Ferrell               6.0  
Sylvester Stallone         6.0  
Chris Hemsworth            6.0  
                       ...  
Florence Pugh              1.0  
Fionn O'Shea               1.0  
Fiona Gordon               1.0  
Ferdia Walsh-Peelo         1.0  
Hiroki Hasegawa            1.0  
Ice Cube                   1.0  
Ivana Baquero              1.0  
Jack Huston                1.0  
Jennifer Garner            1.0  
Jemaine Clement            1.0  
Jason Segel                1.0  
Jason Momoa                1.0  
Jason Clarke               1.0  
Jared Padalecki            1.0  
Jared Leto                 1.0  
Jared Gilman               1.0  
Jane Levy                  1.0  
Jamie Foxx                 1.0  
James Marsden              1.0  
James Badge Dale           1.0  
James Allen McCune         1.0  
Jamal Woolard              1.0  
Jake Johnson               1.0  
Jahking Guillory           1.0  
Jaden Smith                1.0  
Jacob Latimore             1.0  
Jackie Earle Haley         1.0  
Jackie Chan                1.0  
Jack O'Connell             1.0  
Zooey Deschanel            1.0  

[525 rows x 16 columns]
                     Year    Rating
Actors1                            
Christian Bale         11  7.318182
Mark Wahlberg          11  6.690909
Denzel Washington       9  7.200000
Jake Gyllenhaal         9  7.266667
Leonardo DiCaprio       9  7.922222
Brad Pitt               9  7.466667
Adam Sandler            9  5.844444
Will Smith              9  6.977778
Tom Hardy               8  7.300000
Johnny Depp             8  6.800000
Daniel Radcliffe        8  7.075000
Robert Downey Jr.       8  7.512500
Tom Hanks               8  7.200000
Jennifer Lawrence       7  6.985714
Matt Damon              7  7.028571
Matthew McConaughey     7  7.000000
Michael Fassbender      7  6.557143
Tom Cruise              7  7.100000
Channing Tatum          7  6.171429
George Clooney          6  7.066667
Hugh Jackman            6  7.250000
Seth Rogen              6  6.500000
Ben Affleck             6  7.316667
Jesse Eisenberg         6  7.133333
Vin Diesel              6  6.766667
Chris Pine              6  7.266667
Kristen Stewart         6  5.483333
Will Ferrell            6  6.600000
Sylvester Stallone      6  6.700000
Chris Hemsworth         6  6.300000
                  ...       ...
Florence Pugh           1  7.300000
Fionn O'Shea            1  7.400000
Fiona Gordon            1  6.800000
Ferdia Walsh-Peelo      1  8.000000
Hiroki Hasegawa         1  6.900000
Ice Cube                1  5.900000
Ivana Baquero           1  8.200000
Jack Huston             1  5.700000
Jennifer Garner         1  7.000000
Jemaine Clement         1  7.600000
Jason Segel             1  5.100000
Jason Momoa             1  5.200000
Jason Clarke            1  7.100000
Jared Padalecki         1  5.600000
Jared Leto              1  7.900000
Jared Gilman            1  7.800000
Jane Levy               1  6.500000
Jamie Foxx              1  8.400000
James Marsden           1  6.700000
James Badge Dale        1  6.300000
James Allen McCune      1  5.100000
Jamal Woolard           1  6.700000
Jake Johnson            1  6.500000
Jahking Guillory        1  6.100000
Jaden Smith             1  4.900000
Jacob Latimore          1  6.000000
Jackie Earle Haley      1  7.600000
Jackie Chan             1  6.200000
Jack O'Connell          1  7.200000
Zooey Deschanel         1  7.700000

[525 rows x 2 columns]
                     Year  Revenue (Millions)
Actors1                                      
Christian Bale         11          141.783636
Mark Wahlberg          11           95.644545
Denzel Washington       9           92.663750
Jake Gyllenhaal         9           37.708889
Leonardo DiCaprio       9          124.206667
Brad Pitt               9           78.138889
Adam Sandler            9           99.247500
Will Smith              9          148.920000
Tom Hardy               8           27.492500
Johnny Depp             8          160.117500
Daniel Radcliffe        8          182.754286
Robert Downey Jr.       8          320.572500
Tom Hanks               8          125.320000
Jennifer Lawrence       7          267.978333
Matt Damon              7          133.491667
Matthew McConaughey     7           93.845000
Michael Fassbender      7           17.670000
Tom Cruise              7          120.575714
Channing Tatum          7           81.880000
George Clooney          6           73.166667
Hugh Jackman            6          102.961667
Seth Rogen              6           95.088333
Ben Affleck             6          137.126667
Jesse Eisenberg         6           84.990000
Vin Diesel              6          170.481667
Chris Pine              6          125.036667
Kristen Stewart         6          203.658333
Will Ferrell            6          126.151667
Sylvester Stallone      6           60.900000
Chris Hemsworth         6           85.370000
                  ...                 ...
Florence Pugh           1                 NaN
Fionn O'Shea            1                 NaN
Fiona Gordon            1                 NaN
Ferdia Walsh-Peelo      1            3.230000
Hiroki Hasegawa         1            1.910000
Ice Cube                1           54.010000
Ivana Baquero           1           37.620000
Jack Huston             1           26.380000
Jennifer Garner         1           61.690000
Jemaine Clement         1            3.330000
Jason Segel             1           38.540000
Jason Momoa             1           21.270000
Jason Clarke            1           43.250000
Jared Padalecki         1           65.000000
Jared Leto              1                 NaN
Jared Gilman            1           45.510000
Jane Levy               1           54.240000
Jamie Foxx              1          162.800000
James Marsden           1           26.760000
James Badge Dale        1                 NaN
James Allen McCune      1           20.750000
Jamal Woolard           1           36.840000
Jake Johnson            1           82.390000
Jahking Guillory        1            0.150000
Jaden Smith             1           60.520000
Jacob Latimore          1            3.850000
Jackie Earle Haley      1          107.500000
Jackie Chan             1          176.590000
Jack O'Connell          1          115.600000
Zooey Deschanel         1           32.390000

[525 rows x 2 columns]
                     Year  Metascore
Actors1                             
Christian Bale         11  69.181818
Mark Wahlberg          11  55.000000
Denzel Washington       9  67.500000
Jake Gyllenhaal         9  63.111111
Leonardo DiCaprio       9  68.666667
Brad Pitt               9  70.555556
Adam Sandler            9  30.888889
Will Smith              9  48.875000
Tom Hardy               8  66.428571
Johnny Depp             8  56.571429
Daniel Radcliffe        8  63.750000
Robert Downey Jr.       8  60.750000
Tom Hanks               8  66.375000
Jennifer Lawrence       7  61.666667
Matt Damon              7  67.000000
Matthew McConaughey     7  53.000000
Michael Fassbender      7  61.571429
Tom Cruise              7  62.285714
Channing Tatum          7  57.166667
George Clooney          6  68.800000
Hugh Jackman            6  57.333333
Seth Rogen              6  66.166667
Ben Affleck             6  63.833333
Jesse Eisenberg         6  65.166667
Vin Diesel              6  53.833333
Chris Pine              6  70.833333
Kristen Stewart         6  57.500000
Will Ferrell            6  53.333333
Sylvester Stallone      6  48.166667
Chris Hemsworth         6  45.833333
                  ...        ...
Florence Pugh           1  83.000000
Fionn O'Shea            1        NaN
Fiona Gordon            1        NaN
Ferdia Walsh-Peelo      1  79.000000
Hiroki Hasegawa         1  68.000000
Ice Cube                1  67.000000
Ivana Baquero           1  98.000000
Jack Huston             1  38.000000
Jennifer Garner         1  44.000000
Jemaine Clement         1  76.000000
Jason Segel             1  36.000000
Jason Momoa             1        NaN
Jason Clarke            1  64.000000
Jared Padalecki         1  34.000000
Jared Leto              1  63.000000
Jared Gilman            1  84.000000
Jane Levy               1  57.000000
Jamie Foxx              1  81.000000
James Marsden           1  29.000000
James Badge Dale        1  39.000000
James Allen McCune      1  47.000000
Jamal Woolard           1  60.000000
Jake Johnson            1  30.000000
Jahking Guillory        1  69.000000
Jaden Smith             1  33.000000
Jacob Latimore          1  62.000000
Jackie Earle Haley      1  56.000000
Jackie Chan             1  61.000000
Jack O'Connell          1  59.000000
Zooey Deschanel         1  76.000000
------------------------------------------------

popact=movie[(movie['Actors1']=='Christian Bale')|(movie['Actors1']=='Mark Wahlberg')|(movie['Actors1']=='Denzel Washington')|(movie['Actors1']=='Jake Gyllenhaal')|(movie['Actors1']=='Leonardo DiCaprio')]
print(popact['Director'].value_counts())
gpopact=popact.groupby(['Genre1','Genre2','Genre3'])
print(gpopact.agg(np.size).sort_values(by='Year',ascending=False))

----------------------------------------


#---Stats regarding relations between metascore, rating,revenue, runtime

#---IMDB TOP 250. Rating >=8.0 and votes >= 25k

top250=movie[(movie['Rating']>=8.0)&(movie['Votes']>=25000)]
print(top250.shape)
print(top250['Rating'].mean())
print(top250['Revenue (Millions)'].mean())
print(top250['Runtime (Minutes)'].mean())
print(top250['Metascore'].mean())

---------------------------------------
OUTPUT:
8.201351351351354
145.51671232876714
129.9189189189189
78.08571428571429
-----------------------------------




topgenre=top250.groupby(['Genre1','Genre2','Genre3'])
print(topgenre.agg(np.size).sort_values(by='Year',ascending=False))

---------------------------------------
OUTPUT:
                               Rank  Title  Description  Director  Actors1  \
Genre1    Genre2    Genre3                                                   
Action    Adventure Sci-Fi        5      5            5         5        5   
Animation Adventure Comedy        4      4            4         4        4   
Crime     Drama     Mystery       2      2            2         2        2   
Adventure Drama     Sci-Fi        2      2            2         2        2   
Biography Drama     History       2      2            2         2        2   
Drama     Mystery   Sci-Fi        2      2            2         2        2   
Action    Biography Drama         2      2            2         2        2   
Drama     Mystery   Romance       2      2            2         2        2   
Crime     Drama     Thriller      2      2            2         2        2   
Comedy    Drama     Music         2      2            2         2        2   
Adventure Drama     Thriller      2      2            2         2        2   
Biography Drama     Thriller      1      1            1         1        1   
Comedy    Drama     Romance       1      1            1         1        1   
Action    Adventure Comedy        1      1            1         1        1   
Comedy    Drama     Thriller      1      1            1         1        1   
Crime     Drama     History       1      1            1         1        1   
Biography Comedy    Crime         1      1            1         1        1   
Drama     Family    Music         1      1            1         1        1   
          Fantasy   War           1      1            1         1        1   
          Mystery   War           1      1            1         1        1   
Biography Comedy    Drama         1      1            1         1        1   
Animation Adventure Family        1      1            1         1        1   
          Drama     Fantasy       1      1            1         1        1   
          Comedy    Family        1      1            1         1        1   
Action    Adventure Drama         1      1            1         1        1   
Animation Action    Adventure     1      1            1         1        1   
Adventure Drama     War           1      1            1         1        1   
                    Fantasy       1      1            1         1        1   
          Comedy    Drama         1      1            1         1        1   
          Biography Drama         1      1            1         1        1   
Action    Sci-Fi    Thriller      1      1            1         1        1   
          Mystery   Thriller      1      1            1         1        1   
          Drama     Sport         1      1            1         1        1   
          Crime     Drama         1      1            1         1        1   
          Adventure Thriller      1      1            1         1        1   
                    Fantasy       1      1            1         1        1   
Drama     Romance   Sci-Fi        1      1            1         1        1   

                               Actors2  Actors3  Actors4  Year  \
Genre1    Genre2    Genre3                                       
Action    Adventure Sci-Fi           5        5        5     5   
Animation Adventure Comedy           4        4        4     4   
Crime     Drama     Mystery          2        2        2     2   
Adventure Drama     Sci-Fi           2        2        2     2   
Biography Drama     History          2        2        2     2   
Drama     Mystery   Sci-Fi           2        2        2     2   
Action    Biography Drama            2        2        2     2   
Drama     Mystery   Romance          2        2        2     2   
Crime     Drama     Thriller         2        2        2     2   
Comedy    Drama     Music            2        2        2     2   
Adventure Drama     Thriller         2        2        2     2   
Biography Drama     Thriller         1        1        1     1   
Comedy    Drama     Romance          1        1        1     1   
Action    Adventure Comedy           1        1        1     1   
Comedy    Drama     Thriller         1        1        1     1   
Crime     Drama     History          1        1        1     1   
Biography Comedy    Crime            1        1        1     1   
Drama     Family    Music            1        1        1     1   
          Fantasy   War              1        1        1     1   
          Mystery   War              1        1        1     1   
Biography Comedy    Drama            1        1        1     1   
Animation Adventure Family           1        1        1     1   
          Drama     Fantasy          1        1        1     1   
          Comedy    Family           1        1        1     1   
Action    Adventure Drama            1        1        1     1   
Animation Action    Adventure        1        1        1     1   
Adventure Drama     War              1        1        1     1   
                    Fantasy          1        1        1     1   
          Comedy    Drama            1        1        1     1   
          Biography Drama            1        1        1     1   
Action    Sci-Fi    Thriller         1        1        1     1   
          Mystery   Thriller         1        1        1     1   
          Drama     Sport            1        1        1     1   
          Crime     Drama            1        1        1     1   
          Adventure Thriller         1        1        1     1   
                    Fantasy          1        1        1     1   
Drama     Romance   Sci-Fi           1        1        1     1   

                               Runtime (Minutes)  Rating  Votes  \
Genre1    Genre2    Genre3                                        
Action    Adventure Sci-Fi                     5     5.0      5   
Animation Adventure Comedy                     4     4.0      4   
Crime     Drama     Mystery                    2     2.0      2   
Adventure Drama     Sci-Fi                     2     2.0      2   
Biography Drama     History                    2     2.0      2   
Drama     Mystery   Sci-Fi                     2     2.0      2   
Action    Biography Drama                      2     2.0      2   
Drama     Mystery   Romance                    2     2.0      2   
Crime     Drama     Thriller                   2     2.0      2   
Comedy    Drama     Music                      2     2.0      2   
Adventure Drama     Thriller                   2     2.0      2   
Biography Drama     Thriller                   1     1.0      1   
Comedy    Drama     Romance                    1     1.0      1   
Action    Adventure Comedy                     1     1.0      1   
Comedy    Drama     Thriller                   1     1.0      1   
Crime     Drama     History                    1     1.0      1   
Biography Comedy    Crime                      1     1.0      1   
Drama     Family    Music                      1     1.0      1   
          Fantasy   War                        1     1.0      1   
          Mystery   War                        1     1.0      1   
Biography Comedy    Drama                      1     1.0      1   
Animation Adventure Family                     1     1.0      1   
          Drama     Fantasy                    1     1.0      1   
          Comedy    Family                     1     1.0      1   
Action    Adventure Drama                      1     1.0      1   
Animation Action    Adventure                  1     1.0      1   
Adventure Drama     War                        1     1.0      1   
                    Fantasy                    1     1.0      1   
          Comedy    Drama                      1     1.0      1   
          Biography Drama                      1     1.0      1   
Action    Sci-Fi    Thriller                   1     1.0      1   
          Mystery   Thriller                   1     1.0      1   
          Drama     Sport                      1     1.0      1   
          Crime     Drama                      1     1.0      1   
          Adventure Thriller                   1     1.0      1   
                    Fantasy                    1     1.0      1   
Drama     Romance   Sci-Fi                     1     1.0      1   

                               Revenue (Millions)  Metascore  
Genre1    Genre2    Genre3                                    
Action    Adventure Sci-Fi                    5.0        5.0  
Animation Adventure Comedy                    4.0        4.0  
Crime     Drama     Mystery                   2.0        2.0  
Adventure Drama     Sci-Fi                    2.0        2.0  
Biography Drama     History                   2.0        2.0  
Drama     Mystery   Sci-Fi                    2.0        2.0  
Action    Biography Drama                     2.0        2.0  
Drama     Mystery   Romance                   2.0        2.0  
Crime     Drama     Thriller                  2.0        2.0  
Comedy    Drama     Music                     2.0        2.0  
Adventure Drama     Thriller                  2.0        2.0  
Biography Drama     Thriller                  1.0        1.0  
Comedy    Drama     Romance                   1.0        1.0  
Action    Adventure Comedy                    1.0        1.0  
Comedy    Drama     Thriller                  1.0        1.0  
Crime     Drama     History                   1.0        1.0  
Biography Comedy    Crime                     1.0        1.0  
Drama     Family    Music                     1.0        1.0  
          Fantasy   War                       1.0        1.0  
          Mystery   War                       1.0        1.0  
Biography Comedy    Drama                     1.0        1.0  
Animation Adventure Family                    1.0        1.0  
          Drama     Fantasy                   1.0        1.0  
          Comedy    Family                    1.0        1.0  
Action    Adventure Drama                     1.0        1.0  
Animation Action    Adventure                 1.0        1.0  
Adventure Drama     War                       1.0        1.0  
                    Fantasy                   1.0        1.0  
          Comedy    Drama                     1.0        1.0  
          Biography Drama                     1.0        1.0  
Action    Sci-Fi    Thriller                  1.0        1.0  
          Mystery   Thriller                  1.0        1.0  
          Drama     Sport                     1.0        1.0  
          Crime     Drama                     1.0        1.0  
          Adventure Thriller                  1.0        1.0  
                    Fantasy                   1.0        1.0  
Drama     Romance   Sci-Fi                    1.0        1.0  
------------------------------------------------

topdir=top250.groupby('Director')
print(topdir.agg(np.size).sort_values(by='Year',ascending=False))
-----------------------------------------------------
OUTPUT:
                                  Rank  Title  Genre1  Genre2  Genre3  \
Director                                                                
Christopher Nolan                    5      5       5       5       5   
Denis Villeneuve                     3      3       3       3       3   
Martin Scorsese                      3      3       3       3       3   
Quentin Tarantino                    2      2       2       2       2   
Pete Docter                          2      2       2       2       2   
Damien Chazelle                      2      2       2       2       2   
J.J. Abrams                          2      2       2       2       2   
Rajkumar Hirani                      2      2       2       2       2   
Neill Blomkamp                       1      1       1       1       1   
Ridley Scott                         1      1       1       1       1   
Morten Tyldum                        1      1       1       1       1   
Nitesh Tiwari                        1      1       1       1       1   
Olivier Nakache                      1      1       1       1       1   
Paul Greengrass                      1      1       1       1       1   
Paul Thomas Anderson                 1      1       1       1       1   
Mel Gibson                           1      1       1       1       1   
Martin Campbell                      1      1       1       1       1   
Aamir Khan                           1      1       1       1       1   
Lenny Abrahamson                     1      1       1       1       1   
Ron Howard                           1      1       1       1       1   
S.S. Rajamouli                       1      1       1       1       1   
Sean Penn                            1      1       1       1       1   
Spike Jonze                          1      1       1       1       1   
Stephen Chbosky                      1      1       1       1       1   
Steve McQueen                        1      1       1       1       1   
Tate Taylor                          1      1       1       1       1   
Thomas Vinterberg                    1      1       1       1       1   
Tim Miller                           1      1       1       1       1   
Tom Hooper                           1      1       1       1       1   
Tom McCarthy                         1      1       1       1       1   
                               ...    ...     ...     ...     ...   
Makoto Shinkai                       1      1       1       1       1   
Juan José Campanella                 1      1       1       1       1   
Lee Unkrich                          1      1       1       1       1   
Lasse Hallström                      1      1       1       1       1   
Andrew Stanton                       1      1       1       1       1   
Brad Bird                            1      1       1       1       1   
Bryan Singer                         1      1       1       1       1   
Byron Howard                         1      1       1       1       1   
Chan-wook Park                       1      1       1       1       1   
Clint Eastwood                       1      1       1       1       1   
Damián Szifron                       1      1       1       1       1   
Danny Boyle                          1      1       1       1       1   
Darren Aronofsky                     1      1       1       1       1   
David Fincher                        1      1       1       1       1   
David Yates                          1      1       1       1       1   
Dean DeBlois                         1      1       1       1       1   
Edward Zwick                         1      1       1       1       1   
Ethan Coen                           1      1       1       1       1   
Florian Henckel von Donnersmarck     1      1       1       1       1   
Gabriele Muccino                     1      1       1       1       1   
Garth Davis                          1      1       1       1       1   
Gavin O'Connor                       1      1       1       1       1   
George Miller                        1      1       1       1       1   
Guillermo del Toro                   1      1       1       1       1   
James Gunn                           1      1       1       1       1   
Jean-Marc Vallée                     1      1       1       1       1   
John Carney                          1      1       1       1       1   
Joss Whedon                          1      1       1       1       1   
Alejandro González Iñárritu          1      1       1       1       1   
Xavier Dolan                         1      1       1       1       1   

                                  Description  Actors1  Actors2  Actors3  \
Director                                                                   
Christopher Nolan                           5        5        5        5   
Denis Villeneuve                            3        3        3        3   
Martin Scorsese                             3        3        3        3   
Quentin Tarantino                           2        2        2        2   
Pete Docter                                 2        2        2        2   
Damien Chazelle                             2        2        2        2   
J.J. Abrams                                 2        2        2        2   
Rajkumar Hirani                             2        2        2        2   
Neill Blomkamp                              1        1        1        1   
Ridley Scott                                1        1        1        1   
Morten Tyldum                               1        1        1        1   
Nitesh Tiwari                               1        1        1        1   
Olivier Nakache                             1        1        1        1   
Paul Greengrass                             1        1        1        1   
Paul Thomas Anderson                        1        1        1        1   
Mel Gibson                                  1        1        1        1   
Martin Campbell                             1        1        1        1   
Aamir Khan                                  1        1        1        1   
Lenny Abrahamson                            1        1        1        1   
Ron Howard                                  1        1        1        1   
S.S. Rajamouli                              1        1        1        1   
Sean Penn                                   1        1        1        1   
Spike Jonze                                 1        1        1        1   
Stephen Chbosky                             1        1        1        1   
Steve McQueen                               1        1        1        1   
Tate Taylor                                 1        1        1        1   
Thomas Vinterberg                           1        1        1        1   
Tim Miller                                  1        1        1        1   
Tom Hooper                                  1        1        1        1   
Tom McCarthy                                1        1        1        1   
                                      ...      ...      ...      ...   
Makoto Shinkai                              1        1        1        1   
Juan José Campanella                        1        1        1        1   
Lee Unkrich                                 1        1        1        1   
Lasse Hallström                             1        1        1        1   
Andrew Stanton                              1        1        1        1   
Brad Bird                                   1        1        1        1   
Bryan Singer                                1        1        1        1   
Byron Howard                                1        1        1        1   
Chan-wook Park                              1        1        1        1   
Clint Eastwood                              1        1        1        1   
Damián Szifron                              1        1        1        1   
Danny Boyle                                 1        1        1        1   
Darren Aronofsky                            1        1        1        1   
David Fincher                               1        1        1        1   
David Yates                                 1        1        1        1   
Dean DeBlois                                1        1        1        1   
Edward Zwick                                1        1        1        1   
Ethan Coen                                  1        1        1        1   
Florian Henckel von Donnersmarck            1        1        1        1   
Gabriele Muccino                            1        1        1        1   
Garth Davis                                 1        1        1        1   
Gavin O'Connor                              1        1        1        1   
George Miller                               1        1        1        1   
Guillermo del Toro                          1        1        1        1   
James Gunn                                  1        1        1        1   
Jean-Marc Vallée                            1        1        1        1   
John Carney                                 1        1        1        1   
Joss Whedon                                 1        1        1        1   
Alejandro González Iñárritu                 1        1        1        1   
Xavier Dolan                                1        1        1        1   

                                  Actors4  Year  Runtime (Minutes)  Rating  \
Director                                                                     
Christopher Nolan                       5     5                  5     5.0   
Denis Villeneuve                        3     3                  3     3.0   
Martin Scorsese                         3     3                  3     3.0   
Quentin Tarantino                       2     2                  2     2.0   
Pete Docter                             2     2                  2     2.0   
Damien Chazelle                         2     2                  2     2.0   
J.J. Abrams                             2     2                  2     2.0   
Rajkumar Hirani                         2     2                  2     2.0   
Neill Blomkamp                          1     1                  1     1.0   
Ridley Scott                            1     1                  1     1.0   
Morten Tyldum                           1     1                  1     1.0   
Nitesh Tiwari                           1     1                  1     1.0   
Olivier Nakache                         1     1                  1     1.0   
Paul Greengrass                         1     1                  1     1.0   
Paul Thomas Anderson                    1     1                  1     1.0   
Mel Gibson                              1     1                  1     1.0   
Martin Campbell                         1     1                  1     1.0   
Aamir Khan                              1     1                  1     1.0   
Lenny Abrahamson                        1     1                  1     1.0   
Ron Howard                              1     1                  1     1.0   
S.S. Rajamouli                          1     1                  1     1.0   
Sean Penn                               1     1                  1     1.0   
Spike Jonze                             1     1                  1     1.0   
Stephen Chbosky                         1     1                  1     1.0   
Steve McQueen                           1     1                  1     1.0   
Tate Taylor                             1     1                  1     1.0   
Thomas Vinterberg                       1     1                  1     1.0   
Tim Miller                              1     1                  1     1.0   
Tom Hooper                              1     1                  1     1.0   
Tom McCarthy                            1     1                  1     1.0   
                                  ...   ...                ...     ...   
Makoto Shinkai                          1     1                  1     1.0   
Juan José Campanella                    1     1                  1     1.0   
Lee Unkrich                             1     1                  1     1.0   
Lasse Hallström                         1     1                  1     1.0   
Andrew Stanton                          1     1                  1     1.0   
Brad Bird                               1     1                  1     1.0   
Bryan Singer                            1     1                  1     1.0   
Byron Howard                            1     1                  1     1.0   
Chan-wook Park                          1     1                  1     1.0   
Clint Eastwood                          1     1                  1     1.0   
Damián Szifron                          1     1                  1     1.0   
Danny Boyle                             1     1                  1     1.0   
Darren Aronofsky                        1     1                  1     1.0   
David Fincher                           1     1                  1     1.0   
David Yates                             1     1                  1     1.0   
Dean DeBlois                            1     1                  1     1.0   
Edward Zwick                            1     1                  1     1.0   
Ethan Coen                              1     1                  1     1.0   
Florian Henckel von Donnersmarck        1     1                  1     1.0   
Gabriele Muccino                        1     1                  1     1.0   
Garth Davis                             1     1                  1     1.0   
Gavin O'Connor                          1     1                  1     1.0   
George Miller                           1     1                  1     1.0   
Guillermo del Toro                      1     1                  1     1.0   
James Gunn                              1     1                  1     1.0   
Jean-Marc Vallée                        1     1                  1     1.0   
John Carney                             1     1                  1     1.0   
Joss Whedon                             1     1                  1     1.0   
Alejandro González Iñárritu             1     1                  1     1.0   
Xavier Dolan                            1     1                  1     1.0   

                                  Votes  Revenue (Millions)  Metascore  
Director                                                                
Christopher Nolan                     5                 5.0        5.0  
Denis Villeneuve                      3                 3.0        3.0  
Martin Scorsese                       3                 3.0        3.0  
Quentin Tarantino                     2                 2.0        2.0  
Pete Docter                           2                 2.0        2.0  
Damien Chazelle                       2                 2.0        2.0  
J.J. Abrams                           2                 2.0        2.0  
Rajkumar Hirani                       2                 2.0        2.0  
Neill Blomkamp                        1                 1.0        1.0  
Ridley Scott                          1                 1.0        1.0  
Morten Tyldum                         1                 1.0        1.0  
Nitesh Tiwari                         1                 1.0        1.0  
Olivier Nakache                       1                 1.0        1.0  
Paul Greengrass                       1                 1.0        1.0  
Paul Thomas Anderson                  1                 1.0        1.0  
Mel Gibson                            1                 1.0        1.0  
Martin Campbell                       1                 1.0        1.0  
Aamir Khan                            1                 1.0        1.0  
Lenny Abrahamson                      1                 1.0        1.0  
Ron Howard                            1                 1.0        1.0  
S.S. Rajamouli                        1                 1.0        1.0  
Sean Penn                             1                 1.0        1.0  
Spike Jonze                           1                 1.0        1.0  
Stephen Chbosky                       1                 1.0        1.0  
Steve McQueen                         1                 1.0        1.0  
Tate Taylor                           1                 1.0        1.0  
Thomas Vinterberg                     1                 1.0        1.0  
Tim Miller                            1                 1.0        1.0  
Tom Hooper                            1                 1.0        1.0  
Tom McCarthy                          1                 1.0        1.0  
                                ...                 ...        ...  
Makoto Shinkai                        1                 1.0        1.0  
Juan José Campanella                  1                 1.0        1.0  
Lee Unkrich                           1                 1.0        1.0  
Lasse Hallström                       1                 1.0        1.0  
Andrew Stanton                        1                 1.0        1.0  
Brad Bird                             1                 1.0        1.0  
Bryan Singer                          1                 1.0        1.0  
Byron Howard                          1                 1.0        1.0  
Chan-wook Park                        1                 1.0        1.0  
Clint Eastwood                        1                 1.0        1.0  
Damián Szifron                        1                 1.0        1.0  
Danny Boyle                           1                 1.0        1.0  
Darren Aronofsky                      1                 1.0        1.0  
David Fincher                         1                 1.0        1.0  
David Yates                           1                 1.0        1.0  
Dean DeBlois                          1                 1.0        1.0  
Edward Zwick                          1                 1.0        1.0  
Ethan Coen                            1                 1.0        1.0  
Florian Henckel von Donnersmarck      1                 1.0        1.0  
Gabriele Muccino                      1                 1.0        1.0  
Garth Davis                           1                 1.0        1.0  
Gavin O'Connor                        1                 1.0        1.0  
George Miller                         1                 1.0        1.0  
Guillermo del Toro                    1                 1.0        1.0  
James Gunn                            1                 1.0        1.0  
Jean-Marc Vallée                      1                 1.0        1.0  
John Carney                           1                 1.0        1.0  
Joss Whedon                           1                 1.0        1.0  
Alejandro González Iñárritu           1                 1.0        1.0  
Xavier Dolan                          1                 1.0        1.0  

[61 rows x 16 columns]
-------------------------------------
                      Rank  Title  Genre1  Genre2  Genre3  Description  \
Actors1                                                                  
Leonardo DiCaprio        6      6       6       6       6            6   
Aamir Khan               3      3       3       3       3            3   
Christian Bale           3      3       3       3       3            3   
Tom Hardy                2      2       2       2       2            2   
Dev Patel                2      2       2       2       2            2   
Matt Damon               2      2       2       2       2            2   
Matthew McConaughey      2      2       2       2       2            2   
Natalie Portman          1      1       1       1       1            1   
Jay Baruchel             1      1       1       1       1            1   
Joaquin Phoenix          1      1       1       1       1            1   
Logan Lerman             1      1       1       1       1            1   
Lubna Azabal             1      1       1       1       1            1   
Mads Mikkelsen           1      1       1       1       1            1   
Mark Ruffalo             1      1       1       1       1            1   
Miles Teller             1      1       1       1       1            1   
Min-hee Kim              1      1       1       1       1            1   
Prabhas                  1      1       1       1       1            1   
Patrick Stewart          1      1       1       1       1            1   
Ivana Baquero            1      1       1       1       1            1   
Ralph Fiennes            1      1       1       1       1            1   
Ricardo Darín            1      1       1       1       1            1   
Richard Gere             1      1       1       1       1            1   
Robert Downey Jr.        1      1       1       1       1            1   
Ryan Gosling             1      1       1       1       1            1   
Ryan Reynolds            1      1       1       1       1            1   
Ryûnosuke Kamiki         1      1       1       1       1            1   
Sharlto Copley           1      1       1       1       1            1   
Tom Hanks                1      1       1       1       1            1   
Tommy Lee Jones          1      1       1       1       1            1   
Ulrich Mühe              1      1       1       1       1            1   
                   ...    ...     ...     ...     ...          ...   
Ginnifer Goodwin         1      1       1       1       1            1   
Hugh Jackman             1      1       1       1       1            1   
Clint Eastwood           1      1       1       1       1            1   
Amy Poehler              1      1       1       1       1            1   
Andrew Garfield          1      1       1       1       1            1   
Anne Dorval              1      1       1       1       1            1   
Ben Affleck              1      1       1       1       1            1   
Ben Burtt                1      1       1       1       1            1   
Benedict Cumberbatch     1      1       1       1       1            1   
Brad Garrett             1      1       1       1       1            1   
Brad Pitt                1      1       1       1       1            1   
Brie Larson              1      1       1       1       1            1   
Chiwetel Ejiofor         1      1       1       1       1            1   
Chris Pine               1      1       1       1       1            1   
Chris Pratt              1      1       1       1       1            1   
Colin Firth              1      1       1       1       1            1   
Amy Adams                1      1       1       1       1            1   
Daisy Ridley             1      1       1       1       1            1   
Daniel Brühl             1      1       1       1       1            1   
Daniel Craig             1      1       1       1       1            1   
Daniel Day-Lewis         1      1       1       1       1            1   
Daniel Radcliffe         1      1       1       1       1            1   
Darsheel Safary          1      1       1       1       1            1   
Darío Grandinetti        1      1       1       1       1            1   
Edward Asner             1      1       1       1       1            1   
Emile Hirsch             1      1       1       1       1            1   
Emma Stone               1      1       1       1       1            1   
Ferdia Walsh-Peelo       1      1       1       1       1            1   
François Cluzet          1      1       1       1       1            1   
Will Smith               1      1       1       1       1            1   

                      Director  Actors2  Actors3  Actors4  Year  \
Actors1                                                           
Leonardo DiCaprio            6        6        6        6     6   
Aamir Khan                   3        3        3        3     3   
Christian Bale               3        3        3        3     3   
Tom Hardy                    2        2        2        2     2   
Dev Patel                    2        2        2        2     2   
Matt Damon                   2        2        2        2     2   
Matthew McConaughey          2        2        2        2     2   
Natalie Portman              1        1        1        1     1   
Jay Baruchel                 1        1        1        1     1   
Joaquin Phoenix              1        1        1        1     1   
Logan Lerman                 1        1        1        1     1   
Lubna Azabal                 1        1        1        1     1   
Mads Mikkelsen               1        1        1        1     1   
Mark Ruffalo                 1        1        1        1     1   
Miles Teller                 1        1        1        1     1   
Min-hee Kim                  1        1        1        1     1   
Prabhas                      1        1        1        1     1   
Patrick Stewart              1        1        1        1     1   
Ivana Baquero                1        1        1        1     1   
Ralph Fiennes                1        1        1        1     1   
Ricardo Darín                1        1        1        1     1   
Richard Gere                 1        1        1        1     1   
Robert Downey Jr.            1        1        1        1     1   
Ryan Gosling                 1        1        1        1     1   
Ryan Reynolds                1        1        1        1     1   
Ryûnosuke Kamiki             1        1        1        1     1   
Sharlto Copley               1        1        1        1     1   
Tom Hanks                    1        1        1        1     1   
Tommy Lee Jones              1        1        1        1     1   
Ulrich Mühe                  1        1        1        1     1   
                       ...      ...      ...      ...   ...   
Ginnifer Goodwin             1        1        1        1     1   
Hugh Jackman                 1        1        1        1     1   
Clint Eastwood               1        1        1        1     1   
Amy Poehler                  1        1        1        1     1   
Andrew Garfield              1        1        1        1     1   
Anne Dorval                  1        1        1        1     1   
Ben Affleck                  1        1        1        1     1   
Ben Burtt                    1        1        1        1     1   
Benedict Cumberbatch         1        1        1        1     1   
Brad Garrett                 1        1        1        1     1   
Brad Pitt                    1        1        1        1     1   
Brie Larson                  1        1        1        1     1   
Chiwetel Ejiofor             1        1        1        1     1   
Chris Pine                   1        1        1        1     1   
Chris Pratt                  1        1        1        1     1   
Colin Firth                  1        1        1        1     1   
Amy Adams                    1        1        1        1     1   
Daisy Ridley                 1        1        1        1     1   
Daniel Brühl                 1        1        1        1     1   
Daniel Craig                 1        1        1        1     1   
Daniel Day-Lewis             1        1        1        1     1   
Daniel Radcliffe             1        1        1        1     1   
Darsheel Safary              1        1        1        1     1   
Darío Grandinetti            1        1        1        1     1   
Edward Asner                 1        1        1        1     1   
Emile Hirsch                 1        1        1        1     1   
Emma Stone                   1        1        1        1     1   
Ferdia Walsh-Peelo           1        1        1        1     1   
François Cluzet              1        1        1        1     1   
Will Smith                   1        1        1        1     1   

                      Runtime (Minutes)  Rating  Votes  Revenue (Millions)  \
Actors1                                                                      
Leonardo DiCaprio                     6     6.0      6                 6.0   
Aamir Khan                            3     3.0      3                 3.0   
Christian Bale                        3     3.0      3                 3.0   
Tom Hardy                             2     2.0      2                 2.0   
Dev Patel                             2     2.0      2                 2.0   
Matt Damon                            2     2.0      2                 2.0   
Matthew McConaughey                   2     2.0      2                 2.0   
Natalie Portman                       1     1.0      1                 1.0   
Jay Baruchel                          1     1.0      1                 1.0   
Joaquin Phoenix                       1     1.0      1                 1.0   
Logan Lerman                          1     1.0      1                 1.0   
Lubna Azabal                          1     1.0      1                 1.0   
Mads Mikkelsen                        1     1.0      1                 1.0   
Mark Ruffalo                          1     1.0      1                 1.0   
Miles Teller                          1     1.0      1                 1.0   
Min-hee Kim                           1     1.0      1                 1.0   
Prabhas                               1     1.0      1                 1.0   
Patrick Stewart                       1     1.0      1                 1.0   
Ivana Baquero                         1     1.0      1                 1.0   
Ralph Fiennes                         1     1.0      1                 1.0   
Ricardo Darín                         1     1.0      1                 1.0   
Richard Gere                          1     1.0      1                 1.0   
Robert Downey Jr.                     1     1.0      1                 1.0   
Ryan Gosling                          1     1.0      1                 1.0   
Ryan Reynolds                         1     1.0      1                 1.0   
Ryûnosuke Kamiki                      1     1.0      1                 1.0   
Sharlto Copley                        1     1.0      1                 1.0   
Tom Hanks                             1     1.0      1                 1.0   
Tommy Lee Jones                       1     1.0      1                 1.0   
Ulrich Mühe                           1     1.0      1                 1.0   
                                ...     ...    ...                 ...   
Ginnifer Goodwin                      1     1.0      1                 1.0   
Hugh Jackman                          1     1.0      1                 1.0   
Clint Eastwood                        1     1.0      1                 1.0   
Amy Poehler                           1     1.0      1                 1.0   
Andrew Garfield                       1     1.0      1                 1.0   
Anne Dorval                           1     1.0      1                 1.0   
Ben Affleck                           1     1.0      1                 1.0   
Ben Burtt                             1     1.0      1                 1.0   
Benedict Cumberbatch                  1     1.0      1                 1.0   
Brad Garrett                          1     1.0      1                 1.0   
Brad Pitt                             1     1.0      1                 1.0   
Brie Larson                           1     1.0      1                 1.0   
Chiwetel Ejiofor                      1     1.0      1                 1.0   
Chris Pine                            1     1.0      1                 1.0   
Chris Pratt                           1     1.0      1                 1.0   
Colin Firth                           1     1.0      1                 1.0   
Amy Adams                             1     1.0      1                 1.0   
Daisy Ridley                          1     1.0      1                 1.0   
Daniel Brühl                          1     1.0      1                 1.0   
Daniel Craig                          1     1.0      1                 1.0   
Daniel Day-Lewis                      1     1.0      1                 1.0   
Daniel Radcliffe                      1     1.0      1                 1.0   
Darsheel Safary                       1     1.0      1                 1.0   
Darío Grandinetti                     1     1.0      1                 1.0   
Edward Asner                          1     1.0      1                 1.0   
Emile Hirsch                          1     1.0      1                 1.0   
Emma Stone                            1     1.0      1                 1.0   
Ferdia Walsh-Peelo                    1     1.0      1                 1.0   
François Cluzet                       1     1.0      1                 1.0   
Will Smith                            1     1.0      1                 1.0   

                      Metascore  
Actors1                          
Leonardo DiCaprio           6.0  
Aamir Khan                  3.0  
Christian Bale              3.0  
Tom Hardy                   2.0  
Dev Patel                   2.0  
Matt Damon                  2.0  
Matthew McConaughey         2.0  
Natalie Portman             1.0  
Jay Baruchel                1.0  
Joaquin Phoenix             1.0  
Logan Lerman                1.0  
Lubna Azabal                1.0  
Mads Mikkelsen              1.0  
Mark Ruffalo                1.0  
Miles Teller                1.0  
Min-hee Kim                 1.0  
Prabhas                     1.0  
Patrick Stewart             1.0  
Ivana Baquero               1.0  
Ralph Fiennes               1.0  
Ricardo Darín               1.0  
Richard Gere                1.0  
Robert Downey Jr.           1.0  
Ryan Gosling                1.0  
Ryan Reynolds               1.0  
Ryûnosuke Kamiki            1.0  
Sharlto Copley              1.0  
Tom Hanks                   1.0  
Tommy Lee Jones             1.0  
Ulrich Mühe                 1.0  
                        ...  
Ginnifer Goodwin            1.0  
Hugh Jackman                1.0  
Clint Eastwood              1.0  
Amy Poehler                 1.0  
Andrew Garfield             1.0  
Anne Dorval                 1.0  
Ben Affleck                 1.0  
Ben Burtt                   1.0  
Benedict Cumberbatch        1.0  
Brad Garrett                1.0  
Brad Pitt                   1.0  
Brie Larson                 1.0  
Chiwetel Ejiofor            1.0  
Chris Pine                  1.0  
Chris Pratt                 1.0  
Colin Firth                 1.0  
Amy Adams                   1.0  
Daisy Ridley                1.0  
Daniel Brühl                1.0  
Daniel Craig                1.0  
Daniel Day-Lewis            1.0  
Daniel Radcliffe            1.0  
Darsheel Safary             1.0  
Darío Grandinetti           1.0  
Edward Asner                1.0  
Emile Hirsch                1.0  
Emma Stone                  1.0  
Ferdia Walsh-Peelo          1.0  
François Cluzet             1.0  
Will Smith                  1.0  

------------------------------------------

  
topact=top250.groupby('Actors1')
print(topact.agg(np.size).sort_values(by='Year',ascending=False))


#---Stats regarding relations between metascore, rating,revenue, runtime
metrating=movie[(movie['Metascore']>=70)&(movie['Rating']>=8.0)]
metgrp=metrating.groupby(['Metascore','Rating'])
print(metgrp.agg(np.size).sort_values(by='Year',ascending=False))

----------------------------------------
OUTPUT:
 
                  Rank  Title  Genre1  Genre2  Genre3  Description  Director  \
Metascore Rating                                                               
74.0      8.1        3      3       3       3       3            3         3   
71.0      8.2        2      2       2       2       2            2         2   
79.0      8.0        2      2       2       2       2            2         2   
73.0      8.1        2      2       2       2       2            2         2   
81.0      8.0        2      2       2       2       2            2         2   
80.0      8.2        2      2       2       2       2            2         2   
          8.0        2      2       2       2       2            2         2   
85.0      8.5        1      1       1       1       1            1         1   
86.0      8.0        1      1       1       1       1            1         1   
          8.2        1      1       1       1       1            1         1   
87.0      8.1        1      1       1       1       1            1         1   
88.0      8.0        1      1       1       1       1            1         1   
          8.1        1      1       1       1       1            1         1   
          8.3        1      1       1       1       1            1         1   
          8.5        1      1       1       1       1            1         1   
89.0      8.5        1      1       1       1       1            1         1   
85.0      8.0        1      1       1       1       1            1         1   
90.0      8.0        1      1       1       1       1            1         1   
          8.1        1      1       1       1       1            1         1   
91.0      8.1        1      1       1       1       1            1         1   
92.0      8.1        1      1       1       1       1            1         1   
          8.3        1      1       1       1       1            1         1   
93.0      8.1        1      1       1       1       1            1         1   
          8.3        1      1       1       1       1            1         1   
94.0      8.2        1      1       1       1       1            1         1   
96.0      8.0        1      1       1       1       1            1         1   
          8.1        1      1       1       1       1            1         1   
85.0      8.1        1      1       1       1       1            1         1   
82.0      9.0        1      1       1       1       1            1         1   
84.0      8.1        1      1       1       1       1            1         1   
77.0      8.1        1      1       1       1       1            1         1   
74.0      8.0        1      1       1       1       1            1         1   
          8.6        1      1       1       1       1            1         1   
          8.8        1      1       1       1       1            1         1   
75.0      8.1        1      1       1       1       1            1         1   
          8.2        1      1       1       1       1            1         1   
76.0      8.0        1      1       1       1       1            1         1   
          8.1        1      1       1       1       1            1         1   
          8.3        1      1       1       1       1            1         1   
78.0      8.1        1      1       1       1       1            1         1   
84.0      8.0        1      1       1       1       1            1         1   
78.0      8.5        1      1       1       1       1            1         1   
79.0      8.1        1      1       1       1       1            1         1   
          8.6        1      1       1       1       1            1         1   
80.0      8.4        1      1       1       1       1            1         1   
81.0      8.1        1      1       1       1       1            1         1   
          8.4        1      1       1       1       1            1         1   
82.0      8.0        1      1       1       1       1            1         1   
71.0      8.3        1      1       1       1       1            1         1   
98.0      8.2        1      1       1       1       1            1         1   

                  Actors1  Actors2  Actors3  Actors4  Year  Runtime (Minutes)  \
Metascore Rating                                                                
74.0      8.1           3        3        3        3     3                  3   
71.0      8.2           2        2        2        2     2                  2   
79.0      8.0           2        2        2        2     2                  2   
73.0      8.1           2        2        2        2     2                  2   
81.0      8.0           2        2        2        2     2                  2   
80.0      8.2           2        2        2        2     2                  2   
          8.0           2        2        2        2     2                  2   
85.0      8.5           1        1        1        1     1                  1   
86.0      8.0           1        1        1        1     1                  1   
          8.2           1        1        1        1     1                  1   
87.0      8.1           1        1        1        1     1                  1   
88.0      8.0           1        1        1        1     1                  1   
          8.1           1        1        1        1     1                  1   
          8.3           1        1        1        1     1                  1   
          8.5           1        1        1        1     1                  1   
89.0      8.5           1        1        1        1     1                  1   
85.0      8.0           1        1        1        1     1                  1   
90.0      8.0           1        1        1        1     1                  1   
          8.1           1        1        1        1     1                  1   
91.0      8.1           1        1        1        1     1                  1   
92.0      8.1           1        1        1        1     1                  1   
          8.3           1        1        1        1     1                  1   
93.0      8.1           1        1        1        1     1                  1   
          8.3           1        1        1        1     1                  1   
94.0      8.2           1        1        1        1     1                  1   
96.0      8.0           1        1        1        1     1                  1   
          8.1           1        1        1        1     1                  1   
85.0      8.1           1        1        1        1     1                  1   
82.0      9.0           1        1        1        1     1                  1   
84.0      8.1           1        1        1        1     1                  1   
77.0      8.1           1        1        1        1     1                  1   
74.0      8.0           1        1        1        1     1                  1   
          8.6           1        1        1        1     1                  1   
          8.8           1        1        1        1     1                  1   
75.0      8.1           1        1        1        1     1                  1   
          8.2           1        1        1        1     1                  1   
76.0      8.0           1        1        1        1     1                  1   
          8.1           1        1        1        1     1                  1   
          8.3           1        1        1        1     1                  1   
78.0      8.1           1        1        1        1     1                  1   
84.0      8.0           1        1        1        1     1                  1   
78.0      8.5           1        1        1        1     1                  1   
79.0      8.1           1        1        1        1     1                  1   
          8.6           1        1        1        1     1                  1   
80.0      8.4           1        1        1        1     1                  1   
81.0      8.1           1        1        1        1     1                  1   
          8.4           1        1        1        1     1                  1   
82.0      8.0           1        1        1        1     1                  1   
71.0      8.3           1        1        1        1     1                  1   
98.0      8.2           1        1        1        1     1                  1   

                  Votes  Revenue (Millions)  
Metascore Rating                             
74.0      8.1         3                 3.0  
71.0      8.2         2                 2.0  
79.0      8.0         2                 2.0  
73.0      8.1         2                 2.0  
81.0      8.0         2                 2.0  
80.0      8.2         2                 2.0  
          8.0         2                 2.0  
85.0      8.5         1                 1.0  
86.0      8.0         1                 1.0  
          8.2         1                 1.0  
87.0      8.1         1                 1.0  
88.0      8.0         1                 1.0  
          8.1         1                 1.0  
          8.3         1                 1.0  
          8.5         1                 1.0  
89.0      8.5         1                 1.0  
85.0      8.0         1                 1.0  
90.0      8.0         1                 1.0  
          8.1         1                 1.0  
91.0      8.1         1                 1.0  
92.0      8.1         1                 1.0  
          8.3         1                 1.0  
93.0      8.1         1                 1.0  
          8.3         1                 1.0  
94.0      8.2         1                 1.0  
96.0      8.0         1                 1.0  
          8.1         1                 1.0  
85.0      8.1         1                 1.0  
82.0      9.0         1                 1.0  
84.0      8.1         1                 1.0  
77.0      8.1         1                 1.0  
74.0      8.0         1                 1.0  
          8.6         1                 1.0  
          8.8         1                 1.0  
75.0      8.1         1                 1.0  
          8.2         1                 1.0  
76.0      8.0         1                 1.0  
          8.1         1                 1.0  
          8.3         1                 1.0  
78.0      8.1         1                 1.0  
84.0      8.0         1                 1.0  
78.0      8.5         1                 1.0  
79.0      8.1         1                 1.0  
          8.6         1                 1.0  
80.0      8.4         1                 1.0  
81.0      8.1         1                 1.0  
          8.4         1                 1.0  
82.0      8.0         1                 1.0  
71.0      8.3         1                 1.0  
98.0      8.2         1                 1.0  
---------------------------------------------

