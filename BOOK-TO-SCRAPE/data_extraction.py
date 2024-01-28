from bs4 import BeautifulSoup
import requests


# Fonctions de récupération des données

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'lxml')

def get_category(soup):
    try : 
       return soup.find('ul', class_='breadcrumb').find_all('a')[2].text.strip()
    except Exception:
        return None

def get_universal_product_code(soup):
    try: 
        return soup.find_all('tr')[0].td.text
    except Exception:
        return None


def get_title(soup):
    try :
        return soup.find('h1').text
    except Exception:
        return None


def get_price_including_tax(soup):
    try:
        price_including_tax = soup.find_all('tr')[3].td.text.strip()[1:] #Enlève le sigle Euros sur le prix
        return float(price_including_tax)
    except Exception:
        return None

def get_price_excluding_tax(soup):
    try : 
        price_excluding_tax = soup.find_all('tr')[2].td.text.strip()[1:] 
        return float(price_excluding_tax)
    except Exception:
        return None

def get_number_available(soup):
    try : 
        num_available_raw = soup.find_all('tr')[5].td.text
        num_available = num_available_raw.replace('In stock', '').replace('(', '').replace(')', '').replace('available', '').strip()
        return int(num_available)
    except Exception:
        return None 

def get_star_rating(soup):
    words_to_nums = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5} # Dictionnaire pour convertir les mots en nombres
    try : 
        rating_word = soup.find('p', class_='star-rating')['class'][1]
        # Convertir le mot en nombre en utilisant le dictionnaire
        return words_to_nums.get(rating_word, 0)  #Retourne la valeur de la clé si celle-ci est dans le dictionnaire. Si la clé n'est pas présente, la valeur est 0
    except Exception:
        return None  
        

def get_review_rating(soup):
    try : 
        review_number = soup.find_all('tr')[6].td.text
        return int(review_number)
    except Exception:
        return None 


def get_product_description(soup):
    try :
        return soup.find('div', id='product_description').find_next_sibling('p').text
    except Exception:
        return None 
 
def get_image_url(soup, base_url):
    try :
        return soup.find('img')['src'].replace('../../', base_url)
    except Exception:
        return None