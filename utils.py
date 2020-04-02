
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




def CheckSpellKo(Text):
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

