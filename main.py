import sys
import os
import json
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressDialog, QMessageBox
from PySide6.QtCore import QObject, QPropertyAnimation, QEasingCurve, QPointF, QTimer, QUrl, Qt, Signal, QThread
from PySide6.QtGui import QColor, QMovie, QPixmap
from PySide6 import QtCore, QtWidgets
from ui_Login import*
from ui_MainWindow import*
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth
from functions.unidad_1 import*
from clases.Videos import (V_U1_T1,V_U1_T2,V_U1_T3,V_U1_T4,V_U1_T5,V_U2_T1,V_U2_T2,V_U2_T3,V_U2_T4,V_U2_T5,
                           V_U2_T6,V_U2_T7,V_U2_T8,V_U2_T9,V_U3_T1,V_U3_T2,V_U3_T3,V_U3_T4,V_U3_T5,V_U3_T6,
                           V_U3_T7,V_U3_T8,V_U3_T9,V_U4_T1,V_U4_T2,V_U4_T3,V_U4_T4,V_U4_T5,V_U4_T6,V_U4_T7,
                           V_U4_T8)
from clases.Simulaciones import *
from clases.Personalizar import Personalizar

#!########## POR SEGURIDAD, NO ES POSIBLE COMPARTIR LAS CREDENCIALES DEL PROYECTO EN FIREBASE #############
firebaseConfig = {
            'apiKey': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'authDomain': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'databaseURL': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'projectId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'storageBucket': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'messagingSenderId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'appId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            'measurementId': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
firebase = pyrebase.initialize_app(firebaseConfig)
auth_1 = firebase.auth()
storage = firebase.storage()

#!########## POR SEGURIDAD, NO ES POSIBLE COMPARTIR LAS CREDENCIALES DEL PROYECTO EN FIREBASE #############
credentials_data = {
  "type": "service_account",
  "project_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "private_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "client_email": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "auth_uri": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "token_uri": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "auth_provider_x509_cert_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "client_x509_cert_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "universe_domain": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
cred = credentials.Certificate(credentials_data)
firebase_admin.initialize_app(cred)


class Login(QMainWindow,Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.mainWindow = MainWindow(login=self)
        
        # Inicializa elementos en condiciones iniciales
        self.bt_normal.hide()
        self.click_position = None
        
        # Conecta los eventos que controlan los bonones de la barra de titulo
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
        
        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # sizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        # Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.frame_inferior.mouseMoveEvent = self.mover_ventana
        
        # Insertar iconos de usurio y contraseña en los lineEdit
        icon_user = QIcon("resources/images/Login/user.svg")
        icon_email = QIcon("resources/images/Login/email.svg")
        icon_lock = QIcon("resources/images/Login/locked.svg")
        self.emailEdit.addAction(icon_email, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition
        self.passEdit.addAction(icon_lock, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition
        self.userEdit_2.addAction(icon_user, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition
        self.emailEdit_2.addAction(icon_email, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition
        self.passEdit_2.addAction(icon_lock, QLineEdit.LeadingPosition) #QLineEdit.TrailingPosition
        
        # Iniciar sesión y cambio de ventana
        self.bt_IniciarSesion.clicked.connect(self.iniciarSesion)
        
        # Iniciar sesión como invitado
        self.iniciarInvitado.clicked.connect(self.iniciarSesionInvitado)
        self.iniciarInvitado_2.clicked.connect(self.iniciarSesionInvitado)
        
        # Registrarse y cambio de ventana
        self.bt_Registrarme.clicked.connect(self.registrarse)
        
        # Restablecer contraseña
        self.bt_ResetPass_2.clicked.connect(self.restablecer_contrasenia)
        
        # Cambiar a vista de registro
        self.bt_Registrarse.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        
        # Cambiar a vista de inicio de sesión
        self.bt_IniciaSesion.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.bt_IniciaSesion_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        # Cambiar a vista de restablecer contraseña
        self.bt_ResetPass.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        
        
        ###########################################################################################
        #############################! Lee el archivo JSON existente ##############################
        ###########################################################################################
        with open("config.json", "r") as archivo:
            configJson = json.load(archivo)
        if configJson['email']==None or configJson['password']==None:
            self.show()
        else:
            self.mainWindow.iniciarSesion(configJson)
        
        
        
        
    def control_bt_normal(self):
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximize.show()
        
    def control_bt_maximize(self):
        self.showMaximized()
        self.bt_normal.show()
        self.bt_maximize.hide()
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition()
        
    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        
    def mover_ventana(self, event):
        
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                posicion = QPointF(self.pos().x(),self.pos().y()) + event.globalPosition() - self.clickPosition
                self.move(posicion.x(),posicion.y())
                self.clickPosition = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.bt_normal.show()
            self.bt_maximize.hide()
        else:
            self.showNormal()
            self.bt_normal.hide()
            self.bt_maximize.show()
        
    # Iniciar sesión
    def iniciarSesion(self):
        datos = {
            'email': self.emailEdit.text(),
            'password': self.passEdit.text()
        }
        try:
            user=auth.get_user_by_email(datos['email'])
            try:
                user_1 = auth_1.sign_in_with_email_and_password(**datos)
                if user.email_verified:
                    self.actualizar_configJson(datos)
                    self.cambiar_Ventana(datos)
                else:
                    try:
                        auth_1.send_email_verification(user_1['idToken'])
                    except Exception as e:
                        print('Login.iniciarSesion(): '+str(e))
                        pass
                    QMessageBox.information(self, "Correo electrónico sin validar", "Se le ha enviado un enlace de validación a su correo electrónico.\nPor favor revise su correo, acceda al enlace para validarlo y \nvuelva a iniciar sesión.")
            except Exception:
                self.invalidLogin.setText('Correo o contraseña incorrectos')
                self.invalidLogin.setToolTip('Correo o contraseña incorrectos')
        except ValueError as e:
            self.invalidLogin.setText('Ingrese un correo válido')
            self.invalidLogin.setToolTip('Ingrese un correo válido')
        except auth.UserNotFoundError as e:
            self.invalidLogin.setText('Correo no encontrado')
            self.invalidLogin.setToolTip('Correo no encontrado')
        except firebase_admin.exceptions.FirebaseError as e:
            self.invalidLogin.setText('Ocurrió un error con el servidor')
            self.invalidLogin.setToolTip('Ocurrió un error con el servidor')
        except Exception as e:
            self.invalidLogin.setText('Ocurrió un error de concexión')
            self.invalidLogin.setToolTip('Ocurrió un error de concexión')
        
            
    # Iniciar sesión invitado
    def iniciarSesionInvitado(self):
        # Lee el archivo JSON existente
        with open("config.json", "r") as archivo:
            configJson = json.load(archivo)
        datos = {
            'email': None,
            'password': None
        }
        configJson.update(datos)
        # Guarda los datos en un nuevo archivo JSON
        with open("config.json", "w") as archivo:
            json.dump(configJson, archivo, indent=4)
        self.cambiar_Ventana({'email':'invitado','password':''})
            
    # Registrarse
    def registrarse(self):
        datos = {
            'uid': self.userEdit_2.text(),
            'display_name': self.userEdit_2.text(),
            'email': self.emailEdit_2.text(),
            'password': self.passEdit_2.text()
        }
        try:
            user = auth.create_user(**datos)
            user_1 = auth_1.sign_in_with_email_and_password(datos["email"],datos["password"])
            self.stackedWidget.setCurrentIndex(2)
            # Cargar gif de loading.gif
            self.loading_animatrion = QMovie('resources/images/Login/loading.gif')
            self.label_animation.setMovie(self.loading_animatrion)
            self.loading_animatrion.start()
            auth_1.send_email_verification(user_1['idToken'])
            
            # Usamos QTimer para verificar periódicamente si el email se a validado
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.detectar_validacion_email)
            self.timer.start(2000)  # Intervalo de verificación en milisegundos
            
        except ValueError as e:
            self.invalidSignup.setText('Datos no válidos')
            self.invalidSignup.setToolTip('Datos no válidos')
        except auth.EmailAlreadyExistsError as e:
            self.invalidSignup.setText('Este correo ya está registrado')
            self.invalidSignup.setToolTip('Este correo ya está registrado')
        except auth.UidAlreadyExistsError as e:
            self.invalidSignup.setText('Nombre de usuario no disponible')
            self.invalidSignup.setToolTip('Nombre de usuario no disponible')
        except firebase_admin.exceptions.FirebaseError as e:
            self.invalidSignup.setText('Ocurrió un error con el servidor')
            self.invalidSignup.setToolTip('Ocurrió un error con el servidor')
        except Exception as e:
            if len(datos["password"])<6:
                self.invalidSignup.setText('Contraseña debe tener mas de 5 caracteres')
                self.invalidSignup.setToolTip('Contraseña debe tener mas de 5 caracteres')
            else:
                self.invalidSignup.setText(str(e))
                self.invalidSignup.setToolTip(str(e))
            print(e)
    
    # Oculta la ventana de login y muestra la ventana principal
    def cambiar_Ventana(self,datos):
        self.mainWindow.iniciarSesion(datos)
        self.close()
            
    def detectar_validacion_email(self):
        uid = self.userEdit_2.text()
        user = auth.get_user(uid=uid)
        if user.email_verified == True:
            self.timer.stop()
            datos = {'email':self.emailEdit_2.text(),'password':self.passEdit_2.text()}
            self.actualizar_configJson(datos)
            self.cambiar_Ventana(datos)
            self.loading_animatrion.stop()
            
    # Actualiza los datos del archivo config.json dependiendo el caso (se elija o nó la opción de permanecer conectado)
    def actualizar_configJson(self,datos):
        if (self.checkRecordarPass.isChecked() and self.stackedWidget.currentIndex()==0) or (self.checkRecordarPass_2.isChecked() and self.stackedWidget.currentIndex()==2):
            # Lee el archivo JSON existente
            with open("config.json", "r") as archivo:
                configJson = json.load(archivo)
            configJson.update(datos)
            # Guarda los datos en un nuevo archivo JSON
            with open("config.json", "w") as archivo:
                json.dump(configJson, archivo, indent=4)
        else:
            # Lee el archivo JSON existente
            with open("config.json", "r") as archivo:
                configJson = json.load(archivo)
            datos = {
                'email': None,
                'password': None,
            }
            configJson.update(datos)
            # Guarda los datos en un nuevo archivo JSON
            with open("config.json", "w") as archivo:
                json.dump(configJson, archivo, indent=4)
        
    
    # Restablecer contraseña
    def restablecer_contrasenia(self):
        email = self.emailEdit_3.text()
        try:
            auth_1.send_password_reset_email(email)
            self.resetPassStatus.setText('Correo enviado correctamente')
            self.resetPassStatus.setToolTip('Correo enviado correctamente')
        except Exception as e:
            self.resetPassStatus.setText(str(e))
            self.resetPassStatus.setToolTip(str(e))
            print(str(e))
            
    
class MainWindow(QMainWindow,Ui_MainWindow):
    bt_perfilClicado = Signal()
    def __init__(self, login:Login):
        super().__init__()
        self.setupUi(self)
        
        self.login = login
        
        self.estados_iniciales()
        
        self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
        # Conectamos el evento de la animacion del menú lateral
        self.bt_contraer.clicked.connect(self.mover_menu)
        self.bt_expandir.clicked.connect(self.mover_menu)
        
        # Condiciones iniciales
        self.bt_normal.hide()
        self.bt_expandir.hide()
        self.click_position = None
        
        # Conectar eventos de botones de control de ventana
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
        
        # Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # sizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        # Mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        
        #####################################################################################################################
        #!#####################################  Cargar gif a los botones personalizados  ###################################
        #####################################################################################################################
        self.bt_unidad_1.setGifFileName("resources/images/MainWindow/bt_unidad_1.gif")
        self.bt_unidad_2.setGifFileName("resources/images/MainWindow/bt_unidad_2.gif")
        self.bt_unidad_3.setGifFileName("resources/images/MainWindow/bt_unidad_3.gif")
        self.bt_unidad_4.setGifFileName("resources/images/MainWindow/bt_unidad_4.gif")
        self.bt_U1_T1.setGifFileName("resources/images/MainWindow/unidad 1/Unidad_1_Tema_1.gif")
        self.bt_U1_T2.setGifFileName("resources/images/MainWindow/unidad 1/Unidad_1_Tema_2.gif")
        self.bt_U1_T3.setGifFileName("resources/images/MainWindow/unidad 1/Unidad_1_Tema_3.gif")
        self.bt_U1_T4.setGifFileName("resources/images/MainWindow/unidad 1/Unidad_1_Tema_4.gif")
        self.bt_U1_T5.setGifFileName("resources/images/MainWindow/unidad 1/Unidad_1_Tema_5.gif")
        self.bt_U2_T1.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_1.gif")
        self.bt_U2_T2.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_2.gif")
        self.bt_U2_T3.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_3.gif")
        self.bt_U2_T4.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_4.gif")
        self.bt_U2_T5.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_5.gif")
        self.bt_U2_T6.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_6.gif")
        self.bt_U2_T7.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_7.gif")
        self.bt_U2_T8.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_8.gif")
        self.bt_U2_T9.setGifFileName("resources/images/MainWindow/unidad 2/Unidad_2_Tema_9.gif")
        self.bt_U3_T1.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_1.gif")
        self.bt_U3_T2.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_2.gif")
        self.bt_U3_T3.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_3.gif")
        self.bt_U3_T4.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_4.gif")
        self.bt_U3_T5.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_5.gif")
        self.bt_U3_T6.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_6.gif")
        self.bt_U3_T7.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_7.gif")
        self.bt_U3_T8.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_8.gif")
        self.bt_U3_T9.setGifFileName("resources/images/MainWindow/unidad 3/Unidad_3_Tema_9.gif")
        self.bt_U4_T1.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_1.gif")
        self.bt_U4_T2.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_2.gif")
        self.bt_U4_T3.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_3.gif")
        self.bt_U4_T4.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_4.gif")
        self.bt_U4_T5.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_5.gif")
        self.bt_U4_T6.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_6.gif")
        self.bt_U4_T7.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_7.gif")
        self.bt_U4_T8.setGifFileName("resources/images/MainWindow/unidad 4/Unidad_4_Tema_8.gif")
        
        
        #####################################################################################################################
        #!########################################  Eventos de botones de navegación  #######################################
        #####################################################################################################################
        self.bt_unidad_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.bt_unidad_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.bt_unidad_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.bt_unidad_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.bt_U1_T1.clicked.connect(self.init_bt_U1_T1)
        self.bt_U1_T2.clicked.connect(self.init_bt_U1_T2)
        self.bt_U1_T3.clicked.connect(self.init_bt_U1_T3)
        self.bt_U1_T4.clicked.connect(self.init_bt_U1_T4)
        self.bt_U1_T5.clicked.connect(self.init_bt_U1_T5)
        self.bt_U2_T1.clicked.connect(self.init_bt_U2_T1)
        self.bt_U2_T2.clicked.connect(self.init_bt_U2_T2)
        self.bt_U2_T3.clicked.connect(self.init_bt_U2_T3)
        self.bt_U2_T4.clicked.connect(self.init_bt_U2_T4)
        self.bt_U2_T5.clicked.connect(self.init_bt_U2_T5)
        self.bt_U2_T6.clicked.connect(self.init_bt_U2_T6)
        self.bt_U2_T7.clicked.connect(self.init_bt_U2_T7)
        self.bt_U2_T8.clicked.connect(self.init_bt_U2_T8)
        self.bt_U2_T9.clicked.connect(self.init_bt_U2_T9)
        self.bt_U3_T1.clicked.connect(self.init_bt_U3_T1)
        self.bt_U3_T2.clicked.connect(self.init_bt_U3_T2)
        self.bt_U3_T3.clicked.connect(self.init_bt_U3_T3)
        self.bt_U3_T4.clicked.connect(self.init_bt_U3_T4)
        self.bt_U3_T5.clicked.connect(self.init_bt_U3_T5)
        self.bt_U3_T6.clicked.connect(self.init_bt_U3_T6)
        self.bt_U3_T7.clicked.connect(self.init_bt_U3_T7)
        self.bt_U3_T8.clicked.connect(self.init_bt_U3_T8)
        self.bt_U3_T9.clicked.connect(self.init_bt_U3_T9)
        self.bt_U4_T1.clicked.connect(self.init_bt_U4_T1)
        self.bt_U4_T2.clicked.connect(self.init_bt_U4_T2)
        self.bt_U4_T3.clicked.connect(self.init_bt_U4_T3)
        self.bt_U4_T4.clicked.connect(self.init_bt_U4_T4)
        self.bt_U4_T5.clicked.connect(self.init_bt_U4_T5)
        self.bt_U4_T6.clicked.connect(self.init_bt_U4_T6)
        self.bt_U4_T7.clicked.connect(self.init_bt_U4_T7)
        self.bt_U4_T8.clicked.connect(self.init_bt_U4_T8)
        self.bt_return.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.bt_return_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.bt_return_12.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.bt_return_18.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.bt_return_1.clicked.connect(lambda: self.stackedUnidad_1.setCurrentIndex(0))
        self.bt_return_2.clicked.connect(lambda: self.stackedUnidad_1.setCurrentIndex(0))
        self.bt_return_3.clicked.connect(lambda: self.stackedUnidad_1.setCurrentIndex(0))
        self.bt_return_4.clicked.connect(lambda: self.stackedUnidad_1.setCurrentIndex(0))
        self.bt_return_5.clicked.connect(lambda: self.stackedUnidad_1.setCurrentIndex(0))
        self.bt_return_7.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_8.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_9.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_10.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_11.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_24.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_25.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_26.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_27.clicked.connect(lambda: self.stackedUnidad_2.setCurrentIndex(0))
        self.bt_return_13.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_14.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_15.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_16.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_17.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_28.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_29.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_30.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_31.clicked.connect(lambda: self.stackedUnidad_3.setCurrentIndex(0))
        self.bt_return_19.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_20.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_21.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_22.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_23.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_32.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_33.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        self.bt_return_34.clicked.connect(lambda: self.stackedUnidad_4.setCurrentIndex(0))
        
        # Redimenciona el fondo al tamaño de la pantalla
        self.applyBackground()
        
        # Se conecta la señal para cerrar sesión
        self.bt_cerrarSesion.clicked.connect(self.cerrarSesion)
        
        # Se conecta la señal para personalizar perfil
        self.bt_perfil.clicked.connect(self.personalizar)
        
        
    def cambiar_ventana(self):
        self.hide()
        self.login.show()
        
    def control_bt_normal(self):
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximize.show()
        
    def control_bt_maximize(self):
        self.showMaximized()
        self.bt_normal.show()
        self.bt_maximize.hide()
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition()
        
    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        
    def mover_ventana(self, event):
        
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                posicion = QPointF(self.pos().x(),self.pos().y()) + event.globalPosition() - self.clickPosition
                self.move(posicion.x(),posicion.y())
                self.clickPosition = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.bt_normal.show()
            self.bt_maximize.hide()
        else:
            self.showNormal()
            self.bt_normal.hide()
            self.bt_maximize.show()
        
    def mover_menu(self):
        width = self.menu_lateral.width()
        normal = 0
        if width == 0:
            extender = 300
            self.bt_expandir.hide()
            self.bt_contraer.show()
        else:
            self.bt_expandir.show()
            self.bt_contraer.hide()
            extender = normal
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setDuration(500)
        self.animacion.setEasingCurve(QEasingCurve.OutInBack) # InQuad, InOutQuad, InCubic, InOutExpo, OutInBack
        self.animacion.start()
      
    def estados_iniciales(self):
        self.click_bt_U1_T1 = False
        self.click_bt_U1_T2 = False
        self.click_bt_U1_T3 = False
        self.click_bt_U1_T4 = False
        self.click_bt_U1_T5 = False
        self.click_bt_U2_T1 = False
        self.click_bt_U2_T2 = False
        self.click_bt_U2_T3 = False
        self.click_bt_U2_T4 = False
        self.click_bt_U2_T5 = False
        self.click_bt_U2_T6 = False
        self.click_bt_U2_T7 = False
        self.click_bt_U2_T8 = False
        self.click_bt_U2_T9 = False
        self.click_bt_U3_T1 = False
        self.click_bt_U3_T2 = False
        self.click_bt_U3_T3 = False
        self.click_bt_U3_T4 = False
        self.click_bt_U3_T5 = False
        self.click_bt_U3_T6 = False
        self.click_bt_U3_T7 = False
        self.click_bt_U3_T8 = False
        self.click_bt_U3_T9 = False
        self.click_bt_U4_T1 = False
        self.click_bt_U4_T2 = False
        self.click_bt_U4_T3 = False
        self.click_bt_U4_T4 = False
        self.click_bt_U4_T5 = False
        self.click_bt_U4_T6 = False
        self.click_bt_U4_T7 = False
        self.click_bt_U4_T8 = False
    #####################################################################################################################
    #!################################  Métodos de eventos de los botones de cada tema  #################################
    #####################################################################################################################
    def init_bt_U1_T1(self):
        ######################### Se miestra la vista del tema clickeado ###################
        self.stackedUnidad_1.setCurrentIndex(1)
        if not self.click_bt_U1_T1:
            ########################### Se abre el pdf del tema ############################
            self.U1_T1.pdfView.open('resources/pdf/unidad 1/tema 1/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U1_T1 = V_U1_T1(self,self.U1_T1.frameVideo,self.U1_T1.tabWidget,self.bt_return_1)
            ######################### Se inicializa la simulación ##########################
            self.sim_U1_T1 = Sim_U1_T1()
            self.U1_T1.simLayout.addWidget(self.sim_U1_T1)
            self.sim_U1_T1.init()
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U1_T1 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U1_T1.abrir()
    def init_bt_U1_T2(self):
        self.stackedUnidad_1.setCurrentIndex(2)
        if not self.click_bt_U1_T2:
            ########################### Se abre el pdf del tema ############################
            self.U1_T2.pdfView.open('resources/pdf/unidad 1/tema 2/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U1_T2 = V_U1_T2(self,self.U1_T2.frameVideo,self.U1_T2.tabWidget,self.bt_return_2)
            ######################### Se inicializa la simulación ##########################
            self.sim_U1_T2 = Sim_U1_T2()
            self.U1_T2.simLayout.addWidget(self.sim_U1_T2)
            self.sim_U1_T2.init()
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U1_T2 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U1_T2.abrir()
    def init_bt_U1_T3(self):
        self.stackedUnidad_1.setCurrentIndex(3)
        if not self.click_bt_U1_T3:
            ########################### Se abre el pdf del tema ############################
            self.U1_T3.pdfView.open('resources/pdf/unidad 1/tema 3/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U1_T3 = V_U1_T3(self,self.U1_T3.frameVideo,self.U1_T3.tabWidget,self.bt_return_3)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U1_T3 = Sim_U1_T3()
            self.U1_T3.simLayout.addWidget(self.sim_U1_T3)
            self.sim_U1_T3.init()
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U1_T3 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U1_T3.abrir()
    def init_bt_U1_T4(self):
        self.stackedUnidad_1.setCurrentIndex(4)
        if not self.click_bt_U1_T4:
            ########################### Se abre el pdf del tema ############################
            self.U1_T4.pdfView.open('resources/pdf/unidad 1/tema 4/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U1_T4 = V_U1_T4(self,self.U1_T4.frameVideo,self.U1_T4.tabWidget,self.bt_return_4)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U1_T4 = Sim_U1_T4()
            self.U1_T4.simLayout.addWidget(self.sim_U1_T4)
            self.sim_U1_T4.init()
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U1_T4 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U1_T4.abrir()
    def init_bt_U1_T5(self):
        self.stackedUnidad_1.setCurrentIndex(5)
        if not self.click_bt_U1_T5:
            ########################### Se abre el pdf del tema ############################
            self.U1_T5.pdfView.open('resources/pdf/unidad 1/tema 5/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U1_T5 = V_U1_T5(self,self.U1_T5.frameVideo,self.U1_T5.tabWidget,self.bt_return_5)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U1_T5 = Sim_U1_T5()
            self.U1_T5.simLayout.addWidget(self.sim_U1_T5)
            self.sim_U1_T5.init()
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U1_T5 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U1_T5.abrir()
    def init_bt_U2_T1(self):
        self.stackedUnidad_2.setCurrentIndex(1)
        if not self.click_bt_U2_T1:
            ########################### Se abre el pdf del tema ############################
            self.U2_T1.pdfView.open('resources/pdf/unidad 2/tema 1/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T1 = V_U2_T1(self,self.U2_T1.frameVideo,self.U2_T1.tabWidget,self.bt_return_7)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T1 = Sim_U2_T1()
            self.U2_T1.simLayout.addWidget(self.sim_U2_T1)
            self.sim_U2_T1.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T1.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T1 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T1.abrir()
    def init_bt_U2_T2(self):
        self.stackedUnidad_2.setCurrentIndex(2)
        if not self.click_bt_U2_T2:
            ########################### Se abre el pdf del tema ############################
            self.U2_T2.pdfView.open('resources/pdf/unidad 2/tema 2/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T2 = V_U2_T2(self,self.U2_T2.frameVideo,self.U2_T2.tabWidget,self.bt_return_8)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T2 = Sim_U2_T2()
            self.U2_T2.simLayout.addWidget(self.sim_U2_T2)
            self.sim_U2_T2.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T2.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T2 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T2.abrir()
    def init_bt_U2_T3(self):
        self.stackedUnidad_2.setCurrentIndex(3)
        if not self.click_bt_U2_T3:
            ########################### Se abre el pdf del tema ############################
            self.U2_T3.pdfView.open('resources/pdf/unidad 2/tema 3/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T3 = V_U2_T3(self,self.U2_T3.frameVideo,self.U2_T3.tabWidget,self.bt_return_9)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T3 = Sim_U2_T3()
            self.U2_T3.simLayout.addWidget(self.sim_U2_T3)
            self.sim_U2_T3.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T3.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T3 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T3.abrir()
    def init_bt_U2_T4(self):
        self.stackedUnidad_2.setCurrentIndex(4)
        if not self.click_bt_U2_T4:
            ########################### Se abre el pdf del tema ############################
            self.U2_T4.pdfView.open('resources/pdf/unidad 2/tema 4/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T4 = V_U2_T4(self,self.U2_T4.frameVideo,self.U2_T4.tabWidget,self.bt_return_10)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T4 = Sim_U2_T4()
            self.U2_T4.simLayout.addWidget(self.sim_U2_T4)
            self.sim_U2_T4.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T4.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T4 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T4.abrir()
    def init_bt_U2_T5(self):
        self.stackedUnidad_2.setCurrentIndex(5)
        if not self.click_bt_U2_T5:
            ########################### Se abre el pdf del tema ############################
            self.U2_T5.pdfView.open('resources/pdf/unidad 2/tema 5/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T5 = V_U2_T5(self,self.U2_T5.frameVideo,self.U2_T5.tabWidget,self.bt_return_11)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T5 = Sim_U2_T5()
            self.U2_T5.simLayout.addWidget(self.sim_U2_T5)
            self.sim_U2_T5.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T5.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T5 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T5.abrir()
    def init_bt_U2_T6(self):
        self.stackedUnidad_2.setCurrentIndex(6)
        if not self.click_bt_U2_T6:
            ########################### Se abre el pdf del tema ############################
            self.U2_T6.pdfView.open('resources/pdf/unidad 2/tema 6/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T6 = V_U2_T6(self,self.U2_T6.frameVideo,self.U2_T6.tabWidget,self.bt_return_24)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T6 = Sim_U2_T6()
            self.U2_T6.simLayout.addWidget(self.sim_U2_T6)
            self.sim_U2_T6.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T6.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T6 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T6.abrir()
    def init_bt_U2_T7(self):
        self.stackedUnidad_2.setCurrentIndex(7)
        if not self.click_bt_U2_T7:
            ########################### Se abre el pdf del tema ############################
            self.U2_T7.pdfView.open('resources/pdf/unidad 2/tema 7/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T7 = V_U2_T7(self,self.U2_T7.frameVideo,self.U2_T7.tabWidget,self.bt_return_25)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T7 = Sim_U2_T7()
            self.U2_T7.simLayout.addWidget(self.sim_U2_T7)
            self.sim_U2_T7.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T7.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T7 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T7.abrir()
    def init_bt_U2_T8(self):
        self.stackedUnidad_2.setCurrentIndex(8)
        if not self.click_bt_U2_T8:
            ########################### Se abre el pdf del tema ############################
            self.U2_T8.pdfView.open('resources/pdf/unidad 2/tema 8/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T8 = V_U2_T8(self,self.U2_T8.frameVideo,self.U2_T8.tabWidget,self.bt_return_26)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T8 = Sim_U2_T8()
            self.U2_T8.simLayout.addWidget(self.sim_U2_T8)
            self.sim_U2_T8.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T8.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T8 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T8.abrir()
    def init_bt_U2_T9(self):
        self.stackedUnidad_2.setCurrentIndex(9)
        if not self.click_bt_U2_T9:
            ########################### Se abre el pdf del tema ############################
            self.U2_T9.pdfView.open('resources/pdf/unidad 2/tema 9/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U2_T9 = V_U2_T9(self,self.U2_T9.frameVideo,self.U2_T9.tabWidget,self.bt_return_27)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U2_T9 = Sim_U2_T9()
            self.U2_T9.simLayout.addWidget(self.sim_U2_T9)
            self.sim_U2_T9.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U2_T9.setColor(2)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U2_T9 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U2_T9.abrir()
    def init_bt_U3_T1(self):
        self.stackedUnidad_3.setCurrentIndex(1)
        if not self.click_bt_U3_T1:
            ########################### Se abre el pdf del tema ############################
            self.U3_T1.pdfView.open('resources/pdf/unidad 3/tema 1/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T1 = V_U3_T1(self,self.U3_T1.frameVideo,self.U3_T1.tabWidget,self.bt_return_13)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T1.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T1.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T1 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T1.abrir()
    def init_bt_U3_T2(self):
        self.stackedUnidad_3.setCurrentIndex(2)
        if not self.click_bt_U3_T2:
            ########################### Se abre el pdf del tema ############################
            self.U3_T2.pdfView.open('resources/pdf/unidad 3/tema 2/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T2 = V_U3_T2(self,self.U3_T2.frameVideo,self.U3_T2.tabWidget,self.bt_return_14)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T2.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T2.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T2 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T2.abrir()
    def init_bt_U3_T3(self):
        self.stackedUnidad_3.setCurrentIndex(3)
        if not self.click_bt_U3_T3:
            ########################### Se abre el pdf del tema ############################
            self.U3_T3.pdfView.open('resources/pdf/unidad 3/tema 3/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T3 = V_U3_T3(self,self.U3_T3.frameVideo,self.U3_T3.tabWidget,self.bt_return_15)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U3_T3 = Sim_U3_T3()
            self.U3_T3.simLayout.addWidget(self.sim_U3_T3)
            self.sim_U3_T3.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T3.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T3 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T3.abrir()
    def init_bt_U3_T4(self):
        self.stackedUnidad_3.setCurrentIndex(4)
        if not self.click_bt_U3_T4:
            ########################### Se abre el pdf del tema ############################
            self.U3_T4.pdfView.open('resources/pdf/unidad 3/tema 4/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T4 = V_U3_T4(self,self.U3_T4.frameVideo,self.U3_T4.tabWidget,self.bt_return_16)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U3_T4 = Sim_U3_T4()
            self.U3_T4.simLayout.addWidget(self.sim_U3_T4)
            self.sim_U3_T4.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T4.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T4 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T4.abrir()
    def init_bt_U3_T5(self):
        self.stackedUnidad_3.setCurrentIndex(5)
        if not self.click_bt_U3_T5:
            ########################### Se abre el pdf del tema ############################
            self.U3_T5.pdfView.open('resources/pdf/unidad 3/tema 5/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T5 = V_U3_T5(self,self.U3_T5.frameVideo,self.U3_T5.tabWidget,self.bt_return_17)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U3_T5 = Sim_U3_T5()
            self.U3_T5.simLayout.addWidget(self.sim_U3_T5)
            self.sim_U3_T5.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T5.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T5 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T5.abrir()
    def init_bt_U3_T6(self):
        self.stackedUnidad_3.setCurrentIndex(6)
        if not self.click_bt_U3_T6:
            ########################### Se abre el pdf del tema ############################
            self.U3_T6.pdfView.open('resources/pdf/unidad 3/tema 6/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T6 = V_U3_T6(self,self.U3_T6.frameVideo,self.U3_T6.tabWidget,self.bt_return_28)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T6.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T6.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T6 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T6.abrir()
    def init_bt_U3_T7(self):
        self.stackedUnidad_3.setCurrentIndex(7)
        if not self.click_bt_U3_T7:
            ########################### Se abre el pdf del tema ############################
            self.U3_T7.pdfView.open('resources/pdf/unidad 3/tema 7/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T7 = V_U3_T7(self,self.U3_T7.frameVideo,self.U3_T7.tabWidget,self.bt_return_29)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T7.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T7.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T7 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T7.abrir()
    def init_bt_U3_T8(self):
        self.stackedUnidad_3.setCurrentIndex(8)
        if not self.click_bt_U3_T8:
            ########################### Se abre el pdf del tema ############################
            self.U3_T8.pdfView.open('resources/pdf/unidad 3/tema 8/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T8 = V_U3_T8(self,self.U3_T8.frameVideo,self.U3_T8.tabWidget,self.bt_return_30)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T8.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T8.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T8 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T8.abrir()
    def init_bt_U3_T9(self):
        self.stackedUnidad_3.setCurrentIndex(9)
        if not self.click_bt_U3_T9:
            ########################### Se abre el pdf del tema ############################
            self.U3_T9.pdfView.open('resources/pdf/unidad 3/tema 9/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U3_T9 = V_U3_T9(self,self.U3_T9.frameVideo,self.U3_T9.tabWidget,self.bt_return_31)
            ###################### Se crea e inicializa la simulación ######################
            self.U3_T9.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U3_T9.setColor(3)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U3_T9 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U3_T9.abrir()
    def init_bt_U4_T1(self):
        self.stackedUnidad_4.setCurrentIndex(1)
        if not self.click_bt_U4_T1:
            ########################### Se abre el pdf del tema ############################
            self.U4_T1.pdfView.open('resources/pdf/unidad 4/tema 1/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T1 = V_U4_T1(self,self.U4_T1.frameVideo,self.U4_T1.tabWidget,self.bt_return_19)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T1 = Sim_U4_T1()
            self.U4_T1.simLayout.addWidget(self.sim_U4_T1)
            self.sim_U4_T1.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T1.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T1 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T1.abrir()
    def init_bt_U4_T2(self):
        self.stackedUnidad_4.setCurrentIndex(2)
        if not self.click_bt_U4_T2:
            ########################### Se abre el pdf del tema ############################
            self.U4_T2.pdfView.open('resources/pdf/unidad 4/tema 2/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T2 = V_U4_T2(self,self.U4_T2.frameVideo,self.U4_T2.tabWidget,self.bt_return_20)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T2 = Sim_U4_T2()
            self.U4_T2.simLayout.addWidget(self.sim_U4_T2)
            self.sim_U4_T2.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T2.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T2 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T2.abrir()
    def init_bt_U4_T3(self):
        self.stackedUnidad_4.setCurrentIndex(3)
        if not self.click_bt_U4_T3:
            ########################### Se abre el pdf del tema ############################
            self.U4_T3.pdfView.open('resources/pdf/unidad 4/tema 3/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T3 = V_U4_T3(self,self.U4_T3.frameVideo,self.U4_T3.tabWidget,self.bt_return_21)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T3 = Sim_U4_T3()
            self.U4_T3.simLayout.addWidget(self.sim_U4_T3)
            self.sim_U4_T3.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T3.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T3 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T3.abrir()
    def init_bt_U4_T4(self):
        self.stackedUnidad_4.setCurrentIndex(4)
        if not self.click_bt_U4_T4:
            ########################### Se abre el pdf del tema ############################
            self.U4_T4.pdfView.open('resources/pdf/unidad 4/tema 4/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T4 = V_U4_T4(self,self.U4_T4.frameVideo,self.U4_T4.tabWidget,self.bt_return_22)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T4 = Sim_U4_T4()
            self.U4_T4.simLayout.addWidget(self.sim_U4_T4)
            self.sim_U4_T4.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T4.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T4 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T4.abrir()
    def init_bt_U4_T5(self):
        self.stackedUnidad_4.setCurrentIndex(5)
        if not self.click_bt_U4_T5:
            ########################### Se abre el pdf del tema ############################
            self.U4_T5.pdfView.open('resources/pdf/unidad 4/tema 5/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T5 = V_U4_T5(self,self.U4_T5.frameVideo,self.U4_T5.tabWidget,self.bt_return_23)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T5 = Sim_U4_T5()
            self.U4_T5.simLayout.addWidget(self.sim_U4_T5)
            self.sim_U4_T5.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T5.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T5 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T5.abrir()
    def init_bt_U4_T6(self):
        self.stackedUnidad_4.setCurrentIndex(6)
        if not self.click_bt_U4_T6:
            ########################### Se abre el pdf del tema ############################
            self.U4_T6.pdfView.open('resources/pdf/unidad 4/tema 6/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T6 = V_U4_T6(self,self.U4_T6.frameVideo,self.U4_T6.tabWidget,self.bt_return_32)
            ###################### Se crea e inicializa la simulación ######################
            self.sim_U4_T6 = Sim_U4_T6()
            self.U4_T6.simLayout.addWidget(self.sim_U4_T6)
            self.sim_U4_T6.init()
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T6.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T6 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T6.abrir()
    def init_bt_U4_T7(self):
        self.stackedUnidad_4.setCurrentIndex(7)
        if not self.click_bt_U4_T7:
            ########################### Se abre el pdf del tema ############################
            self.U4_T7.pdfView.open('resources/pdf/unidad 4/tema 7/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T7 = V_U4_T7(self,self.U4_T7.frameVideo,self.U4_T7.tabWidget,self.bt_return_33)
            ###################### Se crea e inicializa la simulación ######################
            self.U4_T7.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T7.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T7 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T7.abrir()
    def init_bt_U4_T8(self):
        self.stackedUnidad_4.setCurrentIndex(8)
        if not self.click_bt_U4_T8:
            ########################### Se abre el pdf del tema ############################
            self.U4_T8.pdfView.open('resources/pdf/unidad 4/tema 8/')
            ####################### Se crea la ventana de los videos #######################
            self.v_U4_T8 = V_U4_T8(self,self.U4_T8.frameVideo,self.U4_T8.tabWidget,self.bt_return_34)
            ###################### Se crea e inicializa la simulación ######################
            self.U4_T8.tabWidget.removeTab(2)
            ################## Se adisgna el color al widget del contenido #################
            self.U4_T8.setColor(4)
            ################ Se establece que el botón ya ha sido clickeado ################
            self.click_bt_U4_T8 = True
        ######## Se habilita la ventana de videos para que interactue y sea mostrada #######
        self.v_U4_T8.abrir()
    #####################################################################################################
    #!################### Redimenciona el fondo al tamaño de la pantalla y lo guarda ####################
    #####################################################################################################
    def applyBackground(self):
        # Obtiene las dimensiones de la pantalla
        screen = QApplication.primaryScreen()
        screen_size = screen.size()

        # Carga la imagen original
        pixmap = QPixmap("resources/images/background.png")

        # Redimensiona la imagen al tamaño de la pantalla con interpolación suave
        resized_pixmap = pixmap.scaled(screen_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # Guarda la imagen redimensionada
        resized_pixmap.save("resources/images/resized_background.png")
        
    def personalizar(self):
        self.bt_perfilClicado.emit()
        dialog_personalizar = Personalizar(self)
        dialog_personalizar.exec()
    
    def iniciarSesion(self,datos):
        self.datos = datos
        email = datos['email']
        password = datos['password']
        if email=='invitado':
            self.lb_userID.setText('Invitado')
            self.lb_userName.setText('Invitado')
            self.bt_perfil.setEnabled(False)
            icon = QIcon()
            icon.addFile("resources/images/MainWindow/perfiles/avatar_0.png", QSize(), QIcon.Normal, QIcon.Off)
            self.bt_perfil.setIcon(icon)
            self.show()
        else:
            try:
                self.user_1 = auth_1.sign_in_with_email_and_password(email,password)
                self.user = auth.get_user_by_email(email)
                self.lb_userID.setText(self.user.uid)
                self.lb_userName.setText(self.user.display_name)
                self.bt_perfil.setEnabled(True)
                icon = QIcon()
                self.fotoPerfil = icon
                if self.user.photo_url!=None:
                    nombre_archivo = self.user.photo_url[8:]
                else:
                    nombre_archivo=None
                if nombre_archivo in ('1','2','3','4','5','6','7','8','9','10','0'):
                    if nombre_archivo == '0':
                        extension='.png'
                    else:
                        extension='.svg'
                    icon.addFile("resources/images/MainWindow/perfiles/avatar_"+nombre_archivo+extension, QSize(), QIcon.Normal, QIcon.Off)
                    self.bt_perfil.setIcon(icon)
                elif self.user.photo_url != None:
                    _, extension = os.path.splitext(self.user.photo_url[8:])
                    archivo = "resources/images/MainWindow/perfiles/MiFoto"+extension
                    # Se descarga la foto del usuario
                    storage.child(self.user.photo_url[8:]).download("",archivo)
                    icon.addFile(archivo, QSize(), QIcon.Normal, QIcon.Off)
                    self.bt_perfil.setIcon(icon)
                else:
                    icon.addFile("resources/images/MainWindow/perfiles/avatar_0.png", QSize(), QIcon.Normal, QIcon.Off)
                self.show()
            except Exception as e:
                print(e)
                self.login.stackedWidget.setCurrentIndex(0)
                self.login.show()
    
                
    def cerrarSesion(self):
        # Lee el archivo JSON existente
        with open("config.json", "r") as archivo:
            configJson = json.load(archivo)
        datos = {
            'email': None,
            'password': None,
            'role': 'usuario'
        }
        configJson.update(datos)
        # Guarda los datos en un nuevo archivo JSON
        with open("config.json", "w") as archivo:
            json.dump(configJson, archivo, indent=4)
        
        # Se muestra el login
        self.login.stackedWidget.setCurrentIndex(0)
        self.login.show()
        self.hide()
                
    def actualizarPerfil(self,photo_url,display_name:str,esFoto:bool):
        progress_dialog = QProgressDialog("Cargando...", None, 0, 100,self)
        progress_dialog.setFixedSize(QSize(600,70))
        progress_dialog.setWindowTitle("Actualizando Perfil")
        progress_dialog.setModal(True)  # Hace que la ventana sea modal
        actualizandoPerfil = ActualizandoPerfil(self,photo_url,display_name,esFoto,progress_dialog,self)
        actualizandoPerfil.update_progress.connect(lambda value:progress_dialog.setValue(value))
        actualizandoPerfil.update_textProgress.connect(lambda text:progress_dialog.setLabelText(text))
        actualizandoPerfil.update_closeProgress.connect(lambda:progress_dialog.close())
        actualizandoPerfil.update_bt_perfil.connect(lambda icon:self.bt_perfil.setIcon(icon))
        actualizandoPerfil.update_fotoPerfil.connect(self.setFotoPerfil)
        actualizandoPerfil.update_photo_url.connect(self.setPhoto_url)
        actualizandoPerfil.update_lb_userName.connect(lambda name:self.lb_userName.setText(name))
        actualizandoPerfil.update_error.connect(lambda error:QMessageBox.critical(self, "Error", error))
        progress_dialog.show()
        actualizandoPerfil.start()
        
    def setFotoPerfil(self,fotoPerfil):
        self.fotoPerfil=fotoPerfil
        
    def setPhoto_url(self,photo_url):
        self.photo_url=photo_url
            
#################################################################################################################
#!####################  Clase del hilo donde se ejecuta la actualización del perfil  ############################
#################################################################################################################
class ActualizandoPerfil(QThread):
    update_progress = Signal(int)
    update_textProgress = Signal(str)
    update_closeProgress = Signal()
    update_bt_perfil = Signal(QIcon)
    update_fotoPerfil = Signal(QIcon)
    update_photo_url = Signal(str)
    update_lb_userName = Signal(str)
    update_error = Signal(str)
    
    def __init__(self,mainWindow,photo_url,display_name:str,esFoto:bool,progress_dialog:QProgressDialog, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.mw = mainWindow
        self.photo_url=photo_url
        self.display_name=display_name
        self.esFoto=esFoto
        self.progress_dialog=progress_dialog
        
    def run(self):
        try:
            if self.photo_url!='sinCambio':
                if self.esFoto:
                    _, extension = os.path.splitext(self.photo_url)
                    nombre_archivo = os.path.basename(self.photo_url)
                    try:
                        self.progress_dialog.setLabelText('Subiendo foto...')
                        url = "https://perfiles/fotos/"+self.mw.user.uid+extension
                        storage.child("perfiles/fotos/"+self.mw.user.uid+extension).put(self.photo_url)
                        icon = QIcon()
                        icon.addFile(self.photo_url, QSize(), QIcon.Normal, QIcon.Off)
                        self.update_bt_perfil.emit(icon)
                        self.update_fotoPerfil.emit(icon)
                        self.update_photo_url.emit(url)
                        self.photo_url = url
                    except Exception as e:
                        self.update_error.emit('Hubo un error en la subida de la imagen:\n\n'+str(e))
                        raise ValueError(e)
                else:
                    self.update_textProgress.emit('Subiendo foto...')
                    icon = QIcon()
                    nombre_archivo = self.photo_url[8:]
                    if nombre_archivo == '0':
                        extension='.png'
                        # self.update_photo_url.emit(self.photo_url)
                    else:
                        extension='.svg'
                    icon.addFile("resources/images/MainWindow/perfiles/avatar_"+nombre_archivo+extension, QSize(), QIcon.Normal, QIcon.Off)
                    self.update_bt_perfil.emit(icon)
                    self.update_fotoPerfil.emit(icon)
            else:
                self.photo_url=self.mw.user.photo_url
            self.update_progress.emit(50)
            self.update_textProgress.emit('Actualizando datos...')
            datos={
                'photo_url':self.photo_url,
                'display_name':self.display_name
            }
            try:
                auth.update_user(self.mw.user.uid,**datos)
                self.update_lb_userName.emit(self.display_name)
                self.update_progress.emit(100)
            except Exception as e:
                self.update_error.emit('Hubo un problema un la actualización de los datos:\n\n'+str(e))
                raise ValueError(e)
        except Exception as e:
                
                pass
        self.update_closeProgress.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())