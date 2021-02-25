# NYC CitiBike Analysis

View this analysis on my Tableau [public profile](https://public.tableau.com/profile/brent.meulebroeck#!/vizhome/CitiBikeAnalysis_16141174853830/AlookatNYCridershipduringthe2020peakseasonFebruarythruOctober)

### Overview of rides during 2020 peak biking season (February through October)
![Rides by week](/screenshots/rides_by_week.PNG)
I chose this time period to see how the COVID-19 restrictions impacted overall ridership, as well as looking at different segments of the ridership for insights.

The biking season was off to a great start in February, but as the COVID-19 pandemic took hold restrictions began to be put in place in mid-March. Ridership plummets rapidly to about 1/3 of what is was during the first week of March. As the spring and summer go on the ridership gradually improves and by mid-July has surpassed the early March peak.

![Who is Riding?](/screenshots/who_is_riding.PNG)
Next I brought in some of the demographic information attached to each ride, such as gender, age, and user type (subscriber or customer). Subscribers are annual pass holders, while customers purchase either 24-hour or 3-day passes.

On the bar chart you can see that the average duration of a customer ride is almost double that of a subscriber. This is likely because the customers are short-term users (such as visitors or tourists) who are sightseeing or exploring the city. Subscribers are more likely to be commuters or locals who are running errands.

Also of note is the starting time of rides by subscribers vs. customers. Subscribers have peaks during typical commute times - around 8am and 5pm. Customers have a more gradual increase as the day goes on, peaking around 5-6pm. This fits with them being the more casual users of the CitiBike service.

![Rides by Age and Gender](/screenshots/rides_by_age_and_gender.PNG)
To identify trends in the ages and genders I put them all in a matrix. As expected, the 26-35 age range has the highest number of rides for both males and females throughout the season.

The 'did not specify' gender category rides are concentrated in the 46-55 age range. I thought that was curious so I looked into the number of customers vs. subscribers in each age range, and the 46-55 age group is almost 50/50 split between the two user types and has a higher ratio of customers (short-term users) than any other age group.

![Station Popularity Map](/screenshots/station_map_default_view.PNG)
The station map shows the popularity of stations as starting points (circle size represents how many rides originated at the station) and also how long on average rides are from that station.

On the right I have charts showing the most popular starting and ending stations. If you click on a starting station it will highlight it on the map. If you click an ending station, the map will update to show where the rides originated that end at your selected station. This shows that most rides stay within the vicinity or general area of the starting station.
![End station selected](/screenshots/station_map_with_end_station_sel.PNG)