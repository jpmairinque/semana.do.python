
print("A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?")

bullets, dragons = int(input("How many bullets? ")), int(input("How many dragons? "))


def hero(bullets, dragons):
    print(bullets >= dragons * 2)

hero(bullets,dragons)

