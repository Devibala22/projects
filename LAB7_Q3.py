def remov_extra_space(msg):
    return" ".join(msg.split())
user_msg=input("Enter your message:")
res=remov_extra_space(user_msg)
print("Cleaned message:",res)
