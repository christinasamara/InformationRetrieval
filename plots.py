import matplotlib.pyplot as plt

def plot_metrics(tfc_file, txc_file, colbert_file, query):
    results_tfc = [] 
    f = open(tfc_file, "r")
    lines = f.read().split("\n")
    lines = [float(x) for x in lines]
    print(lines)
    

    plt.plot(lines, color="magenta", marker="o", mfc="pink")
    plt.xticks(range(0, len(lines)+1, 1))
    plt.ylabel("metric")
    plt.xlabel("result")
    plt.title("TFC")
    plt.show()

plot_metrics("ap_results_colbert.txt","ap_results_tfc.txt","ap_results_txc.txt",1)
