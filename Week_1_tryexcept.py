
while True:
    user_input= input("Enter the number:")
    numnber=int(user_input)

    try:
        result=10/numnber
        print(f"the result is {result}")

    except ZeroDivisionError as e:
        print("An Error Occured!")

    else: 
        print("No exception happened:)")