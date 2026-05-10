import requests # Importing Requests
from bs4 import BeautifulSoup # Importing BeutifulSoup From Bs4
import csv # importing CSV To Make Files

def scrape_laptops(url, output_file):
    # 1. Fetching The Webpage
    # Adding a 'User-Agent'
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    # 2. Parse The HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Locate All Product Containers
    # On This Site, Laptops Are Inside Div Tags With Yhe Class 'thumbnail'
    products = soup.find_all('div', class_='thumbnail')
    
    product_data = []

    # 4. Extract Product Name And Price
    for item in products:
        # The Product Name Is Inside An <a> Tag With Class 'title'
        name = item.find('a', class_='title')['title']
        
        # The Price Is In An <h4> Tag With Class 'price'
        price = item.find('h4', class_='price').text
        
        # Description
        desc = item.find('p', class_='description').text.strip()
        
        product_data.append([name, price, desc])

    # 5. Save To CSV
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'Description']) # Header row
            writer.writerows(product_data)
        print(f"✅ Successfully saved {len(product_data)} laptops to {output_file}")
    except IOError as e:
        print(f"❌ Error writing to CSV: {e}")

# Run The Function
if __name__ == "__main__":
    # A reliable practice URL for laptops
    TARGET_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    OUTPUT_FILENAME = "laptops.csv"
    scrape_laptops(TARGET_URL, OUTPUT_FILENAME)
