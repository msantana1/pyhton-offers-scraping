# Python web scraping
This is a test to use Python scraping and look for discounts on Laptops on the e-commerce site: Cyberpuerta

This Python script is desgined to be executed through a Linux cronjob, the principal goal of the script is to send an email with the information of the discount:
- Product URL
- Product name
- Regular price
- Current price
- And total discount

But the Python script prints the content of the email body so in the cronjob it can be configured to store the general output into a log file

The URLs are stored on dictionaries, one per CPU family (Ryzen 7 and i7) so it can be easily retrived the individual data (each URL and its price), the goal of using dictionaries is that it can be easily added new CPU families or data from other e-commerce sites
