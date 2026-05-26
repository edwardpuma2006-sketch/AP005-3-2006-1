#include <iostream> // Incluye la biblioteca necesaria para usar cout.

int main() { // Funcion principal: aqui inicia la ejecucion del programa.
    int a = 10; // Declara una variable entera llamada a y guarda el valor 10.
    int b = 20; // Declara una variable entera llamada b y guarda el valor 20.
    int suma = 0; // Declara la variable suma y la inicializa en cero.

    suma = a + b; // Suma los valores de a y b, y guarda el resultado en suma.
    std::cout << "a = " << a << std::endl;       // Muestra en pantalla el valor de a.
    std::cout << "b = " << b << std::endl;       // Muestra en pantalla el valor de b.
    std::cout << "suma = " << suma << std::endl; // Muestra en pantalla el resultado.
    return 0; // Indica que el programa finalizo correctamente.
} // Fin de la funcion main.
