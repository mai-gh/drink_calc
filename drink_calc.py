#!/usr/bin/env python


# done in ML



liquor_percent = 45



#base_volume = (500 + 750)
bottle_volume = 450
desired_final_percent = 10
#liquor_volume = 1


#liquor_percent = 40
#bottle_volume = 355
#base_volume = 310
# above equals 45 which is ~ 1/5 floz or 1 shot, which should be equal abv to 1 beer at 5%
# used as a test to prove the equation



def find_liqor_volume():
  for i in range(0, 3000):
    test_percent = (i * liquor_percent) / (base_volume + i)
    print(i, test_percent)
    if test_percent >= desired_final_percent:
      print(i, test_percent)
      break


def find_base_volume():
  total_parts = liquor_percent / desired_final_percent  
  base_parts = total_parts - 1
  base_vol = base_parts * liquor_volume
  base_vol_oz = base_vol * .0338
  print(base_vol)
  print(base_vol_oz)

def find_percent():
  alc_percent = (liquor_percent * liquor_volume) / (base_volume + liquor_volume)
  print(alc_percent)

def find_base_and_liquor_volume_bottle_volume():
  # neet bottle_volume and desired_final_percent and liquor_percent

  # first determine ratio to dilute liquor to desired percent
  # 43 / 5 = 8.6 or 8.6:1
  delution_ratio = liquor_percent / desired_final_percent
  liquor_volume = bottle_volume / delution_ratio
  base_volume = bottle_volume - liquor_volume 
  print(liquor_volume, base_volume) 

#find_base_volume()
#find_liqor_volume()
#find_percent()
find_base_and_liquor_volume_bottle_volume()


