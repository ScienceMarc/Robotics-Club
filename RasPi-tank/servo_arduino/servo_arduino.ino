#include <Servo.h>

//Defining Servo Names
Servo servoA, servoB, servoC, servoD;

//Defining/Initialising Variables
char iByte = 0;
String inputString = "";

//Defining a function, to return the numbers from the end of a command.
int intExtract() {
	String temp = "";
	temp += inputString[1];
	temp += inputString[2];
	int tempInt = temp.toInt();
	return tempInt;
}

void setup() {
	Serial.begin(9600); // Starting the serial connection
	digitalWrite(LED_BUILTIN, LOW); // Switching off the onboard LED (for debugging)
	//Attaching and resetting servos
	servoA.attach(9);
	servoA.write(0);
	servoB.attach(8);
	servoB.write(0);
	servoC.attach(7);
	servoC.write(0);
	servoD.attach(6);
	servoD.write(0);
}

void loop() {
	// put your main code here, to run repeatedly:

	if (Serial.available() > 0) { //If serial is not available, then read the character to iByte
		iByte = Serial.read();
		inputString += iByte; //Append ibyte to inputString
	}
	if (inputString[0] != 'a' && inputString[0] != 'b' && inputString[0] != 'c' && inputString[0] != 'd' && inputString[0] != '*') { //If invalid ident then reset
		inputString = "";
	}
	if (inputString.length() >= 3) { //When you reach legnth 3 then work out the identifier for the servo. Then use intExtract to find the number
		if (inputString[0] == 'a') {//Identifier a
			servoA.write(intExtract());
		}
		else if (inputString[0] == 'b') {//Identifier b
			servoB.write(intExtract());
		}
		else if (inputString[0] == 'c') {//Identifier c
			servoC.write(intExtract());
		}
		else if (inputString[0] == 'd') {//Identifier d
			servoD.write(intExtract());
		}
		else if (inputString[0] == '*') {//Identifier *
			servoA.write(intExtract());
			servoB.write(intExtract());
			servoC.write(intExtract());
			servoD.write(intExtract());
		}
		inputString = "";
	}
}