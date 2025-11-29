import re
import sys
import matplotlib.pyplot as plt
import numpy as np

def main():

    if len(sys.argv) != 2:
        print(f"Programm expected one argumet, but received {len(sys.argv)}")
        sys.exit(1)

    filename = sys.argv[1]

    patterns = [
        r"Min latency:\s*([\d.]+)\s*ns",
        r"Max latency:\s*([\d.]+)\s*ns",
        r"Avg latency:\s*([\d.]+)\s*ns",
        r"Jitter \(max-min\):\s*([\d.]+)\s*ns",
    ]

    result = [[], [], [], []]

    with open(filename, "r") as f:
        for line in f:
            for i in range(len(patterns)):
                m = re.search(patterns[i], line)
                if m:
                    result[i].append(float(m.group(1)))


    axis = np.arange(0, len(result[3]), 1)

    plt.plot(axis, [x / max(result[3]) for x in result[3]])
    plt.xlabel("iteration")
    plt.ylabel("Jitter")
    plt.title(f"{filename}")
    plt.show()

if __name__ == '__main__':
    main()