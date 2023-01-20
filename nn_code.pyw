from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#--------------------------------------------------------------------------------------------------------------------------------------

Root=Tk()

#----------------------------------------------------------------------------------------------------------------------------------------

Language=""
Lang_Variable=1

Current_Page_Variable=1

Page_Title=""
Page_Content=""

Current_Font_Type="Bookman Old Style"
Font_Type_Variable=1

New_Data_Variable=0

#----------------------------------------------------------------------------------------------------------------------------------------

def Download_Current_Language():

	global Language
	global Lang_Variable

	try: # In case of user has deleted the language file , this function will make a new file like it. 

		Conexion=sqlite3.connect("config")

		Cursor=Conexion.cursor()

		Cursor.execute("CREATE TABLE CURRENT_LANGUAGE(LANG VARCHAR(2))")

		Cursor.execute("INSERT INTO CURRENT_LANGUAGE VALUES('EN')")

		Conexion.commit()

		Conexion.close()

		del Conexion

		del Cursor

		Language="EN"

	except: # In case that the file already exist, this function will get the previous language selected by the user.

		Conexion=sqlite3.connect("config")

		Cursor=Conexion.cursor()

		Cursor.execute("SELECT LANG FROM CURRENT_LANGUAGE")

		Lista=Cursor.fetchall()

		if Lista[0]==('EN',):

			Language="EN"
			Lang_Variable=1

		elif Lista[0]==('ES',):

			Language="ES"
			Lang_Variable=2

		Conexion.close()

		del Conexion

		del Cursor

		del Lista

#----------------------------------------------------------------------------------------------------------------------------------------

Download_Current_Language()

#----------------------------------------------------------------------------------------------------------------------------------------

def Create_Notebook_Memory():

	global New_Data_Variable
	global Current_Font_Type
	global Font_Type_Variable

	try:

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Cursor.execute("CREATE TABLE DATA(PAGE_NUMBER INTEGER NOT NULL PRIMARY KEY , PAGE_TITLE TEXT NOT NULL , PAGE_CONTENT TEXT NOT NULL)")

		Connection.commit()

		Connection.close()

		del Connection
		del Cursor

		New_Data_Variable=1

	except:

		New_Data_Variable=0

#----------------------------------------------------------------------------------------------------------------------------------------

Create_Notebook_Memory()

#--------------------------------------------------------------------------------------------------------------------------------------

def Create_Config_Settings():

	global Current_Font_Type
	global Font_Type_Variable

	try:

		Connection=sqlite3.connect("config")
		Cursor=Connection.cursor()

		Cursor.execute("CREATE TABLE USER_FONT_TYPE(FONT TEXT NOT NULL)")

		Cursor.execute("INSERT INTO USER_FONT_TYPE VALUES('Bookman Old Style')")

		Connection.commit()

		Connection.close()

		del Connection
		del Cursor

	except:

		Connection=sqlite3.connect("config")
		Cursor=Connection.cursor()

		Cursor.execute("SELECT * FROM USER_FONT_TYPE")

		Downloaded_Data=Cursor.fetchall()

		print(Downloaded_Data)

		if Downloaded_Data[0]==('Bookman Old Style',):

			Current_Font_Type="Bookman Old Style"
			Font_Type_Variable=1

		elif Downloaded_Data[0]==('Arial',):

			Current_Font_Type="Arial"
			Font_Type_Variable=2

		elif Downloaded_Data[0]==('Times New Roman',):

			Current_Font_Type="Times New Roman"
			Font_Type_Variable=3

		elif Downloaded_Data[0]==('Georgia',):

			Current_Font_Type="Georgia"
			Font_Type_Variable=4

		elif Downloaded_Data[0]==('Broadway',):

			Current_Font_Type="Broadway"
			Font_Type_Variable=5

		elif Downloaded_Data[0]==('Berlin Sans FB',):

			Current_Font_Type="Berlin Sans FB"
			Font_Type_Variable=6

		elif Downloaded_Data[0]==('Bodoni MT',):

			Current_Font_Type="Bodoni MT"
			Font_Type_Variable=7

#--------------------------------------------------------------------------------------------------------------------------------------

Create_Config_Settings()

#--------------------------------------------------------------------------------------------------------------------------------------

class VNB():

	def __init__(self,Root):

		global Language
		global Current_Font_Type

		self.Main_Window=Root
		self.Main_Window.config(bg="#320000",bd=10,relief="raised",cursor="cross")
		self.Main_Window.title("Noble Notes")
		self.Main_Window.iconbitmap("img/icon.ico")
		self.Main_Window.resizable(0,0)

		self.Title_Label=Label(self.Main_Window,bg="#820F0F",fg="white",font=(Current_Font_Type,14,"bold"),bd=5,relief="ridge",text="Title")
		self.Title_Label.grid(row=0,column=0,padx=5,pady=5,sticky=W + E)

		self.Title_Variable=StringVar()

		self.Current_Page_StringVar=StringVar()

		self.Search_Page_IMG=PhotoImage(file="img/search_page.png")

		self.Title_Entry=Entry(self.Main_Window,textvariable=self.Title_Variable,justify="center",bg="#580000",fg="white",font=(Current_Font_Type,14,"bold italic"),bd=5,relief="ridge")
		self.Title_Entry.grid(row=0,column=1,columnspan=4,padx=5,pady=5,sticky=W + E)

		self.Save_Info=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Save",command=self.Save_Info)
		self.Save_Info.grid(row=1,column=0,padx=5,pady=5,sticky=W + E)

		self.Update_Info=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Update",command=self.Update_Info)
		self.Update_Info.grid(row=2,column=0,padx=5,pady=5,sticky=W + E)

		self.Delete_Info=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Delete",command=self.Delete_Info)
		self.Delete_Info.grid(row=3,column=0,padx=5,pady=5,sticky=W + E)

		self.Clean_Info=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Clean",command=self.Clean_Fields)
		self.Clean_Info.grid(row=4,column=0,padx=5,pady=5,sticky=W + E)

		self.Config_Program=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Config",command=self.Config_Program)
		self.Config_Program.grid(row=5,column=0,padx=5,pady=5,sticky=W + E)

		self.Exit_Program=Button(self.Main_Window,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Exit",command=self.Close_Window)
		self.Exit_Program.grid(row=6,column=0,padx=5,pady=5,sticky=W + E)

		self.Log_Button=Button(self.Main_Window,width=3,command=self.Log_Info,bg="#820F0F",fg="white",font=(Current_Font_Type,14,"bold"),bd=4,relief="raised",text="©")
		self.Log_Button.grid(row=7,column=0,padx=5,pady=5)

		self.Info_Screen=Text(self.Main_Window,bg="#580000",fg="white",font=(Current_Font_Type,15),bd=7,relief="ridge",width=50,height=16)
		self.Info_Screen.grid(row=1,rowspan=6,column=1,columnspan=4,sticky=W+E)

		self.Info_Screen_Scrollbar=Scrollbar(self.Main_Window,command=self.Info_Screen.yview)
		self.Info_Screen_Scrollbar.grid(row=1,column=5,rowspan=6,sticky="nsew",padx=5)

		self.Info_Screen.config(yscrollcommand=self.Info_Screen_Scrollbar.set)

		self.Back_Page_Button=Button(self.Main_Window,command=self.Back_Page,width=4,bg="#662828",fg="white",font=(Current_Font_Type,16,"bold"),bd=4,relief="raised",text="⇦")
		self.Back_Page_Button.grid(row=7,column=1,padx=5,pady=5)

		self.Page_Number_Entry=Entry(self.Main_Window,justify="center",textvariable=self.Current_Page_StringVar,bg="#8F3B3B",fg="white",font=(Current_Font_Type,14,"bold"),bd=5,relief="ridge")
		self.Page_Number_Entry.grid(row=7,column=2,padx=5,pady=5)

		self.Find_Page_Button=Button(self.Main_Window,command=self.Find_Page,bg="#3D0000",fg="white",font=(Current_Font_Type,18,"bold"),bd=4,relief="raised",image=self.Search_Page_IMG)
		self.Find_Page_Button.grid(row=7,column=3,padx=5,pady=5)

		self.Next_Page_Button=Button(self.Main_Window,command=self.Next_Page,width=4,bg="#662828",fg="white",font=(Current_Font_Type,16,"bold"),bd=4,relief="raised",text="⇨")
		self.Next_Page_Button.grid(row=7,column=4,padx=5,pady=5)

		self.Main_Window.protocol("WM_DELETE_WINDOW",self.Close_Window)

		if Language=="EN":

			self.Save_Info.config(text="Save")
			self.Update_Info.config(text="Update")
			self.Delete_Info.config(text="Delete")
			self.Clean_Info.config(text="Clean")
			self.Config_Program.config(text="Settings")
			self.Exit_Program.config(text="Exit")
			self.Title_Label.config(text="Title")

		elif Language=="ES":

			self.Save_Info.config(text="Guardar")
			self.Update_Info.config(text="Actualizar")
			self.Delete_Info.config(text="Borrar")
			self.Clean_Info.config(text="Limpiar")
			self.Config_Program.config(text="Ajustes")
			self.Exit_Program.config(text="Salir")
			self.Title_Label.config(text="Título")

	def Start(self):

		global Page_Title
		global Page_Content
		global Current_Page_Variable
		global New_Data_Variable
		global Lang_Variable

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)

		Cursor.execute(Sentence)

		Downloaded_Data=Cursor.fetchall()

		for i in Downloaded_Data:

			Page_Title=i[1]
			Page_Content=i[2]

			break

		if New_Data_Variable==1:

			if Lang_Variable==1:

				self.Info_Screen.delete(1.0,END)

				self.Title_Variable.set("Noble Notes - How to Use")

				self.Info_Screen.insert(INSERT,"""-Developer's Note: This message will be only showed the first time this app is opened.
\n-(1)-'Save' to create a memory space that will keep the page's data.
\n-(2)-'Update' to update saved data on the current page's memory space. If you want to update the page's info', before you must make the memory space, in other words, push on 'save' button.
\n-(3)-'Delete' to delete the current page's memory space.
\n-(4)-'Clean' to just erase all words that are on both fields of writting. This don't make changes on the determinate memory space.""")

				self.Current_Page_StringVar.set(Current_Page_Variable)

			elif Lang_Variable==2:

				self.Info_Screen.delete(1.0,END)

				self.Title_Variable.set("Noble Notes - Instrucciones de Uso")

				self.Info_Screen.insert(INSERT,"""-Nota del Desarrollador: Este mensaje solo se mostrará la primera vez que la aplicación sea ejecutada.
\n-(1)-'Guardar' para crear un espacio en memoria que guardará la información de la página actual.
\n-(2)-'Actualizar' para actualizar la información almacenada en el espacio en memoria de la página en cuestión. De querer actualizar la información de una página, primero debes crear el espacio en memoria , o en otras palabras,darle a 'guardar'.
\n-(3)-'Borrar' para eliminar el espacio en memoria creado para almacenar la información de la página en cuestión.
\n-(4)-'Limpiar' para borrar la información encima de ambos campos de escritura. Esto no sobreescribe la información del espacio en memoria.""")

				self.Current_Page_StringVar.set(Current_Page_Variable)

		elif New_Data_Variable==0:

			self.Title_Variable.set(Page_Title)
			self.Info_Screen.insert(INSERT,Page_Content)
			self.Current_Page_StringVar.set(Current_Page_Variable)

			Page_Title=""
			Page_Content=""

		self.Main_Window.mainloop()

	def Save_Info(self):

		global Current_Page_Variable
		global Lang_Variable

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Current_Page_Title=self.Title_Variable.get()
		Current_Page_Content=self.Info_Screen.get(1.0,END)

		if Current_Page_Title=="" or Current_Page_Content=="":

			if Lang_Variable==1:

				messagebox.showwarning("Noble Notes","You must at least set a title to save an entry.")

			elif Lang_Variable==2:
			
				messagebox.showwarning("Noble Notes","Debes al menos colocar un título para guardar una entrada.")
		else:

			try:

				Data_List=[Current_Page_Variable,Current_Page_Title,Current_Page_Content]

				Cursor.execute("INSERT INTO DATA VALUES(?,?,?)",Data_List)

				Connection.commit()

				Connection.close()

				del Connection
				del Cursor
				del Data_List

				if Lang_Variable==1:

					messagebox.showinfo("Noble Notes","Your notes has been saved.")

				elif Lang_Variable==2:
						
					messagebox.showinfo("Noble Notes","Se han guardado tus notas.")

			except:

				if Lang_Variable==1:

					messagebox.showwarning("Noble Notes","This entry already exist.")

				elif Lang_Variable==2:
						
					messagebox.showwarning("Noble Notes","Esta entrada ya existe.")

	def Update_Info(self):

		global Current_Page_Variable
		global Lang_Variable

		value=""

		Current_Page_Title=self.Title_Variable.get()
		Current_Page_Content=self.Info_Screen.get(1.0,END)

		if Current_Page_Title=="" or Current_Page_Content=="":

			if Lang_Variable==1:

					messagebox.showwarning("Noble Notes","You must at least set a title to update an entry.")

			elif Lang_Variable==2:
			
					messagebox.showwarning("Noble Notes","Debes al menos colocar un título para actualizar una entrada.")
		else:

			Connection=sqlite3.connect("data")
			Cursor=Connection.cursor()

			Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)

			Cursor.execute(Sentence)

			Downloaded_Data=Cursor.fetchall()

			if len(Downloaded_Data)==0:

				if Lang_Variable==1:

					messagebox.showerror("Noble Notes","You can't update an entry that don't exist.")

				elif Lang_Variable==2:
							
					messagebox.showerror("Noble Notes","No puedes actualizar una entrada que no existe.")

			else:

				if Lang_Variable==1:

					value=messagebox.askquestion("Noble Notes","Are you sure about update this entry's content?")

				elif Lang_Variable==2:
								
					value=messagebox.askquestion("Noble Notes","¿Estás seguro de actualizar el contenido de esta entrada?")

				if value=="yes":

					Connection=sqlite3.connect("data")
					Cursor=Connection.cursor()

					Current_Page_Title=self.Title_Variable.get()
					Current_Page_Content=self.Info_Screen.get(1.0,END)

					Data_List=[Current_Page_Title,Current_Page_Content,Current_Page_Variable]

					Cursor.execute("UPDATE DATA SET PAGE_TITLE=?,PAGE_CONTENT=? WHERE PAGE_NUMBER=?",Data_List)

					Connection.commit()

					Connection.close()

					del Connection
					del Cursor
					del Data_List

					if Lang_Variable==1:

						messagebox.showinfo("Noble Notes","Your notes has been updated.")

					elif Lang_Variable==2:
									
						messagebox.showinfo("Noble Notes","Notas actualizadas.")
				else:

					pass

	def Delete_Info(self):

		global Current_Page_Variable
		global Lang_Variable

		Data_List=[]

		Current_Page_Title=self.Title_Variable.get()
		Current_Page_Content=self.Info_Screen.get(1.0,END)

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)

		Cursor.execute(Sentence)

		Data_List=Cursor.fetchall()

		Connection.close()

		del Connection
		del Cursor

		if Data_List==[]:

			if Lang_Variable==1:

				messagebox.showwarning("Noble Notes","This entry is empty.")

			elif Lang_Variable==2:
									
				messagebox.showwarning("Noble Notes","Esta entrada está vacía.")

		elif len(Data_List)>0:

			if Lang_Variable==1:

				value=messagebox.askquestion("Noble Notes","Are you sure about delete this entry?")

			elif Lang_Variable==2:
								
				value=messagebox.askquestion("Noble Notes","¿Estás seguro de que deseas borrar esta entrada?")

			if value=="yes":

				Connection=sqlite3.connect("data")
				Cursor=Connection.cursor()

				Sentence="DELETE FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)
		
				Cursor.execute(Sentence)

				Connection.commit()

				Connection.close()

				del Connection
				del Cursor
				del Data_List

				if Lang_Variable==1:

					self.Title_Variable.set("")
					self.Info_Screen.delete(1.0,END)

					messagebox.showinfo("Noble Notes","This page's info' has been deleted.")

				elif Lang_Variable==2:

					self.Title_Variable.set("")
					self.Info_Screen.delete(1.0,END)	

					messagebox.showinfo("Noble Notes","Se ha borrado la información de esta página.")

			else:

				pass

	def Clean_Fields(self):

		self.Info_Screen.delete(1.0,END)
		self.Title_Variable.set("")

	def Config_Program(self):

		self.Main_Window.destroy()

		del self.Main_Window

		Open_Settings_Window()

	def Log_Info(self):

		global Lang_Variable

		if Lang_Variable==1:

			messagebox.showinfo("Noble Notes","-Version 1.1\n\n-Developer: Jesús E. Velásquez")

		elif Lang_Variable==2:
							
			messagebox.showinfo("Noble Notes","-Versión 1.1\n\n-Desarrollador: Jesús E. Velásquez")

	def Next_Page(self):

		global Current_Page_Variable

		Current_Page_Variable+=1

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)

		Cursor.execute(Sentence)

		Downloaded_Data=Cursor.fetchall()

		Page_Title=[]
		Page_Content=[]

		for i in Downloaded_Data:

			Page_Title=i[1]
			Page_Content=i[2]

			break

		self.Title_Variable.set(Page_Title)
		self.Info_Screen.delete(1.0,END)
		self.Info_Screen.insert(INSERT,Page_Content)

		self.Current_Page_StringVar.set(str(Current_Page_Variable))

	def Find_Page(self):

		global Current_Page_Variable
		global Lang_Variable

		Connection=sqlite3.connect("data")
		Cursor=Connection.cursor()

		Searching_Page=self.Current_Page_StringVar.get().strip()

		try:

			Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+Searching_Page

			Cursor.execute(Sentence)

			Downloaded_Data=Cursor.fetchall()

			Page_Title=[]
			Page_Content=[]

			for i in Downloaded_Data:

				Page_Title=i[1]
				Page_Content=i[2]

				break

			if int(Searching_Page)<=0:

				if Lang_Variable==1:

					self.Current_Page_StringVar.set(Current_Page_Variable)

					messagebox.showerror("Searching Error #2","Invalid searching method.")

				elif Lang_Variable==2:

					self.Current_Page_StringVar.set(Current_Page_Variable)
					
					messagebox.showerror("Error de Búsqueda #2","Método de búsqueda inválido.")
			else:

				if Page_Title==[] and Page_Content==[]:

					self.Title_Variable.set("")
					self.Info_Screen.delete(1.0,END)
					self.Info_Screen.insert(INSERT,"")

					if Lang_Variable==1:

						messagebox.showwarning("Noble Notes","This page is empty.")

						Current_Page_Variable=int(Searching_Page)

						self.Current_Page_StringVar.set(Current_Page_Variable)

					elif Lang_Variable==2:

						messagebox.showwarning("Noble Notes","Esta página está vacía.")

						Current_Page_Variable=int(Searching_Page)

						self.Current_Page_StringVar.set(Current_Page_Variable)

				else:

					self.Title_Variable.set(Page_Title)
					self.Info_Screen.delete(1.0,END)
					self.Info_Screen.insert(INSERT,Page_Content)

					Current_Page_Variable=int(Searching_Page)

					self.Current_Page_StringVar.set(Current_Page_Variable)
		except:

			if Lang_Variable==1:

				self.Current_Page_StringVar.set(Current_Page_Variable)

				messagebox.showerror("Searching Error #1","Invalid searching method.")

			elif Lang_Variable==2:

				self.Current_Page_StringVar.set(Current_Page_Variable)

				messagebox.showerror("Error de Búsqueda #1","Método de búsqueda inválido.")



	def Back_Page(self):

		global Current_Page_Variable

		if Current_Page_Variable==1:

			pass

		else:

			Current_Page_Variable-=1

			Connection=sqlite3.connect("data")
			Cursor=Connection.cursor()

			Sentence="SELECT * FROM DATA WHERE PAGE_NUMBER="+str(Current_Page_Variable)

			Cursor.execute(Sentence)

			Downloaded_Data=Cursor.fetchall()

			Page_Title=[]
			Page_Content=[]

			for i in Downloaded_Data:

				Page_Title=i[1]
				Page_Content=i[2]

				break

			if Page_Title==[] and Page_Content==[]:

				global Lang_Variable

				self.Title_Variable.set("")
				self.Info_Screen.delete(1.0,END)
				self.Info_Screen.insert(INSERT,"")

			else:

				self.Title_Variable.set(Page_Title)
				self.Info_Screen.delete(1.0,END)
				self.Info_Screen.insert(INSERT,Page_Content)

			self.Current_Page_StringVar.set(str(Current_Page_Variable))

	def Close_Window(self):

		global Lang_Variable

		value=""

		if Lang_Variable==1:

			value=messagebox.askquestion("Exit","Are you sure about close program?")

		elif Lang_Variable==2:

			value=messagebox.askquestion("Salir","¿Estás seguro de que deseas cerrar el programa?")

		if value=="yes":

			self.Main_Window.destroy()

		else:

			pass

#--------------------------------------------------------------------------------------------------------------------------------------

class Configuration():

	def __init__(self,Root):

		global Language
		global Current_Font_Type
		global Font_Type_Variable

		self.Config_Win=Root
		self.Config_Win.config(bg="#320000",bd=10,relief="raised",cursor="cross")
		self.Config_Win.title("Noble Notes - Settings")
		self.Config_Win.iconbitmap("img/icon.ico")
		self.Config_Win.resizable(0,0)

		self.Language_Label=Label(self.Config_Win,text="Language",bg="#820F0F",fg="white",font=(Current_Font_Type,12,"bold"),bd=5,relief="raised")
		self.Language_Label.grid(row=0,column=0,padx=10,pady=10,sticky=W + E)

		self.Font_Type_Label=Label(self.Config_Win,text="Font Type",bg="#820F0F",fg="white",font=(Current_Font_Type,12,"bold"),bd=5,relief="raised")
		self.Font_Type_Label.grid(row=0,column=1,padx=10,pady=10,sticky=W + E)

		self.Language_StringVar=StringVar()
		self.Font_Type_StringVar=StringVar()

		self.Languages_Box=ttk.Combobox(self.Config_Win,textvariable=self.Language_StringVar,justify="center")
		self.Font_Type_Box=ttk.Combobox(self.Config_Win,textvariable=self.Font_Type_StringVar,justify="center")

		self.Save_Changes_Button=Button(self.Config_Win,bg="#4F0000",fg="white",font=(Current_Font_Type,13,"bold"),bd=4,relief="raised",text="Save Changes",command=self.Save_Changes)
		self.Save_Changes_Button.grid(row=2,column=0,padx=5,pady=5,columnspan=2)

		self.Config_Win.protocol("WM_DELETE_WINDOW",self.Close_Window)
		
		if Language=="ES":

			self.Language_Label.config(text="Idioma")
			self.Font_Type_Label.config(text="Tipo de Fuente")
			self.Config_Win.title("Noble Notes - Ajustes")

			self.Languages_Box["values"]=("Español","Inglés")
			self.Languages_Box.grid(row=1,column=0,padx=10,pady=10)

			self.Languages_Box.current(0)

			self.Font_Type_Box["values"]=("Bookman Old Style",
										"Arial",
										"Times New Roman",
										"Georgia",
										"Broadway",
										"Berlin Sans FB",
										"Bodoni MT")

			self.Font_Type_Box.grid(row=1,column=1,padx=10,pady=10)

			if Font_Type_Variable==1:

				self.Font_Type_Box.current(0)

			elif Font_Type_Variable==2:

				self.Font_Type_Box.current(1)

			elif Font_Type_Variable==3:

				self.Font_Type_Box.current(2)

			elif Font_Type_Variable==4:

				self.Font_Type_Box.current(3)

			elif Font_Type_Variable==5:

				self.Font_Type_Box.current(4)

			elif Font_Type_Variable==6:

				self.Font_Type_Box.current(5)

			elif Font_Type_Variable==7:

				self.Font_Type_Box.current(6)

			self.Save_Changes_Button.config(text="Guardar Cambios")

		elif Language=="EN":

			self.Language_Label.config(text="Language")
			self.Font_Type_Label.config(text="Font Type")
			self.Config_Win.title("Noble Notes - Settings")

			self.Languages_Box["values"]=("Spanish","English")
			self.Languages_Box.grid(row=1,column=0,padx=10,pady=10)

			self.Languages_Box.current(1)

			self.Font_Type_Box["values"]=("Bookman Old Style",
										"Arial",
										"Times New Roman",
										"Georgia",
										"Broadway",
										"Berlin Sans FB",
										"Bodoni MT")

			self.Font_Type_Box.grid(row=1,column=1,padx=10,pady=10)

			if Font_Type_Variable==1:

				self.Font_Type_Box.current(0)

			elif Font_Type_Variable==2:

				self.Font_Type_Box.current(1)

			elif Font_Type_Variable==3:

				self.Font_Type_Box.current(2)

			elif Font_Type_Variable==4:

				self.Font_Type_Box.current(3)

			elif Font_Type_Variable==5:

				self.Font_Type_Box.current(4)

			elif Font_Type_Variable==6:

				self.Font_Type_Box.current(5)

			elif Font_Type_Variable==7:

				self.Font_Type_Box.current(6)

			self.Save_Changes_Button.config(text="Save Changes")

	def Start(self):

		self.Config_Win.mainloop()

	def Save_Changes(self):

		global Language
		global Lang_Variable
		global Current_Font_Type
		global Font_Type_Variable

		Selected_Language=self.Language_StringVar.get()

		Selected_Font_Type=self.Font_Type_StringVar.get()

		if Selected_Language=="Spanish" or Selected_Language=="Español":

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Cursor.execute("UPDATE CURRENT_LANGUAGE SET LANG='ES'")

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

			Language="ES"
			Lang_Variable=2

		elif Selected_Language=="English" or Selected_Language=="Inglés":

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Cursor.execute("UPDATE CURRENT_LANGUAGE SET LANG='EN'")

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

			Language="EN"
			Lang_Variable=1

		if Selected_Font_Type=="Bookman Old Style":

			Font_Type_Variable=1
			Current_Font_Type="Bookman Old Style"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Arial":

			Font_Type_Variable=2
			Current_Font_Type="Arial"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)
			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Times New Roman":

			Font_Type_Variable=3
			Current_Font_Type="Times New Roman"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Georgia":

			Font_Type_Variable=4
			Current_Font_Type="Georgia"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Broadway":

			Font_Type_Variable=5
			Current_Font_Type="Broadway"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Berlin Sans FB":

			Font_Type_Variable=6
			Current_Font_Type="Berlin Sans FB"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		elif Selected_Font_Type=="Bodoni MT":

			Font_Type_Variable=7
			Current_Font_Type="Bodoni MT"

			Connection=sqlite3.connect("config")
			Cursor=Connection.cursor()

			Sentence="UPDATE USER_FONT_TYPE SET FONT='"+Current_Font_Type+"'"

			Cursor.execute(Sentence)

			Connection.commit()

			Connection.close()

			del Connection
			del Cursor

		self.Config_Win.destroy()

		del self.Config_Win

		Open_Main_Window()

	def Close_Window(self):

		self.Config_Win.destroy()

		del self.Config_Win

		Open_Main_Window()

#----------------------------------------------------------------------------------------------------------------------------------------

Virtual_Notebook=VNB(Root)

#----------------------------------------------------------------------------------------------------------------------------------------

def Open_Settings_Window():

	try:

		global Virtual_Notebook
		global Root

		del Virtual_Notebook
		del Root

		Root=Tk()

		Lang_Window=Configuration(Root)
		Lang_Window.Start()

	except:

		Root=Tk()

		Lang_Window=Configuration(Root)
		Lang_Window.Start()

def Open_Main_Window():

	Root=Tk()

	Virtual_Notebook=VNB(Root)
	Virtual_Notebook.Start()

#----------------------------------------------------------------------------------------------------------------------------------------

Virtual_Notebook.Start()

