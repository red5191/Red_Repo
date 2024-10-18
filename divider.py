try:
    chislo1 = float(input('napishi pervoe chislo: '))
    chislo2 = float(input('napishi vtoroe chislo: '))
    chastnoe = chislo1 / chislo2

except ValueError:
    print('eto ne chislo')
except ZeroDivisionError:
    print('na nol\' nel\'zya')

else:
    print(f'poluchilos\': {chastnoe}')

finally:
    print('programma zavershena')
