#include <Servo.h>

//Defining Servo Names
Servo servoA, servoB, servoC, servoD, servoE, servoF;

//Defining/Initialising Variables
char iByte = 0;
String inputString = "";
bool LEDstate = false;

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
	servoE.attach(5);
	servoE.write(0);
	servoF.attach(4);
	servoF.write(0);
}

void loop() {
	// put your main code here, to run repeatedly:

	if (Serial.available() > 0) { //If there are bytes being transmitted over serial
		iByte = Serial.read();
		inputString += iByte; //Concatenate inputString with iByte
	}
	if (inputString[0] != 'a' && inputString[0] != 'b' && inputString[0] != 'c' && inputString[0] != 'd' && inputString[0] != 'e' && inputString[0] != 'f' && inputString[0] != '*') { //If invalid ident then reset
		inputString = "";
	}
	if (inputString.length() >= 3) { //When you reach legnth 3 then work out the identifier for the servo. Then call intExtract to find the number
		switch (inputString[0]) { //Switch checks what identifier is present
		case 'a':
			servoA.write(intExtract());
			break;
		case 'b':
			servoB.write(intExtract());
			break;
		case 'c':
			servoC.write(intExtract());
			break;
		case 'd':
			servoD.write(intExtract());
			break;
		case 'e':
			servoE.write(intExtract());
			break;
		case 'f':
			servoF.write(intExtract());
			break;
		case '*':
			servoA.write(intExtract());
			servoB.write(intExtract());
			servoC.write(intExtract());
			servoD.write(intExtract());
			servoE.write(intExtract());
			servoF.write(intExtract());
			LEDstate = !LEDstate;
			digitalWrite(LED_BUILTIN, LEDstate);
			break;
		}
		inputString = "";
	}
}