#include <Arduino.h>

// Define structure for communication values
struct ComValues
{
    int x;
    int y;
    float t;
};

ComValues *readSerial()
// On attend un message de la forme "12,12,0.4\n"
// Ce qui correpond à x,y,t
{
    static ComValues values;

    if (Serial.available() > 0)
    {
        String message = Serial.readStringUntil('\n');
        int pos1 = message.indexOf(',');
        int pos2 = message.indexOf(',', pos1 + 1);

        values.x = message.substring(0, pos1).toInt();
        values.y = message.substring(pos1 + 1, pos2).toInt();
        values.t = message.substring(pos2 + 1).toFloat();

        // Affichage des valeurs reçues
        Serial.print("Angle 1: ");
        Serial.print(values.x);
        Serial.print(" Angle 2: ");
        Serial.print(values.y);
        Serial.print(" Time: ");
        Serial.println(values.t);

        return &values;
    }
    return nullptr;
}