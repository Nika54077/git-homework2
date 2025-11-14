classes = {"Robotics", "Debate", "Art"}

classes.add("Music")
classes.add("Art")
print(classes)
a = input("შეიყვანეთ კლასი:")
if a in classes:
    print(f"{a} არის სეტში")
else:
    print(f"{a} არ არის სეტში")

morning_classes = {"Math", "Robotics", "Art"}
afternoon_classes = {"Art", "Science", "Robotics"}

common = morning_classes & afternoon_classes
print("საერთო გაკვეთილები:", common)