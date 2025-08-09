def password(correct_password = "admin"):
    return correct_password =="admin"
    
def username(my_name = "Enoch"):
    return my_name == "Enoch"
    
def valid_email(email):
    if '@'  and '.' in email:
        return True
    else:
         return False 
         
def uppercase(alphabet):
    for k in alphabet:
        if k.isupper():
            return True 
    return False 
    
def lowercase(password):
    for char in password:
        if char.islower():
            return True 
    return False 
    
def specialchar(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    for char in password:
      if char in special_characters:
        return True 
    return False 
    
def number(password):
    for char in password:
        if char.isdigit():
            return True 
    return False 
    
def length(password):
    for char in password:
        if len (password) >= 6:
            return True 
    return False 
def validate_password(password):
   if uppercase(password) == True and lowercase(password) ==True and number(password) == True and length(password) == True and specialchar(password) == True:
   else:
       return False 
        
def firstname(name):
    if name.isalpha():
        return True 
    else:
        return False
        
def firstname_len(name):
    if len (name) > 1:
        return True 
    else:
        return False 
        
def name_verify(name):
    if first_len(name) == True and firstname(name) == True:
        return True 
    else:
        return False 
        
def phone_no(phone):
    if phone.isdigit():
        return True 
    else:
        return False                 
        