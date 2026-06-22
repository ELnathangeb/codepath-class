# # def most_endangered(species_list):
# #     smallest = species_list[0]['population']
# #     animal = species_list[0]["name"]
# #     for species in species_list:
# #         if species['population'] < smallest:
# #             smallest = species['population']
# #             animal = species["name"]
# #     return animal

    


# # species_list = [
# #     {"name": "Amur Leopard",
# #      "habitat": "Temperate forests",
# #      "population": 84
# #     },
# #     {"name": "Javan Rhino",
# #      "habitat": "Tropical forests",
# #      "population": 72
# #     },
# #     {"name": "Vaquita",
# #      "habitat": "Marine",
# #      "population": 10
# #     }
# # ]

# # print(most_endangered(species_list))


# # def count_endangered_species(endangered_species, observed_species):
# #     endangered_set = set(endangered_species)
# #     count = 0

# #     for species in observed_species:
# #         if species in endangered_set:
# #             count += 1
# #     return count



# # endangered_species1 = "aA"
# # observed_species1 = "aAAbbbb"

# # endangered_species2 = "z"
# # observed_species2 = "ZZ"

# # print(count_endangered_species(endangered_species1, observed_species1)) 
# # print(count_endangered_species(endangered_species2, observed_species2))  


# # def navigate_research_station(station_layout, observations):
# #     current_position = 0
# #     total_time = 0
# #     for char in observations:
# #         for index,char2 in enumerate(station_layout):
# #             if char == char2:
# #                 total_time += abs(current_position - index)
# #                 current_position = index
# #     return total_time



# # station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# # observations1 = "wildlife"

# # station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# # observations2 = "cba"

# # print(navigate_research_station(station_layout1, observations1))  
# # print(navigate_research_station(station_layout2, observations2))

# # def distinct_averages(species_populations):
# #   avb = set()
# #   lst = sorted(species_populations)

# #   left = 0
# #   right = len(lst) -1 
# #   while left < right:
# #     average =  (lst[left] + lst[right]) / 2
# #     avb.add(average)
    
# #     left +=1
# #     right -= 1
    
# #   return len(avb)

# #   #slower

# # #   while len(lst) > 1:
# # #     min1 = lst.pop(0)
# # #     max1 = lst.pop(-1)
# # #     a = abs(min1 + max1)/2
# # #     avb.add(a)
# # #   return len(avb)




# # species_populations1 = [4,1,4,0,3,5]
# # species_populations2 = [1,100]

# # print(distinct_averages(species_populations1))
# # print(distinct_averages(species_populations2)) 

# #q7
# def max_species_copies(raised_species, target_species):
    
#     raised_species_count = {}
#     target_species_count = {}

#     for char in raised_species:
#         if char in raised_species_count:
#             raised_species_count[char] += 1
#         else:
#             raised_species_count[char] = 1
    
#     for char2 in target_species:
#         if char2 in target_species_count:
#             target_species_count[char2] += 1
#         else:
#             target_species_count[char2] = 1
    
#     copies = float('inf')
    
#     for letter in target_species_count:
#         if letter not in raised_species_count:
#             return 0
#         copies = min(copies, raised_species_count[letter] // target_species_count[letter])

#     return copies



# raised_species1 = "abcba"
# target_species1 = "abc"
# print(max_species_copies(raised_species1, target_species1))  # Output: 1

# raised_species2 = "aaaaabbbbcc"
# target_species2 = "abc"
# print(max_species_copies(raised_species2, target_species2)) # Output: 2



def prioritize_observations(observed_species, priority_species):
    priority_species_set = set(priority_species)
    x = priority_species_set.extend(observed_species)
    return x
        
    



observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 