from dronekit import connect, VehicleMode
import time

# Connect to the APM
vehicle = connect('/dev/ttyUSB0', baud=57600, wait_ready=True)  # Change to '/dev/serial0' for UART

def arm_and_test_motor():
    print("Checking pre-arm status...")
    while not vehicle.is_armable:
        print("Waiting for drone to initialize...")
        time.sleep(2)

    print("Arming motors...")
    vehicle.mode = VehicleMode("STABILIZE")  # Change mode if needed (GUIDED, LOITER, etc.)
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(2)

    print("Motors armed!")

    print("Setting throttle to 50%")
    vehicle.channels.overrides = {'3': 1500}  # Throttle (PWM: 1000-2000)

    time.sleep(5)  # Keep motors running for 5 seconds

    print("Stopping motors...")
    vehicle.channels.overrides = {'3': 1000}  # Min throttle

    time.sleep(2)
    print("Disarming motors...")
    vehicle.armed = False
    time.sleep(2)

    print("Test complete!")
    vehicle.close()

# Run motor test
arm_and_test_motor()
