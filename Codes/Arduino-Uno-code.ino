int sensor1 = A0;
int sensor2 = A1;

void setup(){
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
}




//globals
float percent = 0.05;
int threshold = 1024*percent; //within x% in either direction
int freq = 1000; //data collection frequency ~x milliseconds
int curr1, curr2;

void loop(){
    int data1 = analogRead(sensor1);
    int data2 = analogRead(sensor2);

    if((curr1 >=data1+threshold || curr1 <=data1-threshold) || (curr2>=data2+threshold || curr2<=data2-threshold) ){

        //Display Data to Serial Monitor
	Serial.print(data1);
	Serial.print(",");
	Serial.println(data2);

	//set the current equal to the data
	curr1 = data1;
	curr2 = data2;
    }
    delay(freq);
}
