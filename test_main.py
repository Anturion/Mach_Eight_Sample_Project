import main
import os
import requests
import json

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pandas import json_normalize

load_dotenv()

class TestClass:

    try:
        URL_DATA_SCRAPING = os.environ['URL_DATA_SCRAPING']
    except:
        raise ValueError('Destination URL does not exist')
        
    r = requests.get(URL_DATA_SCRAPING)
    data_raw = BeautifulSoup(r.text, 'lxml').p.text
    json_data_raw = json.loads(data_raw)

    data_frame = json_normalize(json_data_raw['values'])
    data_frame['h_in'] = data_frame.h_in.astype(int)

    sorted_height = sorted(data_frame['h_in'])
    reverse_sorted_height = sorted(data_frame['h_in'], reverse=True)

    def test_valid_input(self):
        main.input = lambda x: '139'
        output = main.APPNBAHeight.compare_value(self)
        assert output == 2 # dataframe length
        
    def test_string_input(self):
        main.input = lambda x: 'hola'
        output = main.APPNBAHeight.compare_value(self)
        assert output == 'The number entered must be integer'
    
    def test_empty_input(self):
        main.input = lambda x: ''
        output = main.APPNBAHeight.compare_value(self)
        assert output == 'The number entered must be integer'

    def test_min_edge_input(self):
        main.input = lambda x: '138'
        output = main.APPNBAHeight.compare_value(self)
        assert output == 'The number must be an integer between 139 and 177'

    def test_max_edge_input(self):
        main.input = lambda x: '178'
        output = main.APPNBAHeight.compare_value(self)
        assert output == 'The number must be an integer between 139 and 177'
    