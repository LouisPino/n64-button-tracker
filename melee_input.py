import pygame
import time
import socket
from pythonosc import udp_client
from pythonosc import osc_message_builder

# Set the IP address and port
ip = "127.0.0.1"  # Localhost
port = 5007  # Port number

client = udp_client.SimpleUDPClient(ip, port)


# Create a socket for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port

sock.setblocking(0)

btn_map = {
    0: "A",
    1: "B",
    2: "X",
    3: "Y",
    4: "DLeft",
    5: "DRight",
    6: "DDown",
    7: "DUp",
    8: "S",
    9: "Z",
    10: "R",
    11: "L",
}



# Initialize Pygame and the joystick subsystem
pygame.init()
pygame.joystick.init()

# Check for connected joysticks and initialize the first one found
if pygame.joystick.get_count() > 0:
    joystick1 = pygame.joystick.Joystick(0)
    joystick2 = pygame.joystick.Joystick(1)
    joystick3 = pygame.joystick.Joystick(2)
    joystick4 = pygame.joystick.Joystick(3)
    joystick1.init()
    joystick2.init()
    joystick3.init()
    joystick4.init()
    print(f"Joystick 1 initialized: {joystick1.get_name()}")
    print(f"Joystick 2 initialized: {joystick2.get_name()}")
    print(f"Joystick 3 initialized: {joystick3.get_name()}")
    print(f"Joystick 4 initialized: {joystick4.get_name()}")
else:
    print("No joysticks detected")
    pygame.quit()
    exit()

# Main loop to process joystick inputs
try:
    while True:
        pygame.event.pump()  # Update internal state
        for i in range(joystick1.get_numbuttons()):
            if joystick1.get_button(i):
                # Create an OSC message
                osc_message = osc_message_builder.OscMessageBuilder(address="/button/P1")
                osc_message.add_arg(f"{btn_map[i]}")  # Add button index as an argument
                osc_message = osc_message.build()
                client.send(osc_message)
            # Handle joystick axes
        for j in range(joystick1.get_numaxes()):
            axis_value = joystick1.get_axis(j)
            if abs(axis_value) > 0.1:  # Deadzone filtering
                osc_message = osc_message_builder.OscMessageBuilder(address=f"/axis/P1")
                osc_message.add_arg(j)
                osc_message.add_arg(float(axis_value))
                osc_message = osc_message.build()
                client.send(osc_message)
            
            
        for i in range(joystick2.get_numbuttons()):
            if joystick2.get_button(i):
                # Create an OSC message
                osc_message = osc_message_builder.OscMessageBuilder(address="/button/P2")
                osc_message.add_arg(f"{btn_map[i]}")  # Add button index as an argument
                osc_message = osc_message.build()

                # Send the OSC message
                client.send(osc_message)
 
        for j in range(joystick2.get_numaxes()):
            axis_value = joystick2.get_axis(j)
            if abs(axis_value) > 0.1:  # Deadzone filtering
                osc_message = osc_message_builder.OscMessageBuilder(address=f"/axis/P2")
                osc_message.add_arg(j)
                osc_message.add_arg(float(axis_value))
                osc_message = osc_message.build()
                client.send(osc_message)
                
        
        for i in range(joystick3.get_numbuttons()):
            if joystick3.get_button(i):
                # Create an OSC message
                osc_message = osc_message_builder.OscMessageBuilder(address="/button/P3")
                osc_message.add_arg(f"{btn_map[i]}")  # Add button index as an argument
                osc_message = osc_message.build()

                # Send the OSC message
                client.send(osc_message)
                
        for j in range(joystick3.get_numaxes()):
            axis_value = joystick3.get_axis(j)
            if abs(axis_value) > 0.1:  # Deadzone filtering
                osc_message = osc_message_builder.OscMessageBuilder(address=f"/axis/P3")
                osc_message.add_arg(j)
                osc_message.add_arg(float(axis_value))
                osc_message = osc_message.build()
                client.send(osc_message)                
                
        for i in range(joystick4.get_numbuttons()):
            if joystick4.get_button(i):
                # Create an OSC message
                osc_message = osc_message_builder.OscMessageBuilder(address="/button/P4")
                osc_message.add_arg(f"{btn_map[i]}")  # Add button index as an argument
                osc_message = osc_message.build()

                # Send the OSC message
                client.send(osc_message)
                
        for j in range(joystick4.get_numaxes()):
            axis_value = joystick4.get_axis(j)
            if abs(axis_value) > 0.1:  # Deadzone filtering
                osc_message = osc_message_builder.OscMessageBuilder(address=f"/axis/P4")
                osc_message.add_arg(j)
                osc_message.add_arg(float(axis_value))
                osc_message = osc_message.build()
                client.send(osc_message)                
                
finally:
    pygame.joystick1.quit()  # Properly shutdown joystick subsystem
    pygame.joystick2.quit()  # Properly shutdown joystick subsystem
    pygame.joystick3.quit()  # Properly shutdown joystick subsystem
    pygame.joystick4.quit()  # Properly shutdown joystick subsystem
    pygame.quit()  # Quit pygame
