

def is_unique(my_str):
    if len(my_str) > 128:
        return False
    for cnt in range(0, len(my_str)-1):
        print("bedore second for")
        for i in range(cnt+1, len(my_str)):
            if my_str[cnt] == my_str[i]:
                return False
            print(cnt)
    return True


my_str = "abd"
print(is_unique(my_str))
