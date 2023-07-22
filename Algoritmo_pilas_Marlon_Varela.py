import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def buscar(self, item):
        return item in self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def tamaño(self):
            return len(self.items)
    
    def vaciar(self):
        del self.items[:]

    def invertir(self):
        self.items = self.items[::-1]
    
    
class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de pilas")

        self.stack = Stack()

        self.label1 = tk.Label(root, text = "Ingrese elementos a la pila")
        self.label1.pack()

        self.entry1 = tk.Entry(root, width=30)
        self.entry1.pack(pady=10)

        self.boton_push = tk.Button(root, text="Push", command = self.añadir_elemento)
        self.boton_push.pack()

        self.label2 = tk.Label(root, text = "Buscar elementos en la pila:")
        self.label2.pack()

        self.entry2 = tk.Entry(root, width=30)
        self.entry2.pack(pady=10)

        self.boton_buscar = tk.Button(root, text = "Buscar", command = self.buscar_elemento)
        self.boton_buscar.pack()

        self.labelinv = tk.Label(root, text = " ")
        self.labelinv.pack()

        self.labelinv = tk.Label(root, text = " ")
        self.labelinv.pack()

        self.boton_pop = tk.Button(root, text="Pop", command = self.remover_elemento)
        self.boton_pop.pack()

        self.boton_top = tk.Button(root, text="Top", command = self.mostrar_top)
        self.boton_top.pack()

        self.boton_peek = tk.Button(root, text="Peek", command = self.mostrar_peek)
        self.boton_peek.pack()

        self.boton_size = tk.Button(root, text="Size", command = self.mostrar_tamaño)
        self.boton_size.pack()

        self.boton_clear = tk.Button(root, text="Clear", command = self.vaciar_pila)
        self.boton_clear.pack()

        self.boton_invertir = tk.Button(root, text="Invertir", command = self.invertir_pila)
        self.boton_invertir.pack()

        self.labelinv = tk.Label(root, text = " ")
        self.labelinv.pack()

        self.label_salida = tk.Label(root, text="")
        self.label_salida.pack(pady=10)

        self.label_salida2 = tk.Label(root, text="")
        self.label_salida2.pack(pady=10)

    def añadir_elemento(self):
        elemento = self.entry1.get()
        if elemento:
            self.stack.push(elemento)
            self.entry1.delete(0, tk.END)
            self.label_salida.config(text=f"Se agrego el elemento {elemento} a la pila.")
            
    def remover_elemento(self):
        elemento = self.stack.pop()
        if elemento is not None:
            self.label_salida.config(text=f"Se removió el elemento {elemento} de la pila.")
        else:
            self.label_salida.config(text="La pila está vacía.")

    def mostrar_top(self):
        top_elemento = self.stack.top()
        if top_elemento is not None:
            self.label_salida.config(text=f"El ultimo elemento de la pila es: {top_elemento}")
        else:
            self.label_salida.config(text="La pila está vacía.")
            
    def mostrar_peek(self):
        peek_elemento = self.stack.peek()
        if peek_elemento is not None:
            self.label_salida.config(text=f"El primer elemento de la pila es: {peek_elemento}")
        else:
            self.label_salida.config(text="La pila está vacía.")

    def mostrar_tamaño(self):
        stack_size = self.stack.tamaño()
        if stack_size:
            self.label_salida.config(text=f"El tamaño de la pila es de {stack_size} elementos")
        else:
            self.label_salida.config(text=f"La pila está vacía.")

    def vaciar_pila(self):
       self.stack.vaciar()
       self.label_salida.config(text=f"La pila fue vaciada con exito.")

    def invertir_pila(self):
        self.stack.invertir()
        self.label_salida.config(text=f"La pila fue invertida con exito.")

    def buscar_elemento(self):
        elemento = self.entry2.get()
        if self.stack.buscar(elemento):
            self.label_salida.config(text=f"El elemento {elemento} se encuentra en la pila.")
            self.entry2.delete(0, tk.END)
        else:
            self.label_salida.config(text=f"El elemento {elemento} no fue encontrado en la pila.")
            self.entry2.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Algoritmo de pilas")
    #root.geometry("400x700")
    stack_gui = StackGUI(root)
    root.mainloop()



