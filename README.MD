# fatculator

## integrantes
- Jose Daniel Patiño Maussa
- Miguel Angel Agudelo
- Leandro Zapata Muñoz

### curso 
- fundamentos De Programacion
#### fecha 
26/05/2025
##### Introducion 
Este proyecto consiste en el desarrollo de una aplicación web o móvil que permite a los usuarios calcular su Índice de Masa Corporal (IMC) de forma rápida y sencilla, a partir del ingreso de su peso y estatura. Además, incorpora un chatbot interactivo que brinda orientación personalizada en base al resultado del IMC, ofreciendo consejos sobre nutrición, actividad física y hábitos saludables.
###### Diseño y Arquitectura 
Componentes principales:

1. Entrada de datos:

Se solicitan al usuario: nombre, género, edad, peso (kg) y altura (cm).

La altura se convierte a metros para el cálculo del IMC.



2. Cálculo del IMC:

Se realiza con la fórmula estándar: IMC = peso / (altura²).

Se utiliza round(..., 1) para redondear el resultado a un decimal.



3. Clasificación del IMC:

Se compara el valor calculado con los rangos establecidos por la OMS:

Bajo peso: IMC < 18.5

Peso normal: 18.5 ≤ IMC < 24.9

Sobrepeso: 25 ≤ IMC < 29.9

Obesidad: IMC ≥ 30


4. Funciones auxiliares:

mostrar_dieta(categoria_imc): brinda recomendaciones dietéticas según la categoría del IMC.

consejos_saludables(edad): ofrece consejos personalizados basados en la edad del usuario.

###### Manual del usuario
 1. Requisitos:

Tener Python instalado (versión 3.x).

Editor o entorno para ejecutar código Python (ej. IDLE, VS Code, PyCharm, terminal).



2. Ejecución:

Abrir el archivo .py que contiene el código.

Ejecutar el programa.

Ingresar los datos solicitados cuando se pidan por pantalla:

Género (H/M)

Edad

Peso en kilogramos

Altura en centímetros

3. Resultados:

El programa mostrará:

El valor del IMC.

La categoría correspondiente (bajo peso, normal, sobrepeso, obesidad).

Una dieta recomendada para esa categoría.

Un consejo de salud personalizado según la edad.




4. Notas:

No se requieren librerías externas.

No es necesario compilar el archivo; se ejecuta directamente con python nombre_del_archivo.py.