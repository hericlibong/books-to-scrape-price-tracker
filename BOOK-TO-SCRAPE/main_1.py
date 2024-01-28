from data_extraction import *
from stockage_csv import save_to_csv


#url pour l'extraction d'un livre unique
#url = 'https://books.toscrape.com/catalogue/needful-things_334/index.html'



cat_url = 'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'
alt_url = 'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/'
base_url = 'https://books.toscrape.com/catalogue'


all_books_url = []
while True:
    #Collecte le Urls des livres de la catégorie choisie
    cat_soup = get_soup(cat_url)    
    books = cat_soup.find_all('h3')
    book_urls = [base_url + book.find('a')['href'].replace('../../..', '') for book in cat_soup.find_all('h3')]
    all_books_url.extend(book_urls)

    #Verifie si une page suivante existe et met à jour cat_url sinon sort de la boucle
    next_button = cat_soup.find(class_='next')
    if next_button:
        next_page_partial_url = next_button.find('a')['href']
        if 'index.html' in cat_url:

            cat_url = cat_url.replace('index.html', next_page_partial_url)
        else :
            cat_url = alt_url + next_page_partial_url
    else:
        break

for book_url in all_books_url:
    soup = get_soup(book_url)

    data = {
        #'product_page_url': url,
        'universal_product_code (upc)': get_universal_product_code(soup),
        'title': get_title(soup),
        'price_including_tax': get_price_including_tax(soup),
        'price_excluding_tax': get_price_excluding_tax(soup),
        'number_available': get_number_available(soup),
        'product_description': get_product_description(soup),
        'category': get_category(soup),
        'star_rating': get_star_rating(soup),
        'review_rating':get_review_rating(soup),
        'image_url': get_image_url(soup)
    }
    save_to_csv(data)

