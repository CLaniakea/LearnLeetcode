#构建自动机失败
class Solution:
    def isNumber(self, s: str) -> bool:
        # start
        length = len(s)
        tag = [''] * length
        tag[0]='start'
        tag[-1]='end'
        for i,st in enumerate(s):
            if st == 'e' or st == '.' or st == '+' or st == '-':
                tag[i] = st
            if st == 'e':
                if (s[i:].find('.') == -1):
                    return True
            if self.judegState(tag[i], st):
                if tag[i] == 'end':
                    return True
                else:
                    continue
            else:
                return False
        return False
            


    def judegState(self, i, st):
        if i == 'start' or i == 'end':
            if st >= '0' and st <= '9':
                return True
            else:
                return False
        else:
            if st == 'e' or st == '+' or st == '-' or st == '.':
                return True
            else:
                return False
        if st == '+' or st == '-':
            if i == 'start':
                return True
            else:
                return False
            

# 异常方法、简单
# 捕获异常可以让程序不被中断，继续执行
class Solution:
    def isNumber(self, s: str) -> bool:
        if 'i' in s:
            return False
        try:
            float(s)
            return True
        except:
            return False

a = '--6'
tag = Solution()
print(tag.isNumber(a))