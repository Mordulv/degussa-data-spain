# degussa-data-spain

Program that extracts data on the purchase and sale price of gold, silver, platinum and palladium, being the website from which the data is extracted: 

https://www.degussa-mp.es/precios

## PROGRAM OUTLINE

![](https://github.com/Guillermo-C-A/degussa-data-spain/blob/master/Readme%20img/program%20outline.png)

## HOW TO USE THE CODE

#### Save the data in a txt 

To obtain a DataFrame and save the information in a txt, you will only have to execute this line of code: 

`Degussa().save_data()`

#### Get the date and the DataFrame 

To obtain the date and the DataFrame of Degussa's data you only have to write the following line of code:

`date, data = Degussa().get_data()`

This way, "date" will be the last date of update and "data" will be the DataFrame that contains all the information. 
