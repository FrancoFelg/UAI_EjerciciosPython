def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage woul you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
def dollars_to_float(d):
    d = d.replace("$", "")
    rta = float(d)
    return rta
    
def percent_to_float(p):
    p = p.replace("%", "")
    rta = float(p )/ 100
    return rta
    
    
main()