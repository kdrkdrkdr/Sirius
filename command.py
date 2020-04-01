
from utils import *
from speech import *
from webbrowser import open_new
from youtube_search import YoutubeSearch
from nlpcontent import NLPContent
import re





def CheckCommand(Text):
    try:

        content = NLPContent(Text)

        print(content)

        kWord = content[0]
        mainContent = CheckSpell(content[1])


        if kWord == '검색':
            open_new(f'https://www.google.com/search?q={mainContent}')



        elif kWord == '노래':
            while True:
                try:
                    ytResult = YoutubeSearch(mainContent + ' 노래', max_results=5).to_dict()
                    ytUrl = 'https://www.youtube.com' + ytResult[0]['link']
                    open_new(ytUrl)
                    break
                except:
                    continue

        
        elif kWord == '날씨':
            soup = GetSoup(
                url=f'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={mainContent}+날씨',
                header={'user-agent': 'Mozilla 5.0', 'referer' :'https://search.naver.com'},
                method=get
            )

            wInfo = ""
            location = soup.find('span', {'class':'btn_select'}).text + '\n'
            todaytemp = '현재온도는 ' + soup.find('span', {'class':'todaytemp'}).text + '도 입니다.\n'
            wInfo += location + todaytemp

            tempinfos = soup.find('ul', {'class':'info_list'}).find_all('li')
            for i, t in enumerate(tempinfos):
                if i == 2:
                    num = ''.join(list(re.split('[^0-9]', t.text)))
                    uv = num.replace(num, f'{num}으로 ')
                    wInfo += t.text.replace(num, uv).replace('자외선', '자외선 지수는')
                
                else:
                    wInfo += t.text.replace('˚', '도').replace('/', '에서 ').replace('체감온도', ', 체감온도는') + '\n'
                    
            TextSpeech(wInfo)
        

        elif kWord == '':
            pass


        else:
            print('제대로 인식이 되지 않았습니다.')
                    
    except ( AttributeError ):
        print("Text ERROR!")
