import pyaudio
import sounddevice as sd
import os 

def mic_checking():
    audio = pyaudio.PyAudio()

    # Get the number of available audio devices
    num_devices = audio.get_device_count()

    # Check if any microphone device is found and enabled
    is_microphone_connected = False
    is_microphone_enabled = False
    for i in range(num_devices):
        device_info = audio.get_device_info_by_index(i)
        if device_info["maxInputChannels"] > 0:
            is_microphone_connected = True
            # Check if the device is enabled using sounddevice
            try:
                with sd.InputStream(device=i):
                    pass
                is_microphone_enabled = True
            except sd.PortAudioError:
                pass
            break
 # Terminate PyAudio
    audio.terminate()
    # Print the microphone connection and enable status
    if is_microphone_connected:
        if is_microphone_enabled:
            #print("Microphone is connected and enabled.")
            return True
        else:
            #print("Microphone is connected but disabled.")
            return False
    else:
        #print("Microphone is not connected.")
        return False
    

def get_user_name():
    user_names = []
    try:
        user_dirs = os.listdir('C:/Users')  
        for user_dir in user_dirs:
            user_names.append(user_dir)
    except Exception as e:
        print(f"Error accessing user directories: {e}")
    
    remove_the_unwantedusers = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
    
    # Remove unwanted user names from the list
    user_names = [user for user in user_names if user not in remove_the_unwantedusers]

    return str(user_names[0])


