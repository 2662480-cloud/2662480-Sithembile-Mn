
#space_burden=a
a=float(input("Enter a S/B ratio: "))

#explosive_density=p
p=float(input("Enter a explosive density: "))

#blasthole_diameter=d
d=float(input("Enter your blasthole diameter: "))

#bench_height=bh
bh=float(input("Enter your bench height: "))


#stemming_factor=sf
sf=25

#stemming_length=sl
sl=sf*(d/1000) #converted  diameter to metres

#charge_length
cl = bh - sl

#linear_charge_mass=m
m=(p*(d**2))/1273

#mass_of_explosive_per_hole = q
q = m * cl
#powder_factor_tech=pf
pf=float(input("Enter the technical powder factor: "))

if pf <= 0.7 and pf >= 0.15:
    b = ((m * (bh - sl)) / (a * pf * bh)) ** (0.5) #burden=b
    s = b * a #spacing=s
    sd = 1 / 3 * b #subrill=sd
    pos_or_neg = input("Is sub_drill positive or negative (+,-,0): ")
    if pos_or_neg == "-":
        pf_actual = ((m * (bh - sl - sd)) / (b * s * bh))
        print(f"Your actual powder factor is: {pf_actual}")
    elif pos_or_neg == "+":
        pf_actual = ((m * (bh - sl + sd)) / (b * s * bh))
        print(f"Your actual powder factor is: {pf_actual}")
    else:
        pf_actual = ((m * (bh - sl)) / (b * s * bh))
        print(f"Your actual powder factor is: {pf_actual}")
    print(f"Your stemming length is: {sl}")
    print(f"Your burden is: {b}")
    e = float(input("Enter the relative effective energy of explosive: ")) #relative_effective_energy=e
    A = float(input("Enter a rock factor constant: ")) #rock_factor_constant=A
    if A >= 6 and A <= 14:
        x50 = A * ((pf) ** (-0.8)) * (q ** 0.167) * ((115 / e) ** 0.633) #mean_fragmentation_size = x50
        print(f"Your mean fragment size is: {x50}")
    else:
        print("Invalid Rock Constant")
else:
    print("Invalid Technical Powder Factor!!")






