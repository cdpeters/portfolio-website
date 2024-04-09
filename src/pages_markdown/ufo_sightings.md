# **UFO Sightings Website**

## **Overview of Project**
The main objective for this project is to create a dynamic website with
JavaScript and additional tools such as the D3 library and Bootstrap for
styling. The subject for the website is UFO sightings with the goal of
presenting tabular data of reported sightings for cataloging and future analysis
purposes. The site contains only "dummy" data as the project is primarily an
exercise in learning the tools necessary to create a dynamic page that is data
driven.

The dataset of UFO sightings is provided as an array of objects with fields such
as date, city, state, country, shape of what was seen, duration, and additional
comments that explain the event. This array is found in
*[data.js](https://github.com/cdpeters/dynamic-UFO-website-javascript/blob/main/static/js/data.js)*.

The code that runs the page does not use a specific framework, just standard
JavaScript and D3 for element selections and event handling and can be found in
*[app.js](https://github.com/cdpeters/dynamic-UFO-website-javascript/blob/main/static/js/app.js)*. Within this file there are functions to build the
table of data, evaluate and store changes to the filter parameters, and perform
the filtering of the data. The accompanying *[index.html](https://github.com/cdpeters/dynamic-UFO-website-javascript/blob/main/index.html)* makes
use of Bootstrap 5.1.3 components to help with structuring and styling the page.
The files *[appOLD.js](https://github.com/cdpeters/dynamic-UFO-website-javascript/blob/main/static/js/appOLD.js)* and
*[indexOLD.html](https://github.com/cdpeters/dynamic-UFO-website-javascript/blob/main/indexOLD.html)* in the repository are a previous version of
the website.

The website is deployed to GitHub pages at the following link: *[UFO Sightings Website](https://cdpeters.github.io/dynamic-UFO-website-javascript/)*.

## **Results**
In this section, as a demonstration of the functionality of the website, an
example of how to use the filter parameters is presented. The site allows the
user to choose a combination of up to five filters to apply to the data,
dynamically updating the table with the remaining records that match the
criteria.

#### *1. Default View of Table*
In the picture shown below is the default view of the filter search form and
complete table of data. Entering a date requires the use of the format
"m/d/yyyy" and the range of dates that the data covers is shown below the input
field. The remaining fields are names or abbreviations (see the corresponding
columns) and in the case of shapes, the table's shape column shows examples of
possible inputs. Note that the picture does not show the complete set of data
but visiting the website will as the user scrolls down the page.

<div align="center">
    <img src="assets/images/ufo_sightings/default_no_filters_scaled.svg"
         alt="default view no filters" />
</div>

#### *2. Date Filter Applied*
Here in this second image a date filter of "1/7/2010" has been applied and the
table has been updated to reflect the data that matches this date (six total
records). Note that the table will only update once the user has pressed enter
or has clicked somewhere else on the page (the input element is not in the focus
state anymore). This behavior is true for all of the filter fields. Also note
that you cannot input a date range, just singular dates.

<div align="center">
    <img src="assets/images/ufo_sightings/filter_date_scaled.svg"
         alt="view with date filter" />
</div>

#### *3. Date and State Filter Applied*
An entry of "ma" in the state field leaves three matching records since both the
date and state fields are now actively filtering the data.

<div align="center">
    <img src="assets/images/ufo_sightings/filter_date_state_scaled.svg"
         alt="view with date and state filter" />
</div>

#### *4. Date, State, and Shape Filter Applied*
In the last image the shape filter is set to "light" leaving two records in the
table now that three different filters have been applied. This is how the
filtering functionality works, type in a filter field and press enter and the
table updates. To remove any given filter, the user would just need to delete
the text they typed in that input field and press enter.

<div align="center">
    <img src="assets/images/ufo_sightings/filter_date_state_shape_scaled.svg"
         alt="view with date, state, and shape filter" />
</div>

## **Summary**
The website demonstrates simple filtering functionality to allow for easy
movement through the data on UFO sightings. This filtering was achieved via an
event listener using D3 and a few array methods (`forEach()` and `filter()`) in
the functions mentioned in the overview. Users can interact with the table using
the filter search form to apply different filters.

One drawback of the site as it is currently structured is that the user can
easily enter in several valid filters and return no records because a large
portion of common cities, states, and countries do not have any matching records
in this dataset. Because of this, the user would have to scroll up and down
several times taking in the entire dataset just to come up with filters that are
useful (actually return matching records).

One recommendation for improving the experience of using the site would be to
change the form's input elements to dropdown menus. Within each dropdown menu,
there could be list of each of the unique values that show up in that column's
data. This way a user would only need to view the dropdown options to get a feel
for the dataset thereby making choosing an option easier right from the start.

A second recommendation would be to change the view of the table to be shown in
pages where just ten or so records are shown at a time. This would allow the
user to always have the filter search form displayed right next to the data they
are viewing. Quick changes to the filters would be more accessible no matter
what page of the table is being shown compared to the current structure which
involves a lot of scrolling.
