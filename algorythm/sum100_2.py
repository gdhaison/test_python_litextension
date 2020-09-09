import numpy as np

def return_str(arr: list):
    return f"{arr[0]}1{arr[1]}2{arr[2]}3{arr[3]}4{arr[4]}5{arr[5]}6{arr[6]}7{arr[7]}8{arr[8]}9"

def sum():
    ar1 = ["-", "+"]
    ar2 = ["+", "-", ""]
    arr = np.array(np.meshgrid(ar1, ar2, ar2, ar2, ar2, ar2, ar2, ar2, ar2)).T.reshape(-1, 9).tolist()
    result = list(map(return_str, arr))

    output = []
    for i in result:
        if eval(i) == 100:
            output.append(i)

    return output

print(sum())
