from dataclasses import dataclass
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from src.settings import BASE_URL


@dataclass
class Client:
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
        'Accept-Encoding': ', '.join(('gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
    }
    session = requests.Session()
    url: str = BASE_URL

    def _request(self, method: str, url: str):
        self.session.headers = self.default_headers
        response = getattr(self.session, method)(url)
        response.raise_for_status()

        return response

    def get_movies_by_name(self, name: str) -> List[Dict[str, str]]:
        url = f'{self.url}/movie/autocomplete?term={name}'
        response = self._request('get', url)
        response_json = response.json()

        return [
            {
                'id': data['id'],
                'title': data['label'],
                'url': data['url'],
                'thumb': data['thumb'],
            } for data in response_json
        ]

    def get_similar_movies(self, movie_id: str):
        url = f'{self.url}/movie/{movie_id}'
        response = self._request('get', url)
        content = response.content.decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        movies_div_list = soup.find_all(class_='item_info item_movie')
        result = []
        for movie_div in movies_div_list:
            result.append({
                'title': self._get_text_from_tag(movie_div, 'div', 'name'),
                'rating': self._get_text_from_tag(movie_div, 'div', 'rat-rating'),
                'img_url': f"{self.url}{self._get_text_from_tag(movie_div, 'img', 'lazy')}",
                'genre': self._get_text_from_tag(movie_div, 'div', 'attr-genre'),
                'country': self._get_text_from_tag(movie_div, 'div', 'attr-country'),
                'duration': self._get_text_from_tag(movie_div, 'div', 'attr-runtime'),
                'description': self._get_text_from_tag(movie_div, 'div', 'attr attr-story'),
            })

        return result

    def _get_text_from_tag(self, tag_obj, tag_name, class_name):
        if element := tag_obj.find(tag_name, {'class': class_name}):
            if tag_name.lower() == 'img':
                return element['data-src']
            return element.text.strip()
        return None
