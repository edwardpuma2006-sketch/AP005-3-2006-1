void inicializarHardware(); // Declaracion de funcion de inicializacion.
void setup();               // Declaracion de setup.
void loop();                // Declaracion de loop.

int main() { // Punto de entrada conceptual del programa.
    inicializarHardware(); // Preparacion interna de la tarjeta.
    setup(); // Llamada una sola vez a la configuracion inicial.
    while (true) { // Ciclo infinito propio de muchos sistemas embebidos.
        loop(); // Llamada repetida al codigo principal del usuario.
    }
    return 0; // En una tarjeta embebida normalmente no se espera llegar aqui.
}
