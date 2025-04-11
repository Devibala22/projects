def count_good_occurrences(feedback):
    words = feedback.lower().split()
    return words.count("good")

feedback = input("Enter your feedback: ")
count = count_good_occurrences(feedback)
print(f"\nThe word 'good' appears {count} times in the feedback.")
