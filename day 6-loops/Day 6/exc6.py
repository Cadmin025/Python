def movie_rating_guide():
    print("Welcome to the Hollywood Movie Rating Guide!")
    print("Rate the movie from 0 to 4 stars. Enter a negative number to quit.")
    
    total_ratings = 0
    num_ratings = 0

    while True:
        try:
            rating = float(input("Enter your rating (0-4): "))
            
            if rating < 0:
                break  # Exit the loop if a negative number is entered
            elif 0 <= rating <= 4:
                total_ratings += rating
                num_ratings += 1
            else:
                print("Invalid input. Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if num_ratings > 0:
        average_rating = total_ratings / num_ratings
        print(f"The average star rating for the movie is: {average_rating:.2f}")
    else:
        print("No ratings were entered.")

    print("Thank you for using the Hollywood Movie Rating Guide!")

# Run the program
movie_rating_guide()