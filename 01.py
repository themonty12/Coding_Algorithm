# 문자열을 뒤에서부터 읽어도 원래 문자열과 같은 단어를 팰린드롬이라 한다.

# 입력으로 주어진 문자열이 팰린드롬인지 판별한 뒤, 팰린드롬이면 빈 문자열을 출력한다.

# 입력된 문자열이 팰린드롬이 아닐 경우 문자열을 반으로 나누어 앞부분의 단어를 기준으로 팰린드롬 단어로 만드는 함수를 작성하시오.

# 예시 1
# s = 'abcdcba'
# return ''

# 예시 2
# s = 'banana'
# return 'bannab'

# 예시 3
# s = 'wabe'
# return 'waaw'

def solution(s):
    mid = len(s) // 2
    for i in range(mid):
        if s[i] != s[-1 -i]:
            if len(s) % 2:                
                result = s[:mid+1] + s[mid-1::-1]
            else:                
                result = s[:mid] + s[mid-1::-1]
            return result

    return ''

s = 'abcdcba'
print(solution(s))

s = 'banana'
print(solution(s))

s = 'wabe'
print(solution(s))

s = 'abcdefg'
print(solution(s))



