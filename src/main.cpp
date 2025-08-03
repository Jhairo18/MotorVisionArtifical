#include <Arduino.h>

// Definir los pines del display
int display[] = {2, 3, 4, 5};
int IN3 = 6;
int IN4 = 7;
int ENB = 11;
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
void velocidadMotor(int nivel) {
  // Asegura que el nivel esté entre 0 y 9
  nivel = constrain(nivel, 0, 9);
  // Mapear nivel de 0–9 a 50–255
  int pwm = map(nivel, 0, 9, 70, 255);
  // Escribir el valor PWM en el pin ENB
  analogWrite(ENB, pwm);
}
void mostrarNumero(int numero) {
  for (int i = 0; i < 4; i++) { // Solo hasta 4
    digitalWrite(display[i], numeros[numero][i]);
  }
}
void mostrarNumeroyVelocidad(int numero) {
  mostrarNumero(numero);
  velocidadMotor(numero);
}
void setup() {
  for(int i = 0; i < 4; i++) {
    pinMode(display[i], OUTPUT); // Mejor usar OUTPUT
  }
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void loop() {
  // for(int i =0;i < 10; i++){
  //   mostrarNumero(i);
  //   delay(1000); 
  // }
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  mostrarNumeroyVelocidad(9);

}