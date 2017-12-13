from tkinter import *
import math

class grau2:
	def __init__(self, janela):
		self.janela= janela

		self.lbt=Label(janela, text="Instruções do software na opção 'Sobre'.")
		self.lbt.pack()
		
		self.lba=Label(janela, text="Valor de 'a': ")
		self.lba.pack()
		
		self.eda=Entry(janela)
		self.eda.focus()
		self.eda.pack()
		
		self.lbb=Label(janela, text="Valor de 'b': ")
		self.lbb.pack()
		
		self.edb=Entry(janela)
		self.edb.pack()
		
		self.lbc=Label(janela, text="Valor de 'c': ")
		self.lbc.pack()

		self.edc=Entry(janela)
		self.edc.pack()

		self.bt=Button(janela, width=8, text="Calcular", command=self.bt_click, bg="green")
		self.bt.pack(side=LEFT)

		self.btpassos=Button(janela, width=8, text="Passo a passo", command=self.bt_passo, bg="gray")
		self.btpassos.pack(side=LEFT)

		self.btpassos=Button(janela, width=8, text="Apagar/Reset", command=self.bt_clickdel, bg="gray")
		self.btpassos.pack(side=LEFT)

		self.btsobre=Button(janela, width=8, text="Sobre", command=self.bt_clicksobre, bg="gray")
		self.btsobre.pack(side=LEFT)
		
		self.bt2=Button(janela, width=8, text="SAIR", command=self.bt_clicksair,fg="black", bg="red")
		self.bt2.pack(side=LEFT)
	
	#def init_window(self):
	#	menu=Menu(self.janela)
	#	self.janela.config(menu=menu)
	#	file1=Menu(menu)
	#	file1.add_command(label="Sobre...", command=self.bt_clicksobre)
	#	menu.add_cascade(label="Ajuda", menu= file1)
	
	def bt_click(self):
		try:
			a=int(self.eda.get())
			b=int(self.edb.get())
			c=int(self.edc.get())
			delta=(b**2)-(4*a*c)
			if delta<0:
				self.lbt["text"]="A sua equação está no formato '(%dx²)+(%dx)+(%d)' e não possui raízes reais, porque o delta é < 0" %(a,b,c)
			else:
				x1= (-b+math.sqrt(delta))/(2*a)
				x2= (-b-math.sqrt(delta))/(2*a)
				if x1==x2:
					self.lbt["text"]= "A sua equação está no formato '(%dx)²+(%dx)+(%d)' e as raízes são: \n x1=x2= %f" %(a,b,c,x1)
				else:
					self.lbt["text"]="A sua equação está no formato '(%dx²)+(%dx)+(%d)' e as raízes são: \n x1= %f \n x2= %f "%(a,b,c,x1,x2)
		except:
			self.lbt["text"]= "Warning: ERR0R"

	def bt_clickdel(self):
		self.eda.delete(0, END)
		self.edb.delete(0, END)
		self.edc.delete(0, END)
		self.lbt["text"]="Instruções do software na opção 'Sobre'."		
		self.eda.focus()
	def bt_passo(self):
		try:
			a=int(self.eda.get())
			b=int(self.edb.get())
			c=int(self.edc.get())
			delta=(b**2)-(4*a*c)
			x1= (-b+math.sqrt(delta))/(2*a)
			x2= (-b-math.sqrt(delta))/(2*a)
			self.lbt["text"]="1º - Calculamos o DELTA através dos coeficientes a=%d,b=%d e c=%d.\n Delta= %d²-4*%d*%d= %d\n2º - Aṕos calular o delta, calculamos os valores de x1 e x2.\nx1=(-(%d)+√%d)/(2*%d)= %f\nx2=(-(%d)-√%d)/(2*%d)= %f" %(a, b, c, b, a, c, delta, b, delta, a, x1, b, delta, a, x2)
				
		except:	
			try:
				a=int(self.eda.get())
				b=int(self.edb.get())
				c=int(self.edc.get())
				delta=(b**2)-(4*a*c)		
				if delta<0:
					self.lbt["text"]="Warning: ERR0R\n A equação %dx²+(%dx)+(%d) não possui raízes reais."%(a, b, c)
			except:
				self.lbt["text"]= "Warning: ERR0R"
				
				
	def bt_clicksobre(self):
		self.lbt["text"]="1º - Os coeficientes a,b e c devem ser inteiros;\n2º - A equação deve estar no formato ax²+bx+c=0; \n3º - Software desenvolvido por: MarceloRocha®."
	def bt_clicksair(self):
		self.janela.destroy()	



root=Tk()
grau2(root)
root.title("Calculadora equações 2º grau")
root.mainloop()
