import numpy as np

def test_output(alg1, alg2, input):
    ting1 = "outputs/" + input + "_" + alg1 + ".out"
    ting2 = "outputs/" + input + "_" + alg2 + ".out"
    with open(ting1, "r") as infile1, open(ting2, "r")  as infile2:
        print(ting1, ting2, infile1.read() == infile2.read())

if __name__ == "__main__":
    bingus = []
    dingus = []
    with open("outputs/nearly_sorted_1000_heap.out", "r") as infile1, open("outputs/nearly_sorted_1000_selection.out", "r")  as infile2:
        for line in infile1:
            line = int(line)
            bingus.append(line)
        for line in infile2:
            line = int(line)
            dingus.append(line)
    bingus = np.array(bingus)
    dingus = np.array(dingus)
    print(bingus == dingus)
    """
    algs = ["quick", "insertion", "heap", "selection"]
    files = ["nearly_sorted_", "random_"]

    for i in range(1,5):
        for j in range(3):
            for m in range(2):
                test_output(algs[j], algs[j+1], files[m] + str(10**i))
    """
