nums=[]

while True:
    num=int(input(">"))
    nums.append(num)
    sing=input(">")
    nums.append(sing)
    num=int(input(">"))
    nums.append(num)

    if input(">")=="=":
        if sing=="+":
            result=nums[0]+nums[2]
        elif sing=="-":
            result=nums[0]-nums[2]
        elif sing=="*":
            result=nums[0]*nums[2]
        elif sing=="/":
            result=nums[0]/nums[2]
        elif sing=="**":
            result=nums[0]**nums[2]
print(result)
