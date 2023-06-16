# Scraping-for-ecommerce-site
Products were scraped and prepared in the right CSV format of WordPress then Uploaded to Woocommerce website.

1- Scraping step : Selenium was used Because the site was dynamic and the products of categories the client defined was scraped and saved in the form of CSV and this was a pure scraped data not ready for uploading.
2- Preparing the Data to be Uploaded : A csv format was exported from the Wordpress website to prepare our scraped data to fit this format to be Uploaded.
3- After preparing the Data additional requirements was needed by the client which were:
- blurbs for Descriptions.
- Each product under the right category
- Edit some scraped data.
  -- The first step blurbs was based on using python to make a connection for every product Description with Chat GPT through GPT API key and give Chat GPT the Description and ask him to make a blurb for this discription.
Categorylinks.py file Scrape the links of categories choosed by the client.
Scrapingstep.py file loop over these links and scrape all the data there.
Scrapeddata.csv is the file before preparing
Fileready.csv is the file ready to be uploaded will all requirments mentioned above.
