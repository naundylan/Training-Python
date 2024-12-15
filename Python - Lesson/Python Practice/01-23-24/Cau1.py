def chuanhoa(vector, minX=0, maxX=1):
    minVal = float(min(vector))
    maxVal = float(max(vector))
    for i in range(len(vector)):
        newElement = (((vector[i] - minX)/(maxX - minX))*(maxVal - minVal)) + minVal
        vector[i] = float(newElement)
        return vector
if __name__ == "__main__":
    print(chuanhoa([6, 3, 9, 8, 7, 1], -1, 1))