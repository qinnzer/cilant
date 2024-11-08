from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QDialog
from PyQt6 import QtWidgets
import sys
import io
from PyQt6 import uic
import sqlite3
import random

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>cilantromes</class>
 <widget class="QWidget" name="cilantromes">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>708</width>
    <height>519</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>cilantromes</string>
  </property>
  <widget class="QWidget" name="sign" native="true">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>711</width>
     <height>521</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background: rgb(249, 248, 242);
</string>
   </property>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>130</y>
      <width>251</width>
      <height>29</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #000000</string>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:18pt; font-weight:600;&quot;&gt;Вход/Регистрация&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="password">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>240</y>
      <width>133</width>
      <height>22</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #e9e8e1;
border: 2px solid rgba(208, 207, 202, 0.9);
color: #000000</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>266</x>
      <y>206</y>
      <width>40</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #000000</string>
    </property>
    <property name="text">
     <string>Логин:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>266</x>
      <y>240</y>
      <width>48</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #000000</string>
    </property>
    <property name="text">
     <string>Пароль:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>206</y>
      <width>133</width>
      <height>22</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #e9e8e1;
border: 2px solid rgba(208, 207, 202, 0.9);
color: #000000</string>
    </property>
   </widget>
   <widget class="QPushButton" name="getlog">
    <property name="geometry">
     <rect>
      <x>322</x>
      <y>320</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="mouseTracking">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 12pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>Вход</string>
    </property>
   </widget>
   <widget class="QLabel" name="error">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>280</y>
      <width>181</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">text-align: center;
color: #000000;</string>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="getregistr">
    <property name="geometry">
     <rect>
      <x>322</x>
      <y>360</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 12pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>Регистрация</string>
    </property>
   </widget>
   <widget class="QPushButton" name="send">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>380</y>
      <width>81</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 10pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>отправить</string>
    </property>
   </widget>
   <widget class="QListWidget" name="peoplelist">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>161</width>
      <height>391</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #e9e8e1;
border: 2px solid rgba(208, 207, 202, 0.9);
color: #000000</string>
    </property>
   </widget>
   <widget class="QListWidget" name="messagelist">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>481</width>
      <height>371</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #e9e8e1;
border: 2px solid rgba(208, 207, 202, 0.9);
color: #000000</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="message">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>380</y>
      <width>401</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #e9e8e1;
border: 2px solid rgba(208, 207, 202, 0.9);
color: #000000;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add">
    <property name="geometry">
     <rect>
      <x>7</x>
      <y>410</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 10pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>добавить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="delet">
    <property name="geometry">
     <rect>
      <x>7</x>
      <y>445</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 10pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>удалить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="update">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>410</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    background-color:  rgb(138, 178, 127);
    color: white; 
    border: none;
    border-radius: 5px; 
    font-size: 10pt;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s; 
}

QPushButton:hover {
    background-color: rgb(98, 138, 87);
    transform: scale(1.05); 
}
</string>
    </property>
    <property name="text">
     <string>обновить</string>
    </property>
   </widget>
   <widget class="QLabel" name="error1">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>410</y>
      <width>161</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: #000000;
text-align: center;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <zorder>add</zorder>
   <zorder>delet</zorder>
   <zorder>update</zorder>
   <zorder>peoplelist</zorder>
   <zorder>messagelist</zorder>
   <zorder>message</zorder>
   <zorder>label</zorder>
   <zorder>label_3</zorder>
   <zorder>getlog</zorder>
   <zorder>label_2</zorder>
   <zorder>error</zorder>
   <zorder>login</zorder>
   <zorder>password</zorder>
   <zorder>send</zorder>
   <zorder>getregistr</zorder>
   <zorder>error1</zorder>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Cilantromes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.users = ''
        self.login_user = ''
        self.data = list()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        # скрытие лишних виджетов
        self.add.hide()
        self.delet.hide()
        self.messagelist.hide()
        self.peoplelist.hide()
        self.send.hide()
        self.update.hide()
        self.message.hide()
        self.getregistr.hide()
        # кнопки
        self.getlog.clicked.connect(self.log)
        self.getregistr.clicked.connect(self.registr)
        self.add.clicked.connect(self.add_user)
        self.delet.clicked.connect(self.del_user)
        self.peoplelist.itemClicked.connect(self.get_username)
        self.send.clicked.connect(self.send_mes)
        self.update.clicked.connect(self.updt)

        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def log(self):
        flag = True
        login = self.login.text()
        self.login_user = login
        password = self.password.text()

        db = sqlite3.connect('members.db')
        c = db.cursor()
        self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
        db.commit()
        db.close()

        for q in range(len(self.data)):
            if login == self.data[q][1]:
                if password == self.data[q][2]:
                    self.error.hide()
                    self.getlog.hide()
                    self.getregistr.hide()
                    self.label.hide()
                    self.label_2.hide()
                    self.label_3.hide()
                    self.login.hide()
                    self.password.hide()
                    self.add.show()
                    self.delet.show()
                    self.messagelist.show()
                    self.peoplelist.show()
                    self.send.show()
                    self.update.show()
                    self.message.show()
                    flag = False
                    db = sqlite3.connect(f'local_{self.login_user}.db')
                    c = db.cursor()
                    try:
                        c.execute("""CREATE TABLE info (
                                    login text,
                                    message text
                                )""")
                    except:
                        pass
                    self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
                    db.close()
                    if len(self.data) > 0:
                        db = sqlite3.connect(f'local_{self.login_user}.db')
                        c = db.cursor()
                        self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
                        db.close()
                        for j in range(len(self.data)):
                            self.peoplelist.addItem(self.data[j][1])

                    # функция uptd()
                    db = sqlite3.connect('members.db')
                    c = db.cursor()
                    newmes = c.execute(f"""SELECT newmessage FROM info
                                                WHERE login = '{self.login_user}'""").fetchall()[0][0].split('α1')
                    db.close()
                    print(newmes)
                    newmes.remove('')
                    if len(newmes) > 0:
                        db = sqlite3.connect(f'local_{self.login_user}.db')
                        c = db.cursor()
                        logins = c.execute(f'''SELECT login FROM info''').fetchall()
                        logins = list(map(lambda x: x[0], logins))
                        for i in range(len(newmes)):
                            if newmes[i].split(':')[0] not in logins:
                                c.execute(f"INSERT INTO info VALUES ('{newmes[i].split(':')[0]}',  '')")
                                db.commit()
                            mes = c.execute(f'''SELECT message FROM info
                                                WHERE login = '{newmes[i].split(':')[0]}' ''').fetchall()[0][0]
                            c.execute(f'''UPDATE info
                                                SET message = '{mes + newmes[i] + 'α1'}'
                                                WHERE login = '{newmes[i].split(':')[0]}' ''')
                            if self.peoplelist.count() == 0:
                                self.peoplelist.addItem(newmes[i].split(':')[0])
                            else:
                                for j in range(self.peoplelist.count()):
                                    if newmes[i].split(':')[0] not in self.peoplelist.item(j).text():
                                        self.peoplelist.addItem(newmes[i].split(':')[0])
                        db.commit()
                        db.close()

                        db = sqlite3.connect('members.db')
                        c = db.cursor()
                        c.execute(f'''UPDATE info
                                SET newmessage = '' 
                                WHERE login = '{self.login_user}' ''')
                        db.commit()
                        db.close()

                    break
                else:
                    self.error.setText('Неверный пароль')
                    flag = False
                    break
        if flag:
            self.error.setText('Аккаунт отсутствует')
            self.getregistr.show()

    def updt(self):
        db = sqlite3.connect('members.db')
        c = db.cursor()
        newmes = c.execute(f"""SELECT newmessage FROM info
                                                        WHERE login = '{self.login_user}'""").fetchall()[0][0].split(
            'α1')
        db.close()
        print(newmes)
        newmes.remove('')
        if len(newmes) > 0:
            db = sqlite3.connect(f'local_{self.login_user}.db')
            c = db.cursor()
            logins = c.execute(f'''SELECT login FROM info''').fetchall()
            logins = list(map(lambda x: x[0], logins))
            for i in range(len(newmes)):
                if newmes[i].split(':')[0] not in logins:
                    c.execute(f"INSERT INTO info VALUES ('{newmes[i].split(':')[0]}',  '')")
                    db.commit()
                mes = c.execute(f'''SELECT message FROM info
                                WHERE login = '{newmes[i].split(':')[0]}' ''').fetchall()[0][0]
                c.execute(f'''UPDATE info
                            SET message = '{mes + newmes[i] + 'α1'}'
                            WHERE login = '{newmes[i].split(':')[0]}' ''')
                if self.peoplelist.count() == 0:
                    self.peoplelist.addItem(newmes[i].split(':')[0])
                else:
                    for j in range(self.peoplelist.count()):
                        if newmes[i].split(':')[0] not in self.peoplelist.item(j).text():
                            self.peoplelist.addItem(newmes[i].split(':')[0])
            db.commit()
            db.close()

            db = sqlite3.connect('members.db')
            c = db.cursor()
            c.execute(f'''UPDATE info
                        SET newmessage = '' 
                        WHERE login = '{self.login_user}' ''')
            db.commit()
            db.close()

    def registr(self):
        login = self.login.text()
        password = self.password.text()
        for i in range(len(self.data)):
            if login == self.data[i][1]:
                self.error.setText('Такой аккаунт уже существует')
                break
            elif self.login == '' or password == '':
                self.error.setText('Неверный формат')
            else:
                self.getregistr.hide()
                db = sqlite3.connect('members.db')
                c = db.cursor()
                c.execute(f"INSERT INTO info VALUES ('{login}',  '{password}', '')")
                db.commit()
                db.close()
                self.error.setText('Аккаунт создан')
                break

    def del_user(self):
        flag_not_user = False
        flag_this_user = False
        correct = True
        name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Кого вы хотите удалить?")
        db = sqlite3.connect(f'local_{self.login_user}.db')
        c = db.cursor()
        self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
        db.commit()
        db.close()
        if ok_pressed:
            while correct:
                for i in range(len(self.data)):
                    if self.login_user == name:
                        flag_this_user = True
                        break
                    elif name == self.data[i][1]:
                        flag_not_user = False
                        correct = False
                        break
                    else:
                        flag_not_user = True
                if not correct:
                    break
                if flag_this_user:
                    name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Это вы")
                elif flag_not_user:
                    name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Такого пользователя нет")
                if not ok_pressed:
                    break
                flag_not_user = False
                flag_this_user = False
        if ok_pressed:
            db = sqlite3.connect(f'local_{self.login_user}.db')
            c = db.cursor()
            c.execute(f"DELETE FROM info WHERE login = '{name}'")
            self.data = c.execute("SELECT login FROM info").fetchall()
            db.commit()
            db.close()
            self.peoplelist.clear()
            self.messagelist.clear()
            for i in range(len(self.data)):
                self.peoplelist.addItem(self.data[i][0])

    def add_user(self):
        flag_not_user = False
        flag_this_user = False
        correct = True
        name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Кому вы хотите написать?")
        db = sqlite3.connect('members.db')
        c = db.cursor()
        self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
        db.commit()
        db.close()
        if ok_pressed:
            while correct:
                for i in range(len(self.data)):
                    if self.login_user == name:
                        flag_this_user = True
                        break
                    elif name == self.data[i][1]:
                        flag_not_user = False
                        correct = False
                        break
                    else:
                        flag_not_user = True
                if not correct:
                    break
                if flag_this_user:
                    name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Это вы")
                elif flag_not_user:
                    name, ok_pressed = QInputDialog.getText(self, "Введите имя", "Такого пользователя нет")
                if not ok_pressed:
                    break
                flag_not_user = False
                flag_this_user = False
        if ok_pressed:
            flag_in_db = False
            self.peoplelist.addItem(name)
            db = sqlite3.connect(f'local_{self.login_user}.db')
            c = db.cursor()
            self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
            for i in range(len(self.data)):
                if name == self.data[i][1]:
                    flag_in_db = True
                    break
            if not flag_in_db:
                c.execute(f"INSERT INTO info VALUES ('{name}', '')")
                db.commit()
            db.close()

    def get_username(self, item):
        self.users = item.text()
        data_user = ''
        db = sqlite3.connect(f'local_{self.login_user}.db')
        c = db.cursor()
        self.data = c.execute("SELECT rowid,  * FROM info").fetchall()
        db.close()
        for i in range(len(self.data)):
            if item.text() == self.data[i][1]:
                data_user = self.data[i][2].split('α1')
                break
        data_user.remove('')
        self.messagelist.clear()
        if len(data_user) > 0:
            self.messagelist.addItems(data_user)

    def send_mes(self):
        self.error1.clear()
        text = self.message.text()
        if self.users == '':
            self.error1.setText('Никто не выбран')
        else:
            if text == '':
                self.error1.setText('Пустое сообщение')
            else:
                self.message.clear()
                db = sqlite3.connect('members.db')
                c = db.cursor()
                mes = c.execute(f'''SELECT newmessage FROM info
                                WHERE login = '{self.users}' ''').fetchall()[0][0]
                mes += f'{self.login_user}:{text}α1'
                c.execute(f'''UPDATE info
                        SET newmessage = '{mes}'
                        WHERE login = '{self.users}'
                ''')
                db.commit()
                db.close()

                db = sqlite3.connect(f'local_{self.login_user}.db')
                c = db.cursor()
                mes = c.execute(f'''SELECT message FROM info
                WHERE login = '{self.users}' ''').fetchall()[0][0]
                mes += f"{self.login_user}:{text}α1"
                c.execute(f'''UPDATE info
                        SET message = '{mes}'
                        WHERE login = '{self.users}' ''')
                db.commit()
                db.close()
                self.messagelist.addItem(f'{self.login_user}:{text}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cilantromes()
    ex.setFixedSize(718, 519)
    ex.show()
    sys.exit(app.exec())
