# **Belly Button Biodiversity Dashboard**

## **Overview of Project**
Dashboards are excellent tools for data science storytelling in that they
abstract away the technical details in favor of interaction with the data at a
high level. This approach allows results focused users to readily identify key
takeaways from the analysis without worrying about the methodologies behind the
analysis. The goal of this project was to create a data dashboard with tools
such as JavaScript, the Plotly library, and D3 methods for reading data and
manipulating the DOM.

### **The Data**
The subject for the dashboard is the biodiversity of microbes found in the human
belly button. The data used for the project is found in
*[samples.json](https://github.com/cdpeters/biodiversity-dashboard-plotly/blob/main/static/data/samples.json)*
and contains the metadata for each volunteer that submitted a sample including
demographic information and washing frequency. Additionally, there is an array
that stores only sample ids and one that stores the sample results (bacteria
cultures found and their Operational Taxonomic Unit (OTU) ID and labels). The
dashboard is aimed at the volunteers who participated who would be able to
select their sample ID from a dropdown menu and see their results in the charts
provided.

### **Charts**
There are three charts provided on the dashboard: a gauge chart, bar chart, and
a bubble chart.
- **Gauge Chart**: Shows belly button washing frequency per week using a gauge.
- **Bar Chart**: Shows the top 10 bacteria cultures found in the sample along
  with their sample values (x-axis), and OTU ID (y-axis). Hovering over a bar
  shows the bacteria names that belong to that OTU ID.
- **Bubble Chart**: Shows all of the cultures found in the sample along with
  their sample values (y-axis) and the OTU ID's (x-axis). The center and size of
  each circle correspond to the sample values and the color corresponds to their
  OTU ID number (see explanation above the bubble chart on the dashboard).

### **Styling Customizations**
Styling of the dashboard was primarily done with Bootstrap. A background image
of microbes found in a belly button was added to the jumbotron. A welcome
message and an explanation of the bubble chart was also included. The layout of
the dashboard was reordered from the first version for a more balanced look and
the bubble chart was expanded to fill the width of the dashboard on a standard
laptop screen using a flex container. These are just three of the customizations
among others added to enhance the page.

The dashboard is deployed to GitHub pages at the following link: *[Belly Button Biodiversity Dashboard](https://cdpeters.github.io/biodiversity-dashboard-plotly/)*.
