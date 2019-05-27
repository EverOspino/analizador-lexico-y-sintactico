
import wx
from nuevo_lexer import tokens
import nuevo_parser

val = 'hola mundo'

class Aplicacion(wx.Frame):
	def __init__(self,parent,title,size):
		wx.Frame.__init__(self, parent=parent, title=title, size=size)
		self.panel = wx.Panel(self, wx.ID_ANY)
		self.Center(True)
		self.Show()

	def crear_boton(self,imagen,tamanio,px,py,funcion):
		bmp = wx.Bitmap(imagen, wx.BITMAP_TYPE_ANY)
		button = wx.BitmapButton(self, id=-1, bitmap=bmp,size=(tamanio,tamanio))
		button.Bind(wx.EVT_BUTTON,funcion)
		button.SetPosition((px,py))
		return button

	def objetos(self):
		self.texto = wx.TextCtrl(self,-1,style=wx.TE_MULTILINE,pos=(60,0),size=(820,510))
		font1 = self.texto.GetFont()
		font1.SetPointSize(15)
		self.texto.SetFont(font1)

		self.boton1 = self.crear_boton('imagenes/buscar.png',50,5,20,self.buscar_archivo)
		self.boton2 = self.crear_boton('imagenes/guardar.png',50,5,100,self.guardar_archivo)
		self.boton3 = self.crear_boton('imagenes/correr.png',50,5,180,self.correr)


	def buscar_archivo(self,event):
		# Create open file dialog
		openFileDialog = wx.FileDialog(self, "Open", "", "", 
		      "ALV files (*.alv)|*.alv", 
		       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

		openFileDialog.ShowModal()
		#print(openFileDialog.GetPath())
		openFileDialog.Destroy()
		self.texto.LoadFile(openFileDialog.GetPath())


	def guardar_archivo(self,event):

		fdlg = wx.FileDialog(self, "Input setting file path", "", "", "ALV files(*.alv)|*.*", wx.FD_SAVE)
		if fdlg.ShowModal() == wx.ID_OK:
			i = fdlg.GetFilterIndex()
			if i == 0:
				try:
				    f = open(fdlg.GetPath(), "w")
				    f.write(self.texto.GetValue())
				    for i in self.itemDataMap.keys():
				        entry = self.itemDataMap[i]
				        f.write('%s,%s,%s,%s\n' % (entry[1], entry[2], entry[4].smsc, entry[3]))
				    f.close()
				except:
				    pass
		fdlg.Destroy()

        
	def correr(self,event):
		if self.texto.GetValue() != None:
			nuevo_parser.ejecutar_parser(self.texto.GetValue())
			
		

if __name__ == '__main__':
	app = wx.App()
	frame = Aplicacion(None, u"prueba", (900,550))
	frame.objetos()
	app.MainLoop()


