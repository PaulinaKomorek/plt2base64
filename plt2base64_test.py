import matplotlib.pyplot as plt
import plt2base64

def to_base64_test():
    plt.plot([0, 1, 2], [0, 1, 2])
    output = plt.to_base64()
    with open("valid.txt", "r") as fs:
        valid=fs.read()
        assert output==valid 

to_base64_test()

