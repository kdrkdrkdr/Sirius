
from requests import get, post, exceptions
from bs4 import BeautifulSoup
from json import loads





def GetSoup(url, header, method, data=None):
    while True:
        try:
            if method == post:
                html = method(url, headers=header, data=data).text
            else:
                html = method(url, headers=header).text

            soup = BeautifulSoup(html, 'html.parser')
            return soup
            
        except (exceptions.ChunkedEncodingError, exceptions.SSLError, exceptions.Timeout, exceptions.ConnectionError):
            pass




def CheckSpell(Text):
    r = post(
        url = 'http://speller.cs.pusan.ac.kr/results',
        headers = {
            'user-agent':'Mozilla 5.0',
            'referer':'http://speller.cs.pusan.ac.kr',
        },
        data = {'text1':Text}
    )
    soup = BeautifulSoup(r.content, 'html.parser')
    script = soup.find_all('script')[-1].text

    try:
        spelldata = script.split('$(document).ready(function(){\n\tdata = ')[1].split(';\n')[0]
        candWord = loads(spelldata)[0]['errInfo'][0]['candWord']

        if candWord == "":
            return Text
        else:
            return candWord

    except ( IndexError ):
        return Text


pos_dict = {
    'Adverb': {'너무', '매우', }, 

    'Noun': {'노래', '날씨', '검색', '뉴스', },

    'Josa': {'는', '의', '이다', '입니다', '이', '이는', '를', '라', '라는', '좀', },

    'Verb': {'하는', '하다', '하고'},
    
    'Adjective': {'예쁜', '예쁘다'},
    
    'Exclamation': {'우와'},
}


