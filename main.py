from customer import Customer
from restaurant import Restaurant
from review import Review

# Create customer instances
customer1 = Customer("George", "Washington")
customer2 = Customer("Lia", "Wars")

# Define restaurant1,2 (assuming Restaurant takes a name as its argument)
restaurant1 = Restaurant("Shop Corner")
restaurant2 = Restaurant("Runners Bay")


review1 = customer1.add_review(restaurant1, 4)
review2 = customer2.add_review(restaurant1, 5)
review3 = customer1.add_review(restaurant2, 2)

# Access information
print(customer1.get_full_name())
print(restaurant1.average_star_rating()) 
print(Customer.find_by_name("George Washington")) 
print(Customer.find_all_by_given_name("George"))