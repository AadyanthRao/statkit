import sys

OPERATIONS = ["mean"]

def mean(values):
    return sum(values) / len(values)

def main():
    op = sys.argv[1]
    nums = [float(x) for x in sys.argv[2:]]
    if op == "mean":
        print(mean(nums))
    else:
        print(f"Unknown operation '{op}'. Available: {OPERATIONS}")

if __name__ == "__main__":
    main()