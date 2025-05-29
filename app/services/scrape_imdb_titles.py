"""
Scrape IMDB movie details
ScrapeIMDBTitle() -> Scrap movie details
"""

import requests as re

from bs4 import BeautifulSoup as BS

from app.constants import Lan_Dict


class ScrapeIMDBTitle:
    """
    Scrape IMDB title using Language and Geners
    """

    def __init__(self):
        self.base_url = "https://www.imdb.com/search/title/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
        }

    def get_scrap(self, lan, geners):
        """
        Create correct request to convert response in to BeautifulSoup object
        Args:
            lan (string): Language  Hindi / English / Marathi
            geners (string): Horror / Comedy / Drama / Romantic

        Returns:
            BeautifulSoup: Return beautiful soup object
        """

        try:
            lan = Lan_Dict[lan.upper()]
            list_genr = ",".join(
                genr if isinstance(geners, list) else geners for genr in geners
            )
            new_url = (
                self.base_url
                + f"?title_type=feature&user_rating=7,10&genres={list_genr}&languages={lan}"
            )
            resp = re.get(new_url, headers=self.headers)
            return BS(resp.content, "html5lib")
        except Exception as e:
            print(f"Problem while accessing website {e}")

    def get_imdb_titles(self, lan, geners):
        """
        Scrape title from IMDB website

        Args:
            lan (_type_): Language Hindi / English / Marathi
            geners (_type_): Geners  Horror / Comedy / Drama / Romantic

        Returns:
            list : IMDB movie unique ID list
        """
        imbd_id = []
        soup = self.get_scrap(lan, geners)
        rows = soup.findAll("a", attrs={"class": "ipc-title-link-wrapper"})
        for row in rows:
            href = row.get("href")
            movie_id = href.split("/")[2]
            imbd_id.append(movie_id)
        return imbd_id
