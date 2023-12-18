class Restaurant:
    # List to store all instances of restaurants
    all_restaurants = []

    # Constructor method to put a new restaurant with a name
    def __init__(self, name):
      
        self.name = name

        self.reviews = []

        # Adding current restaurant instance to the list of all restaurants
        Restaurant.all_restaurants.append(self)

    # Method to get the name of the restaurant
    def get_name(self):
        print(self.name)

    # Class method to get all instances of restaurants
    @classmethod
    def get_all(cls):
        print(cls.all_restaurants)

    def print_reviews(self):
        print(self.reviews)

    def get_customers(self):
        print(list(set(review.get_customer() for review in self.reviews)))

    # Method to calculate and return the average star rating for the restaurant
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)

