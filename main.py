# python3

def parallel_processing(n, m, data):
    output = []
    time = n * [0]
    thread_num = 0
    for thread in range((len(data))):
        for i in range(n):
            if time[thread_num] > time[i]:
                thread_num = i 
        output.append((thread_num, time[thread_num]))
        print(data[thread])
        time[thread_num] += data[thread]
        thread_num = 0
    return output
def main():
    data = []
    n, m = list(map(int,input().split()))
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0],i[1])
if __name__ == "__main__":
    main()
