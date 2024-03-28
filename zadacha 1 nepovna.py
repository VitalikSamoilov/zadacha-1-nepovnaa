import re
from pathlib import Path
filename = Path("zarplata.txt")

def total_salary(filename : str):
    with open(filename, "r+", encoding="utf-8") as file:
        zarplata = file.readlines()
    return (zarplata)
print(total_salary(filename))  
# total_salary
# pettern = r"[^0-9]"    
        




