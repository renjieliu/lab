#using SQL to generate the dates and day number

# create table t (id int)
# insert into t select 1
# go
#
# insert into t select max(id)+1 from t
# go 365
#
#
# select hmp =  '"' +  cast (cast(dateadd(day, id-1, '2020-01-01') as date) as varchar) + '" : ['  + cast(id as varchar) + ','  +
# cast(MONTH(cast(dateadd(day, id-1, '2020-01-01') as date)) as varchar ) + '' + cast(Day(cast(dateadd(day, id-1, '2020-01-01') as date)) as varchar)
# + '],'
# from t

def isPrime(n):
    if n in [1, 2]:
        return 1
    for i in range(2, int(n**0.5+1)):
        if n%i==0:
            return 0
    return 1

def isPrimeDate(hmp):
    output = {}
    for k,v in hmp.items():
        if isPrime(v[0]) and isPrime(v[1]):
            output[k] = ['Prime Day', v]
        elif isPrime(v[0]):
            output[k] = ['Day Number Prime', v]
        elif isPrime(v[1]):
            output[k] = ['Day itself Prime', v]
    return output

print(isPrimeDate({"2020-01-01" : [1,11], "2020-01-02" : [2,12], "2020-01-03" : [3,13], "2020-01-04" : [4,14], "2020-01-05" : [5,15], "2020-01-06" : [6,16], "2020-01-07" : [7,17], "2020-01-08" : [8,18], "2020-01-09" : [9,19], "2020-01-10" : [10,110], "2020-01-11" : [11,111], "2020-01-12" : [12,112], "2020-01-13" : [13,113], "2020-01-14" : [14,114], "2020-01-15" : [15,115], "2020-01-16" : [16,116], "2020-01-17" : [17,117], "2020-01-18" : [18,118], "2020-01-19" : [19,119], "2020-01-20" : [20,120], "2020-01-21" : [21,121], "2020-01-22" : [22,122], "2020-01-23" : [23,123], "2020-01-24" : [24,124], "2020-01-25" : [25,125], "2020-01-26" : [26,126], "2020-01-27" : [27,127], "2020-01-28" : [28,128], "2020-01-29" : [29,129], "2020-01-30" : [30,130], "2020-01-31" : [31,131], "2020-02-01" : [32,21], "2020-02-02" : [33,22], "2020-02-03" : [34,23], "2020-02-04" : [35,24], "2020-02-05" : [36,25], "2020-02-06" : [37,26], "2020-02-07" : [38,27], "2020-02-08" : [39,28], "2020-02-09" : [40,29], "2020-02-10" : [41,210], "2020-02-11" : [42,211], "2020-02-12" : [43,212], "2020-02-13" : [44,213], "2020-02-14" : [45,214], "2020-02-15" : [46,215], "2020-02-16" : [47,216], "2020-02-17" : [48,217], "2020-02-18" : [49,218], "2020-02-19" : [50,219], "2020-02-20" : [51,220], "2020-02-21" : [52,221], "2020-02-22" : [53,222], "2020-02-23" : [54,223], "2020-02-24" : [55,224], "2020-02-25" : [56,225], "2020-02-26" : [57,226], "2020-02-27" : [58,227], "2020-02-28" : [59,228], "2020-02-29" : [60,229], "2020-03-01" : [61,31], "2020-03-02" : [62,32], "2020-03-03" : [63,33], "2020-03-04" : [64,34], "2020-03-05" : [65,35], "2020-03-06" : [66,36], "2020-03-07" : [67,37], "2020-03-08" : [68,38], "2020-03-09" : [69,39], "2020-03-10" : [70,310], "2020-03-11" : [71,311], "2020-03-12" : [72,312], "2020-03-13" : [73,313], "2020-03-14" : [74,314], "2020-03-15" : [75,315], "2020-03-16" : [76,316], "2020-03-17" : [77,317], "2020-03-18" : [78,318], "2020-03-19" : [79,319], "2020-03-20" : [80,320], "2020-03-21" : [81,321], "2020-03-22" : [82,322], "2020-03-23" : [83,323], "2020-03-24" : [84,324], "2020-03-25" : [85,325], "2020-03-26" : [86,326], "2020-03-27" : [87,327], "2020-03-28" : [88,328], "2020-03-29" : [89,329], "2020-03-30" : [90,330], "2020-03-31" : [91,331], "2020-04-01" : [92,41], "2020-04-02" : [93,42], "2020-04-03" : [94,43], "2020-04-04" : [95,44], "2020-04-05" : [96,45], "2020-04-06" : [97,46], "2020-04-07" : [98,47], "2020-04-08" : [99,48], "2020-04-09" : [100,49], "2020-04-10" : [101,410], "2020-04-11" : [102,411], "2020-04-12" : [103,412], "2020-04-13" : [104,413], "2020-04-14" : [105,414], "2020-04-15" : [106,415], "2020-04-16" : [107,416], "2020-04-17" : [108,417], "2020-04-18" : [109,418], "2020-04-19" : [110,419], "2020-04-20" : [111,420], "2020-04-21" : [112,421], "2020-04-22" : [113,422], "2020-04-23" : [114,423], "2020-04-24" : [115,424], "2020-04-25" : [116,425], "2020-04-26" : [117,426], "2020-04-27" : [118,427], "2020-04-28" : [119,428], "2020-04-29" : [120,429], "2020-04-30" : [121,430], "2020-05-01" : [122,51], "2020-05-02" : [123,52], "2020-05-03" : [124,53], "2020-05-04" : [125,54], "2020-05-05" : [126,55], "2020-05-06" : [127,56], "2020-05-07" : [128,57], "2020-05-08" : [129,58], "2020-05-09" : [130,59], "2020-05-10" : [131,510], "2020-05-11" : [132,511], "2020-05-12" : [133,512], "2020-05-13" : [134,513], "2020-05-14" : [135,514], "2020-05-15" : [136,515], "2020-05-16" : [137,516], "2020-05-17" : [138,517], "2020-05-18" : [139,518], "2020-05-19" : [140,519], "2020-05-20" : [141,520], "2020-05-21" : [142,521], "2020-05-22" : [143,522], "2020-05-23" : [144,523], "2020-05-24" : [145,524], "2020-05-25" : [146,525], "2020-05-26" : [147,526], "2020-05-27" : [148,527], "2020-05-28" : [149,528], "2020-05-29" : [150,529], "2020-05-30" : [151,530], "2020-05-31" : [152,531], "2020-06-01" : [153,61], "2020-06-02" : [154,62], "2020-06-03" : [155,63], "2020-06-04" : [156,64], "2020-06-05" : [157,65], "2020-06-06" : [158,66], "2020-06-07" : [159,67], "2020-06-08" : [160,68], "2020-06-09" : [161,69], "2020-06-10" : [162,610], "2020-06-11" : [163,611], "2020-06-12" : [164,612], "2020-06-13" : [165,613], "2020-06-14" : [166,614], "2020-06-15" : [167,615], "2020-06-16" : [168,616], "2020-06-17" : [169,617], "2020-06-18" : [170,618], "2020-06-19" : [171,619], "2020-06-20" : [172,620], "2020-06-21" : [173,621], "2020-06-22" : [174,622], "2020-06-23" : [175,623], "2020-06-24" : [176,624], "2020-06-25" : [177,625], "2020-06-26" : [178,626], "2020-06-27" : [179,627], "2020-06-28" : [180,628], "2020-06-29" : [181,629], "2020-06-30" : [182,630], "2020-07-01" : [183,71], "2020-07-02" : [184,72], "2020-07-03" : [185,73], "2020-07-04" : [186,74], "2020-07-05" : [187,75], "2020-07-06" : [188,76], "2020-07-07" : [189,77], "2020-07-08" : [190,78], "2020-07-09" : [191,79], "2020-07-10" : [192,710], "2020-07-11" : [193,711], "2020-07-12" : [194,712], "2020-07-13" : [195,713], "2020-07-14" : [196,714], "2020-07-15" : [197,715], "2020-07-16" : [198,716], "2020-07-17" : [199,717], "2020-07-18" : [200,718], "2020-07-19" : [201,719], "2020-07-20" : [202,720], "2020-07-21" : [203,721], "2020-07-22" : [204,722], "2020-07-23" : [205,723], "2020-07-24" : [206,724], "2020-07-25" : [207,725], "2020-07-26" : [208,726], "2020-07-27" : [209,727], "2020-07-28" : [210,728], "2020-07-29" : [211,729], "2020-07-30" : [212,730], "2020-07-31" : [213,731], "2020-08-01" : [214,81], "2020-08-02" : [215,82], "2020-08-03" : [216,83], "2020-08-04" : [217,84], "2020-08-05" : [218,85], "2020-08-06" : [219,86], "2020-08-07" : [220,87], "2020-08-08" : [221,88], "2020-08-09" : [222,89], "2020-08-10" : [223,810], "2020-08-11" : [224,811], "2020-08-12" : [225,812], "2020-08-13" : [226,813], "2020-08-14" : [227,814], "2020-08-15" : [228,815], "2020-08-16" : [229,816], "2020-08-17" : [230,817], "2020-08-18" : [231,818], "2020-08-19" : [232,819], "2020-08-20" : [233,820], "2020-08-21" : [234,821], "2020-08-22" : [235,822], "2020-08-23" : [236,823], "2020-08-24" : [237,824], "2020-08-25" : [238,825], "2020-08-26" : [239,826], "2020-08-27" : [240,827], "2020-08-28" : [241,828], "2020-08-29" : [242,829], "2020-08-30" : [243,830], "2020-08-31" : [244,831], "2020-09-01" : [245,91], "2020-09-02" : [246,92], "2020-09-03" : [247,93], "2020-09-04" : [248,94], "2020-09-05" : [249,95], "2020-09-06" : [250,96], "2020-09-07" : [251,97], "2020-09-08" : [252,98], "2020-09-09" : [253,99], "2020-09-10" : [254,910], "2020-09-11" : [255,911], "2020-09-12" : [256,912], "2020-09-13" : [257,913], "2020-09-14" : [258,914], "2020-09-15" : [259,915], "2020-09-16" : [260,916], "2020-09-17" : [261,917], "2020-09-18" : [262,918], "2020-09-19" : [263,919], "2020-09-20" : [264,920], "2020-09-21" : [265,921], "2020-09-22" : [266,922], "2020-09-23" : [267,923], "2020-09-24" : [268,924], "2020-09-25" : [269,925], "2020-09-26" : [270,926], "2020-09-27" : [271,927], "2020-09-28" : [272,928], "2020-09-29" : [273,929], "2020-09-30" : [274,930], "2020-10-01" : [275,101], "2020-10-02" : [276,102], "2020-10-03" : [277,103], "2020-10-04" : [278,104], "2020-10-05" : [279,105], "2020-10-06" : [280,106], "2020-10-07" : [281,107], "2020-10-08" : [282,108], "2020-10-09" : [283,109], "2020-10-10" : [284,1010], "2020-10-11" : [285,1011], "2020-10-12" : [286,1012], "2020-10-13" : [287,1013], "2020-10-14" : [288,1014], "2020-10-15" : [289,1015], "2020-10-16" : [290,1016], "2020-10-17" : [291,1017], "2020-10-18" : [292,1018], "2020-10-19" : [293,1019], "2020-10-20" : [294,1020], "2020-10-21" : [295,1021], "2020-10-22" : [296,1022], "2020-10-23" : [297,1023], "2020-10-24" : [298,1024], "2020-10-25" : [299,1025], "2020-10-26" : [300,1026], "2020-10-27" : [301,1027], "2020-10-28" : [302,1028], "2020-10-29" : [303,1029], "2020-10-30" : [304,1030], "2020-10-31" : [305,1031], "2020-11-01" : [306,111], "2020-11-02" : [307,112], "2020-11-03" : [308,113], "2020-11-04" : [309,114], "2020-11-05" : [310,115], "2020-11-06" : [311,116], "2020-11-07" : [312,117], "2020-11-08" : [313,118], "2020-11-09" : [314,119], "2020-11-10" : [315,1110], "2020-11-11" : [316,1111], "2020-11-12" : [317,1112], "2020-11-13" : [318,1113], "2020-11-14" : [319,1114], "2020-11-15" : [320,1115], "2020-11-16" : [321,1116], "2020-11-17" : [322,1117], "2020-11-18" : [323,1118], "2020-11-19" : [324,1119], "2020-11-20" : [325,1120], "2020-11-21" : [326,1121], "2020-11-22" : [327,1122], "2020-11-23" : [328,1123], "2020-11-24" : [329,1124], "2020-11-25" : [330,1125], "2020-11-26" : [331,1126], "2020-11-27" : [332,1127], "2020-11-28" : [333,1128], "2020-11-29" : [334,1129], "2020-11-30" : [335,1130], "2020-12-01" : [336,121], "2020-12-02" : [337,122], "2020-12-03" : [338,123], "2020-12-04" : [339,124], "2020-12-05" : [340,125], "2020-12-06" : [341,126], "2020-12-07" : [342,127], "2020-12-08" : [343,128], "2020-12-09" : [344,129], "2020-12-10" : [345,1210], "2020-12-11" : [346,1211], "2020-12-12" : [347,1212], "2020-12-13" : [348,1213], "2020-12-14" : [349,1214], "2020-12-15" : [350,1215], "2020-12-16" : [351,1216], "2020-12-17" : [352,1217], "2020-12-18" : [353,1218], "2020-12-19" : [354,1219], "2020-12-20" : [355,1220], "2020-12-21" : [356,1221], "2020-12-22" : [357,1222], "2020-12-23" : [358,1223], "2020-12-24" : [359,1224], "2020-12-25" : [360,1225], "2020-12-26" : [361,1226], "2020-12-27" : [362,1227], "2020-12-28" : [363,1228], "2020-12-29" : [364,1229], "2020-12-30" : [365,1230], "2020-12-31" : [366,1231]}))
