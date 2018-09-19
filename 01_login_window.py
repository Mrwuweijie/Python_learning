#coding = utf-8
"""
要求：编写登录接口
    输入用户名密码
    认证成功后显示欢迎信息
    输错三次后锁定
"""
customer_info = {"Henry" : "123456", "Bob" : "789"}

MAX_input_count     = 3
user_input_count    = 0

#TODO:  增加从配置文件读取用户名和密码的功能；
#       新输入的账号密码显示记录在配置文件中，可以考虑增加时间等信息
#       最大输入次数可以从配置文件中读取

print(" Welcome to xxx.com!\n")
print(" Please enter your account password:\n")
while user_input_count < MAX_input_count :

    input_account_name = str(input("Input your account name: "))
    if input_account_name in customer_info.keys() :
        input_password = str(input("Please enter your passward: "))
        if input_password == customer_info[input_account_name] :
            print("Login successfully!")
            break
        else :
            print("User's name or passward is wrong!\n")
            user_input_count += 1
    else :
        print("Whether to creat a new account?")
        confirm_data = str(input('Y or N ? '))
        if confirm_data == 'Y' :
            new_user_name = str(input("Enter new username: "))
            new_password = str(input("Enter new password: "))
            customer_info[new_user_name] = new_password
            print("New aaccount has created!")
            break
        else :

            break

else :
    print("You have try too much time! Please try later!")
