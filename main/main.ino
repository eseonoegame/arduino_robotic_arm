#include "MyServo.h"
#include "MyJoystick.h"

#define NB_SERVOS 6
#define NB_JOYSTICKS 2

void SetPositionInitiale(MyServo servos[])
{
	// Mettre les servos dans leurs positions initiales
	for (int i = 0; i < NB_SERVOS; i++)
	{
		servos[i].SetPosition(servos[i].getAngle());
	}

	delay(2000);
	Serial.println("Les servo moteurs sont en position initiale.");
}

void controlArmWithJoystick(MyJoystick joysticks[], MyServo servos[])
{
	for (int joy = 0; joy < NB_JOYSTICKS; joy++) // On boucle sur les joysticks
	{
		for (int axe = 0; axe < 2; axe++) // On boucle sur les axes des joysticks
		{
			joysticks[joy].getValues();
			int servoId = joy << 1 | axe;
			if (joysticks[joy].getRawValues()[axe] > 900)
			{
				servos[servoId].SetPlus();
				String message = "servo " + String(servoId) + " en mouvement +.";
				Serial.println(message);
			}

			if (joysticks[joy].getRawValues()[axe] < 200)
			{
				servos[servoId].SetMoins();
				String message = "servo " + String(servoId) + " en mouvement -.";
				Serial.println(message);
			}
		}
	}
}

void setup() // vide et c'est normal.
{
}

void loop()
{
	// Initialisation des constantes, broches de la carte
	const int SERVO_PINS[] = {2, 3, 4, 5, 6, 7};
	const int INITIAL_ANGLES[] = {90, 45, 90, 90, 90, 90};
	const int JOYSTICK_PINS[][3] = {{A0, A1, 8}, {A2, A3, 9}};

	// Création des objets de la classe MyServo et MyJoystick
	MyServo servos[NB_SERVOS] = {
		MyServo(SERVO_PINS[0], INITIAL_ANGLES[0]),
		MyServo(SERVO_PINS[1], INITIAL_ANGLES[1]),
		MyServo(SERVO_PINS[2], INITIAL_ANGLES[2]),
		MyServo(SERVO_PINS[3], INITIAL_ANGLES[3]),
		MyServo(SERVO_PINS[4], INITIAL_ANGLES[4]),
		MyServo(SERVO_PINS[5], INITIAL_ANGLES[5])};

	MyJoystick joysticks[NB_JOYSTICKS] = {
		MyJoystick(JOYSTICK_PINS[0][0], JOYSTICK_PINS[0][1], JOYSTICK_PINS[0][2]),
		MyJoystick(JOYSTICK_PINS[1][0], JOYSTICK_PINS[1][1], JOYSTICK_PINS[1][2])};

	// --- setup ----
	Serial.begin(9600);			 // Initialisation de la communication série à 9600 bauds
	SetPositionInitiale(servos); // On met les servos moteurs à leur positions initiales. Important que pour la position réelle du bras soit la même que servo.angle
	Serial.println("Initialisation terminée.");

	while (true) // Code executé en boucle par le microcontrôleur.
	{
		controlArmWithJoystick(joysticks, servos); // On contrôle le bras avec les joysticks
		// joysticks[0].testJoystick(); // On teste le joystick 1
		// servos[0].testServo(3, 10);  // On teste le servo 1
		yield();
	}
}
