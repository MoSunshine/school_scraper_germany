# -*- coding: utf-8 -*-
"""

This script is used to scrape all schools from class 5-13 in baden_wuerttemberg based on the city id.

@author: Moritz Wegener, moritz.wegener@uni-koeln.de
"""
import requests
import pandas as pd
import json
###list of all city ids###
city_id_list = [790,356,190,316,1082,659,1012,77,317,424,116,425,301,78,711,1083,75,70,5,816,1084,852,79,952,754,156,791,1013,1014,956,157,564,32,33,6,34,509,957,1015,958,510,158,452,1085,924,959,1086,500,660,1118,182,117,285,960,1016,583,396,159,584,1087,160,817,85,1017,80,733,359,586,191,518,585,511,286,661,192,579,872,1137,384,1018,532,81,901,1088,530,193,1089,634,1090,565,1091,756,928,961,587,35,1009,453,755,318,194,962,36,118,1092,1093,662,963,183,1019,1058,853,964,119,1020,37,1122,663,1021,635,397,152,426,427,1123,818,82,535,398,929,38,930,965,254,1010,734,319,7,912,812,1094,83,819,589,1095,8,854,120,320,966,84,712,757,588,287,195,735,255,590,967,591,363,237,752,364,454,758,592,428,759,593,399,400,256,257,1022,161,931,792,533,196,258,288,855,1059,736,932,9,1080,86,760,731,39,40,761,636,913,394,856,885,1023,41,455,968,713,304,121,512,857,737,87,933,714,969,566,238,456,934,88,715,664,762,763,321,1024,401,1025,89,914,1096,457,122,1026,90,1117,197,513,594,503,820,514,764,386,879,970,10,630,1097,595,793,821,596,536,91,402,322,198,323,637,449,971,972,638,788,567,639,537,794,906,886,515,458,716,459,199,973,123,1060,42,200,1027,124,1028,1029,324,597,730,460,92,325,43,665,365,568,429,598,162,281,259,71,666,822,201,1098,729,403,640,239,366,282,655,151,581,289,569,125,44,1061,765,599,1062,667,538,766,823,1120,738,404,461,795,260,796,93,1124,11,12,516,767,935,94,202,126,668,261,127,405,305,306,95,570,600,326,887,915,367,96,858,768,601,797,383,888,30,889,859,848,974,571,45,128,936,163,290,97,975,1099,291,327,1100,203,602,204,769,641,669,739,1056,849,1063,937,517,368,430,717,234,603,824,670,431,98,671,976,938,825,770,860,890,939,462,463,420,307,188,1064,464,539,99,604,504,129,465,1125,642,308,1146,309,1008,13,861,130,1126,328,329,605,14,798,606,916,505,1030,46,862,466,519,672,673,810,100,907,1127,863,15,977,47,432,572,607,1119,674,1101,433,740,406,891,978,330,864,407,292,331,608,1006,979,540,1128,205,262,467,771,1065,240,150,1031,1129,826,772,1102,541,206,207,332,865,29,940,164,560,827,1032,708,675,381,387,361,676,556,643,186,468,542,677,208,1033,263,165,1034,917,131,333,48,609,1103,850,866,543,50,774,49,293,562,310,1104,741,773,799,166,153,132,382,1130,241,280,1066,369,101,294,242,243,408,370,880,918,469,678,980,1067,981,235,264,1035,334,867,302,470,680,868,209,1036,679,982,718,114,210,1131,471,72,211,335,73,610,16,167,1105,409,909,51,434,388,502,133,410,611,983,336,828,573,869,212,134,17,681,775,265,847,371,472,644,422,135,631,1068,136,372,1037,213,473,544,829,1069,474,1070,892,682,1132,612,984,613,1133,941,893,266,267,1038,1039,214,337,137,742,545,800,1040,435,919,18,436,411,546,683,475,811,102,776,801,244,614,138,985,894,629,870,139,168,338,520,311,476,477,437,215,52,53,216,438,986,920,478,54,987,988,339,521,217,547,615,218,245,55,1134,548,56,777,1071,340,559,479,439,707,925,522,743,246,295,312,549,219,684,57,19,58,942,480,59,373,989,341,685,390,686,342,990,719,943,523,616,140,268,269,991,141,233,1072,687,440,1041,220,221,688,921,481,1042,689,60,802,247,561,992,993,690,169,813,691,524,441,74,1135,374,412,550,103,692,413,61,1073,222,617,574,248,385,507,895,1136,896,375,482,142,897,62,170,803,357,994,944,414,945,483,1106,446,104,995,484,804,778,63,485,557,154,184,693,20,779,645,898,709,830,654,418,391,871,899,1107,1043,646,814,355,787,694,525,223,905,343,442,946,279,270,1044,996,922,720,171,831,344,695,21,149,105,1074,486,696,647,697,271,1145,832,620,345,1138,447,997,1055,721,722,64,106,833,1108,107,621,998,947,526,746,22,487,834,488,835,249,745,836,575,172,723,489,272,698,699,346,273,224,173,706,448,1045,1139,490,143,837,443,700,1046,701,577,786,144,999,648,225,1140,1141,527,528,649,23,805,491,415,1075,622,908,313,780,492,174,347,1007,926,623,873,624,702,838,24,1047,314,145,416,806,551,1076,1142,744,283,910,501,618,807,348,619,948,558,874,392,3,724,175,274,625,376,108,349,226,781,146,350,1048,296,808,650,1077,1049,552,626,875,839,747,900,782,923,840,748,783,1078,377,109,1079,883,954,627,1050,1051,227,65,228,749,1000,275,529,351,1001,1002,1109,176,1052,841,147,276,1143,725,751,1110,632,750,726,809,651,389,177,493,1053,1144,578,393,450,1111,904,25,250,657,881,352,148,494,444,277,378,111,1112,902,1054,110,784,876,1003,297,842,26,949,877,66,27,1113,379,495,229,185,417,28,178,251,652,727,179,843,67,298,68,299,1004,1005,353,230,844,553,496,112,497,531,1114,498,703,554,656,180,181,950,300,845,628,704,1115,69,278,1116,576,354,555,785,231,882,878,653,232,380,705,846,113,728,951,499,252,903,445]
###empty lists for results###
result_list = []
result_id = []
###loop over all cities###
for city_id in city_id_list:
   ###combine predefined url with filter with the city id###
   url = "https://schulfinder.kultus-bw.de/api/schools?branches=&city%5B%5D="+str(city_id)+"&distance=&district=&outposts=1&owner=&school_kind=1%2C2%2C3%2C4%2C5%2C6%2C7&term=&trades=&types=3%2C16%2C15&work_schedule=&tablet_tranche=&_=1642083022528"
   ###get results for each city in json format and extract for each school the data###
   page = requests.get(url).text
   json_array = json.loads(page)
   for i in range(len(json_array)):
       json_object = json_array[i]
       school_id = json_object["uuid"]
       name = json_object["name"]
       city = json_object["city"]
       lat = json_object["lat"]
       lng = json_object["lng"]
       if school_id not in result_id:
           result_id.append(school_id)
           result_list.append({"school_id":school_id,"name":name,"city":city,"lat":lat,"lng":lng})
###save results as csv file###
result = pd.DataFrame(result_list)    
result.to_csv("../results/db_baden_wuerttemberg.csv",encoding="utf-8",sep=",",index=False)
   