# # # # # def extract_nft_names(nft_collection):
# # # # #     x = []

# # # # #     for nft in nft_collection:
# # # # #         x.append(nft["name"])
# # # # #     return x


    

# # # # # # Example usage:
# # # # # nft_collection = [
# # # # #     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
# # # # #     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
# # # # #     {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
# # # # # ]

# # # # # nft_collection_2 = [
# # # # #     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
# # # # #     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
# # # # # ]

# # # # # nft_collection_3 = [
# # # # #     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# # # # # ]

# # # # # print(extract_nft_names(nft_collection))
# # # # # print(extract_nft_names(nft_collection_2))
# # # # # print(extract_nft_names(nft_collection_3))



# # # # # def extract_nft_names(nft_collection):
# # # # #     nft_names = []
# # # # #     for nft in nft_collection:
# # # # #         nft_names.append(nft["name"])
# # # # #     return nft_names

# # # # # #rigth now it looks like ot [rojmts pit every sinngle letter lets fix it i think it might me the +=]
# # # # # nft_collection = [
# # # # #     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
# # # # #     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# # # # # ]

# # # # # nft_collection_2 = [
# # # # #     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# # # # # ]

# # # # # nft_collection_3 = []

# # # # # print(extract_nft_names(nft_collection))
# # # # # print(extract_nft_names(nft_collection_2))
# # # # # print(extract_nft_names(nft_collection_3))


# # # # def identify_popular_creators(nft_collection):
# # # #     creator_count = {}

# # # #     for nft in nft_collection:
# # # #         creator = nft["creator"]

# # # #         if creator in creator_count:
# # # #             creator_count[creator] += 1
# # # #         else:
# # # #             creator_count[creator] = 1
# # # #     popular = []

# # # #     for creator in creator_count:
# # # #         if creator_count[creator] > 1:
# # # #             popular.append(creator)
# # # #     return popular

# # # # #so bascaily make a dict so it would be the name of the pereson and the value wil probably be the the count
# # # # #and so we made the the names into creator and then we say if it is already in reator_count we had the count to it and if not we make it 1
# # # # #and then we made a popoular list and if creator cout is mroe than 1 we retur the popular

    
# # # # #How many times does each loop run? (Time Complexity)
# # # # #How much extra memory am I creating? (Space Complexity)

# # # # # Time Complexity: O(n) because we go through the NFTs once, and then through the unique creators. Since the number of creators can't be more than the number of NFTs, it's still O(n).
# # # # # Space Complexity: O(k) because the dictionary stores one entry for each unique creator.



# # # # nft_collection = [
# # # #     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
# # # #     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
# # # #     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# # # # ]

# # # # nft_collection_2 = [
# # # #     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
# # # #     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
# # # #     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# # # # ]

# # # # nft_collection_3 = [
# # # #     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# # # # ]

# # # # print(identify_popular_creators(nft_collection))
# # # # print(identify_popular_creators(nft_collection_2))
# # # # print(identify_popular_creators(nft_collection_3))



# # # # def average_nft_value(nft_collection):
# # # #     avg = []

# # # #     if not nft_collection:
# # # #         return 0

# # # #     for nft in nft_collection:
# # # #         avg.append(nft["value"])
# # # #     x = sum(avg)/ len(avg)
# # # #     return x
    
# # # # Time Complexity: O(n), where n is the number of NFTs.
# # # # The function loops through the NFT list once to collect the values, then sum(avg) loops through the values again. This is O(n + n), which simplifies to O(n).

# # # # Space Complexity: O(n), because the avg list stores one value for each NFT in the collection.



# # # # nft_collection = [
# # # #     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
# # # #     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
# # # #     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# # # # ]
# # # # print(average_nft_value(nft_collection))

# # # # nft_collection_2 = [
# # # #     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
# # # #     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# # # # ]
# # # # print(average_nft_value(nft_collection_2))

# # # # nft_collection_3 = []
# # # # print(average_nft_value(nft_collection_3))


# # # def search_nft_by_tag(nft_collections, tag):
# # #     result = []
# # #     for collection in nft_collections:
# # #         for nft in collection:
# # #             if tag in nft["tags"]:
# # #                 result.append(nft["name"])
# # #     return result
        

# # # nft_collections = [
# # #     [
# # #         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
# # #         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
# # #     ],
# # #     [
# # #         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
# # #         {"name": "City Lights", "tags": ["modern", "landscape"]}
# # #     ]
# # # ]

# # # nft_collections_2 = [
# # #     [
# # #         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
# # #         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
# # #     ],
# # #     [
# # #         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
# # #     ]
# # # ]

# # # nft_collections_3 = [
# # #     [
# # #         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
# # #     ],
# # #     [
# # #         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
# # #         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
# # #     ]
# # # ]

# # # print(search_nft_by_tag(nft_collections, "landscape"))
# # # print(search_nft_by_tag(nft_collections_2, "sunset"))
# # # print(search_nft_by_tag(nft_collections_3, "modern"))


# # # def find_task_pair(task_times, available_time):
# # #     hash = set()
# # #     for i in task_times:
# # #         diff = available_time - i
# # #         if diff in hash:
# # #             return True
# # #         hash.add(i)
# # #     return False





# # # task_times = [30, 45, 60, 90, 120]
# # # available_time = 105
# # # print(find_task_pair(task_times, available_time))

# # # task_times_2 = [15, 25, 35, 45, 55]
# # # available_time = 100
# # # print(find_task_pair(task_times_2, available_time))

# # # task_times_3 = [20, 30, 50, 70]
# # # available_time = 60
# # # print(find_task_pair(task_times_3, available_time))



# # def find_smallest_gap(work_sessions):
# #     smallest_gap = float("inf")

# #     for i in range(len(work_sessions)- 1):
# #         current_end = work_sessions[i][1]
# #         next_start = work_sessions[i+1][0]

# #         CEM = (current_end // 100) * 60 + (current_end % 100)
# #         NSM = (next_start //100) * 60 + (next_start % 100)

# #         gap = NSM - CEM

# #         if gap < smallest_gap:
# #             smallest_gap = gap
# #     return smallest_gap

# # work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
# # print(find_smallest_gap(work_sessions))

# # work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
# # print(find_smallest_gap(work_sessions_2))

# # work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
# # print(find_smallest_gap(work_sessions_3))



# def calculate_expenses(expenses):
#     calcuate = {}
    

#     for expense, money in expenses:
#             if expense in calcuate:
#                 calcuate[expense] += money
#             else:
#                 calcuate[expense] = money
#     max1 = float("-inf")
#     name = ''
#     for ex, mon  in calcuate.items():
#         if mon > max1:
#             max1 = mon
#             name = ex

#     return (calcuate, name)
  



# expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
#             ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
# print(calculate_expenses(expenses))

# expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
#               ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
# print(calculate_expenses(expenses_2))

# expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
#               ("Utilities", 50.0), ("Food", 25.0)]
# print(calculate_expenses(expenses_3))


class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(char.isalpha() or char.isspace() for char in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")


alice = Villager("Alice", "Koala", "guvnor")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)

alice.set_catchphrase("#?!")
print(alice.catchphrase)

# apollo = Villager("Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "yip yip")
# print(bones.greet_player("Elnathan"))
# print(bones.greet_player("Samia"))

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

