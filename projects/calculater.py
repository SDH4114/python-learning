operators = "+-*/"
instance = input("> ")
current_number = ""
nums =[]
for i in instance:
    if i.isdigit():
        current_number+=i
    elif i in operators:
        nums.append(int(current_number))
        current_number = ""
        if i == "+":
            nums.append("+")
        elif i == "-":
            nums.append("-")
        elif i == "/":
            nums.append("/")
        elif i == "*":
            nums.append("*")
    elif i == "=":
        nums.append(int(current_number))
        result = nums[0]
        for el in range(1,len(nums),2):
            operators = nums[el]
            number = nums[el+1]
            if operators == "+":
                result += number
            elif operators == "-":
                result -= number
            elif operators == "*":
                result *= number
            elif operators == "/":
                result /= number
        print(result)


