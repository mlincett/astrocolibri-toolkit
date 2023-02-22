""" Wrapper around Astro-COLIBRI API"""

from .www import WebServer

import json

import pandas as pd
from astropy.table import Table

import logging

logger = logging.getLogger(__name__)

class SearchResult:
    def __init__(self, json_data) -> None:
        self.data = json.dumps(json_data)
        self.
        pass

    @staticmethod
    def from_response(r):
        return SearchResult(r.text)

    def to_pandas(self):
        df = pd.read_json(self.data, orient="split")
        return df

    def to_astropy(self):
        table = Table.read(self.data, format="pandas.json")
        return table


class ColibriAPI:
    base_url = "https://astro-colibri.herokuapp.com/"

    def __init__(self) -> None:
        self.srv = WebServer(self.base_url)

    def query(self, func : str, params : dict):
        func_url = self.base_url + '/' + func
        return self.srv.get(func_url, params)

    def cone_search(self, ra : float, dec : float, radius : float, datemin : int, datemax = int) -> SearchResult:
        """Performs a cone search

        Args:
            ra (float): right ascension J2000.0 [deg]
            dec (float): declination [deg]
            radius (float): search radius [deg]
        """
        func = "cone_search"
        cone = f"[{ra},{dec},{radius}]"

        # pars = { "cone": cone, "datemin" : datemin, "datemax" : datemax }
        pars = { "cone": cone } # "datemin" : datemin, "datemax" : datemax }
        r = self.query(func, pars)

        print(r.url)

        return SearchResult.from_response(r)
        #return r
