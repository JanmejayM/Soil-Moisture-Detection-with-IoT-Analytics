

## Project developed by:          
### Janmejay Mohapatra 
#### B.Tech in Electrical & Electronics Engineering


# Soil-Moisture-Detection-with-IoT-Analytics



<p1>This project relates to soil moisture detection and automatic plant watering. The moisture sensor partially buried on soil continuously monitors the moisture of the soil. The data of Soil Moisture is sent to the ThingSpeak platform. The data on the Thingspeak Platform is directly transmitted to the app specially made for this project i.e. ”ESP_SOIL_MOISTURE” App. This data is also stored in ThingSpeak and also visual analysis is done using graphs. This continuous moisture analysis will also be useful for research and development purposes.</p1><br></br>
In addition to that, this project also comes with a minimum and maximum value of moisture percentage depending on which plants will be watered. The ability of this project to communicate via the internet makes it an “Internet of Things (IoT)” device. It also reduces the cost of the project and is more efficient when compared to its existing alternatives. This project is programmed using Thonny IDE in MicroPython language.

# System Architecture:

![System Architecture ](https://user-images.githubusercontent.com/89799094/150679374-bc27e68a-8822-43f1-a82a-c61179ca8826.png)



# Components Description:

1)	NodeMCU ESP8266: It is an open-source IoT development board whose firmware runs on the ESP8266 Wi-Fi module, it performs three significant operations. It fetches information from the soil moisture sensor and calculate moisture percentage, transmits the real-time Moisture percentage value to the ThingSpeak IoT platform, activation the signal to relay 1 channel for ON/OFF operation of the Water Pump.


2)	Relay Module 1-Channel: It acts as a switch to ON/OFF the Water Pump depending on the Signal from NodeMCU as we are using an external 5V source to power the Water Pump.


3)	Soil Moisture Sensor: It sends an analog voltage signal to the 10-bit ADC pin of NodeMCU. This signal is then converted into moisture percentage by NodeMCU by some calculations.


4)	ThingSpeak: Here ThingSpeak is used to store real-time data streams in the cloud and later used for communicating this real-time data to our App.


5)	ESP_SOIL_MOISTURE App: This App is made by using MIT App Inventor. This app is specially designed to receive real-time moisture percentages from ThingSpeak. It also shows the last time of updated system, this is mainly done to check continuity of the system.


6)	Mini Water Pump: This is a small submersible water pump operating between 3V-6V. This pump is used to sprinkle water in the plant.


7)	ESP_SOIL_MOISTURE App 
It is an App that is specially made for the project of  “Soil Moisture Detection” using the MIT App Inventor platform. It receives the real-time value of Moisture Percentage from ThingSpeak.




![image](https://user-images.githubusercontent.com/89799094/150679666-609e6aab-04e0-4c51-9cab-69472fd4b31e.png)







# Circuit Diagram:
![image](https://user-images.githubusercontent.com/89799094/150679465-1fda26d4-2d7e-4bc4-b231-56a2e81e6b9b.png)








# Methodolody:



![image](https://user-images.githubusercontent.com/89799094/150679699-60c7476d-c2e0-4f65-b66e-6499ae0aac3b.png)



•	The Values already set in the code are
<br></br>
a.	Minimum value - 30
<br></br>
b.	Maximum value – 50




# Implementation:




![image](https://user-images.githubusercontent.com/89799094/150679744-f146b945-dac4-478b-9d38-6830d1852840.png)




