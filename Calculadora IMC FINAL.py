#Valores que mostramos en pantalla
# Definimos las variables que vamos a usar


Nombre = input('Ingrese su nombre: ')
Genero = input ('Ingrese su genero (H/M): ')
edad = int (input ('Ingrese su edad: '))
peso = float (input ('Ingrese su peso en kg: '))
altura = int (input ('Ingrese su altura en centimetros: ')) /100


#Calculamos el IMC; usando round para redondear el resultado a un decimal
# La formula es peso en kg dividido por altura en metros al cuadrado

imc = round (peso / (altura * altura),1)

# Determinamos  la categoría del IMC
# Usamos una variable para almacenar la categoría del IMC


#usamos bucles if y elif para determinar la categoria del IMC

if imc < 18.5:
    categoria_imc = "Bajo peso"
    print(f"{Nombre} el IMC es {imc}, se clasifica como bajo peso")
elif imc >= 18.5 and imc < 24.9:
    categoria_imc = "Peso normal"
    print(f"{Nombre} el IMC es {imc}, se clasifica como peso saludable")
elif imc >= 25 and imc < 29.9:
    categoria_imc = "Sobrepeso"
    print(f"{Nombre} el IMC es {imc}, se clasifica como sobrepeso")
elif imc >= 30:
    categoria_imc = "Obesidad"
    print(f"{Nombre} el IMC es {imc}, se clasifica como obesidad")



#Mostramos el resultado del IMC, observamos en que categoria esta el usuario y sugerimos una dieta

# Definimos una función para mostrar la dieta recomendada según la categoría del IMC

def mostrar_dieta(categoria_imc):
    """Muestra una dieta recomendada según la categoría del IMC."""
    print("- Dieta Recomendada -")
    if categoria_imc == "Bajo peso":
        print("Dieta alta en calorías y proteínas.")
        print("Ejemplo: batidos de proteínas, frutos secos.")
    elif categoria_imc == "Peso normal":
        print("Dieta equilibrada y variada.")
        print("Ejemplo: frutas, verduras, proteínas magras.")
    elif categoria_imc == "Sobrepeso":
        print("Dieta baja en calorías y rica en fibra.")
        print("Ejemplo: ensaladas, legumbres, granos enteros.")
    elif categoria_imc == "Obesidad":
        print("Dieta muy baja en calorías y controlada por un profesional.")
        print("Ejemplo: plan de comidas personalizado.")

#Mostramos concejos segun edad
# Definimos una función para dar consejos saludables según la edad
# usamos if y elif para determinar los consejos

def consejos_saludables(edad):
    print("- Consejo Personalizado -")
    if edad < 18:
        print("Eres menor de edad. Prioriza una alimentación sana para el crecimiento.")
    elif edad < 40:
        print("Aprovecha tu etapa activa: combina alimentación saludable con ejercicio regular.")
    elif edad < 60:
        print("Mantén el control del colesterol, la presión arterial y evita el sedentarismo.")
    else:
        print("Cuida tus huesos y corazón. Prioriza calcio, vitamina D y caminatas suaves.")

    



# Funciones para mostrar recomendaciones saludables

# Mostramos la dieta recomendada según la categoría del IMC
if categoria_imc:
    mostrar_dieta(categoria_imc)

# Mostramos consejos saludables según la edad
consejos_saludables(edad)