import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def scrape_comic(url):
    try:
        # Extract comic number from URL
        match = re.search(r'/(\d+)/?$', url)
        comic_number = match.group(1) if match else 'latest'
        print(f"\nComic number: {comic_number}")

        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Comic title
        title = soup.find('div', id='ctitle')
        if title:
            print("Comic Title:", title.get_text(strip=True))

        # Comic image and hover text
        comic_div = soup.find('div', id='comic')
        if comic_div:
            img_tag = comic_div.find('img')
            if img_tag:
                iTitle = img_tag.get('title') or img_tag.get('alt') or "No hover text"
                iSource = urljoin(url, img_tag['src'])
                print("Hover Text:", iTitle)
                print("Image Link:", iSource)

        # Next comic link
        next_link = soup.find('a', rel='next')
        if next_link:
            next_url = urljoin(url, next_link['href'])
        else:
            next_url = None

        return next_url

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    url = "https://xkcd.com/1/"

    while url:
        url = scrape_comic(url)

        if not url:
            print("No next comic link found. Ending.")
            break


if __name__ == "__main__":
     main()