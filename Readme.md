# **Turkish Super League Scraper**

## **Project Overview**
The **Turkish Super League Scraper** is a Python script designed to scrape historical season data from the Turkish Super League's official website using the `requests` and `BeautifulSoup` libraries. The script fetches links to season-specific pages, extracts standings data for each season, and processes it into a structured format using pandas.

---

## **Features**
- **Season Link Extraction**: Collects all available season links from the history page.
- **Data Scraping**: Retrieves team standings data for each season.
- **Error Handling**: Logs warnings and errors, ensuring smooth execution and debugging.
- **Data Output**: Processes the extracted data into a pandas DataFrame for further analysis.

---

## **How To Run**
- **Clone the Repository**: 
```bash
    git clone https://github.com/ykerimcgr/Turkish_Super_League_Scraper.git
    cd Turkish_Super_League_Scraper
    python -m venv <your_virtual_environment_name>
```
- **Install Dependencies**:
```
    source <your_virtual_environment_name>/bin/activate
    pip install -r requirements.txt
```
- **Execute Script**:
```
    python scrape.py
```