class Review:
    # List to store all instances of reviews
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # Give customer, restaurant, and rating to the review instance
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        # Adding current review instance to list of all reviews
        Review.all_reviews.append(self)

        # Appending review to customer's reviews and restaurant's reviews
        customer.reviews.append(self)
        restaurant.reviews.append(self)

    def get_rating(self):
        return self.rating

    # Class method to get all instances of reviews
    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews

    #Method to get customer assosiacted with the review
    def get_customer(self):
        return self.customer

    # Method to get the restaurant associated with the review
    def get_restaurant(self):
        return self.restaurant
