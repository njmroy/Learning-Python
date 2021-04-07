#Write a function named kinetic_energy that accepts an object’s mass (in kilograms) and velocity
#(in meters per second) as arguments. The function should return the amount of kinetic energy that the object has.
#Write a program that asks the user to enter values for mass and velocity, then calls the kinetic_energy function to
#get the object’s kinetic energy.

#Kinetic energy functio definition. Accept mass and velocity as parameter variables, return calculation.
def kinetic_energy(mass,velocity):
        return(0.5*mass*velocity*velocity)

#Main function definition. Accept mass and velocity values from user, convert to floats, call kinetic
#energy function, print output for user, return null to exit.
def main():
    mass = float(input("Enter mass value: "))
    velocity = float(input("Enter velocity value: "))
    k=kinetic_energy(mass, velocity)
    print("Kinetic energy is: "+str(k))
    return

#Main function call
main()
