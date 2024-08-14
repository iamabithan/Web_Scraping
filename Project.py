import requests
from bs4 import BeautifulSoup

def fetch_news(url, article_class, title_class=None, filename="news.txt", header=None):
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return 
    
    soup = BeautifulSoup(page.content, 'html.parser')
    articles = soup.find_all(class_=article_class)
    
    if not articles:
        print(f"No elements found with class name '{article_class}'")
        return
    
    with open(filename, 'w', encoding='utf-8') as file:
        if header:
            file.write(header)
            file.write('\n\n')
        
        for count, article in enumerate(articles, 1):
            if title_class:
                for tag in article.find_all(class_=title_class):
                    tag.decompose()
            file.write(f'News {count}:\n')
            file.write(article.get_text(separator='\n'))
            file.write('\n\n')
        
        file.write("Project by Abithan")
    
    print(f"File '{filename}' saved successfully")

def indianexpress():
    fetch_news(
        url="https://indianexpress.com",
        article_class='other-article',
        title_class='title',
        filename='Indian_Express.txt'
    )

def timesnow():
    fetch_news(
        url="https://www.timesnownews.com/latest-news",
        article_class='_16rp',
        filename='Timesnow_News.txt',
        header="Latest News"
    )

def thinamalar():
    fetch_news(
        url="https://www.dinamalar.com/news/latest-tamil-news",
        article_class='MuiTypography-root MuiTypography-body1 css-17pdzv3',
        filename='Thinamalar_News.txt',
        header="Latest Tamil News"
    )

def thinathandhi():
    fetch_news(
        url="https://www.dailythanthi.com/",
        article_class='NewsWithMobile',
        filename='Thinathandhi_News.txt',
        header="Latest Tamil News"
    )

def main():
    print("1. Tamil\n2. English\n")
    try:
        getlang = int(input("Enter number to select language: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if getlang == 1:
        print("1. Thinamalar\n2. Thinathandhi\n")
        try:
            getnews = int(input("Enter number to select Article: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if getnews == 1:
            thinamalar()
        elif getnews == 2:
            thinathandhi()
        else:
            print("Invalid Input")
    elif getlang == 2:
        print("1. Indian Express\n2. Timesnow\n")
        try:
            getnews2 = int(input("Enter number to select Article: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if getnews2 == 1:
            indianexpress()
        elif getnews2 == 2:
            timesnow()
        else:
            print("Invalid Input")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()