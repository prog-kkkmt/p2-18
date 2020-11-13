s1=(60*int(input())) + int(input()) # есть 2 бегуна они начали и закончили в разное время найти кто быстрее
f1=(60*int(input())) + int(input())
s2=(60*int(input())) + int(input())
f2=(60*int(input())) + int(input())
t1=f1-s1
t2=f2-s2
if(t1<t2):
    print("первый быстрее")
else:
    print("второй  быстрее")
