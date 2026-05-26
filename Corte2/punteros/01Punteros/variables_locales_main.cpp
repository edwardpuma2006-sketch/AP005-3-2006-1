#include <iostream> // Incluye la biblioteca necesaria para cout.

int main() { // Inicia la funcion principal del programa.
    int a = 10; // Variable local de main.
    int b = 20; // Variable local de main.
    int suma = 0; // Variable local de main.

    suma = a + b; // Usa las variables locales para calcular un resultado.
    std::cout << "suma = " << suma << std::endl; // Muestra el valor guardado en suma.
    return 0; // Finalizacion exitosa del programa.
} // Al terminar main, sus variables locales normales dejan de ser validas.
