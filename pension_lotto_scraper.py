import requests
from bs4 import BeautifulSoup

def getLastNo():
    req = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=win720')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # 회차 크롤링
    no = soup.select('div.section_title > h2 > strong')

    # 최신 회차 번호를 가져온다
    return no[0].text

def crawlingLotto(nums):
    # 로또 이번주 당첨 번호 사이트 주소
    req = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=win720&Round=' + str(nums))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 회차 크롤링
    no = soup.select('div.section_title > h2 > strong')
    # # 추첨일
    # date = soup.select('div.win_result > p')
    # 당첨 번호 (첫 6개 숫자만 가져오기)
    nums_win = soup.select('div.prize > ul > li')[:6]
    # 조 번호
    nums_bonus = soup.select('div.prize > h4 > strong')

    # 출력할 결과 문자열 생성
    result = [nums_bonus[0].text + "조"]
    for t in nums_win:
        result.append(t.text)

    return result

if __name__ == "__main__":
    lastno = int(getLastNo()[:-1])

    for i in range(lastno, lastno - 50, -1):
        nums = crawlingLotto(i)
        print(nums)
