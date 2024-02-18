import requests
from bs4 import BeautifulSoup
from file_helper import FileHelper


class Crawler:

    def __init__(self, start_url, depth):
        self.start_urls = start_url
        self.depth = depth
        self.visitedUrls = set()

    def get_urls(self, url, number):
        if url in self.visitedUrls:
            return set()
        self.visitedUrls.add(url)
        links = set()
        content = ''
        try:
            content = requests.get(url, timeout=20)
            content.raise_for_status()
            soup = BeautifulSoup(content.text, 'html.parser')
            try:
                if 'en' not in soup.html['lang']:
                    return set()
            except Exception:
                pass
            anchors = soup.find_all('a')
            for anchor in anchors:
                link = requests.compat.urljoin(url, anchor.get('href'))
                links.add(link)
        except requests.RequestException:
            pass

        file_helper = FileHelper()

        try:
            file_helper.make_file(content.content.decode('utf-8'), str(number), 'results')
        except Exception as e:
            pass

        return links


    def crawl(self):
        urls_content = {}
        urls_to_crawl = set()
        current_number = 1

        for start_url in self.start_urls:
            urls_to_crawl.add(start_url)

        for depth in range(self.depth + 1):
            new_urls = set()
            for url in urls_to_crawl:
                if (url not in self.visitedUrls) and (url + '/' not in self.visitedUrls):
                    last_domain = url.split("/")[-1]
                    if (".css" not in last_domain) and (".pdf" not in last_domain) and (".js" not in last_domain):
                        links = self.get_urls(url, current_number)
                        urls_content[current_number] = url
                        new_urls.update(links)
                        current_number += 1
            urls_to_crawl = new_urls
        file_helper = FileHelper()
        file_helper.make_file(urls_content, 'index.txt', 'index', should_use_json=True)