str_length = input("Please ENTER THE Length : \n")
str_Width = input("Please EMTER THE Width : \n")
# لازم أحول دلوقتي علشان استحالة تكون أرقام الطول و العرض بالضبط #
Length = float(str_length)
Width = float(str_Width)
str_Total_Cost = input(" HOW MUCH IT COST FOR 1 METER ? : \n ")
NEW_Total_Cost = float(str_Total_Cost)
AREA = Length * Width
STR_AREA = str(AREA)
Float_Total_Cost = NEW_Total_Cost * AREA
str_float_total_cost = str(Float_Total_Cost)
print(" THE TOTAL AREA IS " + STR_AREA)
print(" GIVE THE GUY THE COST FOR HIS WORK  :  $" + (str_float_total_cost))
