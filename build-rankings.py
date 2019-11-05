import math
import numpy
import json
import sys

mult_dict = { 0.094: 1.0,0.135137432: 1.5,0.16639787: 2.0,0.192650919: 2.5,0.21573247: 3.0,0.236572661: 3.5,0.25572005: 4.0,0.273530381: 4.5,0.29024988: 5.0,0.306057377: 5.5,0.3210876: 6.0,0.335445036: 6.5,0.34921268: 7.0,0.362457751: 7.5,0.37523559: 8.0,0.387592406: 8.5,0.39956728: 9.0,0.411193551: 9.5,0.42250001: 10.0,0.432926419: 10.5,0.44310755: 11.0,0.4530599578: 11.5,0.46279839: 12.0,0.472336083: 12.5,0.48168495: 13.0,0.4908558: 13.5,0.49985844: 14.0,0.508701765: 14.5,0.51739395: 15.0,0.525942511: 15.5,0.53435433: 16.0,0.542635767: 16.5,0.55079269: 17.0,0.558830576: 17.5,0.56675452: 18.0,0.574569153: 18.5,0.58227891: 19.0,0.589887917: 19.5,0.59740001: 20.0,0.604818814: 20.5,0.61215729: 21.0,0.619399365: 21.5,0.62656713: 22.0,0.633644533: 22.5,0.64065295: 23.0,0.647576426: 23.5,0.65443563: 24.0,0.661214806: 24.5,0.667934: 25.0,0.674577537: 25.5,0.68116492: 26.0,0.687680648: 26.5,0.69414365: 27.0,0.700538673: 27.5,0.70688421: 28.0,0.713164996: 28.5,0.71939909: 29.0,0.725571552: 29.5,0.7317: 30.0,0.734741009: 30.5,0.73776948: 31.0,0.740785574: 31.5,0.74378943: 32.0,0.746781211: 32.5,0.74976104: 33.0,0.752729087: 33.5,0.75568551: 34.0,0.758630378: 34.5,0.76156384: 35.0,0.764486065: 35.5,0.76739717: 36.0,0.770297266: 36.5,0.7731865: 37.0,0.776064962: 37.5,0.77893275: 38.0,0.781790055: 38.5,0.78463697: 39.0,0.787473578: 39.5,0.79030001: 40.0,0.79030001: 40 }
d = sorted(mult_dict.iteritems())

output = {}

######################################################### SETTINGS ###############################################################

# Cuts the number of pokemon rankings for mons below a certain pokedex number in half if set to true
new_focus = False
# Sets the number to cut rankings at - set to cut gen 1-4 now
focus_num = 495

# settings for great league rankings

# always output these pokemon (by pokedex id number)
whitelist_g = [202]
# output a limited amount of these
greylist_g = [315,407,422,423,396,397,398,519,520,521,304,305,306,21,22,48,49,74,75,76,16,17,18,265,266,267,268,269,10,11,12,307,308,111,112,464,283,284,293,294,295,23,24,190,424,311,336,427,428,41,42,169,509,510,109,110,69,70,71,13,14,15,276,277,300,301,128,117,118,56,57,52,53,161,162,529,263,264,37,38,399,400,331,332,351,421,19,20,200,201,425,426,355,356,261,262,58,59,198,199,228,229,25,26,353,354,92,93,94,504,505,506,507,508,216,217,191,192,322,323,333,334,218,219,316,317,278,279,422,423,420,421,351,406,407,315,51,1,2,4,5,7,8,338,77,78,152,153,155,156,158,159,161,162,177,178,189,200,220,221,252,253,255,256,258,259,262,277,284,286,288,287,295,297,340,372,387,388,390,391,392,393,394,395,400,402,428,428,429,460]
# Community day IDs: 149, 3, 6, 9, 181, 248, 134, 135, 136, 196, 197, 470, 471, 154, 157, 160, 376, 473, 373, 289, 254, 257, 260, 282, 475, 389, 292, 395, 330, 497, 500, 503
# never output these
blacklist_g = []
# never output non-whitelisted mons with a max cp below this
min_cp_g = 1220
# maximum number of results for a standard mon
maxr_g = 100
# maximum results for mons that cap under the league's CP limit
medr_g = 50
# maximum results for mons that are greylisted
medg_g = 20
# maximum results for greylisted mons and reallllly low cp mons still above the minimum
minr_g = 10

# settings for ultra league rankings

# always output these pokemon (by pokedex id number)
whitelist_u = []
# output a limited amount of these
greylist_u = []
# never output these
blacklist_u = []
# never output non-whitelisted mons with a max cp below this
min_cp_u = 2300
# maximum number of results for a standard mon
maxr_u = 3
# maximum results for mons that cap under the league's CP limit
medr_u = 2
# maximum results for greylisted mons and reallllly low cp mons still above the minimum
minr_u = 1

###############################################################################################################################

with open('pogo-mon-data.json') as json_file:  
    data = json.load(json_file)
    for p in data:
    	batk = int(p['atk'])
    	bdef = int(p['def'])
    	bsta = int(p['sta'])
    	num = int(p['id'])
    	evos = p['evolutions']

    	max_cp = max(10,int( 0.6245741058 * (batk+15) * math.sqrt((bdef+15)*(bsta+15))/10))
    	if max_cp < min_cp_g and not int(num) in whitelist_g:
    		print('Skip: '+p['name']+' | Max CP: '+str(max_cp))
    		continue

    	gl_out = { }
    	ul_out = { }

    	for atkiv in range(16):
			for defiv in range(16):
				for staiv in range(16):

					glvl = 0
					gl_mult = 0.094
					gl_mult = math.sqrt( (15010.0/(batk+atkiv)/ math.sqrt((bdef+defiv)*(bsta+staiv)) ) )
					for mult, lvl in d:
						if (mult > gl_mult ):
							break
						glvl = lvl
						gmult = mult

					ghp = max(10,int(gmult*(staiv + bsta)))
					gl_comb = float((gmult ** 2) * (atkiv + batk) * (defiv + bdef) * ghp)
					dupe = False

					while gl_comb in gl_out.keys():
						gl_comb = numpy.nextafter(gl_comb, 1)
						dupe = True

					gl_out[gl_comb] = { "atkv": atkiv, "defv": defiv, "stav": staiv, "lvl": glvl, "dupe": dupe }

					if max_cp > 2300:
						ulvl = 0
						ul_mult = 0.094
						ul_mult = math.sqrt( (25010.0/(batk+atkiv)/ math.sqrt((bdef+defiv)*(bsta+staiv)) ) )
						for mult, lvl in d:
							if (mult > ul_mult ):
								break
							ulvl = lvl
							umult = mult

						uhp = max(10,int(umult*(staiv + bsta)))
						ul_comb = float((umult ** 2) * (atkiv + batk) * (defiv + bdef) * uhp)
						dupe = False

						while ul_comb in ul_out.keys():
							ul_comb = numpy.nextafter(ul_comb, 1)
							dupe = True

						ul_out[ul_comb] = { "atkv": atkiv, "defv": defiv, "stav": staiv, "lvl": ulvl, "dupe": dupe }

    	form = 'unset' if not '(' in p['name'] else p['name'][p['name'].find("(")+1:p['name'].find(")")]
    	output[p['name']] = []
    	out = sorted(gl_out.items(), reverse=True)
    	i = 0
    	min_norm = 1600
    	min_low = 1500
    	max_sp = out[0][0]
    	lim = maxr_g
    	lim = medr_g if int(num) in whitelist_g or max_sp < 1700000.0 else lim
    	lim = medg_g if max_cp < min_norm or int(num) in greylist_g or max_sp < 1500000.0 else lim
    	lim = minr_g if max_cp < min_low else lim
    	if new_focus:
    		lim = lim / 2 if num < focus_num else lim
    	if lim < 100:
    		print('>>>>>>>>>>>> Limited: '+p['name']+' | Ranks: '+str(lim))
    	for sp, data in out:
    		if i == 0:
    			max_sp = sp
    		if i >= lim:
    			break
    		if data['dupe']:
    			lim -= 1
    		else:
    			i += 1
    		
    		output[p['name']].append({
	    		'id': num,
	    		'form': form,
			    'mode': 'great',
			    'rank': i,
			    'ivs': [data['atkv'],data['defv'],data['stav']],
			    'maxlevel': data['lvl'],
			    'evolutions': evos,
			    'stat-product': int(sp)
			    })
    	if max_cp > min_cp_u:
	    	out = sorted(ul_out.items(), reverse=True)
	    	i = 0
	    	min_norm = 2600
	    	min_low = 2500
	    	lim = medr_u if max_cp < min_norm or int(num) in whitelist_u else maxr_u
	    	lim = minr_u if max_cp < min_low or int(num) in greylist_u else lim
	    	for sp, data in out:
	    		if i >= lim:
	    			break
	    		if data['dupe']:
	    			lim -= 1
	    		else:
	    			i += 1
	    		output[p['name']].append({
	    			'id': num,
	    			'form': form,
				    'mode': 'ultra',
				    'rank': i,
				    'ivs': [data['atkv'],data['defv'],data['stav']],
				    'maxlevel': data['lvl'],
			    	'evolutions': evos,
			    	'stat-product': int(sp)
				    })

with open('rankings.json', 'w') as outfile:
	json.dump(output, outfile, indent=4, sort_keys=True)

