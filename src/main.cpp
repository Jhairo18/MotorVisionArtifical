#include <Arduino.h>

// Definir los pines del display
int display[] = {2, 3, 4, 5};

byte numeros[10][4] = {
  {0,0,0,0}, //0
  {1,0,0,0}, //1
  {0,1,0,0}, //2
  {1,1,0,0}, //3
  {0,0,1,0}, //4
  {1,0,1,0}, //5
  {0,1,1,0}, //6
  {1,1,1,0}, //7
  {0,0,0,1}, //8
  {1,0,0,1}  //9
};
void mostrarNumero(int numero) {
  for (int i = 0; i < 4; i++) { // Solo hasta 4
    digitalWrite(display[i], numeros[numero][i]);
  }
}
void setup() {
  for(int i = 0; i < 4; i++) {
    pinMode(display[i], OUTPUT); // Mejor usar OUTPUT
  }
}

void loop() {
  for(int i =0;i < 10; i++){
    mostrarNumero(i);
    delay(1000); 
  }
}