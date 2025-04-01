# This file is created to analyse dune volumes using the JARKUS analysis toolbox

import yaml
import pickle
from JAT.Jarkus_Analysis_Toolbox import Transects, Extraction

######################
# LOAD SETTINGS FROM FILE
######################
config = yaml.safe_load(open("./Examples/DuneVolumeS/DuneVolumS_Transect.yml"))

#%%###################
# LOAD DATA
######################
# Load jarkus dataset
data = Transects(config)

# To view the metadata:
# print(data.dataset)
# print(data.variables)

#
# The following step makes sure the requested years and transects are available in the dataset.
data.get_availability(config)

# Those that were available are saved as follows: 
print(data.transects_filtered)
print(data.years_filtered)
# Note that only the years from 1980 onwards are available for this specific transect!

####################
# SAVE + PLOT DATA
######################

# Create elevation plots for the available transects - saved as png and pickle
data.get_transect_plot_dunes(config)

# Extract all requested dimensions for the available transects and years
# assign class
# extract = Extraction(data, config)
# this is were all dimensions are extractd and pickle files are saved. 
# extract.get_all_dimensions()
# note that extract.dimensions holds the dataframe with dimensions for the last transect after applying the function above.

# dimensions = extract.get_requested_variables()

# extract.get_dataframe_per_dimension()

