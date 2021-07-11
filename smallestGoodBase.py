# 20210618
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # 上面提到的 base 进制转十进制公式。
        # 使用等比数列求和公式可简化时间复杂度
        def sum_with(base, N):
            return (1 - base ** N) // (1 - base)
            # return sum(1 * base ** i for i in range(N))
        # bin(n) 会计算出 n 的二进制表示， 其会返回形如 '0b10111' 的字符串，因此需要减去 2。
        for N in range(len(bin(n)) - 2, 0, -1):
            l = 2
            r = n - 1
            while l <= r:
                mid = (l + r) // 2
                v = sum_with(mid, N)

                if v < n:
                    l = mid + 1
                elif v > n:
                    r = mid - 1
                else:
                    return str(mid)