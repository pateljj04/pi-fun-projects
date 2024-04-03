from gpiozero import LightSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# Initialize the light sensor and tonal buzzer
light_sensor = LightSensor(4)  # Change the pin number accordingly
buzzer = TonalBuzzer(14)       # Change the pin number accordingly

# Define the minimum and maximum frequencies for the tonal buzzer
MIN_FREQUENCY = 100  # Hz
MAX_FREQUENCY = 1000  # Hz

# Main loop
try:
    while True:
        # Measure light intensity
        light_intensity = light_sensor.value
        
        # Print the light intensity
        print("Light intensity:", light_intensity)
        
        # Adjust the buzzer pitch based on light intensity
        # Convert light intensity (0-1) to frequency within the defined range
        
        frequency = MIN_FREQUENCY + (MAX_FREQUENCY - MIN_FREQUENCY) * light_intensity

        # Output Frequency for Debugging
        print(frequency)

        #TODO: Fix logic for out of range Error. 
        
        if frequency < 999:
            buzzer.play(Tone(frequency))
        else:
            buzzer.stop()
        
        # Sleep for a short duration
        sleep(0.1)
        
except KeyboardInterrupt:
    # Clean up the Buzzer
    buzzer.stop()
