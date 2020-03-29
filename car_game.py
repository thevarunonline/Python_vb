command=""
started=False
while True:
    command=input("> ").lower()
    if command=='start':
        if started==True:
            print("Car is already started")
        else:
            started=True
            print("Car is started")
    elif command=='stop':
        if not started==True:
            print("Car alreay stopped")
        else:
            started=False
            print("Car stopped")
    elif command=='help':
        print("""
start- to start car
stop- to stop car
quit- to exit
        """)
    elif command=='quit':
        print("exited...")
        break
else:
    print("We did not understand...PLease refer to help")

