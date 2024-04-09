# **Mapping Earthquakes with Leaflet**

## **Overview of Project**
The GeoJSON standard is a very common format for representing geographical
features for mapping and thus is an important tool to be familiar with when it
comes to those types of visualizations. This project is primarily concerned with
the plotting of map data from a GeoJSON source using the Leaflet library.
Setting up map base layers, including the tile layers from Mapbox, overlay
layers of different sets of data, and information popups are a few of the main
objectives that are completed within this work.

The context for this project is the mapping of global earthquake data from the
past seven days from the U.S. Geological Survey's earthquake website
(*[earthquake.usgs.gov](https://earthquake.usgs.gov/)*). Two different USGS
datasets are used, one for all of the earthquakes in the past seven days, and
one that captures the quakes that registered 4.5+ in magnitude. Additionally, a
layer of tectonic plate data from the following GitHub *[tectonic plates
repository](https://github.com/fraxen/tectonicplates)* was included to compare
earthquake locations against fault lines. The data is read in via D3's
`d3.json()` function by passing the URL provided by the USGS site and the
tectonic plates repository as an argument.

Leaflet is then used to facilitate creating the map and adding the data layers
including circle markers and popups for each earthquake. This is achieved by
making a base layer object containing the map tile layers, and an overlay object
containing the data layers. The `L.control.layers()` method is then applied to
allow for control over which base map is selected and which data layer is
visible. The size of the circle for each data point is proportional to its
magnitude, and the color is related to the range that its magnitude falls
within. The major earthquake layer also has proportional size and relevant
coloring (dark red for earthquakes greater than 6 in magnitude). A legend is
included to clarify the ranges of magnitudes and their colors. Tectonic plate
fault lines are also included as a selectable data layer.

The complete map is displayed as an html page for a simple full screen view of
the earthquake data. All files related to the final map are found in the directory *[Earthquake_Challenge](https://github.com/cdpeters/mapping-earthquakes-leaflet/tree/main/Earthquake_Challenge)*.
