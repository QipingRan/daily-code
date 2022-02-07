def isvalid(nums):
    for i in range(1, 10):
        if i not in nums:
            return False

    if nums[2]+nums[4]+nums[6]!=15:
        return False
    if nums[0]+nums[4]+nums[8]!=15:
        return False

    for i in range(2):
        if nums[3*i]+nums[1+3*i]+nums[2+3*i]!=15:
            return False
        if nums[i]+nums[i+3]+nums[i+6]!=15:
            return False
    
    return True

def main():
    f=open("./input.txt.txt")
    for line in f:
        nums=list(map(int, line.split()))

        if isvalid(nums):
            print("valid")
        else:
            print("unvalid")

    f.close()




    
        
    
    




main()
