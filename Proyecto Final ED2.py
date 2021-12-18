#Proyecto Final Estructura de datos II
#Camila Nunez, 114118138
#Abel Calcagno, 8-952-333
import os
import random
class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

    def get_depth(self):
        """method of getting depth of BiTree"""
        if self.root is None:
            return 0
        else:
            node_queue = list()
            node_queue.append(self.root)
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)
                while q_len:
                    q_node = node_queue.pop(0)
                    q_len = q_len - 1
                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)
                depth = depth + 1
            return depth




tree = arbol()

while True:
    os.system("cls")
    print("Entradas Concierto")
    opc = input("\n1.-Ingresar persona  \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")
    personas= [64, 69, 149, 72, 100, 51, 111, 85, 54, 95, 128, 97, 22, 45, 20, 1, 30, 49, 8, 79, 17, 39, 35, 6, 68, 138, 109, 25, 91, 5, 145, 86, 126, 83, 89, 113, 90, 106, 108, 144, 15, 41, 65, 125, 99, 143, 117, 73, 93, 78, 103, 9, 131, 60, 129, 132, 104, 3, 107, 147, 112, 75, 141, 82, 67, 56, 110, 150, 19, 66, 74, 63, 70, 137, 27, 76, 14, 11, 10, 124, 101, 102, 52, 16, 96, 43, 80, 12, 135, 28, 136, 57, 120, 24, 115, 55, 18, 116, 123, 23, 148, 146, 81, 77, 87, 50, 13, 140, 133, 122, 119, 31, 4, 121, 29, 94, 44, 127, 48, 58, 61, 42, 21, 118, 62, 2, 92, 130, 134, 34, 36, 7, 84, 139, 98, 26, 37, 88, 33, 71, 38, 32, 40, 47, 46, 142, 114, 105, 53, 59]
    id = 0
    if opc == '1':
        r = random.randint(0, 149)
        nodo = personas.pop(r)

        if nodo == None:
            print("Capacidad maxima alcanzada")
        if tree.buscar(nodo, tree.root) == None:
            nodo = int(nodo)
            print("Ticket nuevo ingresado:", nodo)
            tree.root = tree.insert(tree.root, nodo)
            print("NIVEL: ", tree.get_depth() )
        else:
            print("\nTicket ya ingresado: ", tree.buscar(nodo, tree.root), " invalido...")
        nodo = 0

    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el Ticket a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nTicket no encontrado...")
            else:
                print("\nTicket encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()