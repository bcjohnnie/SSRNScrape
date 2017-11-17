# SSRNScrape
A Python script to scrape recently posted articles to various SSRN ejournals

Currently dependent on the selenium package.

Testing implementation visits a specific SSRN ejournal page, re-sorts to descending by date published (there may be a better way to do this using the requests library).

The script then takes the HTML of the first n entries, and pulls out relevant metadata.  Currently just prints data to console, planning to add this data to a dictionary so that it can be output programmatically in HTML and turned into an email list of recent postings.
