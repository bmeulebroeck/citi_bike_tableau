# NYC CitiBike Analysis

<h3>Data gathering and analysis</h3>
<p>The task given was to explore the available ride data from NYC's CitiBike bikeshare program to identify interesting phenomena that could be visualized via Tableau.</p>

<p>The first step was to explore the data and determine a time frame to evaluate. My initial thought was to get a few years worth of data, starting in 2018, in order to see two full years of trends prior to the impact of COVID-19 in early 2020.</p> 

<p>The data is available in monthly CSV files that contain information on each unique ride during that month (start/end time, start/end stations with details, gender, user type). I downloaded all the files from January 2018 through December 2020. Upon downloading I realized how extensive these files are due to the popularity of the CitiBike program in NYC. On the low end was around 700k rides, and the high end was around 2.5 million rides.</p>

<p>I used a python script to combine the monthly CSVs into yearly files for 2018, 2019, and 2020. These files combined were just over 10GB, which I knew would present problems when I loaded into Tableau. I decided to focus my analysis on just the peak season of 2020, from February through the end of October.</p>

<h3>Tableau Visuals and Analysis</h3>
</p>I began with the station map. I decided to populate the map with the trip start stations, and then used size to indicate how many rides started from each station, and used color to give an indicator of average trip duration in minutes (calculated field) from those stations. I also set up bar charts showing the most popular stations to start and end a trip. As expected the most popular stations are located in lower Manhattan in the commercial core of New York City.</p>

<p>I pulled the map and charts into a dashboard for the story presentation. I set up the starting station bar chart to highlight a station's location on the map to make them easier to locate. When an ending station is selected, the map updates to show where rides ending at that station originated. This gives an idea of how bikes are used in different parts of the city, whether for short neighborhood trips or sight-seeing or for commuiting from the residential borroughs into the commercial part of Manhattan.</p>

<p>Next I built some visuals around the demographics of the riders. I set up groups for gender and for age to enable me to build charts more effectively. Through these charts I found that just over half of riders are between age 26 to 45, and the majority are male. Interesting to note that the age group 46 to 55 had the largeset number of rides without a known gender by a substantial amount versus other age groups. Further analysis would be required to determine what is causing the numbers to be much higher in that age group.</p> 

<p>In looking at gender, age, and subscriber type I found a few items of note. First is that the average ride duration for customers is almost double the average ride duration for subscribers. This suggests that customers and perhaps using the bikes for casual exploration and sightseeing, as opposed to subscribers who are likely using them to commute or complete errands. I also looked at the hour of start time and found that subscribers peak during commute times - 8am and 5pm - while customers slowly ramp up through the morning and early afternoon to one peak around 5-6pm.</p>