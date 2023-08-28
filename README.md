# Horoscope Scraper

## Technologies
- Python
- BeautifulSoup
- pywhatkit (WhatsApp integration)

## Overview
The **Horoscope Scraper** is a Python script designed to fetch the latest weekly horoscope information from horoscoponegro.com and then deliver it via WhatsApp to a list of hardcoded users.

The script utilizes the following technologies:

- **Python:** The programming language used to build the scraper.
- **BeautifulSoup:** A Python library used for web scraping, which allows you to extract data from HTML and XML documents.
- **pywhatkit:** This library provides an interface to interact with WhatsApp through Python code.

## How to Use
1. **Installation:**
   Start by installing the required packages using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
2. **Running the Scraper:**
   Run the main script named main.py using Python:
   ```bash
   python main.py

## The script will perform the following steps:

Scrape the latest weekly horoscope information from horoscoponegro.com using BeautifulSoup.
Format the scraped data.
Send the formatted information to the predefined list of users via WhatsApp using pywhatkit's WhatsApp integration.
Make sure you have the required WhatsApp integration set up using pywhatkit. The script does not require explicit credentials for pywhatkit but will need you to be logged in on WhatsappWeb.

Remember to regularly update the script to account for any changes in the website's structure or any updates to the libraries being used.

Feel free to customize and enhance the script according to your needs and preferences.