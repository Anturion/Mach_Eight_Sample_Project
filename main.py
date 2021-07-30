import os
import requests
import sys
import json

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pandas import json_normalize

load_dotenv()

class APPNBAHeight:

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

    def __init__(self):

        self.compare_value()
   
    def compare_value(self):
        
        data_1=[]

        number_to_compare = input('Write a integer to search conincidences or type "exit" to close app: ')
        
        if number_to_compare == 'exit':
            print('Bye!')
            return sys.exit()

        try:
            int(number_to_compare)
        except ValueError:
            message = 'The number entered must be integer'
            print('The number entered must be integer')
            
            return message

        if int(number_to_compare) < self.sorted_height[0] + self.sorted_height[1] or int(number_to_compare) > self.reverse_sorted_height[0] + self.reverse_sorted_height[1]:
            message = f'The number must be an integer between {self.sorted_height[0] + self.sorted_height[1]} and {self.reverse_sorted_height[0] + self.reverse_sorted_height[1]}'
            print(message)

            return message 

        for column_1 in self.data_frame.itertuples(index=False):
            for column_2 in self.data_frame.itertuples(index=False):
                if (column_1.h_in + column_2.h_in == int(number_to_compare)
                    and column_1.first_name + column_1.last_name != column_2.first_name + column_2.last_name):
                    data_save =[
                        f'{column_1.first_name} ' 
                        f'{column_1.last_name}', 
                        f'{column_2.first_name} ' 
                        f'{column_2.last_name}'
                    ]
                    if sorted(data_save) not in data_1:
                        data_1.append(sorted(data_save))
                        print(f'- {data_save[0]}     {data_save[1]}')
        return len(data_1)

if __name__ == "__main__":
    APPNBAHeight()





