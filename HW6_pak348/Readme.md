This Assignment involved creating models for Energy Distribution. I worked on my own for most of the assignment and took a little help from my friends for Chi-Square distribution.

## An interesting urban question is "can we measure and predict energy use based on observables that are easily acquired". For example the urban observatory at CUSP can monitor lights: they are a relatively easy observable. All you need is a camera, and a pipeline to process your data. But how does the light coming from a window relate to the total energy consumption? We generally postulate that light is a proxy for occupancy, and that occupancy is a good predictor of energy consumption.

### So let's test if the last link holds. If we have data on the energy consumed by a building how well does that relate to the number of units in the building?

#### Data on energy consumption can be found here for the city of NY https://data.cityofnewyork.us/Environment/Energy-and-Water-Data-Disclosure-for-Local-Law-84-/rgfe-8y2z


#### However this datasets does not have the number of units. We can find that in the Pluto dataset.
#### Reading in the Pluto data for manhattan, which will give me the number of units ber building Manhattan/MNMapPLUTO.shp


