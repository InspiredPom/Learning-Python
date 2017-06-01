import random
import time
choices=[
"Yes",
"No",
"Probably",
"Probably Not"
]
while True:
    input("Ask a Simple Yes or No Question\n")
    for i in range(0,1):
        print("*Shakes Metaphorical Magic Ball*\n...")
        time.sleep(1)
        print("*Shakes Metaphorical Magic Ball Again*\n...")
    print(random.choice(choices))
    print("\n")
    break;