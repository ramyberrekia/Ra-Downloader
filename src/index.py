from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon,QApplication
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import os
from os import path
import sys
import urllib.request
import pafy
from main import Ui_MainWindow

class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Window()
        self.Handel_Buttons() # نستدعي هذه الفنكشن في الكونستراكتور بحيث يتم التعامل معها على طول

    def Handel_Window(self):
        self.setWindowTitle('Download it!')
        self.setFixedSize(631,300)
        self.setWindowTitle('Downloader.')
        self.setWindowIcon(QIcon('img/download.png'))


    def Handel_Buttons(self):
        self.DowloadButton.clicked.connect(self.Handel_Download)# هنا نستدعي الobject حقت ال download button و نقول إذا ضُغط هذا الزر فإن هذه الفنكشن ستُربط مع فنكشن أخرى
        self.BrowseButton.clicked.connect(self.Handel_Browse)
        self.DowloadButton_2.clicked.connect(self.Download_Youtube_Video)
        self.BrowseButton_4.clicked.connect(self.get_theVideo_Quality)
        self.BrowseButton_2.clicked.connect(self.save_browse)
        self.BrowseButton_3.clicked.connect(self.playlist_browse)
        self.DowloadButton_3.clicked.connect(self.Download_Youtube_Playlists)
    def Handel_Browse(self):
        save_location = QFileDialog.getSaveFileName(caption='Save as',directory='.',filter='All Files *.*')
        self.lineEdit.setText(save_location[0])
    def save_browse(self):
        save_location = QFileDialog.getExistingDirectory(self,'Select Download Directory')
        self.lineEdit_4.setText(save_location)
    def playlist_browse(self):
        save_location = QFileDialog.getExistingDirectory(self, 'Select Download Directory')
        self.lineEdit_6.setText(save_location)
    def Handel_Progress(self,blocknum,blocksize,totalsize):
        counting = blocknum * blocksize # نحسب كم حجم البلوكا الواحدة

        if totalsize > 0:
            percentage = counting * 100 / totalsize # نحسب النسبة
            self.progressBar.setValue(int(percentage)) # هنا نقله عشان نحط النسبة في الprogress bar.
            QApplication.processEvents() # هذا السطر هو الي يخلي الwindow يشتغل وما يجيه not responding.

    def Handel_Download(self):
        url = self.lineEdit_2.text() # نأخذ رابط الملف الذي نريد تحميله من الفراغ الأول في التطبيق
        saveLoc = self.lineEdit.text() # نأخذ مكان حفظ الملف من الفراغ الثاني في التطبيق
        try:
            urllib.request.urlretrieve(url, saveLoc,self.Handel_Progress)  # هنا نبدأ التحميل من خلال مكتبة الurllib التي بدورها تأخذ 3 arguments
            # الأول هو خاص برابط الملف الذي نريد تحميله
            # الثاني خاص بالمكان الذي سنحفظ فيه الملف
            # الثالث خاص بالprogress bar
            QMessageBox.information(self, "I Completed my work :)","Download Successfully Completed.")  # هذه بمثابة أنه يظهرلي window صغيرة يقولي فيه على انو التحميل نجح


        except Exception:
            QMessageBox.warning(self, "I Didn't complete my work :(", "Download Failed.")

        self.progressBar.setValue(0)  # نسوي ريسيت لكل شئ بعد اكتمال التحميل
        self.lineEdit_2.setText('')
        self.lineEdit.setText('')
    def get_theVideo_Quality(self):
        video_link = self.lineEdit_3.text()
        v = pafy.new(video_link)
        print(v.title)
        print(v.duration)
        print(v.rating)
        print(v.author)
        s = v.allstreams
        for n in s:
            data = '{} {} {}'.format(n.mediatype, n.extension,n.quality )
            self.comboBox.addItem(data)
    def Download_Youtube_Video(self):
        video_link = self.lineEdit_3.text()
        save_location = self.lineEdit_4.text()
        v = pafy.new(video_link)
        streams = v.allstreams
        quality = self.comboBox.currentIndex()
        download = streams[quality].download(filepath=save_location)
        QMessageBox.information(self, "Check your video folder :)","Download Successfully Completed.")  # هذه بمثابة أنه يظهرلي window صغيرة يقولي فيه على انو التحميل نجح

        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.comboBox.clear()

    def Download_Youtube_Playlists(self):
        playlist_link = self.lineEdit_5.text()
        save_location = self.lineEdit_6.text()
        playlist = pafy.get_playlist(playlist_link)
        videos = playlist['items']

        os.chdir(save_location)

        if os.path.exists(str(playlist['title'])):
            os.chdir(str(playlist['title']))
        else:
            os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

        for video in videos:
            p = video['pafy']
            best = p.getbest(preftype='mp4')
            best.download()

        QMessageBox.information(self, "Check your video folder :)","Download Successfully Completed.")  # هذه بمثابة أنه يظهرلي window صغيرة يقولي فيه على انو التحميل نجح

        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.comboBox.clear()
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp() # نأخذ نسخة من الclass الي نقدر ننشأ منه window
    window.show() # لإظهار ال window
    app.exec_() # هذا عبارة عن loop يخلي ال window ظاهرة دائما في الشاشة، إذا لم تكن هذه ال loop رح تظهر ال window و تختفي على طول.


if __name__ == '__main__': # في هذا السطر إحنا بنحدد و نختار السطر الي رح يبدأ منه الكود و في هاذي الأسطر إخترنا أنه يبدأ من ال function 'main'
    main()