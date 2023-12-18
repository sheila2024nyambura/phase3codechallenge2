from review import Review

class Customer:
    # List to keep all instances of customers
    all_customers = []

    # Constructor method to put a new customer with given and family names
    def __init__(self, given_name, family_name):
     
        self.given_name = given_name
        self.family_name = family_name

        # Adding current customer instance to list of all customers
        Customer.all_customers.append(self)

        self.reviews = []

    # Method to get the given name of the customer
    def get_given_name(self):
        return self.given_name

    # Method to get the family name of the customer
    def get_family_name(self):
        return self.family_name

    # Method to get the full name of the customer
    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def get_all(cls):
        return cls.all_customers

    # getting the number of reviews  by the customer
    def get_num_reviews(self):
        return len(self.reviews)

    # method to find a customer by their full name
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.get_full_name() == name:
                return customer
        return None

    # Class method to find all customers with a given name
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.get_given_name() == name]

    # adding a new review for the customer
    def add_review(self, restaurant, rating):
       
        review = Review(self, restaurant, rating)

        # Adding the review to the list of reviews for this customer
        self.reviews.append(review)
        
      
        return review

    def get_restaurants(self):
        return list(set(review.get_restaurant() for review in self.reviews))
