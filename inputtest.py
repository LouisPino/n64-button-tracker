import pygame
import time
import socket
from pythonosc import udp_client
from pythonosc import osc_message_builder

# Set the IP address and port
ip = "127.0.0.1"  # Localhost
port = 5006       # Port number
dest_port = 5007  # Port number

client = udp_client.SimpleUDPClient(ip, dest_port)


# Create a socket for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
sock.bind((ip, port))

sock.setblocking(0)
print(f"Listening for messages on {ip}:{port}")

# Infinite loop to keep the server runnin

# Initialize Pygame and the joystick subsystem
pygame.init()
pygame.joystick.init()

# Check for connected joysticks and initialize the first one found
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")
else:
    print("No joystick detected")
    pygame.quit()
    exit()

# Main loop to process joystick inputs
try:
    while True:
        pygame.event.pump()  # Update internal state
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                message = f"Button {i} pressed"
                print(message)
                # Create an OSC message
                osc_message = osc_message_builder.OscMessageBuilder(address="/button/press")
                osc_message.add_arg(i)  # Add button index as an argument
                osc_message = osc_message.build()

                # Send the OSC message
                client.send(osc_message)
                time.sleep(0.1)  # Sleep to reduce CPU usage

finally:
    pygame.joystick.quit()  # Properly shutdown joystick subsystem
    pygame.quit()  # Quit pygame
