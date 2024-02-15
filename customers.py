import csv

customers = {
    'mel': {'username': 'mel', 'password': 'password', 'name': 'Mel Wilson'},
    'squash': {'username': 'squash', 'password': '1234', 'name': 'Sara Squash'},
    'bunsen': {'username': 'bunsen', 'password': 'muppet', 'name': 'Bunsen Honeydew'},
    'hoon': {'username': 'hoon', 'password': 'blindmelon', 'name': 'Shannon Hoon'}
}

def get_by_username(username):
    return customers.get(username)

class Melon :

    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url =image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        return (
            f"<Melon: {self.melon_id}, {self.common_name}>"
        )
    
    def print_str(self):
        return f"${self.price:.2f}"
    
    def get_with_id(melon_id):
        return melon_dict[melon_id]
                          
    def all_melons():     
        return list(melon_dict.values())

melon_dict = {}


with open('melons.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row['melon_id']
        melon = Melon(
            melon_id,
            row['common_name'],
            float(row['price']),
            row['image_url'],
            row['color'],
            eval(row['seedless'])
        )
        melon_dict[melon_id] = melon

print(melon)