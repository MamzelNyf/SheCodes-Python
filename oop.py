# Q1
class Book:
    def __init__(self, title, author, num_pages,current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1

    def bookmark_page(self,page_number):
        self.bookmarked_page = page_number

    def go_to_page(self,page_number):
        self.current_page = page_number

    def move_bookmark(self):
        self.bookmarked_page = self.current_page

    def turn_page(self, forward):
        if forward:
            if self.current_page == self.num_pages:
                self.current_page = 1
            else: 
                self.current_page += 1
        else:
            if self.current_page == 1:
                self.current_page = self.num_pages
            else: 
                self.current_page -= 1
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages


book_1 = Book("Cats", "Real Person", 213,1)
# print(book_1.title)

# 1. Go directly to a specific page number.
book_1.go_to_page(34)
print(book_1.current_page)

# 2. Bookmark a specific page number, i.e. not just the current page.
book_1.bookmark_page(53)
print(book_1.bookmarked_page)

# 3. Automatically go back to the start of the book (i.e. page 1) when the user turns the final page.
book_1.go_to_page(213)
print(book_1.current_page)
book_1.turn_page(True)
print(book_1.current_page)
book_1.turn_page(False)
print(book_1.current_page)

print() 

# Q2

# importing math library to be able to use sqrt() square root function
# from math import sqrt

class Rectangle:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width

    def __str__(self):
        if self.heigth == self.width:
            return f"This is a square with a width of {self.width}cm"
        else:
            return f"This is a rectangle with a width of {self.width}cm and a heigth of {self.heigth}cm"

    def square_or_not(self):
        if self.heigth == self.width:
            print(f"This is a square with a width of {self.width}cm")
        else:
            print(f"This is a rectangle with a width of {self.width}cm and a heigth of {self.heigth}cm")

    def area(self):
        self.area = self.heigth * self.width 
    
    def perimeter(self):
        self.perimeter = 2*(self.heigth+self.width)

    def diagonal(self):
        # **2 gives square, **0.5 gives square root
        self.diagonal = (self.heigth**2 + self.width**2)**0.5
        # using pow(x,y): Return x raised to the power y.
        # self.diagonal = pow(pow(self.heigth, 2) + pow(self.width,2),0.5)

    # using sqrt() function
    # def diagonal(self):
    #     self.diagonal = sqrt(pow(self.heigth, 2) + pow(self.width,2))


rectangle_1 = Rectangle(4,5)
print(rectangle_1) # using __str__
rectangle_1.square_or_not() # using a method

print() 

rectangle_1.area()
print(f"The shape has an area of {rectangle_1.area}cm")

rectangle_1.perimeter()
print(f"The shape has an perimeter of {rectangle_1.perimeter}cm")

rectangle_1.diagonal()
print(f"The shape has a diagonal of {rectangle_1.diagonal}cm")

print() 

rectangle_2 = Rectangle(5,5)
print(rectangle_2)
rectangle_2.square_or_not()

print() 

# Q3

class Vehicle:
    def __init__ (self, make, model, colour, seating_capacity,max_speed,max_fuel,fuel_available):
        self.make = make
        self.model = model
        self.colour = colour
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed
        self.max_fuel = max_fuel
        self.fuel_available = fuel_available
        self.fuel_consumption_per_km = 1


    def __str__(self):
        return f"This {self.make} {self.model} is {self.colour}, with {self.seating_capacity} seats and can drive up to {self.max_speed}km/h"

    def rev_engine(self):
        print("VRRRMMMM!")

    

    def fuel_left(self, distance_driven, refuelled, distance_after_refuelled):
        
        def fuel_comparison(fuel_available):
            if fuel_available < 20 and fuel_available > 0: 
                print(f"You have only {fuel_available}L of fuel left. Refuelled urgently!")
            elif fuel_available > 20:
                print(f"You have {fuel_available}L of fuel left.")
            else:
                print(f"You are out of gaz.")
        
        if distance_driven > self.fuel_available:
            max_distance = self.max_fuel - self.fuel_available
            print(f"You can drive maximum {max_distance}km with your leftover fuel.")
        elif refuelled and distance_after_refuelled == 0:
            self.fuel_available = self.max_fuel
            print("Your tank is full")
        elif refuelled and distance_after_refuelled != 0:
            self.fuel_available = self.max_fuel - (distance_after_refuelled * self.fuel_consumption_per_km)
            fuel_comparison(self.fuel_available)
        else:
            self.fuel_available -= (distance_driven * self.fuel_consumption_per_km)
            fuel_comparison(self.fuel_available)

        

vehicle_1 = Vehicle("Peugeot", "206", "blue", 4, 150, 100, 50)
print(vehicle_1)
vehicle_1.rev_engine()
vehicle_1.fuel_left(23,False,0)
vehicle_1.fuel_left(15,False,0)
vehicle_1.fuel_left(12,False,0)
vehicle_1.fuel_left(0,True,0)
vehicle_1.fuel_left(48,False,20)
vehicle_1.fuel_left(25,True,85)
vehicle_1.fuel_left(100,True,40)





