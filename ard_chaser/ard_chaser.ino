// LED chaser controlled from Python (face recognition)
// '1' = allowed face seen  -> LEDs chase
// '0' = unknown / no face  -> all LEDs off

// External LED pins
#define led 6
#define led1 7
#define led2 8
#define led3 9

int data, flag = 2;   // flag: 2 = no signal yet, 1 = chaser on, 0 = off

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);   // must match 9600 in the Python script

  // Start with everything off
  digitalWrite(led, LOW);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop()
{
  // Read the latest signal sent by Python
  while (Serial.available())
  {
    data = Serial.read();

    if (data == '1')
    {
      flag = 1;
    }
    else if (data == '0')
    {
      flag = 0;
    }
  }

  if (flag == 1)
  {
    // Chaser: one LED on at a time, left to right
    digitalWrite(led, HIGH);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    delay(200);

    digitalWrite(led, LOW);
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    delay(200);

    digitalWrite(led, LOW);
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
    delay(200);

    digitalWrite(led, LOW);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
    delay(200);

    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if (flag == 0)
  {
    // Everything off
    digitalWrite(led, LOW);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(LED_BUILTIN, LOW);
  }
}