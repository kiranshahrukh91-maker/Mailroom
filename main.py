# Mailroom: reads the subscribers from Data/subscribers.csv.


def read_subscribers() -> str:
    file = open("Data/subscribers.csv")
    text: str = file.read()
    file.close()
    return text
    
    



print(read_subscribers())
    
