# cara tidak pythonic
fileku = open("pesan.txt", "w")
fileku.write("halo kawan\nApa kabarmu hari ini ?")
fileku.close()


print(f"\nPYTHONISTA\n")

# Pythonic
with open("rockstar.txt", "w") as famousa:
    famousa.write(
        f"Assalamualaikum Warahmatullahi Wabarokatu\nApa Kabar mu kawan ?")
