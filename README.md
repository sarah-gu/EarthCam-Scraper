# EarthCam Datasets

EarthCam Hall of Fame images are scraped from the gethofitems.php file on the earthcam.com site. When on a specific camera page, click the Network tab on inspect element, then find the gethofimages.php?... file on the lefthand side and double click. This is the link that images are loaded from in this script. For convenience, change the 'city_name' parameter to whatever camera you're scraping from in the parse script. 

The file will save the images to a '(city_name)_photos' and '(city_name)_metadata' folder, where each of the files have a unique number identifier and correspond across the photos and metadata folder. Metadata includes information about the time and date the image was scraped. 

After scraping the data you will need to run the corrupt


# NYC Photos
nyc_photos folder contains ~73000 images, from around March 2020 - Jan 2021, and can be found in /proj/vondrick/datasets/EarthCam/nyc_photos and /proj/vondrick/datasets/EarthCam/nyc_metadata 

# Mulberry St. Photos
littleitaly_hd_photos folder contains ~25000 images, from Sep. 2013 to June 2021
