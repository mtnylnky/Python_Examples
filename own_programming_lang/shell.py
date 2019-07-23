import anka
while True:
    text=input("anka >>> ")
    result, error=anka.run('<stdin>',text)

    if error:print(error.as_string())
    else:print(result)