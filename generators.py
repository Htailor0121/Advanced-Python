# def remoteControlNext():
#     yield "CN"
#     yield "DMA"
# for value in remoteControlNext():
#     print(value)

def fibbo():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a + b

for f in fibbo():
    if f>=50:
        break
    print(f)
# for the understanding










