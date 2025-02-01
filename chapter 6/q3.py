p1 = "make a lot of money"
p2 = "subscribe now"
p3 = "click this"
p4 = "buy now"

message = input("enter the message : ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("the messge is a spam message")

else:
    print("the message is not spam")