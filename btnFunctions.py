import os
import subprocess
import ctypes
import sys
import psutil
from send2trash import send2trash

from tkinter import messagebox

def runAsAdmin(command):
        if ctypes.windll.shell32.IsUserAnAdmin():
                return subprocess.run(command, shell=True)
        else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", command, None, 1)

def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS2
        except Exception:
                base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

# Abre la ubicación de los archivos temporales
def deleteTempFiles():
        username = os.environ.get('USERNAME')
        temp_folder_paths = [
                fr"C:\Users\{username}\AppData\Local\Temp",
                r"C:\Windows\Temp"
        ]

        for folder_path in temp_folder_paths:
                os.system(f"start explorer {folder_path}")

# Elimina los archivos temporales (lento)
r""" 
def deleteTempFiles()              
 username = os.environ.get('USERNAME')
    
        folderPaths = [
                fr"C:\Users\{username}\AppData\Local\Temp",
                os.environ['TEMP']
        ]
        
        filesDeleted = False
        emptyFolderMsgShown = False

        for folderPath in folderPaths:
                if os.path.exists(folderPath):
                        files = os.listdir(folderPath)
                        if files:
                                for file in files:
                                        filePath = os.path.join(folderPath, file)
                                        try:
                                                send2trash(filePath)
                                                filesDeleted = True
                                                print('Archivo eliminado:', filePath)
                                        except PermissionError:
                                                print('No se puede eliminar el archivo:', filePath)
                                                continue

        if filesDeleted:
                print("Se han eliminado los archivos temporales.")
        elif not emptyFolderMsgShown:
                print("No se encontraron archivos temporales para eliminar.")
        """


"""                   
for folderPath in folderPaths:
        if os.path.exists(folderPath):
        files = os.listdir(folderPath)
        if files:
                filesDeleted = True
                for file in files:
                        filePath = os.path.join(folderPath, file)
                        print('Deleting file:', filePath)
                        time.sleep(1)
                        os.remove(filePath) 
     """                                                    

def fixInternet():
        confirmation = messagebox.askquestion("Solución de problemas de conexión a Internet", "¿Está seguro de que desea solucionar problemas de conexión a Internet", icon='warning')
        if confirmation == "yes":    
                commands = [
                        "netsh int ip reset c:\resetlog.txt",
                        "netsh winsock reset",
                        "netsh int ip reset",
                        "ipconfig /release",
                        "ipconfig /renew",
                        "ipconfig /flushdns"
                ]
                
                for command in commands:
                        runAsAdmin(command)
                messagebox.showinfo("Solucionar internet", "Se han aplicado correctamente las soluciones para solucionar problemas de conexión a Internet.")

def close_open_files(file_path):
    try:
        file_handle = open(file_path, 'w')
        file_handle.close()
    except PermissionError:
        pass
    
def openMsconfig():
        subprocess.run('msconfig', shell=True)

def is_file_in_use(file_path):
    for proc in psutil.process_iter(['name']):
        try:
            files = proc.open_files()
            if any(file.path == file_path for file in files):
                return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return False

def openAdvanceSystSettings():
       subprocess.run('sysdm.cpl', shell=True) 

def openWindowsFeatures():
       subprocess.run('optionalfeatures', shell=True) 

def openDevicesAndPrinter():
       subprocess.run('control printers', shell=True) 

def openNtworkConnections():
       subprocess.run('ncpa.cpl', shell=True) 

def openProxy():
       subprocess.run('start ms-settings:network-proxy', shell=True) 

def scannow():
        confirmation = messagebox.askquestion("Escanear archivos del sistema", "¿Está seguro de que desea escanear los archivos del sistema?", icon='warning')
        if confirmation == "yes":    
                command = 'sfc /scannow'
                runAsAdmin(command)

                messagebox.showinfo("Escanear archivos del sistema", "El escaneo de archivos del sistema se ha completado correctamente.")


def dism():
        confirmation = messagebox.askquestion("Herramienta DISM", "¿Está seguro de que desea ejecutar la herramienta DISM?", icon='warning')
        if confirmation == "yes":
                commands = [
                        "DISM /Online /Cleanup-Image /ScanHealth",
                        "DISM /Online /Cleanup-Image /CheckHealth",
                        "DISM /Online /Cleanup-Image /RestoreHealth",
                        "DISM /Online /Cleanup-Image /startComponentCleanup",
                ]
                
                for command in commands:
                        runAsAdmin(command)

                messagebox.showinfo("Herramienta DISM", "Herramienta DISM se completó correctamente.")


def checkDisk():
        confirmation = messagebox.askquestion("Comprobación de disco", "¿Está seguro de que desea realizar una comprobación de disco?", icon='warning')
        if confirmation == "yes":
                command = 'chkdsk /f /r /b /x'
                runAsAdmin(command)

                messagebox.showinfo("Comprobación de disco", "La comprobación de disco se ha completado correctamente.")             

def diskdeFragmentation():
        subprocess.run('dfrgui', shell=True) 

def servicesMSC():
        subprocess.run("services.msc", shell=True) 

def openWindowsDefender():
        os.system("start start windowsdefender:")

def openBackgroundApps():
        os.system("start ms-settings:privacy-backgroundapps")
