#!/usr/bin/env python
# coding: utf-8

# In[12]:


#assingning elements to different list
list1=[]
n=int(input("enter the number of elements you want to enter in the list"))
for x in range(0,n):
    list1.append(input("enter the a data for the list (To enter new data click enter on your keyboard)"))
    
    
print("Your list ",list1)

#changing a value in list 1
m=int(input("Enter the index number where you want to change the value in the list "))

if(m<len(list1)):
    ele=input("Enter new data")
    list1[m]=ele
    
else:
    print("the index you have entered is out of range for the list")
    

print(list1)    


# In[8]:


#acessing elements from a tuple
mytup=(1,2,3,"machine","learning","lets go")
print(mytup)
n=int(input("enter the index of the element that you would like to acesses: "))

if (n<6):
    print("acessed element is:",mytup[n])
    print("\n")

else:
    print("enter a number in the range from 0 to 5")
    
print("All the other elements of the tupples are:")
for i in range(0,len(mytup)):
    print(mytup[i])


# In[1]:


#Deleting different dictionary elements
mydict={"India":"Indian rupees","U.S.A":"dollars","Russia":"Russian Ruble","Canada":"canadian dollar","france":"european euro","japan":"japanese yen",}
print(mydict)
n=int(input("How many elements do to want to delete "))
for i in range(0,n):
    ele=input("enter the key from the dictionary which you want to delete ")
    del mydict[ele]
    print("Dictionary after deleting key value pair of the key ",ele," is",mydict)
    
print("Final dictionary is :",mydict)


# In[ ]:




