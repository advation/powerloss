int powerIn = A0;

void setup() 
{                
  Serial.begin(9600);
  pinMode(powerIn, INPUT);  
}

void loop() 
{
   int sensorValue = analogRead(powerIn);   
   Serial.println(sensorValue);    
   delay(1);
}
