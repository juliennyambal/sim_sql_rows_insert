import random
import numpy as np
n = 60
for er_id in np.arange(1,n):
    
    #order_id = random.randint(1,32)
    cst_id  = random.randint(1,32)
    er_total_amount = np.round(random.random()*10000,2)
    er_shipping_amount = np.round(random.random()*10000,2) 
    er_discount_amount = np.round(random.random()*10000,2)
    er_status = ["Requested","Responded","Accepted","Completed"]
    er_lat = 0
    er_long = 0
    er_city = ["Benoni","Boksburg","Brakpan","Carletonville","Germiston","Johannesburg",
              "Krugersdorp","Pretoria","Randburg","Randfontein","Roodepoort","Soweto","Springs","Vanderbijlpark","Vereeniging"]
    month = random.randint(1,10)
    day = random.randint(1,31)
    er_date = "2019-%02d-%02d" % (month,day)
    er_country = "South Africa"
    er_province_state = "Gauteng"
    er_store_id = random.randint(1,32)
    er_store_name = ["SEGWAGWA Cash n Carry","Advance Cash n Carry","7 Eleven (OK Franchise)","Boxer","Cambridge Food",
                        "Checkers","Checkers Hyper","Checkout","Choppies","Devland Metro Cash & Carry","Friendly (OK Franchise)",
                        "Discount Cash & Carry","Food Lovers Market","Game Stores","Jumbo Cash & Carry","Kit Kat Group",
                        "Makro","MEGASAVE (Cash & Carry)","OK Grocer","OK Minimark""OK Value","Pick n Pay Stores",
                        "Rhino Cash & Carry","Shoprite","ShopriteHyper","Spar","Woolworths","USave","USave Superstore"]
    er_qty_total = random.randint(1,50)
    
    print("(\'%s\',\'%s\',%.2f,%.2f,%.2f,\'%s\',\'%s\',\'%.2f\',\'%.2f\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d)," % 
      (er_id,cst_id,er_total_amount,er_shipping_amount,er_discount_amount,
       er_date,er_status[random.randint(1,len(er_status)-1)],er_lat,er_long,
       er_city[random.randint(1,len(er_city)-1)],
       er_country,er_province_state,er_store_id,er_store_name[random.randint(1,len(er_store_name)-1)],er_qty_total))
