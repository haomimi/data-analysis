from ReadData import ReadData

def mainFunc():
    filepath = 'D:/Code/readfile/data.csv'
    d = ReadData(filepath)
    print(d.data.keys())

if __name__ == "__main__":
    
    mainFunc()