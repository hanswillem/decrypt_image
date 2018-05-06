#Put cipher.txt and key.txt in the same folder as this processing sketch.
#Made with Processing 2.2.1 in Python mode.


#decrypt the cipher
def decrypt(c, k):
    m = []
    for i in range(len(c)):
        m.append((c[i] - k[i]) % 99999999)
    m = [-1 * i for i in m] #reintroduce the minus sign
    return m


#read list from file (cipher.txt and key.txt)
def readList(fileName):
    f = open(fileName)
    l = [int(i) for i in f]
    return l


#display the image
def display(m):
    loadPixels()
    for i in range(len(m)):
        pixels[i] = m[i]
    updatePixels()


def setup():
    size(128, 128)
    background(255)
    c = readList('cipher.txt')
    k = readList('key.txt')
    m = decrypt(c, k)
    display(m)
