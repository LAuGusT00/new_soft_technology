import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    headers = {"User-Agent": User_Agent}
    url="https://www.shicimingju.com/book/xiyouji.html"
    page_text=requests.get(url=url,headers=headers).content.decode('UTF-8')
    print(page_text)
    tatal_text_soup=BeautifulSoup(page_text,"lxml")
    li_list=tatal_text_soup.select(".book-mulu >ul >li")
    fp=open("./爬取文件/西游记.txt","w",encoding="utf-8")
    for li in li_list:
        chapter_titles=li.a.string
        chapter_url=li.a["href"]
        chapter_url="https://www.shicimingju.com"+chapter_url
        chapter_text=requests.get(url=chapter_url,headers=headers).content.decode('UTF-8')
        essay_text_soup=BeautifulSoup(chapter_text,"lxml")
        essay_text=essay_text_soup.find("div",class_="chapter_content").text
        fp.write(chapter_titles+":"+essay_text+"\n")
        print(chapter_titles,"爬取成功！！！")
