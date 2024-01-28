from data_extraction import *
from stockage_csv import save_to_csv

url = 'https://books.toscrape.com/catalogue/needful-things_334/index.html'
base_url = 'https://books.toscrape.com/'

soup = get_soup(url)

data = {
    'product_page_url': url,
    'universal_product_code (upc)': get_universal_product_code(soup),
    'title': get_title(soup),
    'price_including_tax': get_price_including_tax(soup),
    'price_excluding_tax': get_price_excluding_tax(soup),
    'number_available': get_number_available(soup),
    'product_description': get_product_description(soup),
    'category': get_category(soup),
    'star_rating': get_star_rating(soup),
    'review_rating':get_review_rating(soup),
    'image_url': get_image_url(soup, base_url)
}
save_to_csv(data)

