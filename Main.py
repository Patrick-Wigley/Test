
print("Task One:")
def count_sum(num):
    sum = 0
    nums = [i for i in str(num) if i.isdigit()]
    count = len(nums)
    for i in nums:
        
        sum += int(i)
        

    print(f"Count of digits is {count}")
    print(f"Total sum is: {sum}")
      

count_sum(input("Input your numbers: "))
print("\n") # Creating space in terminal

print("Task Two:")
def group_by_owners(file_dict):
    organised_dict = {} 
    names_collected = []

    for k, w in file_dict.items():

        if w not in names_collected:
            names_collected.append(w)
            organised_dict.update({w: [k]})
            
        else:
            organised_dict[w].append(k)


    print(organised_dict)


   
   
file_dict_example = {"Input.txt": "Dan", "Main.py": "Stan", "Other_File.txt": "Dan"}
group_by_owners(file_dict_example)

