import numpy as vt
import math

print("BIENVENIDO AL PROGRAMA DE ALGEBRA LINEAL")
print ("Por favor, ingresar su nombre de usuario :")
nombre=input()
print("\n") 
print("Hola", nombre,"BIENVENIDO AL PROGRAMA DE ALGEBRA LINEAL, ¿Qué deseas hacer?" )
print("\n")  
def menu():
    print (
       "-------- MENU DE OPERACIONES -------" "\n"
       "1.-Suma de vectores" "\n"
        "2.-Resta de vectores" "\n"
        "3.-Norma o modulo" "\n"
        "4.-Ángulo" "\n"
        "5.- consultar ejercicios aplicados" "\n"
          "\n"
        "0-.SALIR DEL PROGRAMA PRINCIPAL")
Archivo =open("Proyecto.txt","w")
Archivo.write(nombre)  
while True:
      menu()
      op= input("Ingrese una opción :")
      if op=="1":
         print ("-------- MENU DE OPERACIONES -------" "\n"
         "1.-Suma de vectores R2" "\n"
         "2.-Suma de vectores R3" "\n"
         "\n"    
         "0.- SALIR DEL SUBMENÚ")
         
         ops= input("Ingrese una opción a realizar")
         if ops=="1":
            a=int(input("Digite el primer valor del vector en R2 :"))
            b=int(input("Digite el segundo valor del vector en R2 :"))
            vt1=vt.array((a,b))
            print("\n")
            print("--AHORA, PROCEDA A INGRESAR LOS VALORES DEL SEGUNO VECTOR EN R2--""\n")
            c=int(input("Digite el primer valor del segundo vector en R2 :"))
            d=int(input("Digite el segundo valor del segundo vector en R2 :"))
            vt2=vt.array((c,d))
            suma=(vt1+vt2)
            print("\n")
            print("El resultado de la suma de los vectores"+str(vt1)+" y "+str(vt2)+" es :"+str(suma))
        
         elif ops=="2":
              a2=int(input("Digite el primer valor del vector  en R3 :"))
              b2=int(input("Digite el segundo valor del vector en R3 :"))
              c2=int(input("Digite el tercer valor del vector en R3 :"))
              vt1a=vt.array((a2,b2,c2))
              print("\n")
              print("--AHORA, PROCEDA A INGRESAR LOS VALORES DEL SEGUNO VECTOR EN R3--""\n")
              d2=int(input("Digite el primer valor del segundo vector en R3 :"))
              e2=int(input("Digite el segundo valor del segundo vector en R3 :"))
              f2=int(input("Digite el segundo valor del segundo vector en R3 :"))
              vt2a=vt.array((d2,e2,f2))
              sumaa=(vt1a+vt2a)
              print("\n")
              print("El resultado de la suma de los vectores"+str(vt1a)+" y "+str(vt2a)+" es :"+str(sumaa))
         elif ops==0:
              print(menu)
          
        
      elif op=="2":
           print ("-------- MENU DE OPERACIONES -------" "\n"
           "1.-Resta de vectores R2" "\n"
           "2.-Resta de vectores R3" "\n"
           "\n"    
           "0.- SALIR DEL SUBMENÚ")
           opr= input("Ingrese una opción a realizar ")
           if opr=="1":
              a=int(input("Digite el primer valor del vector en R2 :"))
              b=int(input("Digite el segundo valor del vector en R2 :"))
              vt1=vt.array((a,b))  
              print("\n")
              print("--AHORA, PROCEDA A INGRESAR LOS VALORES DEL SEGUNO VECTOR EN R2--""\n")
              c=int(input("Digite el primer valor del segundo vector en R2 :"))
              d=int(input("Digite el segundo valor del segundo vector en R2 :"))
              vt2=vt.array((c,d))
              resta=(vt1-vt2)
              print("\n")
              print("El resultado de la resta de los vectores"+str(vt1)+" y "+str(vt2)+" es :"+str(resta))
           elif opr=="2":
                a2=int(input("Digite el primer valor del vector  en R3 :"))
                b2=int(input("Digite el segundo valor del vector en R3 :"))
                c2=int(input("Digite el tercer valor del vector en R3 :"))
                vt1a=vt.array((a2,b2,c2))
                print("\n")
                print("--AHORA, PROCEDA A INGRESAR LOS VALORES DEL SEGUNO VECTOR EN R3--""\n")
                d2=int(input("Digite el primer valor del segundo vector en R3 :"))
                e2=int(input("Digite el segundo valor del segundo vector en R3 :"))
                f2=int(input("Digite el segundo valor del segundo vector en R3 :"))
                vt2a=vt.array((d2,e2,f2))
                restaa=(vt1a-vt2a)
                print("\n")
                print("El resultado de la resta de los vectores"+str(vt1a)+" y "+str(vt2a)+" es :"+str(restaa))
           elif ops==0:
                print(menu)
                
      elif op=="3":
           print("\n")
           print("-------- MENU DE OPERACIONES -------" "\n"
           "1.-Magnitud de un vector en R2" "\n"
           "2.-Magnitu de un vector en R3" "\n"
           "\n"    
           "0.- SALIR DEL SUBMENÚ")
           opm= input("Digite una opción a realizar :")
           if opm=="1":
              a=int(input("Digite el primer valor del vector en R2 :"))
              b=int(input("Digite el segundo valor del vector en R2 :"))
              vt1=vt.array((a,b))
              norma=(vt.linalg.norm(vt1))
              print("\n")
              print("La Magnitud del vector "+str(vt1)+" es :"+str(norma))
           elif opm=="2":
                a=int(input("Digite el primer valor del vector en R3 :"))
                b=int(input("Digite el segundo valor del vector en R3 :"))
                c=int(input("Digite el tercer valor del vector en R3 :"))
                vt1=vt.array((a,b,c))
                normaa=(vt.linalg.norm(vt1))
                print("\n")
                print("La Magnitud del vector "+str(vt1)+" es :"+str(normaa))
           elif ops==0:
                print(menu)
             
       
      elif op=="4": 
           print("-------- MENU DE OPERACIONES -------" "\n"
           "1.-Ángulo de un vector en R2" "\n"
           "2.-Ángulo de un vector en R3" "\n"
           "\n"    
           "0.- SALIR DEL SUBMENÚ")
           opa= input("Digite una opción a realizar :")
           if opa=="1":
            a=int(input("Digite el primer valor del vector en R2 :"))
            b=int(input("Digite el segundo valor del vector en R2 :"))
            vt1=vt.array((a,b))
            norma=(vt.linalg.norm(vt1))
            tang=math.tan(norma)
            print("El angulo de"+str(vt1)+"es:"+str(tang))
           elif opa=="2":
            a=int(input("Digite el primer valor del vector en R3 :"))
            b=int(input("Digite el segundo valor del vector en R3 :"))
            c=int(input("Digite el tercer valor del vector en R3 :"))
            vt1=vt.array((a,b,c))
            norma=(vt.linalg.norm(vt1))
            tanga=math.tan(norma)
            print("El angulo de"+str(vt1)+"es:"+str(tanga))
          
           elif ops==0:
                print(menu)
             
      
           
      elif op=="5":
          print("-------- MENU DE RESULTADO -------" "\n"
           "1.-Resultado de suma en R2" "\n"
           "2.-Resultado de suma en r3" "\n"
           "3.-Resultado de resta en r2" "\n" 
           "4.-Resultado de resta en r3" "\n"
           "5.-Resultado de magnitud r2" "\n"
           "6.-Resultado de magnitud r3" "\n"
           "7-.Resulatado de angulo r2" "\n"
           "8-.Resultado de angulo r3" "\n"
           "\n"    
           "0.- SALIR DEL MENÚ")
          r= input("Digite una opción a realizar :")
          if r=="1":
             print(Archivo.writer('suma=% s'%suma))
             Archivo.close() 
          elif r=="2":
             print(Archivo.writer('sumaa=% s'%sumaa))
             Archivo.close()  
          elif r=="3":
             print(Archivo.writer('resta=% s'%resta))
             Archivo.close()   
          elif r=="4":
             print(Archivo.writer('restaa=% s'%restaa))
             Archivo.close()     
          elif r=="5":
            print(Archivo.writer('norma=% s'%norma))
            Archivo.close()     
          elif r=="6":
            print(Archivo.writer('normaa=% s'%normaa))
            Archivo.close()        
          elif r=="7":
            print(Archivo.writer('tang=% s'%tang))
            Archivo.close()      
          elif r=="8":
            print(Archivo.writer('tanga=% s'%tanga))
            Archivo.close()  
          elif ops==0:
                print(menu)           
                print(ops)
      elif op=="0":
         x=input("¿Desea salir del programa? SI/NO") 
         if x=="si":
           break
      else:
         print(menu)
                
                
                
                
                
                
                