## Scraping "Bagnowka" archive using Scrapy
This script scrapes all photos and attached data to be used by Beit-Hatfutsot Open Databases. Images are *uploaded to an AWS s3 bucket.

*_In prder to enable the scraping, valid access keys should be applied in the "bphotos/settings.py" file._

### Usage
#### 1. Scrape
Using the command line, run:

```scrapy crawl bphotos -o bphotos.json```

After the prossess is completed, a .json file will be added to the folder, containg all the data for each photo, including Urls for stored original sized images and thumbnails.

#### 2. Convert scraped photos into valid BH DBS data
run `prsing.py` (don't forget to change the name of the input file to match the one produced by ceawler and make sure output is valid).

#### 3. Merge items with identical info
Using the output file from previous step, run `merge_galleries.py`
(and make sure that the output is valid).










