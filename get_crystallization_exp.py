#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Python module to retrieve the crystallization experiment details of a structure deposited in the protein database (PDB).

Requirements:

- PyPDB
- requests
- BeautifulSoup
'''

import pypdb
import requests
from bs4 import BeautifulSoup

def make_request(url_experiment):

    # make the HTML request using the built URL
    request = requests.get(url_experiment)

    return(request)

def make_soup(request):

    # make the soup for the complete website returned by the request
    soup_fullpage = BeautifulSoup(request.text, 'html.parser')

    # find the relevant table in the soup
    soup_crystal_info = soup_fullpage.find('table', {'class': 'table table-bordered table-condensed'})

    return(soup_crystal_info)

def get_crystallization_exp(soup_crystal_info):

    # create empty lists for the informations
    titles = []
    details = []

    # get the keys for the dictionary
    soup_info_titles = soup_crystal_info.find_all('th')
    for title in soup_info_titles[1:]:
        titles.append(title.text)

    # get the values for the dictionary
    soup_crystallization_exp_details = soup_crystal_info.find_all('td')
    for detail in soup_crystallization_exp_details:
        details.append(detail.text)

    # make the dictionary
    crystallization_exp = dict(zip(titles, details))

    return(crystallization_exp)

def get_info(pdb_code):

    # enter the desired pdb code below
    #pdb_code = '5U79'

    # ULR to reach the M&M details
    url_experiment = 'http://www.rcsb.org/pdb/explore/materialsAndMethods.do?structureId=' + pdb_code

    # functions to run
    request = make_request(url_experiment)
    soup_crystal_info = make_soup(request)
    crystallization_details = {pdb_code : get_crystallization_exp(soup_crystal_info)}

    return(crystallization_details)


if __name__ == '__main__':
    get_info()
