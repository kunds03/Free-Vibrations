import numpy as np
import matplotlib.pyplot as plt

def cases(dis, vel, omega):

    # Time
    t = np.linspace(0,100, 2000)

    match (dis, vel):
        
        # Case 1: when displacement and velocity = 0
        case  (0, 0):
            disFun = np.zeros_like(t)
            velFun = np.zeros_like(t)
            accFun = np.zeros_like(t)

            disTitle = "x(t) = 0"
            velTitle = "x'(t) = 0"
            accTitle = "x''(t) = 0"

        # Case 2: when displacement = 0 and velocity = some value
        case (0,_):
            disFun = (vel / omega) * np.sin(omega * t)
            velFun = vel * np.cos(omega * t)
            accFun = -(vel * omega) * np.sin(omega * t)

            disTitle = f"x(t) = {round(vel/omega, 3)} sin({omega}t)"
            velTitle = f"x'(t) = {vel} cos({omega}t)"
            accTitle = f"x''(t) = -{round(vel * omega, 3)} sin({omega}t)"

        # Case 3: when displacement = some value and velocity = 0
        case(_,0):
            disFun = dis * np.cos(omega * t)
            velFun = -(dis * omega) * np.sin(omega * t)
            accFun = -(dis * (omega**2)) * np.cos(omega * t)

            disTitle = f"x(t) = {dis} cos({omega}t)"
            velTitle = f"x'(t) = -{round(dis * omega, 3)} sin({omega}t)"
            accTitle = f"x''(t) = -{round(dis * (omega**2), 3)} cos({omega}t)"

        # Case 4: when displacement and velocity = some value
        case(_, _):
            disFun = (dis * np.cos(omega * t)) + ((vel / omega) * np.sin(omega * t))
            velFun = -((dis * omega) * np.sin(omega * t)) + (vel * np.cos(omega * t))
            accFun = -((dis * omega ** 2) * np.cos(omega * t)) - ((vel * omega) * np.sin(omega * t))

            disTitle = f"x(t) = {dis} cos({omega}t) + {round(vel/omega, 3)} sin({omega}t)"
            velTitle = f"x'(t) = -{round(dis * omega, 3)} sin({omega}t) + {vel} cos({omega}t)"
            accTitle = f"x''(t) = -{round(dis * (omega**2), 3)} cos({omega}t) - {round(vel * omega, 3)} sin({omega}t)"
            

    graphs(t, disFun, velFun, accFun, disTitle, velTitle, accTitle)



def graphs(time, disEquation, velEquation, accEquation, disTitle, velTitle, accTitle):

    disEquation[np.abs(disEquation) > 1000] = np.nan
    velEquation[np.abs(velEquation) > 1000] = np.nan
    accEquation[np.abs(accEquation) > 5000] = np.nan

    plt.figure(figsize=(10, 10))

    # Displacement
    plt.subplot(3, 1, 1)
    plt.plot(time, disEquation)
    plt.title(f"{disTitle}")
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.grid(True)

    # Velocity
    plt.subplot(3, 1, 2)
    plt.plot(time, velEquation)
    plt.title(f"{velTitle}")
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.grid(True)

    # Acceleration
    plt.subplot(3, 1, 3)
    plt.plot(time, accEquation)
    plt.title(f"{accTitle}")
    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.grid(True)

    plt.tight_layout()
    plt.show()




def main ():
    print("At t = 0, please provide values for k and m (MUST BE SI UNITS) and for displacement (x(t)) and velocity (x'(t))\n")

    # getting the value for k
    k_value = input("Please enter a k value in SI units: ")
    
    while True:
        try:
            k_value  = int(k_value)
            break
        except ValueError:
            k_value = input("Please enter a k value in SI units: ")

    
    # getting the value for m
    m_value = input("Please enter a m value in SI units: ")
    
    while True:
        try:
            m_value  = int(m_value)
            break
        except ValueError:
            m_value = input("Please enter a m value in SI units: ")

    
    # getting the displacement value and if a proper value isnt provided then displacement = 0
    displacement = input("Please provide a displacement value (IF A VALUE ISNT GIVEN DISPLACEMENT WILL AUTOMATICALLY BE 0): ")

    try:
        displacement = int (displacement)
    except ValueError:
        displacement = 0
    

    # getting the velocity value and if a proper value isnt provided then velocity = 0
    velocity = input("Please provide a velocity value (IF A VALUE ISNT GIVE VELOCITY WILL AUTOMATICALLY BE 0): ")

    try:
        velocity = int (velocity)
    except ValueError:
        velocity = 0
    

    # Finding values omega, frequency, and time period
    omega = round(np.sqrt(k_value / m_value), 3)
    frequency = round((2 * np.pi) / omega,3)
    timePeriod = round(1 / frequency, 3)

    # print to check the values
    print(f"omega (w) = {omega} \nfrequency (f) = {frequency} \nTime Period (T) = {timePeriod}")


    # Calling the cases function to create the equations for displacement, velocity, and acceleration
    cases(displacement, velocity, omega)



if __name__ == "__main__":
    main()