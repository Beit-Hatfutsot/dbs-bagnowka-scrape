### Scraping "Bagnowka" archive using Scrapy
This script scrapes all photos and attached data to be used by Beit-Hatfutsot Open Databases. Images are *uploaded to a AWS s3 bucket.

*_In prder to enable the scraping, valid access keys should be applied in the "bphotos/settings.py" file._

**Usage:**

Using the command line, run:

```scrapy crawl bphotos -o bphotos.json```

After the prossess is completed, a .json file will be added to the folder, containg all the data for each photo, including Urls for stored original sized images and thumbnails.








