import requests
from bs4 import BeautifulSoup

#Prompt the user to enter ISBN, publication number, and author name
isbn = input("Enter ISBN: ")
pub_number = input("Enter Publication Number: ")
author_name = input("Enter Author Name: ")

def search_publications(isbn, pub_number, author_name):
    """
    Searches the web for publications based on ISBN, publication number, and author name.

    Parameters:
    - isbn (str): The ISBN of the publication.
    - pub_number (str): The publication number.
    - author_name (str): The name of the author.

    Returns:
    None
    """
    # Construct the search query
    search_query = f"{isbn} {pub_number} {author_name}"
    
    # Example: Search on Google
    url = f"https://www.google.com/search?q={search_query}"

    try:
        # Send an HTTP GET request to the search engine
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML response
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all search result links
            search_results = soup.find_all('a')

            # Print each search result link
            for result in search_results:
                link = result.get('href')
                print(link)

    except Exception as e:
        # Handle any errors that occur during the process
        print(f"An error occurred: {e}")



#Call the search_publications function with the provided parameters
search_publications(isbn, pub_number, author_name)
