# **Citi Bike Bike Sharing Study with Tableau**

## **Overview of Project**
Constructing data visualizations and linking them together to tell a story is
the main aim of data science. Here, using Tableau, a data story is constructed
linking several visualizations covering different facets of the data in order to
determine if the success of a bike sharing service in NYC could be replicated in
a new city. A data story is a common approach in business proposals, and thus
this project serves as practice of an important skill for those who work with
data.

The data used for this project was downloaded from [Citibike trip history data](https://ride.citibikenyc.com/system-data)
on their ride Citibike NYC website. To get to the csv's for download, click on
the link "Download Citi Bike trip history data". The csv used here focuses on
data from August 2019 and will come in a zip file that is labeled
*201908-citibike-tripdata.csv.zip* in the list of datasets. The data contains
information such as trip durations, user types, gender and birth year, start and
end station id's, latitudes, and longitudes, as well as bike id's.

The Tableau story, found within the NYC_CitiBike_Challenge workbook at the
following link:
[NYC_CitiBike_Challenge](https://public.tableau.com/app/profile/cdpeters1/viz/NYC_CitiBike_Challenge_16506220556720/August2019NYCCitibikeStudy).
The same workbook can be found on the profile link: [Tableau Public Profile](https://public.tableau.com/app/profile/cdpeters1/vizzes).

## **Results**
### **Convert Trip Duration to Datetime**
After downloading the data and becoming familiar with the dataset there was one
transformation that needed to be made. The trip duration column was a string and
needed to be converted to a datetime object using the `pandas.to_datetime()`
function. The original column was kept along with the newly created datetime
type column called `tripduration_dt`. After this conversion, the DataFrame was
written to a csv called `2019_august_citibike_tripdata.csv`. The original csv
and this new csv are not stored on the repository due to their size.

Using the transformed csv, all of the visualizations below were created in
Tableau and a Tableau story was assembled and published at the link mentioned
above.

### **Ride Durations by All Users**
The following graph shows the durations of bike rides for all users of the
service. The breakdown is split into hours as seen on the top of the graph and
minutes on the bottom of the graph. The y-axis is the number of rides at the
given duration.

<div align="center">
    <img src="assets/images/bike_sharing/ride_durations_by_all_users.svg"
         alt="Ride Durations by All Users" />
</div>

The graph reveals that the most popular trip durations occur around the 7-12
minute mark. This is likely due to customers using the bike specifically to get
from one place to the next as opposed to just riding for the sake of riding. The
graph flattens out right before the first hour mark, so in general, longer ride
durations are not as common.

### **User Demographics**
Before moving on to the next trip duration breakdown, it is useful to see the
user demographics for the service. Here are two pie charts looking at both user
type and gender breakdown for the bike riders.

<div align="center">
    <img src="assets/images/bike_sharing/user_demographics.svg"
         alt="User Demographics" />
</div>

The Citi Bike service is primarily made up of subscribers. Any service created
in a new city would likely want to prioritize regular repeat users in developing
their subscriber model as it is likely that this will be the dominant user type.

As far as the gender breakdown, the data reveals that males account for a higher
share of the user base than the other genders. This could mean that marketing
efforts should be aimed at males. However, this could also mean that an increase
in the marketing efforts aimed at the other genders could be a potential
opportunity for growth.

### **Ride Durations by Gender**
Now that the gender demographics have been discussed, here is the trip duration
breakdown by gender. The graph is structured in the same way as the first trip
duration graph.

<div align="center">
    <img src="assets/images/bike_sharing/ride_durations_by_gender.svg"
         alt="Ride Durations by Gender" />
</div>

The results confirm the same conclusions made in the *Ride Durations by All
Users* section about the length of most bike rides even across genders. It is
also confirmed that males account for a larger number of trips taken. The graph
flattens for all three gender designations right around the same point as well.

### **Trips by All Users (Weekday per Hour)**
The chart below shows the most popular times to start a ride by day of the week
and by hour for all users.

<div align="center">
    <img src="assets/images/bike_sharing/trips_by_all_users_weekday_per_hour.svg"
         alt="Trips by All Users (Weekday per Hour)" />
</div>

For weekdays, the most popular times are morning and late afternoon,
specifically around 7-9am and 5-6pm respectively. The most popular days are
Monday, Tuesday, Thursday and Friday.

For weekends, there is consistent riding throughout the middle of the day on
both days starting around 10am and ending around 7pm.

The results here can help in choosing which hours will be best for maintenance,
specifically early morning or late night seems to fit best.

### **Trips by Gender (Weekday per Hour)**
A further breakdown of trip start times by gender is shown below.

<div align="center">
    <img src="assets/images/bike_sharing/trips_by_gender_weekday_per_hour.svg"
         alt="Trips by Gender (Weekday per Hour)" />
</div>

Here, the trends among males and females confirm the trends found in the
previous heatmap. The heatmap is darker in color for males indicating more rides
occurring which reflects the demographics as discussed earlier. For the gender
designation "unknown", further investigation is likely necessary to see if low
sample size has led to this different looking trend in the heatmap.

### **Trips by Demographic by Weekday**
A different take on the trip start time data is shown here with a breakdown
across user type and gender. Here time of day is not considered.

<div align="center">
    <img src="assets/images/bike_sharing/trips_by_demographic_by_weekday.svg"
         alt="Trips by Demographic by Weekday" />
</div>

There is clearly more activity among the subscriber base, and the data also
confirms heavy usage among subscribers on the days mentioned above (Mon, Tue,
Thu, Fri, and weekends). In looking at the customer data (non-subscribers) there
is actually consistent usage across all days of the week. Further investigation
is needed to understand the very light usage by the gender designation "unknown"
among the subscriber base (this again could be due to low sample size).

### **Average Trip Duration**
Here, average trip duration is plotted vs birth year of all users.

<div align="center">
    <img src="assets/images/bike_sharing/average_trip_duration.svg"
         alt="Average Trip Duration" />
</div>

The general trend seen in this graph is that younger riders often ride for
longer durations. Perhaps some sort of mileage program with discounts after
accruing ride mileage could interest older riders in riding for longer or
inspire them to choose a Citi bike over a ride share service when they need to
travel a longer distance.

### **Top Start and End Locations**
Lastly, here is a map showing the top locations for starting and ending rides.
The larger the size and darker the color of the data point the more rides where
started or ended there.

<div align="center">
    <img src="assets/images/bike_sharing/top_start_and_end_locations.svg"
         alt="Top Start and End Locations" />
</div>

It is clear with the knowledge of NYC, that the most common starting and ending
destinations are around city attractions, primarily ones that tourists are
interested in. This could be valuable information for planning where bike
stations should be located for a program in a new city. Ensure the stations are
in high traffic areas so that convenience is built in to the service.

## **Summary**
In conclusion, any bike sharing service should be concerned with ensuring the
subscriber experience is top notch as a starting point. One way in which this
can be achieved is by making bikes available in the most relevant and high
traffic areas in the city that is being serviced by the program. This includes
number of bikes as well as stations at which someone can start and end their
rides. Another way is to ensure that bikes are repaired and maintained outside
of mid to late morning and late afternoon hours during the weekdays and
throughout the day on weekends so that bikes are always available.

The data also shows that there are marketing opportunities to increase user
numbers among female and unknown gender designations. Additionally, the ride
durations are short and are primarily used as transportation tools, but
incentive programs could be created to inspire longer rides and using bikes as
alternate transportation options to motor vehicles.

### **Additional Data Visualizations**
As a recommendation for follow up visualizations, the ride duration breakdown
based on user type could be explored. It would be interesting to see if
subscribers take longer trips or is it just that they use the service for short
trips more often than everyday customers. Another visualization that could be
worth exploring is how the cost of the service might be affecting trip durations
and whether or not a user joins as a subscriber (duration vs. cost graph). It
might be that the shorter duration is in some way tied to how the service is
charged to the user.
