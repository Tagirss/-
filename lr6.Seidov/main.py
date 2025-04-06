from modules import *
if __name__ == "__main__":
    print_modules_result(10,20,30,25,15,5)
    print(random_number(1,5))
    print(random_choice_from_list([4,6,3,7,4]))
    print(square_root(9))
    print(factorial(5))
    print(round_up(4.34))
    print(set_and_get_locale())
    print(format_number_with_locale(43))
    print(format_currency(56))
    print(precise_division(5.4, 8.5))
    print(set_precision_and_round(4.76,2))
    print_book_details(Book("title", "author"))
    print(average_student_age([Student("Alice","Hill", 20, [5,4,5,5]), Student("Max","Ol", 30, [3, 4, 2])]))
    cars = {
    "Model S": Car("Tesla", "Model S", 2020, 15000),
    "Civic": Car("Honda", "Civic", 2018, 50000)
    }
    print(get_car_by_model(cars, "Civic"))
    update_car_mileage(Car("bmw", "i5", "2005", 4.5), 5.6)
    print(create_new_student("alex","went", 12, [4,5,4,3]))
    
