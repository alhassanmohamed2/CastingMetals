import math 

# density = 7.13 #gm/cm3
# mass = 333.73 #gm
# coef_friction = 0.4
# volume = 46351.06 #mm3
# area = 11813.96 #mm2
# time_coff = 2
# p = 0
# c = 1
# h = 40



density = float(input("Write the value of density in gm/cm3\n"))
mass = float(input("Write the value of mass in gm\n"))
coef_friction = float(input("Write the value of coff. friction\n"))
volume = float(input("Write the value of vloume in mm3\n"))
area = float(input("Write the value of area in mm2\n"))
time_coff = float(input("Write the value of coff. of time\n"))


p = float(input("From type of gating system write the value of p :\n")) #mm
c = float(input("From type of gating system write the value of c :\n")) #mm
h = float(input("From type of gating system write the value of h :\n")) #mm

def weight():
    return volume * density * 10 ** -6 #gm

def gross_weight():
    return 1.3 * weight() #kg


def calculate_pouring_time():
    return time_coff * math.sqrt(gross_weight()) #sec

def calc_height():
    effictive_H = h - ((p ** 2) / (2 * c)) 
    return effictive_H # mm

def choke_area():
    return gross_weight() / ((density / 10 **6) * calculate_pouring_time() * coef_friction * math.sqrt(2 * 9810 * calc_height())) / 100 #cm2



def check_density(cast_iron = False):
    # As : Ar : Ag
    if density > 4.5 and not cast_iron:
        As = choke_area()
        Ar = 2 * choke_area()
        Ag = choke_area()
       
        return {"msg": "we will use pressurized gating system with gating ratio 1 : 2 : 1", 
                "ratio" :  "1 : 2 : 1", "area_values_msg" : [f"Ag = {As} cm2", f"Ar = {Ar} cm2", f"As = {Ag} cm2"], 
                "area_values":{"As":As, "Ar": Ar, "Ag": Ag }}
    
    elif density < 4.5 and not cast_iron:
        Ag =  choke_area()
        As = 2 * choke_area()
        Ar = 2 * choke_area()
        
        # Ag : Ar : As
        return {"msg": "we will use unpressurized gating system with gating ratio 1 : 2 : 2", 
                "ratio" :  "1 : 2 : 2", "area_values_msg" : [f"Ag = {Ag} cm2", f"Ar = {As} cm2", f"As = {Ar} cm2"], 
                "area_values":{"Ag":Ag, "As": As, "Ar": Ar  }}
    
    elif cast_iron:
        Ag = choke_area()
        As = 2 *choke_area()
        Ar = 2 * choke_area()
        
        #Ag : Ar : As
        return {"msg": "we will use nonpressurized gating system with gating ratio because it's cast iron 1 : 2 : 2", 
                "ratio" :  "1 : 2 : 2", "area_values_msg" : [f"Ag = {Ag} cm2", f"Ar = {As} cm2", f"As = {Ar} cm2"], 
                "area_values":{"Ag":Ag, "As": As, "Ar": Ar  }}
    
#Dt / Db = (hb / ht) * 1/4

# Db = sqrt(choke_area() * 4 / pi) = Ds

# hb = calc_height()

# Dt = Db * (hb / ht) ** 1 / 4

def choke_area_diameter():
    return math.sqrt(choke_area() * 4 / math.pi) #cm2


def spure_top_diameter():
    ht = float(input("Input ht value\n"))
    return choke_area_diameter() * ((calc_height() / ht) ** (1/4)) #cm

# Dr = ( (4 * 1.3 * (volume / area)) / (1 - 2 * 1.3 * volume) / Hr * area )

def riser_diameter():
    return  (4 * 1.3 * (volume / area)) / (1 - ((2 * 1.3) / calc_height()) * (volume / area)) / 10 #cm

print("Weight = ",weight() , "\n")
print("Gross Weight = ",gross_weight() , "\n")
print("Pouring Time = ",calculate_pouring_time() , "\n")
print("Effective height H= ",calc_height(), "\n")
print("Choke Area = ",choke_area() , "\n")
print("Spure bottom diameter = ",choke_area_diameter())
print("Areas (A spure , A ingate , A runner) = ",check_density(True)["area_values_msg"],"\n") 
print("Spure top diameter = ",spure_top_diameter(), "\n")
print("Riser Diamter",riser_diameter(), "\n")
    
