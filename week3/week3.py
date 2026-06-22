# # def is_valid_post_format(posts):
# #     stack = []
# #     matches = {
# #         ')': '(',
# #         ']': '[',
# #         '}': '{'
# #     }
    
# #     for char in posts:
# #         if char in "([{":
# #             stack.append(char)
# #         elif char in ")]}":
# #             if not stack:
# #                 return False
# #             top = stack.pop()

# #             if top != matches[char]:
# #                 return False
# #     return len(stack) == 0




# # print(is_valid_post_format("()"))
# # print(is_valid_post_format("()[]{}")) 
# # print(is_valid_post_format("(]"))


# def reverse_comments_queue(comments):
#   stack = []

#   for char in comments:
#     stack.append(char)

#     reverse = []
#   while stack:
#     reverse.append(stack.pop())
#   return reverse






# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# def is_symmetrical_title(title):

#     y = title.replace(" ", "")
#     z = y.lower()
#     left = 0
#     right = len(z) - 1
    
#     while left < right:
#         if z[left] != z[right]:
#             return False
#         left += 1
#         right -= 1
#     return True




# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 


# def engagement_boost(engagements):
#     left = 0
#     right = len(engagements) -1
#     result = [0] * len(engagements)
#     position = len(engagements) - 1

#     while left <= right:
#         L = engagements[left] * engagements[left]
#         R = engagements[right] * engagements[right]
#         if L > R:
#             result[position] = L
#             left +=1 
#         else:
#             result[position] = R
#             right -= 1
#         position -= 1
        
#     return result

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))

# def clean_post(post):
#     stack = []
    
#     for char in post:
#         if stack and char.swapcase() == stack[-1]: #i think this checks if both of them have 
#             stack.pop()
#         else:
#             stack.append(char)
#     return "".join(stack) #this turns it back into. string basicaly you join them with "

# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 

# from collections import deque 
# def edit_post(post):
#     p = post.split() #split it to make it easier
#     result = [] #Make a new list to store the new want

#     for word in p:
#         queue = deque() #Made a que for each word[char]

#         for char in word:
#             queue.appendleft(char)# this adds eacj character tp the ;eft so it woud be like B then OB

#         rev_word = "".join(queue) #this makes it into a word
#         result.append(rev_word) #this adds all the wordds together
#     return " ".join(result) #this makes the wrods into a sentece




# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 


# def proces_text(draft):
#     stack = []

#     for char in draft:
#         if char == "#":
#             if stack:
#                 stack.pop()
#             else:
#                 stack.append(char)
#     return "".join(stack)

# def post_compare(draft1, draft2):
#     return proces_text(draft1) == proces_text(draft2)




    
# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 


# def manage_stage_changes(changes):
#     stack = []

#     for word in changes:
#         if stack and word == "Cancel":
#             stack.pop()
#         else:
#             stack.append(word)

#         letter = []

#         for i in stack:
#             i.split()
#             letter.append(i[-1])
#     return letter
        






# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


from collections import deque
def process_performance_requests(requests):
    order = []

    queue = deque()

    for number, word in requests:
        if 









print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
