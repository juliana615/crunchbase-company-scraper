from crunchbase import Crunchbase
import json

def get_credentials():
    with open('credentials.json') as file:
        credentials = json.load(file)
    return credentials

def get_urls():
    with open('urls.json') as file:
        urls = json.load(file)

def get_data():
    credentials = get_credentials()
    crunchbase_urls = get_urls()

    crunchbase = Crunchbase()

    crunchbase.login(email=credentials.get('email'), password=credentials.get('password'))

    crunchbase_data = list()

    for name, url in crunchbase_urls.items():
        data = crunchbase.process_profile(pro=True, name=name, url=url)
        if data is not None:
            crunchbase_data.append(data)

        # Writes the scraped data to the JSON file
        with open('data/demo_crunchbase_data.json', 'w', newline='') as json_file:
            json.dump(crunchbase_data, fp=json_file, indent=3, ensure_ascii=False)
        
def main():
    get_data()

if __name__ == '__main__':
    main()