
response={}
response["Hi"]="Hi! I am a chatbot"
response["Hello"]="Hello!"


x=input("say: ")
x=str(x)
if x not in response:
    print("Sorry I can not answer it")
else:

    print(response[x])
