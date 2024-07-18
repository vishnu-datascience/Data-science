#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self,name    = input('Enter your name:-  '),
                last_name      = input('Enter last name:-  '),
                city           = input('Enter your city:-  '),
                user_id        = input('Enter preferred user_id:-  '),
                password       = input('Enter your password:-  '),
                phone          = input('Enter phone number:-  ')):
        self.name     =  name
        last_name     =  last_name
        city          =  city
        user_id       =  user_id
        password      =  password
        phone         =  phone
    
    def login(self):
        attempts = 1
        
        while True:
            signin = input('Enter Your user_id:-  ')
            password = input('Enter password:-  ')
            
            if signin == self.user_id and password == self.password:
                print('successfully loged in')
                break
            else:
                if attempts==3:
                    print('maximum attemps reached, call customer care reset password')
                    break
                else:
                        print('user_id or password is invalid')
                        attempts +=1
                        continue


# In[2]:


## instantiating a class and create a object for the class. Here bank is an object for class Account
bank = Account()


# In[3]:


# calling method
bank.login()


# In[ ]:




