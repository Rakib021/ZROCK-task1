def key_val_dict(dict,key):
  if key in dict:
    del dict[key]
    return True
  else:
    return False
  
my_dict ={'a':1,'b':2,'c':3,'d':4,'e':5}
remove_key = input("enter removing key into dictionary :")

if key_val_dict(my_dict,remove_key):
  print("successfully removed key" , my_dict)
else:
  print("failed to remove key")