import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import logging
from typing import List

logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )

# Define base URL and headers for web scraping
BASE_URL = "https://fbref.com"
HISTORY_PAGE = "/en/comps/26/history/Super-Lig-Seasons"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

def get_season_links( url = BASE_URL + HISTORY_PAGE ) -> List[ str ]:  
    """
    Fetch all season links from history page.

    Parameters
    ----------
    url : str
        URL of the history page, default is the history page of Super Lig.

    Returns
    -------
    List[str]
        A list of strings, each is a link to a season page.
    """
    
    logging.info("\nFetching historical season links...\n")
    response = requests.get( url = url, headers = HEADERS )

    # If any error occured, raise it
    response.raise_for_status()

    # Fetch HTML content of the page
    soup = BeautifulSoup( response.content, 'html.parser' )
    links = []

    seasons_table = soup.find( 'table', class_ = 'stats_table' )
    # print( seasons_table )

    if seasons_table is None:
        logging.error( 'Seasons Table Not Found: ERROR!' )
        return links
    
    seasons_address = seasons_table.find_all( 'a', href=True )
    for address in seasons_address:
        if 'Super-Lig-Stats' in address[ 'href' ]:
            links.append( BASE_URL + address['href'] )

    result = []
    for link in links:
        if link not in result:
            result.append( link )

    logging.info( f'Retrieve {len( result )} Of Season Link\n' )
    return result

def fetch_season_data( url: str ) -> pd.DataFrame:
    logging.info(f"Fetching standings data from: {url}")
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    standings_table = soup.find( 'table', id = lambda x : x.startswith( 'results' ) )
    if standings_table is None:
        logging.warning(f"Standings table not found on page: {url}")
        raise ValueError("Standings table not found")
    
    df = pd.read_html( StringIO( str( standings_table )))[0]
    df = df.iloc[:, :-4]
    return df


def main():
    seasons = get_season_links()
    df = fetch_season_data( seasons[1] )

    print( df )


if __name__ == '__main__':
    main()
