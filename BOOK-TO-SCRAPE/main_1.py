from data_extraction import *
from stockage_csv import save_to_csv




book_to_scrape = 'https://books.toscrape.com/'

def get_category_links(start_url):
    soup = get_soup(start_url)
    category_list = []
    list_link = soup.find('ul', class_= 'nav').find_all('li')
    for a in list_link:
        category_list.append(start_url + a.find('a')['href'])
    category_url = category_list[1:]
    return category_url



def get_books_by_category(cat_url):
    base_url = 'https://books.toscrape.com/catalogue'
    all_books_url = []
    while True:
        #Collecte le Urls des livres de la catégorie choisie
        cat_soup = get_soup(cat_url)    
        #books = cat_soup.find_all('h3')
        book_urls = [base_url + book.find('a')['href'].replace('../../..', '') for book in cat_soup.find_all('h3')]
        all_books_url.extend(book_urls)

        #Verifie si une page suivante existe et met à jour cat_url sinon sort de la boucle
        next_button = cat_soup.find(class_='next')
        if next_button:
            next_page_partial_url = next_button.find('a')['href']
            # Construit correctement l'URL de la page suivante 
            cat_url = "/".join(cat_url.split("/")[:-1]) + "/" + next_page_partial_url
        else:
            break
    return all_books_url




category_urls = get_category_links(book_to_scrape)
for cat_url in category_urls:
    books_urls = get_books_by_category(cat_url)
    for book_url in books_urls:
        soup = get_soup(book_url)

        data = {
            'product_page_url': book_url,
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
        print(data)

