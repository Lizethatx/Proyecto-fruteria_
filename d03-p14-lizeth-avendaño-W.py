#practica 14
#avendaño garcia lizeth           d03 
#amezcua garcia juan angel david  d03
#horario: L,MI 17:00 - 19:00
#lemus plascencia ivan fernando   d01
#venegas lozano celina            d01
#horario: M,J 19:00 - 21:00

from colorama import Cursor,Fore,Back,init,Style; #Llama a colorama
import time
from os import system #Importa os para poder limpiar pantalla y pausar el programa
import os; #Llamo funciones del sistema operativo para poder borrar pantalla
import msvcrt; #Llama funcion para poder leer lo que se presiona en el teclado
from msvcrt import getch; #Este recurso funciona en python y lee la pulsacion de tecla

def ventana(): #Esta funcion sirve para dibujar la ventana mediante ciclos for
    largo=65; yFija=2
    ancho=20; xFija=30
    for i in range(largo):  #Se dibujan las lineas horizontales
        print(Cursor.POS(xFija+i,yFija)+Back.RED+"°");
        print(Cursor.POS(xFija+i,yFija+1+ancho)+Back.RED+"°");
        if(i>1 and i<(largo-3)):
            print(Cursor.POS(xFija+i,yFija+1)+Back.LIGHTYELLOW_EX+" ");
            print(Cursor.POS(xFija+i+1,yFija+ancho)+Back.LIGHTYELLOW_EX+" ");
    for i in range(ancho+1):  #Se dibujan las lineas verticales
        print(Cursor.POS(xFija,yFija+i)+Back.RED+"°");
        print(Cursor.POS(xFija+1,yFija+i)+Back.RED+"°");
        print(Cursor.POS(xFija+largo-2,yFija+i)+Back.RED+"°");
        print(Cursor.POS(xFija+largo-1,yFija+i)+Back.RED+"°");
        if i<ancho and i>0:
            print(Cursor.POS(xFija+2,yFija+i+1)+Back.LIGHTYELLOW_EX+" ");
            print(Cursor.POS(xFija+largo-3,yFija+i)+Back.LIGHTYELLOW_EX+" ");

   
def menu(posicion):#Esta funcion es para crear el menu principal
    yFija=2;
    xFija=30;
    opciones=["[1]Altas","[2]Bajas","[3]Ventas","[4]Salir"]
    posicion=0;
    while True:
            print(Cursor.POS(5,27)+Style.BRIGHT+Fore.BLUE+"practica 14"); #Dibuja la formacion de los estudiantes cuando aparece el menu
            print(Cursor.POS(26,27)+Fore.RED+"avendaño garcia lizeth          |d03|");
            print(Cursor.POS(26,28)+Fore.RED+"amezcua garcia juan angel david |d03|");
            print(Cursor.POS(26,29)+Fore.BLUE+"Horario: L,MI 17:00 - 19:00");
            print(Cursor.POS(68,27)+Fore.RED+"lemus plascencia ivan fernando |d01|");
            print(Cursor.POS(68,28)+Fore.RED+"venegas lozano celina          |d01|");
            print(Cursor.POS(68,29)+Fore.BLUE+"Horario: M,J 19:00 - 21:00");

            print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+leerLineaEspecifica(3)); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+27,i+yFija+7)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+27,i+yFija+7)+Fore.BLACK+Back.WHITE+opciones[posicion]+"  <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                if posicion==0:
                    menuAltasBajas("Menu Altas");
                elif posicion==1:
                    menuAltasBajas("Menu Bajas");   
                elif posicion==2:
                    menuVenta();
                elif posicion==3:
                    vSalir();
                    break;
                system("cls");
                ventana();      
            elif tecla=="1":
                menuAltasBajas("Menu Altas");
                system("cls");
                ventana();
            elif tecla=="2":
                menuAltasBajas("Menu Bajas");
                system("cls");
                ventana();
            elif tecla=="3":
                menuVenta();
                system("cls");
                ventana();
            elif tecla == "4":
                vSalir();
                break;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;
                
def menuAltasBajas(titulo):#Esta funcion es un menu para altas o bajas segun sea el caso
    yFija=2;
    xFija=30;
    opciones=["[1]Fruteria","[2]Producto","[3]Empleado","[4]Salir"]
    posicion=0;
    system("cls");
    ventana();
    while True:
            print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+titulo); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                if posicion==0: # Cuando se realiza una baja o alta de FRUTERIA aqui se manda a llamar a su respectiva funcion
                    if titulo=="Menu Altas":
                        menuAltaFruteria();
                    else:
                        menuBajaFruteria();
                elif posicion==1:# Cuando se realiza una baja o alta de Producto aqui se manda a llamar a su respectiva funcion
                    if titulo=="Menu Altas":
                        menuAltaProducto(); 
                    else:
                        menuBajaProducto();
                elif posicion==2:#Cuando se realiza una baja o alta de EMPLEADOcto aqui se manda a llamar a su respectiva funcion
                    if titulo=="Menu Altas":
                        menuAltaEmpleado();
                    else:
                        menuBajaEmpleado();
                elif posicion==3:
                    break;
                system("cls");
                ventana();
            elif tecla=="1":
                if titulo=="Menu Altas":
                    menuAltaFruteria();
                else:
                    menuBajaFruteria();
                system("cls");
                ventana();
            elif tecla=="2":
                if titulo=="Menu Altas":
                    menuAltaProducto(); 
                else:
                    menuBajaProducto();
                system("cls");
                ventana();
            elif tecla=="3":
                if titulo=="Menu Altas":
                    menuAltaEmpleado();
                else:
                    menuBajaEmpleado();
                system("cls");
                ventana();
            elif tecla == "4":
                break;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;

def menuAltaFruteria():#Esta funcion permite dar de alta los datos de la fruteria
    yFija=2;
    xFija=30;
    opciones=["[1]Modificar nombre ","[2]Modificar Telefono","[3]Modificar Correo","[4]Salir"]
    posicion=0;
    system("cls");
    ventana();
    while True:
            print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Alta datos Fruteria"); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                system("cls");
                ventana();
                if posicion==0:
                    nombre=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el nombre de la fruteria: "); 
                    escribirEnLineaEspecifica(3,nombre);
                    break;
                elif posicion==1:
                    while True:
                        telefono=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el telefono de la fruteria: ");
                        if es_int(telefono)==True:
                            break;
                        print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero ");
                        time.sleep(3);
                        print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                         ");
                        print(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
                    escribirEnLineaEspecifica(4,telefono);
                    break;
                elif posicion==2:
                    correo=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el correo de la fruteria: "); 
                    escribirEnLineaEspecifica(5,correo);
                    break;
                elif posicion==3:
                    break;
                system("cls");
                ventana();  
            elif tecla=="1":
                system("cls");
                ventana();
                nombre=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el nombre de la fruteria: "); 
                escribirEnLineaEspecifica(3,nombre);
                break;
            elif tecla=="2":
                system("cls");
                ventana();
                while True:
                    telefono=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el telefono de la fruteria: ");
                    if es_int(telefono)==True:
                        break;
                    print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero ");
                    time.sleep(3);
                    print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                         ");
                    print(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
                escribirEnLineaEspecifica(4,telefono);
                break; 
            elif tecla=="3":
                system("cls");
                ventana();
                correo=input(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingrese el correo de la fruteria: "); 
                escribirEnLineaEspecifica(5,correo);
                break;
            elif tecla == "4":
                break;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;

def menuBajaFruteria():#Esta funcion permite dar de baja los datos de la fruteria
    yFija=2;
    xFija=30;
    opciones=["[1]Dar de baja nombre ","[2]Dar de baja Telefono","[3]Dar de baja Correo","[4]Salir"]
    posicion=0;
    system("cls");
    ventana();
    while True:
            print(Cursor.POS(xFija+20,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Baja datos Fruteria"); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                if posicion==0:
                    escribirEnLineaEspecifica(3,"          ");
                    break;
                elif posicion==1:
                    escribirEnLineaEspecifica(4,"          ");
                    break;  
                elif posicion==2:
                    escribirEnLineaEspecifica(5,"          ");
                    break;
                elif posicion==3:
                    break;
                system("cls");
                ventana();
            elif tecla=="1":
                escribirEnLineaEspecifica(3,"         ");
                break;
            elif tecla=="2":
                escribirEnLineaEspecifica(4,"         ");
                break;
            elif tecla=="3":
                escribirEnLineaEspecifica(5,"         ");
                break;
            elif tecla == "4":
                break;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;
                    
def menuAltaProducto():#Esta funcion permite dar de alta un producto
    yFija=2;
    xFija=30;
    opciones=["[1]Ingresar datos ","[2]Cancelar"]
    posicion=0;
    system("cls");
    ventana();
    while True:
            print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Alta Producto"); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                if posicion==0:
                    auxMenuAltaProducto();
                elif posicion==1:
                    break;
                system("cls");
                ventana();      
            elif tecla=="1":
                auxMenuAltaProducto();
                system("cls");
                ventana();
            elif tecla=="2":
                break;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;
    
def auxMenuAltaProducto():#Funcion auxiliar para menuAltaProducto
    yFija=2;
    xFija=30;
    system("cls");
    ventana();
    print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Alta datos Producto");
    while True:
        nombre=input(Cursor.POS(xFija+5,yFija+6)+Fore.WHITE+Back.BLACK+"Ingrese el nombre de la fruta: ");
        aux=nombre.replace(" ","");
        if aux.isalpha()==True:
            break;
        print(Cursor.POS(xFija+5,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa unicamente letras");
        time.sleep(3);
        print(Cursor.POS(xFija+5,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                              ");
        print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
    nombre=nombre.upper();
    while True:
        piezas=input(Cursor.POS(xFija+5,yFija+8)+Fore.WHITE+Back.BLACK+"Ingrese las piezas de la fruta: ");
        if es_int(piezas)==True:
            break;
        print(Cursor.POS(xFija+5,yFija+9)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero entero");
        time.sleep(3);
        print(Cursor.POS(xFija+5,yFija+9)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                         ");
        print(Cursor.POS(xFija+5,yFija+8)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");

    while True:
        precio=input(Cursor.POS(xFija+5,yFija+10)+Fore.WHITE+Back.BLACK+"Ingrese el costo de la pieza: ");
        if es_float(precio)==True:
            break;
        print(Cursor.POS(xFija+5,yFija+11)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero");
        time.sleep(3);
        print(Cursor.POS(xFija+5,yFija+11)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                     ");
        print(Cursor.POS(xFija+5,yFija+10)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
    
    if buscarLinea(nombre)!="NO ENCONTRADO":
        indice=buscarLinea(nombre);
        escribirEnLineaEspecifica(indice+1,str(precio))
        actualizarFruta(leerLineaEspecifica(indice+3),"SUMA",piezas);
        contador=leerLineaEspecifica(indice+3);
        piezas=leerLineaEspecifica(indice+2);
    else:
        archivo = open("d03-p14-lizeth-avendaño-W.txt", mode='a', encoding='utf-8');
        archivo.write(nombre+"\n");
        archivo.write(precio+"\n");
        archivo.write(piezas+"\n");
        idenAux=leerLineaEspecifica(2);
        escribirEnLineaEspecifica(2,str(int(idenAux)+1));
        contador=leerLineaEspecifica(2);
        contador=contador[0:len(contador)-1];
        archivo.write(contador+"-P\n");
    system("cls")
    ventana();
    print(Cursor.POS(xFija+25,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Producto Guardado");
    print(Cursor.POS(xFija+5,yFija+5)+Fore.WHITE+Back.BLACK+"Nombre : "+nombre);
    print(Cursor.POS(xFija+5,yFija+6)+Fore.WHITE+Back.BLACK+"Precio : "+precio);
    print(Cursor.POS(xFija+5,yFija+7)+Fore.WHITE+Back.BLACK+"Piezas : "+piezas);
    print(Cursor.POS(xFija+5,yFija+8)+Fore.WHITE+Back.BLACK+"ID : "+contador+"-P");
    time.sleep(3);
    
def menuBajaProducto():
    
    yFija=2;
    xFija=30;
    print(Cursor.POS(xFija+20,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Baja Producto"); 
    opcion =verificarDecision("   Baja Producto"," ID de producto");
    system("cls");
    ventana();
    print(Cursor.POS(xFija+20,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Baja Producto"); 
    if opcion==True:
        identi=input(Cursor.POS(xFija+12,yFija+4)+Fore.WHITE+Back.BLACK+"Ingrese el ID del producto: ");
        encontrado=buscarLinea(identi);
        
        if encontrado=="NO ENCONTRADO":
            print(Cursor.POS(xFija+14,yFija+6)+Fore.WHITE+Back.BLACK+"El ID que ingresaste no existe vericalo ");
            print(Cursor.POS(xFija+14,yFija+7)+Fore.WHITE+Back.BLACK+"      y vuelve a intentarlo ");
            time.sleep(3);
        else:
            if identi.find("-P")==-1:
                print(Cursor.POS(xFija+14,yFija+6)+Fore.WHITE+Back.BLACK+"El ID que ingresaste no existe vericalo ");
                print(Cursor.POS(xFija+14,yFija+7)+Fore.WHITE+Back.BLACK+"      y vuelve a intentarlo ");
                time.sleep(3);
                return;
            escribirEnLineaEspecifica(encontrado,"       ");
            escribirEnLineaEspecifica(encontrado-1,"       ");
            escribirEnLineaEspecifica(encontrado-2,"       ");
            escribirEnLineaEspecifica(encontrado-3,"       ");
            print(Cursor.POS(xFija+18,yFija+5)+Fore.WHITE+Back.BLACK+"Producto ELIMINADO ");
            time.sleep(3);
                
def menuAltaEmpleado():
    yFija=2;
    xFija=30;
    print(Cursor.POS(xFija+24,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Alta Empleado"); 
    if(verificarDecision("     Alta "," Datos de empleado")==True):
        system("cls")
        ventana();
        print(Cursor.POS(xFija+24,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Alta Empleado"); 
        while True:
            nombre=input(Cursor.POS(xFija+5,+yFija+6)+Fore.WHITE+Back.BLACK+"Ingrese nombre: ");
            aux=nombre.replace(" ","");
            if aux.isalpha()==True:
                break;
            print(Cursor.POS(xFija+5,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa unicamente letras");
            time.sleep(3);
            print(Cursor.POS(xFija+5,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                              ");
            print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
        nombre=nombre.upper();
        while True:
            salario=input(Cursor.POS(xFija+5,+yFija+8)+Fore.WHITE+Back.BLACK+"Ingrese salario: ");
            if es_float(salario)==True:
                break;
            print(Cursor.POS(xFija+5,yFija+9)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero");
            time.sleep(3);
            print(Cursor.POS(xFija+5,yFija+9)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                     ");
            print(Cursor.POS(xFija+5,yFija+8)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
        
        xx = open("d03-p14-lizeth-avendaño-W.txt", mode='r+', encoding='utf-8');
        idString=xx.readline();
        identificador=int(idString[0:len(idString)-1])+1;
        escribirEnLineaEspecifica(1,str(identificador));
        xx.write(nombre+"\n");
        xx.write(salario+"\n");
        xx.write(str(identificador)+"-E"+"\n");
        xx.close();
        print(Cursor.POS(xFija+24,+yFija+10)+Fore.WHITE+Back.MAGENTA+"REGISTRO EXITOSO");
        print(Cursor.POS(xFija+23,+yFija+12)+Fore.LIGHTYELLOW_EX+Back.BLUE+"Nombre: "+nombre);
        print(Cursor.POS(xFija+27,+yFija+13)+Fore.LIGHTYELLOW_EX+Back.BLUE+"ID: "+str(identificador)+"-E");
        print(Cursor.POS(xFija+25,+yFija+14)+Fore.LIGHTYELLOW_EX+Back.BLUE+"Salario :"+salario);
        time.sleep(4);

def menuBajaEmpleado():
    largo=60;
    yFija=2;
    ancho=20;
    xFija=30;
    print(Cursor.POS(xFija+23,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Baja Empleado"); 
    opcion =verificarDecision("   Baja empleado"," ID de empleado: ");
    system("cls");
    ventana();
    print(Cursor.POS(xFija+23,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Baja Empleado"); 
    if opcion==True:
        identificador=input(Cursor.POS(xFija+12,yFija+5)+Fore.WHITE+Back.BLACK+"Ingrese el ID del empleado: ");
        encontrado=buscarLinea(identificador);
        if encontrado=="NO ENCONTRADO":
            print(Cursor.POS(xFija+14,yFija+7)+Fore.WHITE+Back.BLACK+"El ID que ingresaste no existe vericalo ");
            print(Cursor.POS(xFija+14,yFija+8)+Fore.WHITE+Back.BLACK+"      y vuelve a intentarlo ");
            time.sleep(3);
        else:
            if identificador.find("-E")==-1:
                print(Cursor.POS(xFija+14,yFija+7)+Fore.WHITE+Back.BLACK+"El ID que ingresaste no existe vericalo ");
                print(Cursor.POS(xFija+14,yFija+8)+Fore.WHITE+Back.BLACK+"      y vuelve a intentarlo ");
                time.sleep(3);
                return;
            escribirEnLineaEspecifica(encontrado,"       ");
            escribirEnLineaEspecifica(encontrado-1,"       ");
            escribirEnLineaEspecifica(encontrado-2,"       ");
            print(Cursor.POS(xFija+16,yFija+6)+Fore.WHITE+Back.BLACK+"Empleado ELIMINADO ");
            time.sleep(2);          

def menuVenta():
    yFija=2;
    xFija=30;
    opcion=0;
    system("cls");
    ventana();
    print(Cursor.POS(xFija+28,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Ventas"); 
    precios=[];
    productos=[];
    
    contenido = open("d03-p14-lizeth-avendaño-W.txt").read().split("\n");

    while True:
        idEmpleado=str(input(Cursor.POS(xFija+5,yFija+5)+Fore.WHITE+Back.BLACK+"Ingrese el ID del empleado: "));
        if idEmpleado.find("-E")!=-1:
            break;
        
        print(Cursor.POS(xFija+14,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"No es ID de empleado");
        time.sleep(3);
        print(Cursor.POS(xFija+5,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                              ");
        print(Cursor.POS(xFija+5,yFija+5)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
    encontrado=buscarLinea(idEmpleado);
    if encontrado=="NO ENCONTRADO" or idEmpleado=="":
            print(Cursor.POS(xFija+14,yFija+7)+Fore.WHITE+Back.BLACK+"No existe ese empleado verifica");
            print(Cursor.POS(xFija+14,yFija+8)+Fore.WHITE+Back.BLACK+"    y vuelve a intentarlo ");
            time.sleep(3);
    else:
        while opcion!=1:
            system("cls");
            ventana();
            print(Cursor.POS(xFija+28,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"Ventas");
            
            while True:
                idProducto=input(Cursor.POS(xFija+4,yFija+6)+Fore.WHITE+Back.BLACK+"Ingrese el ID del producto: ");
                if idProducto.find("-P")!=-1:
                    break;
                print(Cursor.POS(xFija+4,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"No es ID de producto");
                time.sleep(3);
                print(Cursor.POS(xFija+4,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                              ");
                print(Cursor.POS(xFija+4,yFija+6)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
            if buscarLinea(idProducto)!="NO ENCONTRADO":
                indice=buscarLinea(idProducto);
                cantidad=int(contenido[int(indice)-2]);
                if int(contenido[int(indice)-2])<=0:
                    print(Cursor.POS(xFija+4,yFija+7)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"No hay mas piezas disponibles");
                    time.sleep(3);
                else:
                    contenido.pop(int(indice)-2)
                    contenido.insert(indice-2,str(cantidad-1));
                    #contenido = open("d03-p14-lizeth-avendaño-W.txt").read().split("\n")
                    productos.append(leerLineaEspecifica(int(indice)));
                    precios.append(leerLineaEspecifica(int(indice)-2));
            else:
                print(Cursor.POS(xFija+8,yFija+8)+Fore.WHITE+Back.BLACK+"No existe ese producto verifica ");
                print(Cursor.POS(xFija+8,yFija+9)+Fore.WHITE+Back.BLACK+"    y vuelve a intentarlo ");
                time.sleep(3);
            system("cls");
            ventana();
            opciones=["[1]Continuar Vendiendo","[2]Cobrar","[3]Salir"]
            posicion=0;
			
            while True:
                print(Cursor.POS(xFija+30,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"VENTAS"); 
                for i in range (len(opciones)):
                    if i!=posicion:
                        print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                    elif i==posicion:
                        print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
                tecla=pedir_tecla();
                if tecla=="enter":
                    if posicion==0:
                        break;
                    elif posicion==1:
                        if len(productos)==0 and len(precios)==0:
                            system("cls");
                            ventana();
                            print(Cursor.POS(xFija+10,yFija+5)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+"No hay productos en el carrito de compras");
                            time.sleep(3);
                            opcion=1;
                        else:
                            ticket(productos,precios,idEmpleado);
                            opcion=1;
                        break;  
                    elif posicion==2:
                        opcion=1;
                        break;
                                
                elif tecla=="1":
                    break;
                elif tecla=="2":
                    ticket(productos,precios,idEmpleado);
                    opcion=1;
                    break;  
                elif tecla=="3":
                    opcion=1;
                    break;
                elif tecla=="up":
                    posicion-=1;
                elif tecla=="down":
                    posicion+=1;
                if posicion<0:
                    posicion=len(opciones)-1;
                elif posicion>len(opciones)-1:
                    posicion=0;
     
def ticket(productos,precios,identificador):
    yFija=2;
    xFija=30;
    system("cls");
    ventana();
    print(Cursor.POS(xFija+23,yFija+2)+Fore.WHITE+Back.BLACK+leerLineaEspecifica(3));
    print(Cursor.POS(xFija+25,yFija+3)+Fore.WHITE+Back.BLACK+leerLineaEspecifica(4));
    print(Cursor.POS(xFija+22,yFija+4)+Fore.WHITE+Back.BLACK+leerLineaEspecifica(5));
    indice=buscarLinea(identificador);
    print(Cursor.POS(xFija+15,yFija+6)+Fore.WHITE+Back.BLACK+"Empleado: "+leerLineaEspecifica(indice-2).replace("\n","")+" ID: "+leerLineaEspecifica(indice).replace("\n",""));
    print(Cursor.POS(xFija+17,yFija+8)+Fore.WHITE+Back.BLACK+"PRODUCTOS ","  ID  ","  PRECIO");
    total=0;
    f=8;
    for x in productos:
        f+=1;
        indice=int(buscarLinea(x[0:len(x)-1]))
        print(Cursor.POS(xFija+17,yFija+f)+Fore.WHITE+Back.BLACK+leerLineaEspecifica(indice-3).replace("\n",""))
        print(Cursor.POS(xFija+29,yFija+f)+Fore.WHITE+Back.BLACK+leerLineaEspecifica(indice).replace("\n",""))
        print(Cursor.POS(xFija+33,yFija+f)+Fore.WHITE+Back.BLACK+"    $"+leerLineaEspecifica(indice-2).replace("\n",""));
    for y in precios:
        total=total+float(y);
    print(Cursor.POS(xFija+28,yFija+f+2)+Fore.WHITE+Back.BLACK+"TOTAL:   $"+str(total));
    for x in productos:
        actualizarFruta(x,"resta",0);
    while True:
        pago=input(Cursor.POS(xFija+18,yFija+f+3)+Fore.WHITE+Back.BLACK+"Cantidad recibida: $");
        if es_float(pago)==True:
            break;
        print(Cursor.POS(xFija+5,yFija+f+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero");
        time.sleep(3);
        print(Cursor.POS(xFija+5,yFija+f+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                     ");
        print(Cursor.POS(xFija+5,yFija+f+3)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
    pago=float(pago);
    while True:
        if pago<total:
            print(Cursor.POS(xFija+6,yFija+f+4)+Fore.WHITE+Back.BLACK+"El monto ingresado es menor intentelo de nuevo");
            time.sleep(2);
            print(Cursor.POS(xFija+4,yFija+f+4)+Fore.WHITE+Back.BLACK+"                                                ");
            print(Cursor.POS(xFija+6,yFija+f+3)+Fore.WHITE+Back.BLACK+"                                             ");
            while True:
                pago=input(Cursor.POS(xFija+18,yFija+f+3)+Fore.WHITE+Back.BLACK+"Cantidad recibida: ");
                if es_float(pago)==True:
                    break;
                print(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"Ingresa un numero");
                time.sleep(3);
                print(Cursor.POS(xFija+5,yFija+4)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                             ");
                print(Cursor.POS(xFija+5,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.BLACK+"                                                  ");
            pago=float(pago);       
        else:
            print(Cursor.POS(xFija+6,yFija+f+5)+Fore.WHITE+Back.BLACK+"                                                 ")
            print(Cursor.POS(xFija+18,yFija+f+5)+Fore.WHITE+Back.BLACK+"Cambio a devolver: $"+str(pago-total));
            break;
    time.sleep(2);
    print(Cursor.POS(xFija+18,yFija+f+8)+Fore.YELLOW+Back.BLACK+"Presione ESC para salir");
    while True:
            tecla=pedir_tecla();
            if tecla=="esc":
                break;
    system("cls");
    
def leerLineaEspecifica(posicion):
    archivo = open("d03-p14-lizeth-avendaño-W.txt", mode='r+', encoding='utf-8');
    linea="";
    for i in range(0,posicion):
        linea=archivo.readline();
    archivo.close();
    return linea;

def actualizarFruta(identificador,tipo,nuevasPiezas):
    indice=buscarLinea(identificador.replace("\n",""));
    idenAux=leerLineaEspecifica(int(indice)-1);

    if(tipo=="SUMA"):
        pie=int(idenAux.replace("\n",""))+int(nuevasPiezas);
    else:
        pie=int(idenAux)-1;
    escribirEnLineaEspecifica(indice-1,str(pie));
            
def vSalir(): #Despliega la venta de finalizar
    yFija=2;
    xFija=30;
    system("cls");
    ventana();
    print(Cursor.POS(xFija+22,yFija+6)+Fore.WHITE+Back.MAGENTA+"FINALIZANDO PROGRAMA");
    time.sleep(3);
    system("cls");
    
def escribirEnLineaEspecifica(posicion,cadena):#Esta funcion sirve para escribir en una linea especifica mediante la posicion
    contenido = open("d03-p14-lizeth-avendaño-W.txt").read().split("\n")
    contenido.pop(posicion-1)
    contenido.insert(posicion-1,cadena)
    f = open("d03-p14-lizeth-avendaño-W.txt", "r+")
    f.writelines("\n".join(contenido))
    f.close

def es_float(variable):
    try:
        float(variable)
        return True
    except:
        return False

def es_int(variable):
    try:
        int(variable)
        return True
    except :
        return False
                
def buscarLinea(Buscada): #Esta funcion no facilita buscar una palabra en el txt y regresa el numero de linea o NO ENCONTRADO
    archivo = open("d03-p14-lizeth-avendaño-W.txt", mode='r+', encoding='utf-8');
    i=0;
    while True:
        linea=archivo.readline()
        if not linea:
            break;
        i+=1;
        if linea==Buscada+"\n":
            archivo.close();
            return i;
    archivo.close();
    return "NO ENCONTRADO";

def verificarDecision(opcion,cadena):#Este menu sirve para confimar la decision tomada por el usuario
    yFija=2;
    xFija=30;
    opciones=["[1]Ingresar "+cadena,"[2]Cancelar"]
    posicion=0;
    system("cls");
    ventana();
    while True:
            print(Cursor.POS(xFija+26,yFija+3)+Style.BRIGHT+Fore.WHITE+Back.MAGENTA+opcion[3:len(opcion)]); 
            for i in range (len(opciones)):
                if i!=posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.WHITE+Back.BLACK+opciones[i]+"         ");
                elif i==posicion:
                    print(Cursor.POS(xFija+5,i+yFija+6)+Fore.BLACK+Back.WHITE+opciones[posicion]+"   <<");
            tecla=pedir_tecla();
            if tecla=="enter":
                if posicion==0:
                    return True;    
                elif posicion==1:
                    return False;
            elif tecla=="1":
                return True;
            elif tecla=="2":
                return False;
            elif tecla=="up":
                posicion-=1;
            elif tecla=="down":
                posicion+=1;
            if posicion<0:
                posicion=len(opciones)-1;
            elif posicion>len(opciones)-1:
                posicion=0;

def pedir_tecla(): #Esta funcion sirve para detectar la tecla presionada por el usuario
        key=getch();
        k=str(ord(key))
        if k=="72":
            return "up";
        elif k=="80":
            return "down";
        elif k=="27":
            return "esc";
        elif k=="13":
            return "enter";
        elif k=="49":
            return "1";
        elif k=="50":
            return "2";
        elif k=="51":
            return "3";
        elif k=="52":
            return "4";

def iniciar():
    init(autoreset=True); #Se inicia el colorama, que se autoresetee para evitar basura en la consola
    ventana();#Se dibuja el marco de el menu
    menu(0);#Se dibujan los opciones
iniciar();

