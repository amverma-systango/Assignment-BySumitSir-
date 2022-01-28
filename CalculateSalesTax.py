import pandas as pd
import csv

productCatalogDf = pd.read_csv("ProductCatalog.csv")
salesTaxDf = pd.read_csv("SalesTax.csv")

with open("result.csv", "w", newline="") as csvFileObject:
    thewritter = csv.writer(csvFileObject)

    thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

    salseTaxDfIndex = 0

    while salseTaxDfIndex < len(salesTaxDf):
        productCatalogDfIndex = 0
        while productCatalogDfIndex < len(productCatalogDf):
            taxprice = (float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex])* float(productCatalogDf['ProductCost'][productCatalogDfIndex]))/100
            salesprice = float(productCatalogDf['ProductCost'][productCatalogDfIndex])+taxprice
    
            thewritter.writerow([productCatalogDf['ProductName'][productCatalogDfIndex], productCatalogDf['ProductCost'][productCatalogDfIndex], salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex], taxprice, salesprice, salesTaxDf['Country'][salseTaxDfIndex]])
            productCatalogDfIndex+=1
        salseTaxDfIndex+=1
