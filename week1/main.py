# def reverse_sentence(sentence):
#     words = sentence.split()
#     if len(words) == 1:
#         return sentence

#     result = ""
    
#     for i in range(len(words) -1, -1, -1): #range(start, stop, step)
#         result += words[i] + " "
#     return result.strip()

# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

# sentence = "Pooh"
# print(reverse_sentence(sentence))


# def count_evens(lst):
#     count = 0

#     for i in lst:
#             if len(i) % 2 == 0:
#                 count += 1
#     return count


# lst = ["na", "nana", "nanana", "batman", "!"]
# print(count_evens(lst))

# lst = ["the", "joker", "robin"]
# print(count_evens(lst))

# lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
# print(count_evens(lst))


# def remove_name(people, secret_identity):
#     while secret_identity in people:
#         people.remove(secret_identity)
#     return people

# people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
# secret_identity = 'Bruce Wayne'
# print(remove_name(people, secret_identity))

# def count_digits(n):

#     count = 0

#     if n == 0:
#         count += 1
#         return count
#     else: 
#         while n > 0:
#             count += 1
#             n = n // 10
#         return count

# n = 964
# print(count_digits(n))

# n = 0
# print(count_digits(n))

# def lineup(artists, set_times):
#     final = dict(zip(artists, set_times))
#     return final



# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))



# def get_artist_info(artist, festival_schedule):
#     return festival_schedule.get(artist, "{'message': 'Artist not found'}")

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  


# def total_sales(ticket_sales):
#     x = ticket_sales.values()
#     result = 0

#     for i in x:
#         result += i
#     return result




# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))


# def identify_conflicts(venue1_schedule, venue2_schedule):
#     result = {}
#     for key, value in venue1_schedule.items():
#         if (key, value) in venue2_schedule.items():
#             result[key]= value
#     return result

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))
# from collections import Counter
# def best_set(votes):
#     x = votes.values()
#     c = Counter(x)
    
#     result = max(c, key=c.get)
#     return result

    


# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))


# def max_audience_performances(audiences):
#     m = max(audiences)
#     count = 0
#     for i in audiences:
#         if i == m:
#             count += i
#     return count



# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

def max_audience_performances(audiences):
    d = {}

    



audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
