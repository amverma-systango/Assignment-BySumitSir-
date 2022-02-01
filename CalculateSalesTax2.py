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
            print( type(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]), " ", type(productCatalogDf['ProductCost'][productCatalogDfIndex]) )
            try:
                if( float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]) >= 0.0 and float(productCatalogDf['ProductCost'][productCatalogDfIndex])> 0.0):
                    taxprice = (float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex])* float(productCatalogDf['ProductCost'][productCatalogDfIndex]))/100

                    salesprice = float(productCatalogDf['ProductCost'][productCatalogDfIndex])+taxprice
        
                    thewritter.writerow([productCatalogDf['ProductName'][productCatalogDfIndex], productCatalogDf['ProductCost'][productCatalogDfIndex], salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex], taxprice, salesprice, salesTaxDf['Country'][salseTaxDfIndex]])
                    productCatalogDfIndex+=1
                else:
                    print("input file contain invalid values")
                    break;
            except ValueError:
                print("input file contain characters instead of values")
                break;
            except:
                print("invalid inputs")

        salseTaxDfIndex+=1
