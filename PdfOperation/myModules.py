import PyPDF2
import os.path, time
import fpdf

class Pdf:
    def __init__(self,path):
        self.path=path
        self.dictDetails={}

    def openPDF(self):
        self.pdfObj=open(self.path,"rb")
        return self.pdfObj
    def closePdf(self,obj):
        obj.close()
    def getDetails(self):
        obj=self.openPDF()
        pdfReader=PyPDF2.PdfFileReader(obj)
        pdfDetails=pdfReader.documentInfo
        newDict =pdfDetails.copy()
        newDict['ModifiedTime']=time.ctime(os.path.getmtime(self.path))
        newDict['CreationTime']=time.ctime(os.path.getctime(self.path))
        self.closePdf()
        return newDict
    def readPdf(self):
        pdfObj=self.openPDF()
        pdfReader=PyPDF2.PdfFileReader(pdfObj)
        pages=pdfReader.getNumPages()
        for count in range(pages):
            obj=pdfReader.getPage(count)
            print(obj.extractText())
            print(f"Page {count+1}")

        self.closePdf(pdfObj)



if __name__ == '__main__':
    myPdf=Pdf("Hello.pdf")
    myPdf.getDetails()

