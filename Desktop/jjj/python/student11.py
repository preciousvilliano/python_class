name = input("Enter your student name: ")
gender = input("Enter student gender: ")
age = int(input("Enter student age: "))
phone_num = input("Enter your sudent phone number: ")
email_address =input("Enter your student email address: ")

print(f'Student Name: {name}')
print(f'Student gender: {gender}')
print(f'Student age: {age}')
print(f'Student phone number: {phone_num}')
print(f'Student email: {email_address}')

def student_info():
    name = input("Enter your student name: ")
    gender = input("Enter student gender: ")
    age = int(input("Enter student age: "))
    phone_num = input("Enter your sudent phone number: ")
    email_address =input("Enter your student email address: ")

    print(f'Student Name: {name}')
    print(f'Student gender: {gender}')
    print(f'Student age: {age}')
    print(f'Student phone number: {phone_num}')
    print(f'Student email: {email_address}')
    
    return name,gender,age,phone_num,email_address