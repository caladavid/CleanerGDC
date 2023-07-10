import customtkinter as ctk
import tkinter as tk
import psutil
import os
from PIL import Image, ImageOps

from btnFunctions import deleteTempFiles, fixInternet, openMsconfig, openAdvanceSystSettings, openWindowsFeatures, openDevicesAndPrinter, openNtworkConnections, openProxy, scannow, dism, checkDisk, resource_path, diskdeFragmentation, servicesMSC, openWindowsDefender, openBackgroundApps


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CleanerGDC")   
        self.geometry("900x600")   
        self.resizable(0, 0)
        self.wm_iconbitmap(resource_path("images/logo.ico"))

        ctk.set_appearance_mode("light")


        self.sideBar = sideBar(self)
        self.main = Main(self)

class sideBar(ctk.CTkFrame):
    def __init__(self, parents):
        super().__init__(parents)
        self.place(x=0, y=0, relwidth=0.1, relheight=1)

        self.createWidgetsSideBar()  

    def createWidgetsSideBar(self):
        logoPath = resource_path("images/logoJPG.jpg")
        settingsPath = resource_path("images/settingsJPG.jpg")

        backgroundColor = "white"

        background = ctk.CTkLabel(self, bg_color=backgroundColor, text="")
        background.place(relx=0, rely=0, relwidth=1, relheight=1) 
         
        lineBackground = ctk.CTkLabel(self, bg_color="#BDBDBD", text="", anchor="e", width=1)
        lineBackground.place(relx=0.9, y = 20, relheight=0.95)   

        #create the grid
        self.rowconfigure((0, 1,), weight=1,)

        logoImg = ctk.CTkImage(Image.open(resource_path(logoPath)), size=(60, 30))
        Logo = ctk.CTkLabel(self, text="", image = logoImg, bg_color=backgroundColor,)

        settingsImg = Image.open(settingsPath).convert("RGB")
        coloredSettingsImg = ImageOps.expand(settingsImg, border=10, fill=backgroundColor)
        settingsImg = ctk.CTkImage(coloredSettingsImg, size=(60, 60))

        settings = ctk.CTkButton(self, text="", fg_color=backgroundColor, image = settingsImg, width=0, height=0, hover=False )

        Logo.grid(row=0, sticky="N", padx=10, pady=20)
        settings.grid(row=1, sticky="S", padx=10, pady=20)

class Main(ctk.CTkFrame):
    def __init__(self, parents):
        super().__init__(parents)
        self.place(relx= 0.1, y = 0, relwidth= 0.9, relheight = 1)

        self.createWidgets()

    def nextPage(self):
        global isClicked
        isClicked = False

        if not isClicked:
            self.createWidgets2()
            isClicked = True
        else:
            self.createWidgets()
            isClicked = False

    def backPage(self):
            self.createWidgets()


    def createWidgets(self):
        tempFilesPath = resource_path("images/tempFiles.png")
        fixInternetPath = resource_path("images/fixInternet.png")
        devicesAndPrintertPath = resource_path("images/devicesAndPrinter.png")
        advanceSystSettingsPath = resource_path("images/advanceSystSettings.png")
        WindowsFeaturesPath = resource_path("images/WindowsFeatures.png")
        networkConnectionsPath = resource_path("images/networkConnections.png")
        MsconfigPath = resource_path("images/Msconfig.png")
        nextPath = resource_path("images/next.png")
        proxyPath = resource_path("images/proxy.png")


        username = os.environ.get('USERNAME')

        blue = "#1366DE"
        hoverColor = "#1676fc"
        backgroundColor = "white"
        myFont = ctk.CTkFont(family="Poppins", size=14)

        #Background
        background = ctk.CTkLabel(self, bg_color=backgroundColor, text="")
        background.place(relx=0, rely=0, relwidth=1, relheight=1)

        #Images
        tempFilesImg = ctk.CTkImage(Image.open(tempFilesPath), size=(55, 60))
        fixInternetImg = ctk.CTkImage(Image.open(fixInternetPath), size=(60, 50))
        devicesAndPrinterImg = ctk.CTkImage(Image.open(devicesAndPrintertPath), size=(60, 60))
        advanceSystSettingsImg = ctk.CTkImage(Image.open(advanceSystSettingsPath), size=(60, 60))
        WindowsFeaturesImg = ctk.CTkImage(Image.open(WindowsFeaturesPath), size=(60, 60))
        networkConnectionsImg = ctk.CTkImage(Image.open(networkConnectionsPath), size=(60, 60))
        MsconfigImg = ctk.CTkImage(Image.open(MsconfigPath), size=(60, 60))
        nextImg = ctk.CTkImage(Image.open(nextPath), size=(30, 30))
        proxyImg = ctk.CTkImage(Image.open(proxyPath), size=(60, 60))

        #Texts
        welcomeText = ctk.CTkLabel(self, text= "Bienvenido a\nCleanerGDC", font=('Poppins', 45, "bold"), bg_color=backgroundColor)
        usernameText = ctk.CTkLabel(self, text= fr"Usuario: {username}", font=('Poppins', 18), bg_color=backgroundColor)
        

        #buttons    
        tempFilesBtn = ctk.CTkButton(self, text = "Eliminar archivos\ntemporales", image=tempFilesImg, compound="top", bg_color=backgroundColor, fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=deleteTempFiles)
        fixInternetBtn = ctk.CTkButton(self, text = "Solucionar Internet",image=fixInternetImg, compound="top", bg_color=backgroundColor, fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=fixInternet)
        advanceSystSettingsBtn = ctk.CTkButton(self, text = " Configuración\nAvanzada del Sistema", bg_color=backgroundColor, image=advanceSystSettingsImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openAdvanceSystSettings)
        MsconfigBtn = ctk.CTkButton(self, text = "Configuración del\nSistema (Msconfig)", bg_color=backgroundColor, image=MsconfigImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openMsconfig)
        WindowsFeaturesBtn = ctk.CTkButton(self, text = "Características\nde Windows", bg_color=backgroundColor, image=WindowsFeaturesImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openWindowsFeatures)
        devicesAndPrinterBtn = ctk.CTkButton(self, text = "Dispositivos\ne impresoras", image=devicesAndPrinterImg, compound="top", bg_color=backgroundColor, fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=15, hover_color=hoverColor, font=myFont, command=openDevicesAndPrinter)
        networkConnectionslBtn = ctk.CTkButton(self, text = "Conexiones de red", bg_color=backgroundColor, image=networkConnectionsImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openNtworkConnections)
        proxyBtn = ctk.CTkButton(self, text = "Proxy", bg_color=backgroundColor, image=proxyImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openProxy)
        
        
        nextPageBtn = ctk.CTkButton(self, text="Siguiente", bg_color=backgroundColor, fg_color=blue, image=nextImg, compound="right", text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=self.nextPage)

        #create the grid
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        #place the widgets
        welcomeText.grid(row=0, column=1, sticky="nswe", columnspan=2)
        usernameText.grid(row=3, column=1, sticky="nswe", columnspan=2)
        

        tempFilesBtn.grid(row=1, column=0, padx=15, pady=15, sticky="nswe")
        fixInternetBtn.grid(row=1, column=1,  padx=15, pady=15, sticky="nswe")
        advanceSystSettingsBtn.grid(row=1, column=2, padx=15, pady=15, sticky="nswe")
        MsconfigBtn.grid(row=1, column=3, padx=15, pady=15, sticky="nswe")
        WindowsFeaturesBtn.grid(row=2, column=0, padx=15, pady=15, sticky="nswe")
        devicesAndPrinterBtn.grid(row=2, column=1, padx=15, pady=15, sticky="nswe")
        networkConnectionslBtn.grid(row=2, column=2, padx=15, pady=15, sticky="nswe")
        proxyBtn.grid(row=2, column=3, padx=15, pady=15, sticky="nswe")

        nextPageBtn.grid(row=3, column=3, padx=15, pady=15, ipady=15, sticky="e")

    def createWidgets2(self):
        backPath = resource_path("images/back.png")
        scannowPath = resource_path("images/scannow.png")
        repairFilesPath = resource_path("images/repairFiles.png")
        checkDiskPath = resource_path("images/checkDisk.png")
        diskDeFragmentation = resource_path("images/diskDeFragmentation.png")
        servicesMsc = resource_path("images/servicesMsc.png")
        windowsDefender = resource_path("images/windowsDefender.png")
        applications = resource_path("images/applications.png")

        ram_info = psutil.virtual_memory()

        blue = "#1366DE"
        hoverColor = "#1676fc"
        backgroundColor = "white"
        myFont = ctk.CTkFont(family="Poppins", size=14)

        background = ctk.CTkLabel(self, bg_color=backgroundColor, text="")
        background.place(relx=0, rely=0, relwidth=1, relheight=1)

        #Images
        backImg = ctk.CTkImage(Image.open(backPath), size=(30, 30))
        scannowImg = ctk.CTkImage(Image.open(scannowPath), size=(60, 60))
        repairFilesImg = ctk.CTkImage(Image.open(repairFilesPath), size=(60, 60))
        checkDiskImg = ctk.CTkImage(Image.open(checkDiskPath), size=(60, 60))
        diskDeFragmentationImg = ctk.CTkImage(Image.open(diskDeFragmentation), size=(60, 60))
        servicesMscImg = ctk.CTkImage(Image.open(servicesMsc), size=(60, 60))
        windowsDefenderImg = ctk.CTkImage(Image.open(windowsDefender), size=(60, 60))
        applicationsImg = ctk.CTkImage(Image.open(applications), size=(60, 60))

        #Text
        welcomeText = ctk.CTkLabel(self, text= "Bienvenido a\nCleanerGDC", font=('Poppins', 45, "bold"), bg_color=backgroundColor)
        ramText = ctk.CTkLabel(self, text= fr"Memoria (RAM): {ram_info.total / 1024 / 1024 / 1024:.2f} GB", font=('Poppins', 18), bg_color=backgroundColor)

        #buttons  
        scannowBtn = ctk.CTkButton(self, text = "Escanear archivos\ndañados (scannow)", bg_color=backgroundColor, image=scannowImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=scannow)
        dismBtn = ctk.CTkButton(self, text = "Reparar archivos\ndañados (DISMS)", bg_color=backgroundColor, image=repairFilesImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=dism)
        checkDiskBtn = ctk.CTkButton(self, text = "Escanear disco\nduro (chkdsk)", bg_color=backgroundColor, image=checkDiskImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=checkDisk)
        diskDeFragmentationBtn = ctk.CTkButton(self, text = "Desfragmentación\nde disco", bg_color=backgroundColor, image=diskDeFragmentationImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=diskdeFragmentation)
        servicesMscBtn = ctk.CTkButton(self, text = "Servicios de\nWindows", bg_color=backgroundColor, image=servicesMscImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=servicesMSC)
        windowsDefenderBtn = ctk.CTkButton(self, text = "Windows Defender", bg_color=backgroundColor, image=windowsDefenderImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openWindowsDefender)
        applicationsBtn = ctk.CTkButton(self, text = "Aplicaciones de\nSegundo Plano", bg_color=backgroundColor, image=applicationsImg, compound="top", fg_color=blue, text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=openBackgroundApps)
       
        
        backPageBtn = ctk.CTkButton(self, text="Atrás", bg_color=backgroundColor, fg_color=blue, image=backImg, compound="left", text_color=backgroundColor, border_color=blue, corner_radius=10, hover_color=hoverColor, font=myFont, command=self.backPage)  

        #create the grid
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        #place the widgets
        welcomeText.grid(row=0, column=1, sticky="nswe", columnspan=2)
        ramText.grid(row=3, column=1, sticky="nswe", columnspan=2)

        scannowBtn.grid(row=1, column=0, padx=15, pady=15, ipady=50, sticky="nswe")
        dismBtn.grid(row=1, column=1, padx=15, pady=15, ipady=50, sticky="nswe")
        checkDiskBtn.grid(row=1, column=2, padx=15, pady=15, ipady=50, sticky="nswe")
        diskDeFragmentationBtn.grid(row=1, column=3, padx=15, pady=15, ipady=50, sticky="nswe")
        servicesMscBtn.grid(row=2, column=0, padx=15, pady=15, ipady=50, sticky="nswe")
        windowsDefenderBtn.grid(row=2, column=1, padx=15, pady=15, ipady=50, sticky="nswe")
        applicationsBtn.grid(row=2, column=2, padx=15, pady=15, ipady=50, sticky="nswe")
        

        backPageBtn.grid(row=3, column=0, padx=15, pady=15, ipady=15, sticky="w")

if __name__ == "__main__":
    app = App()
    app.mainloop()   