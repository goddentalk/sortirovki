import random
import time


l = 100
a = []


print("Несортированный пузырёк")
a = []
nsb_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j+1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
nsb_ltime=time.time()
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",nsb_ltime-nsb_ftime)
print('\n')


print("Частично сортированный пузырёк")
a = []
chsb_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)

s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
chsb_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",chsb_ltime-chsb_ftime)
print('\n')


print("Сортированный пузырёк")
a = []
sb_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
sb_ltime=time.time()
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",sb_ltime-sb_ftime)
print('\n')


print("Вставка несортированный список")
a = []
nvst_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0,1000))
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
nvst_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",nvst_ltime-nvst_ftime)
print('\n')


print("Вставка частично сортированный")
a = []
chvst_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0,1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
chvst_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",chvst_ltime-chvst_ftime)
print('\n')


print("Вставка сортированный список")
a = []
svst_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
svst_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",svst_ltime-svst_ftime)
print('\n')


print("Выбором несортированный список")
a = []
nsch_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
nsch_ltime=time.time()
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",nsch_ltime-nsch_ftime)
print('\n')


print("Выбором частично сортированный список")
a = []
chsch_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
chsch_ltime=time.time()
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",chsch_ltime-chsch_ftime)
print('\n')


print("Выбором сортированный список")
a = []
sch_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s=0
p=0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
sch_ltime=time.time()
print(a)
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",sch_ltime-sch_ftime)
print('\n')


print("Шелла несортированный список")
a = []
nshel_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos - diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos - diap]
            pos -= diap
            a[pos] = cur
    diap = diap // 2
print(a)
nshel_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",nshel_ltime-nshel_ftime)
print('\n')


print("Шелла частично сортированный список")
a = []
chshel_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos - diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos - diap]
            pos -= diap
            a[pos] = cur
    diap = diap // 2
print(a)
chshel_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",chshel_ltime-chshel_ftime)
print('\n')


print("Шелла сортированный список")
a = []
sshel_ftime=time.time()
for i in range(0, l):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
diap = len(a) // 2
while diap > 0:
    for i in range(diap, len(a)):
        cur = a[i]
        pos = i
        while pos >= diap and a[pos - diap] > cur:
            s += 1
            p += 1
            a[pos] = a[pos - diap]
            pos -= diap
            a[pos] = cur
    diap = diap // 2
print(a)
sshel_ltime=time.time()
print('Сравнения -', s)
print('Перестановки -', p)
print("Затраченное время",sshel_ltime-sshel_ftime)
print('\n')


def test(arr):
    global c_comp, c_swap
    c_comp, c_swap = 0, 0
    quick_sort(arr, 0, len(arr) - 1)


def quick_sort(x, ibeg, iend):
    global c_comp, c_swap
    if (iend - ibeg) <= 1:
        return
    isep = (ibeg + iend) // 2
    sep = x[isep]
    i = ibeg
    j = iend
    while True:
        while x[i] < sep:
            i += 1
            c_comp += 1
        while x[j] > sep:
            j -= 1
            c_comp += 1
        if i <= j:
            x[i], x[j] = x[j], x[i]
            c_swap += 1
            i += 1
            j -= 1
        if i >= j:
            break
    quick_sort(x, ibeg, j)
    quick_sort(x, i, iend)


print("QSort несортированный список")
x = []
nqs_ftime=time.time()
for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
test(x)
print(x)
nqs_ltime=time.time()
print('Сравнения - '+str(c_comp))
print('Перестановки - '+str(c_swap))
print('Затраченное время:',nqs_ltime-nqs_ftime)
print('\n')


print("QSort частично сортированный список")
x = []
chqs_ftime=time.time()
for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
for j in range(0, len(x) // 2):
    for j in range(0, len(x) // 2):
        if x[j] > x[j + 1]:
            x[j + 1], x[j] = x[j], x[j + 1]
print(x)
test(x)
print(x)
chqs_ltime=time.time()
print('Сравнения - '+str(c_comp))
print('Перестановки - '+str(c_swap))
print('Затраченное время:',chqs_ltime-chqs_ftime)
print('\n')


print("QSort ортированный список")
x = []
sqs_ftime=time.time()
for i in range(0, l):
    x.append(random.randint(0, 1000))
print(x)
x.sort()
print(x)
test(x)
print(x)
sqs_ltime=time.time()
print('Сравнения - ' + str(c_comp))
print('Перестановки - ' + str(c_swap))
print('Затраченное время:',sqs_ltime-sqs_ftime)
print('\n')
