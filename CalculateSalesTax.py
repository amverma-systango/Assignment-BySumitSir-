import pandas as pd
import csv

productCatalogDf = pd.read_csv("ProductCatalog.csv")
salesTaxDf = pd.read_csv("SalesTax.csv")

with open("result.csv", "w", newline="") as f:
    thewritter = csv.writer(f)

    thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

    i = 0
    print(type(float(salesTaxDf['SalseTaxInPercent'][i])))


    while i < len(salesTaxDf):
        j = 0
        while j < len(productCatalogDf):
            taxprice = (float(salesTaxDf['SalseTaxInPercent'][i])* float(productCatalogDf['ProductCost'][j]))/100
            salesprice = float(productCatalogDf['ProductCost'][j])+taxprice
            #print(f"{salesTaxDf['Country'][i]}         {salesTaxDf['SalseTaxInPercent'][i]}%           {productCatalogDf['ProductName'][j]}           {productCatalogDf['ProductCost'][j]} {salesprice} cost AT")
            thewritter.writerow([productCatalogDf['ProductName'][j], productCatalogDf['ProductCost'][j], salesTaxDf['SalseTaxInPercent'][i], taxprice, salesprice, salesTaxDf['Country'][i]])
            j+=1
        i+=1


#print(productCatalogDf)
#print(salesTaxDf)


# country product tax actualprice aftertaxprice

# Country  SalseTaxInPercent    ProductName ProductCost

