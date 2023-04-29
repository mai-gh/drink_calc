#!/usr/bin/env python3

import argparse

liquors = {}
mixers = {}


## how much mixer and liquor for a simple highball?
# drink_calc --container-vol 500 --ice-weight 100 --desired-abv 6 --liquor-abv 40


## how strong is my drink?
# drink_calc --ice-weight 100 --mixer-vol 300 --liquor-abv 40 

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--container-vol", dest='container_vol', type=int, help="How many mL is your container")
ap.add_argument("-m", "--mixer-vol",     dest='mixer_vol',     type=int, help="How many mL of mixer? ")
ap.add_argument("-l", "--liquor-vol",    dest='liquor_vol',    type=int, help="How many mL liquor]")
ap.add_argument("-p", "--liquor-abv",    dest='liquor_abv',    type=int, help="How many mL liquor]")
ap.add_argument("-i", "--ice-weight",    dest='ice_weight',    type=int, default=0, help="How many grams of ice?")
ap.add_argument("-a", "--final-abv",     dest='final_abv',     type=int, help="How much alcohol by volume should the result contain?")
a = vars(ap.parse_args())

a["ice_vol"] = a["ice_weight"] / 0.9168

ml_to_floz = lambda ml : ml * .0338

#TODO: ice melting


if a["final_abv"] and not a["mixer_vol"] and not a["liquor_vol"]:
  a["delution_ratio"] = a["liquor_abv"] / a["final_abv"]
  a["liquor_vol"] = a["container_vol"] / a["delution_ratio"]
  a["mixer_vol"] = a["container_vol"] - a["liquor_vol"] - a["ice_vol"]
  





print(f'{a["container_vol"]=}')
print(f'{a["mixer_vol"]=}')
print(f'{a["liquor_vol"]=}')
print(f'{a["liquor_abv"]=}')
print(f'{a["ice_weight"]=}')
print(f'{a["ice_vol"]=}')
print(f'{a["final_abv"]=}')

