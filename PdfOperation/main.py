import myModules
if __name__ == '__main__':
    obj=myModules.Pdf('Output.pdf')

    try:
        print(obj.readPdf())
    except:
        print("File is corrupted")