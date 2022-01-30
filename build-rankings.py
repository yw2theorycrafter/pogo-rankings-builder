import math
import json
import sys
from termcolor import colored

mult_dict = {
    0.094: 1.0,
    0.1351374318: 1.5,
    0.16639787: 2.0,
    0.192650919: 2.5,
    0.21573247: 3.0,
    0.2365726613: 3.5,
    0.25572005: 4.0,
    0.2735303812: 4.5,
    0.29024988: 5.0,
    0.3060573775: 5.5,
    0.3210876: 6.0,
    0.3354450362: 6.5,
    0.34921268: 7.0,
    0.3624577511: 7.5,
    0.3752356: 8.0,
    0.387592416: 8.5,
    0.39956728: 9.0,
    0.4111935514: 9.5,
    0.4225: 10.0,
    0.4329264091: 10.5,
    0.44310755: 11.0,
    0.4530599591: 11.5,
    0.4627984: 12.0,
    0.472336093: 12.5,
    0.48168495: 13.0,
    0.4908558003: 13.5,
    0.49985844: 14.0,
    0.508701765: 14.5,
    0.51739395: 15.0,
    0.5259425113: 15.5,
    0.5343543: 16.0,
    0.5426357375: 16.5,
    0.5507927: 17.0,
    0.5588305862: 17.5,
    0.5667545: 18.0,
    0.5745691333: 18.5,
    0.5822789: 19.0,
    0.5898879072: 19.5,
    0.5974: 20.0,
    0.6048236651: 20.5,
    0.6121573: 21.0,
    0.6194041216: 21.5,
    0.6265671: 22.0,
    0.6336491432: 22.5,
    0.64065295: 23.0,
    0.6475809666: 23.5,
    0.65443563: 24.0,
    0.6612192524: 24.5,
    0.667934: 25.0,
    0.6745818959: 25.5,
    0.6811649: 26.0,
    0.6876849038: 26.5,
    0.69414365: 27.0,
    0.70054287: 27.5,
    0.7068842: 28.0,
    0.7131691091: 28.5,
    0.7193991: 29.0,
    0.7255756136: 29.5,
    0.7317: 30.0,
    0.7347410093: 30.5,
    0.7377695: 31.0,
    0.7407855938: 31.5,
    0.74378943: 32.0,
    0.7467812109: 32.5,
    0.74976104: 33.0,
    0.7527290867: 33.5,
    0.7556855: 34.0,
    0.7586303683: 34.5,
    0.76156384: 35.0,
    0.7644860647: 35.5,
    0.76739717: 36.0,
    0.7702972656: 36.5,
    0.7731865: 37.0,
    0.7760649616: 37.5,
    0.77893275: 38.0,
    0.7817900548: 38.5,
    0.784637: 39.0,
    0.7874736075: 39.5,
    0.7903: 40.0,
    0.792803968: 40.5,
    0.79530001: 41.0,
    0.797800015: 41.5,
    0.8003: 42.0,
    0.802799995: 42.5,
    0.8053: 43.0,
    0.8078: 43.5,
    0.81029999: 44.0,
    0.812799985: 44.5,
    0.81529999: 45.0,
    0.81779999: 45.5,
    0.82029999: 46.0,
    0.82279999: 46.5,
    0.82529999: 47.0,
    0.82779999: 47.5,
    0.83029999: 48.0,
    0.83279999: 48.5,
    0.83529999: 49.0,
    0.83779999: 49.5,
    0.84029999: 50.0,
}
mult_dict_buddy = {
    0.094: 1.0,
    0.1351374318: 1.5,
    0.16639787: 2.0,
    0.192650919: 2.5,
    0.21573247: 3.0,
    0.2365726613: 3.5,
    0.25572005: 4.0,
    0.2735303812: 4.5,
    0.29024988: 5.0,
    0.3060573775: 5.5,
    0.3210876: 6.0,
    0.3354450362: 6.5,
    0.34921268: 7.0,
    0.3624577511: 7.5,
    0.3752356: 8.0,
    0.387592416: 8.5,
    0.39956728: 9.0,
    0.4111935514: 9.5,
    0.4225: 10.0,
    0.4329264091: 10.5,
    0.44310755: 11.0,
    0.4530599591: 11.5,
    0.4627984: 12.0,
    0.472336093: 12.5,
    0.48168495: 13.0,
    0.4908558003: 13.5,
    0.49985844: 14.0,
    0.508701765: 14.5,
    0.51739395: 15.0,
    0.5259425113: 15.5,
    0.5343543: 16.0,
    0.5426357375: 16.5,
    0.5507927: 17.0,
    0.5588305862: 17.5,
    0.5667545: 18.0,
    0.5745691333: 18.5,
    0.5822789: 19.0,
    0.5898879072: 19.5,
    0.5974: 20.0,
    0.6048236651: 20.5,
    0.6121573: 21.0,
    0.6194041216: 21.5,
    0.6265671: 22.0,
    0.6336491432: 22.5,
    0.64065295: 23.0,
    0.6475809666: 23.5,
    0.65443563: 24.0,
    0.6612192524: 24.5,
    0.667934: 25.0,
    0.6745818959: 25.5,
    0.6811649: 26.0,
    0.6876849038: 26.5,
    0.69414365: 27.0,
    0.70054287: 27.5,
    0.7068842: 28.0,
    0.7131691091: 28.5,
    0.7193991: 29.0,
    0.7255756136: 29.5,
    0.7317: 30.0,
    0.7347410093: 30.5,
    0.7377695: 31.0,
    0.7407855938: 31.5,
    0.74378943: 32.0,
    0.7467812109: 32.5,
    0.74976104: 33.0,
    0.7527290867: 33.5,
    0.7556855: 34.0,
    0.7586303683: 34.5,
    0.76156384: 35.0,
    0.7644860647: 35.5,
    0.76739717: 36.0,
    0.7702972656: 36.5,
    0.7731865: 37.0,
    0.7760649616: 37.5,
    0.77893275: 38.0,
    0.7817900548: 38.5,
    0.784637: 39.0,
    0.7874736075: 39.5,
    0.7903: 40.0,
    0.792803968: 40.5,
    0.79530001: 41.0,
    0.797800015: 41.5,
    0.8003: 42.0,
    0.802799995: 42.5,
    0.8053: 43.0,
    0.8078: 43.5,
    0.81029999: 44.0,
    0.812799985: 44.5,
    0.81529999: 45.0,
    0.81779999: 45.5,
    0.82029999: 46.0,
    0.82279999: 46.5,
    0.82529999: 47.0,
    0.82779999: 47.5,
    0.83029999: 48.0,
    0.83279999: 48.5,
    0.83529999: 49.0,
    0.83779999: 49.5,
    0.84029999: 50.0,
    0.842803729: 50.5,
    0.8453000188: 51.0,
}

standard_mult = sorted(mult_dict.iteritems())
buddy_mult = sorted(mult_dict_buddy.iteritems())

output = {}

######################################################### SETTINGS ###############################################################

# Mainly for debugging. Turn everything to False before running.
verbose = True
debug = False
print_optimal = False

spip_print = [
    "bulbasaur",
    "charmander",
    "squirtle",
    "pidgey",
    "rattata",
    "ekans",
    "sandshrew",
    "clefairy",
    "vulpix",
    "jigglypuff",
    "zubat",
    "paras",
    "psyduck",
    "abra",
    "bellsprout",
    "geodude",
    "ponyta",
    "seel",
    "gastly",
    "drowzee",
    "krabby",
    "voltorb",
    "cubone",
    "hitmonchan",
    "hitmonlee",
    "lickitung",
    "koffing",
    "rhyhorn",
    "chansey",
    "tangela",
    "goldeen",
    "staryu",
    "scyther",
    "jynx",
    "electabuzz",
    "magmar",
    "pinsir",
    "lapras",
    "omanyte",
    "kabuto",
    "aerodactyl",
    "snorlax",
    "dratini",
    "chikorita",
    "cyndaquil",
    "totodile",
    "togetic",
    "mareep",
    "yanma",
    "girafarig",
    "pineco",
    "dunsparce",
    "qwilfish",
    "sneasel",
    "houndour",
    "phanpy",
    "stantler",
    "hitmontop",
    "miltank",
    "larvitar",
    "treecko",
    "mudkip",
    "zigzagoon",
    "wurmple",
    "lotad",
    "wingull",
    "ralts",
    "surskit",
    "shroomish",
    "slakoth",
    "nincada",
    "mawile",
    "carvanha",
    "wailmer",
    "spoink",
    "trapinch",
    "cacnea",
    "solrock",
    "corphish",
    "lileep",
    "anorith",
    "feebas",
    "castform",
    "duskull",
    "chimecho",
    "absol",
    "spheal",
    "clamperl",
    "bagon",
    "beldum",
    "turtwig",
    "chimchar",
    "piplup",
    "kricketot",
    "cranidos",
    "shieldon",
    "shellos",
    "glameow",
    "stunky",
    "gible",
    "hippopotas",
    "Skorupi",
    "snover",
    "snivy",
    "tepig",
    "oshawott",
    "panpour",
    "ferroseed",
    "litwick",
    "golett",
    "deino",
]
spip_print = map(lambda x: x.lower(), spip_print)
spip_print = []

# Include mega evolutions
megas = True
# Cuts the number of pokemon rankings for mons below a certain pokedex number in half if set to true
new_focus = False
# Sets the number to cut rankings at - set to cut gen 1-4 now
focus_num = 495

# settings for great league rankings

# Attack weighted pokemon to output
atkw_g = [
    389,
    282,
    468,
    475,
    210,
    232,
    614,
    36,
    576,
    40,
    549,
    547,
    510,
    26,
    573,
    192,
    44,
    315,
    2,
    388,
    421,
    357,
    275,
    460,
    71,
    272,
    182,
    45,
    542,
    154,
    407,
    470,
    97,
    334,
    634,
    560,
    594,
    411,
]
# Build up a list of attack weights for pokemon
atkw = False
# Build up a list of buddy weights for pokemon
bdw = True
# always output these pokemon (by pokedex id number)
whitelist_g = [202]
# output a limited amount of these
greylist_g = [
    315,
    407,
    422,
    423,
    396,
    397,
    398,
    519,
    520,
    521,
    304,
    305,
    306,
    21,
    22,
    48,
    49,
    74,
    75,
    76,
    16,
    17,
    18,
    265,
    266,
    267,
    268,
    269,
    10,
    11,
    12,
    307,
    308,
    111,
    112,
    464,
    283,
    284,
    293,
    294,
    295,
    23,
    24,
    190,
    424,
    311,
    336,
    427,
    428,
    41,
    42,
    169,
    509,
    510,
    109,
    110,
    69,
    70,
    71,
    13,
    14,
    15,
    276,
    277,
    300,
    301,
    128,
    117,
    118,
    56,
    57,
    52,
    53,
    161,
    162,
    529,
    263,
    264,
    37,
    38,
    399,
    400,
    331,
    332,
    351,
    421,
    19,
    20,
    200,
    201,
    425,
    426,
    355,
    356,
    261,
    262,
    58,
    59,
    198,
    199,
    228,
    229,
    25,
    26,
    353,
    354,
    92,
    93,
    94,
    504,
    505,
    506,
    507,
    508,
    216,
    217,
    191,
    192,
    322,
    323,
    333,
    334,
    218,
    219,
    316,
    317,
    278,
    279,
    422,
    423,
    420,
    421,
    351,
    406,
    407,
    315,
    51,
    1,
    2,
    4,
    5,
    7,
    8,
    338,
    77,
    78,
    152,
    153,
    155,
    156,
    158,
    159,
    161,
    162,
    177,
    178,
    189,
    200,
    220,
    221,
    252,
    253,
    255,
    256,
    258,
    259,
    262,
    277,
    284,
    286,
    288,
    287,
    295,
    297,
    340,
    372,
    387,
    388,
    390,
    391,
    392,
    393,
    394,
    395,
    400,
    402,
    428,
    428,
    429,
    460,
]
# Community day IDs: 149, 3, 6, 9, 181, 248, 134, 135, 136, 196, 197, 470, 471, 154, 157, 160, 376, 473, 373, 289, 254, 257, 260, 282, 475, 389, 292, 395, 330, 497, 500, 503
# never output these
blacklist_g = []
# never output non-whitelisted mons with a max cp below this
min_cp_g = 1220
# maximum number of results for a standard mon
maxr_g = 50
# maximum results for mons that cap under the league's CP limit
medr_g = 50
# maximum results for mons that are greylisted
medg_g = 5
# maximum results for greylisted mons and reallllly low cp mons still above the minimum
minr_g = 5

# settings for ultra league rankings

# always output these pokemon (by pokedex id number)
whitelist_u = []
# output a limited amount of these
greylist_u = []
# never output these
blacklist_u = []
# never output non-whitelisted mons with a max cp below this
min_cp_u = 2350
# maximum number of results for a standard mon
maxr_u = 50
# maximum results for mons that cap under the league's CP limit
medr_u = 50
# maximum results for greylisted mons and reallllly low cp mons still above the minimum
minr_u = 5

###############################################################################################################################

evo_map = {}

with open("pogo-mon-data.json") as json_file:
    data = json.load(json_file)
    for p in data:
        mon = p["name"]
        evos = p["evolutions"]
        for evo in evos:
            if not evo in evo_map:
                evo_map[evo] = []
            evo_map[evo].append(mon)
        if not mon in evo_map:
            evo_map[mon] = []
        evo_map[mon].append(mon)

pbuffer = []


def print_optimal(mon, data, evo_map, print_optimal):
    if not print_optimal:
        return
    for base in evo_map[mon]:
        if (
            base.lower() in spip_print
            or (
                data["lvl"] > 41.0
                and (data["atkv"] != 15 or data["defv"] != 15 or data["stav"] != 15)
            )
            or ("mega " in mon.lower() and megas == True)
        ):
            if "mega " in base.lower():
                continue
            if (
                data["lvl"] > 40.0
                and data["atkv"] == 15
                and data["defv"] == 15
                and data["stav"] == 14
            ):
                data["stav"] = 15
                if debug == False:
                    continue
            plvl = int(data["lvl"])
            plvl = str(plvl) if plvl <= 35 else "35"
            text = ""
            # text = p['name'] + ' | Level: ' + str(data['lvl']) + ' | IVs: ' + str(data['atkv']) + ' ' + str(data['defv']) + ' ' + str(data['stav'])
            # text = '!addpokemon <'+base+'> <1L,'+plvl+'L> <'+str(data['atkv'])+'a,'+str(data['atkv'])+'a> <'+str(data['defv'])+'d,'+str(data['defv'])+'d> <'+str(data['stav'])+'s,'+str(data['stav'])+'s> all'
            if text not in pbuffer:
                pbuffer.append(text)
                print(text)


if __name__ == "__main__":
    with open("pogo-mon-data.json") as json_file:
        data = json.load(json_file)
        for p in data:
            batk = int(p["atk"])
            bdef = int(p["def"])
            bsta = int(p["sta"])
            num = int(p["id"])
            evos = p["evolutions"]

            max_cp = int(
                0.6245741058 * (batk + 15) * math.sqrt((bdef + 15) * (bsta + 15)) / 10
            )
            buddy_max_cp = int(
                0.66471407369 * (batk + 15) * math.sqrt((bdef + 15) * (bsta + 15)) / 10
            )
            if buddy_max_cp < min_cp_g and not int(num) in whitelist_g:
                if verbose:
                    print("Skip: " + p["name"] + " | Max CP: " + str(buddy_max_cp))
                continue

            gl_out = []
            glb_out = []
            ul_out = []
            aw_processing = []
            for atkiv in range(16):
                for defiv in range(16):
                    for staiv in range(16):

                        glvl = 0
                        gl_mult = math.sqrt(
                            (
                                15010.0
                                / (batk + atkiv)
                                / math.sqrt((bdef + defiv) * (bsta + staiv))
                            )
                        )
                        for mult, lvl in standard_mult:
                            if mult > gl_mult:
                                break
                            glvl = lvl
                            gmult = mult

                        ghp = max(10, int(gmult * (staiv + bsta)))
                        atkval = float(gmult * (atkiv + batk))
                        mon_sp = float(
                            (gmult ** 2) * (atkiv + batk) * (defiv + bdef) * ghp
                        )
                        ivcomb = atkiv + staiv + defiv + glvl

                        gl_out.append(
                            {
                                "mult": gmult,
                                "atkv": atkiv,
                                "defv": defiv,
                                "stav": staiv,
                                "lvl": glvl,
                                "atkval": atkval,
                                "sp": mon_sp,
                                "ivcomb": ivcomb,
                            }
                        )

                        aw_processing.append(
                            {
                                "atkval": atkval,
                                "sp": mon_sp,
                                "atkv": atkiv,
                                "defv": defiv,
                                "stav": staiv,
                                "lvl": glvl,
                                "ivcomb": ivcomb,
                            }
                        )

                        if bdw and glvl > 30.0:
                            glvl = 0
                            gl_mult = math.sqrt(
                                (
                                    15010.0
                                    / (batk + atkiv)
                                    / math.sqrt((bdef + defiv) * (bsta + staiv))
                                )
                            )
                            for mult, lvl in buddy_mult:
                                if mult > gl_mult:
                                    break
                                glvl = lvl
                                gmult = mult
                            ghp = max(10, int(gmult * (staiv + bsta)))
                            atkval = float(gmult * (atkiv + batk))
                            mon_sp = float(
                                (gmult ** 2) * (atkiv + batk) * (defiv + bdef) * ghp
                            )
                            ivcomb = atkiv + staiv + defiv + glvl

                            glb_out.append(
                                {
                                    "mult": gmult,
                                    "atkv": atkiv,
                                    "defv": defiv,
                                    "stav": staiv,
                                    "lvl": glvl,
                                    "atkval": atkval,
                                    "sp": mon_sp,
                                    "ivcomb": ivcomb,
                                }
                            )

                        if buddy_max_cp > 2300:
                            ulvl = 0
                            ul_mult = 0.094
                            ul_mult = math.sqrt(
                                (
                                    25010.0
                                    / (batk + atkiv)
                                    / math.sqrt((bdef + defiv) * (bsta + staiv))
                                )
                            )
                            for mult, lvl in buddy_mult:
                                if mult > ul_mult:
                                    break
                                ulvl = lvl
                                umult = mult

                            uhp = max(10, int(umult * (staiv + bsta)))
                            atkval = float(umult * (atkiv + batk))
                            mon_sp = float(
                                (umult ** 2) * (atkiv + batk) * (defiv + bdef) * uhp
                            )
                            ivcomb = atkiv + staiv + defiv + ulvl

                            ul_out.append(
                                {
                                    "sp": mon_sp,
                                    "atkval": atkval,
                                    "atkv": atkiv,
                                    "defv": defiv,
                                    "stav": staiv,
                                    "lvl": ulvl,
                                    "ivcomb": ivcomb,
                                }
                            )

            form = (
                "unset"
                if not "(" in p["name"]
                else p["name"][p["name"].find("(") + 1 : p["name"].find(")")]
            )
            output[p["name"]] = []
            out = sorted(
                gl_out, key=lambda x: (x["sp"], x["atkval"], x["ivcomb"]), reverse=True
            )
            i = 0
            min_norm = 1600
            min_low = 1500
            max_sp = out[0]
            lim = maxr_g
            lim = medr_g if int(num) in whitelist_g or max_sp < 1700000.0 else lim
            lim = (
                medg_g
                if buddy_max_cp < min_norm
                or int(num) in greylist_g
                or max_sp < 1500000.0
                else lim
            )
            lim = minr_g if buddy_max_cp < min_low else lim
            if new_focus:
                lim = lim / 2 if num < focus_num else lim
            if lim < maxr_g and verbose:
                print("Limited: " + p["name"] + " | Ranks: " + str(lim))
            last_sp = 0.0
            last_atk = 0.0
            for data in out:
                if i == 0:
                    print_optimal(p["name"], data, evo_map, print_optimal)
                if i >= lim:
                    break
                elif last_sp != data["sp"] or last_atk != data["atkval"]:
                    i += 1
                last_sp = data["sp"]
                last_atk = data["atkval"]

                output[p["name"]].append(
                    {
                        "id": num,
                        "form": form,
                        "mode": "great",
                        "type": "stat-product",
                        "rank": i,
                        "ivs": [data["atkv"], data["defv"], data["stav"]],
                        "maxlevel": data["lvl"],
                        "evolutions": evos,
                    }
                )

            if atkw and int(num) in atkw_g:
                i = 0
                out = sorted(
                    aw_processing,
                    key=lambda x: (x["atkval"], x["sp"], x["ivcomb"]),
                    reverse=True,
                )
                last_sp = 0.0
                last_atk = 0.0
                for data in out:
                    if (
                        i == 0
                        and data["atkv"] >= 14
                        and data["defv"] >= 14
                        and data["stav"] >= 14
                    ):
                        break
                    if i >= lim:
                        break
                    elif last_sp != data["sp"] or last_atk != data["atkval"]:
                        i += 1
                    last_sp = data["sp"]
                    last_atk = data["atkval"]
                    output[p["name"]].append(
                        {
                            "id": num,
                            "form": form,
                            "mode": "great",
                            "type": "attack",
                            "rank": i,
                            "ivs": [data["atkv"], data["defv"], data["stav"]],
                            "maxlevel": data["lvl"],
                            "evolutions": evos,
                        }
                    )

            if bdw:
                lim = 5
                i = 0
                out = sorted(
                    glb_out,
                    key=lambda x: (x["sp"], x["atkval"], x["ivcomb"]),
                    reverse=True,
                )
                last_sp = 0.0
                last_atk = 0.0
                for data in out:
                    if data["lvl"] > 50.0 and i == 0 and debug:
                        cp = int(
                            data["mult"]
                            * data["mult"]
                            * (batk + data["atkv"])
                            * math.sqrt((bdef + data["defv"]) * (bsta + data["stav"]))
                            / 10
                        )
                        color = (
                            "red"
                            if data["atkv"] == 15
                            and data["defv"] == 15
                            and data["stav"] == 15
                            else "cyan"
                        )
                        color = (
                            "magenta"
                            if float(int(data["lvl"])) != data["lvl"]
                            else color
                        )
                        print(
                            colored(
                                p["name"]
                                + " | Level: "
                                + str(data["lvl"])
                                + " | CP: "
                                + str(cp)
                                + " | IVs: "
                                + str(data["atkv"])
                                + " "
                                + str(data["defv"])
                                + " "
                                + str(data["stav"]),
                                color,
                            )
                        )
                    if i == 0:
                        if (
                            verbose
                            and data["atkv"] >= 10
                            and data["defv"] >= 12
                            and data["stav"] >= 12
                            and data["lvl"] >= 42.0
                        ):
                            cp = int(
                                data["mult"]
                                * data["mult"]
                                * (batk + data["atkv"])
                                * math.sqrt(
                                    (bdef + data["defv"]) * (bsta + data["stav"])
                                )
                                / 10
                            )
                            print(
                                str(data["lvl"])
                                + ": "
                                + p["name"]
                                + " | "
                                + str(cp)
                                + " | IVs: "
                                + str(data["atkv"])
                                + " "
                                + str(data["defv"])
                                + " "
                                + str(data["stav"])
                            )
                        if (
                            data["atkv"] == 15
                            and data["defv"] == 15
                            and data["stav"] == 15
                        ) or data["lvl"] <= 50.0:
                            break
                        if verbose:
                            print("Buddy Rankings: " + p["name"])
                        print_optimal(p["name"], data, evo_map, print_optimal)
                    if i >= lim:
                        break
                    elif last_sp != data["sp"] or last_atk != data["atkval"]:
                        i += 1
                    last_sp = data["sp"]
                    last_atk = data["atkval"]
                    output[p["name"]].append(
                        {
                            "id": num,
                            "form": form,
                            "mode": "great",
                            "type": "buddy",
                            "rank": i,
                            "ivs": [data["atkv"], data["defv"], data["stav"]],
                            "maxlevel": data["lvl"],
                            "evolutions": evos,
                        }
                    )

            if buddy_max_cp > min_cp_u:
                out = sorted(
                    ul_out,
                    key=lambda x: (x["sp"], x["atkval"], x["ivcomb"]),
                    reverse=True,
                )
                i = 0
                min_norm = 2600
                min_low = 2500
                lim = (
                    medr_u
                    if buddy_max_cp < min_norm or int(num) in whitelist_u
                    else maxr_u
                )
                lim = (
                    minr_u if buddy_max_cp < min_low or int(num) in greylist_u else lim
                )
                for data in out:
                    if i >= lim:
                        break
                    else:
                        i += 1
                    output[p["name"]].append(
                        {
                            "id": num,
                            "form": form,
                            "mode": "ultra",
                            "type": "stat-product",
                            "rank": i,
                            "ivs": [data["atkv"], data["defv"], data["stav"]],
                            "maxlevel": data["lvl"],
                            "evolutions": evos,
                        }
                    )

    with open("rankings.json", "w") as outfile:
        json.dump(output, outfile, indent=4, sort_keys=True)
