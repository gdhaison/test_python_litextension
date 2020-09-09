def sum(n):
    root = "123456789"
    length = len(root) + 1
    out = []
    def cal(x, i):
        if i + 1 == length:
            if eval(x) == n:
                out.append(x.lstrip("+"))
            return
        for j in range(i + 1, length):
            cal(f"{x}+{root[i:j]}", j)
            cal(f"{x}-{root[i:j]}", j)
    cal("", 0)
    return out
print(sum(100))
