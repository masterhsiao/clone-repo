#import stuff
import pandas as pd
from pathlib import Path
%matplotlib inline
#set file path
file_path = Path('Desktop/CSV/Jan_9.csv')
JS = pd.read_csv(file_path)
JS.columns
JS['Location'].value_counts()
#create variable equal to extended price of ingredients / packaging /
#supplies in different locations
Sumner_Vault = JS.loc[JS['Location'] == 'Sumner Vault', [' Ext. Price']]

Sumner_Machinery_part = JS.loc[JS['Location'] == 'Sumner Machinery part', [' Ext. Price']]

Manteca_Warehouse = JS.loc[JS['Location'] == 'Manteca Warehouse', [' Ext. Price']]

Manteca_Bakery= JS.loc[JS['Location'] == 'Manteca Bakery', [' Ext. Price']]

Transit = JS.loc[JS['Location'] == 'Transit', [' Ext. Price']]

Manteca_Dry_Mix = JS.loc[JS['Location'] == 'Manteca Dry Mix', [' Ext. Price']]

GLBC_Warehouse = JS.loc[JS['Location'] == 'GLBC Warehouse', [' Ext. Price']]

Peterson_Warehouse = JS.loc[JS['Location'] == 'Peterson Warehouse', [' Ext. Price']]

SVault = Sumner_Vault.sum()

SMachine = Sumner_Machinery_part.sum()

sumner_total = SVault + SMachine
isumner_total = int(sumner_total)

manteca_total = Manteca_Warehouse.sum() + Manteca_Bakery.sum() + Manteca_Dry_Mix.sum()
imanteca_total = int(manteca_total)

transit_total = Transit.sum()
itransit_total =int(transit_total)

GLBC_total = GLBC_Warehouse.sum()
iGLBC_total = int(GLBC_total)

Peterson_total = Peterson_Warehouse.sum()
iPeterson_total = int(Peterson_total)


Sumner_Vault_ing = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'INGREDIENT'), [' Ext. Price']]
Sumner_Vault_ing = Sumner_Vault_ing.sum()
iSumner_Vault_ing = int(Sumner_Vault_ing)

Sumner_Vault_pac = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'PACKAGING'), [' Ext. Price']]
Sumner_Vault_pac = Sumner_Vault_pac.sum()
iSumner_Vault_pac = int(Sumner_Vault_pac)

Sumner_Vault_supp = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'SUPPLIES'), [' Ext. Price']]
Sumner_Vault_supp = Sumner_Vault_supp.sum()
iSumner_Vault_supp = int(Sumner_Vault_supp)

Sumner_Vault_fin = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'FINISHED GOODS'), [' Ext. Price']]
Sumner_Vault_fin = Sumner_Vault_fin.sum()
iSumner_Vault_fin = int(Sumner_Vault_fin)

Manteca_Warehouse_ing = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'INGREDIENT'), [' Ext. Price']]
Manteca_Warehouse_ing = Manteca_Warehouse_ing.sum()
iManteca_Warehouse_ing = int(Manteca_Warehouse_ing)

Manteca_Warehouse_pac = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'PACKAGING'), [' Ext. Price']]
Manteca_Warehouse_pac = Manteca_Warehouse_pac.sum()
iManteca_Warehouse_pac = int(Manteca_Warehouse_pac)

Manteca_Warehouse_supp = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'SUPPLIES'), [' Ext. Price']]
Manteca_Warehouse_supp = Manteca_Warehouse_supp.sum()
iManteca_Warehouse_supp = int(Manteca_Warehouse_supp)

Manteca_Warehouse_fin = JS.loc[(JS['Location'] == 'Sumner Vault') & (JS['Custom #'] == 'FINISHED GOODS'), [' Ext. Price']]
Manteca_Warehouse_fin = Manteca_Warehouse_fin.sum()
iManteca_Warehouse_fin = int(Manteca_Warehouse_fin)


print("What is the inventory date?   Enter:month/day/year")
inventory_date = input()

#create an input question that ask for 4 totals
#CELEBRATION
#CHOCOLATE
# IN TRANSIT TO IWI
    #CELEBRATION
    #CHOCOLATE
    
# SET ALL as variables
print("CELEBRATION CAKE in IWI:$____")
CELEBRATION = input()
print("CHOCOLATE CAKE in IWI:$____")
CHOCOLATE = input()

CELEBRATION = int(CELEBRATION)
CHOCOLATE = int(CHOCOLATE)

print("CELEBRATION CAKE in TRANSIT:$____")
CELEBRATION_transit = input()
print("CHOCOLATE CAKE in TRANSIT:$____")
CHOCOLATE_transit = input()

CELEBRATION_transit = int(CELEBRATION_transit)
CHOCOLATE_transit = int(CHOCOLATE_transit)


IWI_TOTAL = CHOCOLATE_transit + CELEBRATION_transit + CHOCOLATE + CELEBRATION
IWI_TOTAL = int(IWI_TOTAL)

#print out all locations, broken down into ext price with variables.
print(f'Inventory report of {inventory_date}\n')

print(f'Sumner Total:            ${isumner_total:,d}\nSumner Ingredients:      ${iSumner_Vault_ing:,d}\nSumner Packaging:        ${iSumner_Vault_pac:,d}\nSumner Supplies:           ${iSumner_Vault_supp:,d}\nSumner Finished Goods:   ${iSumner_Vault_fin:,d}\n')
print(f'Manteca Total:           ${imanteca_total:,d}\nManteca Ingredients:     ${iManteca_Warehouse_ing:,d}\nManteca Packaging:       ${iManteca_Warehouse_pac:,d}\nManteca Supplies:          ${iManteca_Warehouse_supp:,d}\nManteca Finished Goods:  ${iManteca_Warehouse_fin:,d}\n')
print(f'Transit Total(not IWI):    ${itransit_total:,d}\nPeterson Total:          ${iPeterson_total:,d}\nGLBC Total:                    ${iGLBC_total:,d}\n')
print(F'IWI TOTAL:                 ${IWI_TOTAL:,d}\nCelebration in IWI:        ${CELEBRATION:,d}\nChocolate in IWI:          ${CHOCOLATE:d}\nCelebration in Transit     ${CELEBRATION_transit:,d}\nChocolate in Transit:      ${CHOCOLATE_transit:,d}')