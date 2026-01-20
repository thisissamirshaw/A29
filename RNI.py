# WAP similar to Two Sum problem but 
# we have to return the two numbers instead of their indices.
# For example, given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [2, 7].
lt = [2,7,11,15,9,0]
target=9
for i in range(len(lt)):                                      #TC O(n^2)
    for j in range(i+1, len(lt)):
        if lt[i] + lt[j] == target:
            print(lt[i],lt[j])
            #break
        # else:
        #     print(None)
    #break     

# # #WAP similar to Two Sum problem but we have to return the two numbers instead of their indices.
# # # For example, given nums = [2, 7, 11, 15], target = 9,
# # # Because nums[0] + nums[1] = 2 + 7 = 9,
# # # return [2, 7].
# # def two_sum(nums, target):
# #     num_dict = {}
# #     for i, num in enumerate(nums):
# #         complement = target - num
# #         if complement in num_dict:
# #             return (num_dict[complement], num)
# #         num_dict[num] = i
# #     return None
# # # Now without using function in Normal Input Output format, also state that 
# # # Which programming paradigm it belongs to.
# # nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# # target = int(input("Enter the target sum: "))
# # result = two_sum(nums, target)
# # if result:
# #     print("The two numbers that add up to the target are:", result)
# # else:
# #     print("No two numbers add up to the target.")
# # # This code follows the Procedural Programming paradigm 
# # # as it is structured around procedures or routines (functions) to operate on the data.
# # #Explain why in details it comes under that paradigm, POP is a programming paradigm
# # # that is based on the concept of procedure calls, where procedures (also known as routines,
# # # subroutines, or functions) are a set of instructions that perform a specific task.

# # In POP, the program is divided into small parts called procedures,
# # which can be called and executed independently. Each procedure can take input parameters,
# # perform operations on them, and return output values. The main focus of POP is on the
# # sequence of actions to be performed, rather than the data itself.
# # In the provided code, the two_sum function is a procedure that takes a list of numbers
# # and a target sum as input parameters. It performs a series of operations to find
# # two numbers that add up to the target sum and returns them as output. The program
# # is structured around this procedure, which is called with specific inputs to achieve
# # the desired outcome. This procedural approach to solving the problem is characteristic
# # of the Procedural Programming paradigm.

# #Now do the program entirely in POP without functions.
# nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# target = int(input("Enter the target sum: "))
# num_dict = {}
# result = None
# for i, num in enumerate(nums):
#     complement = target - num
#     if complement in num_dict:
#         result = (complement, num)
#         break
#     num_dict[num] = i
# if result:
#     print("The two numbers that add up to the target are:", result)
# else:
#     print("No two numbers add up to the target.")
# # This code follows the Procedural Programming paradigm 
# # as it is structured around procedures or routines (functions) to operate on the data.
# #Explain why in details it comes under that paradigm, POP is a programming paradigm
# # that is based on the concept of procedure calls, where procedures (also known as routines,
# # subroutines, or functions) are a set of instructions that perform a specific task.
# # In POP, the program is divided into small parts called procedures,
# # which can be called and executed independently. Each procedure can take input parameters,
# # perform operations on them, and return output values. The main focus of POP is on the
# # sequence of actions to be performed, rather than the data itself.
# # In the provided code, the logic to find two numbers that add up to the target sum
# # is implemented directly in the main body of the program without encapsulating it
# # within a function. The program follows a sequence of steps to achieve the desired outcome,
# # which is characteristic of the Procedural Programming paradigm.

# #Now do the program entirely in POP without functions and only using list data structure
# nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# target = int(input("Enter the target sum: "))
# result = None
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             result = (nums[i], nums[j])
#             break
#     if result:
#         break
# if result:
#     print("The two numbers that add up to the target are:", result)
# else:
#     print("No two numbers add up to the target.")
# # This code follows the Procedural Programming paradigm 
# # as it is structured around procedures or routines (functions) to operate on the data.
# #Explain why in details it comes under that paradigm, POP is a programming paradigm
# # that is based on the concept of procedure calls, where procedures (also known as routines,
# # subroutines, or functions) are a set of instructions that perform a specific task.
# # In POP, the program is divided into small parts called procedures,
# # which can be called and executed independently. Each procedure can take input parameters,
# # perform operations on them, and return output values. The main focus of POP is on the
# # sequence of actions to be performed, rather than the data itself.
# # In the provided code, the logic to find two numbers that add up to the target sum
# # is implemented directly in the main body of the program without encapsulating it
# # within a function. The program follows a sequence of steps to achieve the desired outcome,
# # which is characteristic of the Procedural Programming paradigm.