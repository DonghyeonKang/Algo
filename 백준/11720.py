# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
b = input()
a = list(input())
print(sum(int(i) for i in a))
