def dfs(n):
    if n>7:
        return
    else:
        print(n)
        dfs(n*2)
        dfs(n*2+1)

if __name__ == '__main__':
    dfs(1)