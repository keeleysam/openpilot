from cereal import car
from selfdrive.car import dbc_dict

gra_acc_buttons_dict = {
  "main": False,
  "set": False,
  "resume": False,
  "cancel": False,
  "accel": False,
  "decel": False,
  "timegap": False
}

class CAR:
  GENERICMQB = "Generic Volkswagen MQB Platform Vehicle"

# Mega-fingerprint used to identify any and all MQB platform vehicles. Specific
# make and model characteristics are looked up from the VIN later.
FINGERPRINTS = {
  CAR.GENERICMQB: [
    {178: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 695: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1122: 8, 1123: 8,
     1124: 8, 1646: 8, 1648: 8, 1153: 8, 134: 8, 1162: 8, 1175: 8, 159: 8, 795: 8, 679: 8, 681: 8, 173: 8, 1712: 6,
     1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8, 1312: 8, 806: 8, 253: 8, 1792: 8, 257: 8, 260: 8, 262: 8,
     897: 8, 264: 8, 779: 8, 780: 8, 783: 8, 278: 8, 279: 8, 792: 8, 283: 8, 285: 8, 286: 8, 901: 8, 288: 8, 289: 8,
     290: 8, 804: 8, 294: 8, 807: 8, 808: 8, 809: 8, 299: 8, 302: 8, 1351: 8, 346: 8, 870: 8, 1385: 8, 896: 8, 64: 8,
     898: 8, 1413: 8, 917: 8, 919: 8, 927: 8, 1440: 5, 929: 8, 930: 8, 427: 8, 949: 8, 958: 8, 960: 4, 418: 8, 981: 8,
     987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1514: 8, 1515: 8, 1520: 8, 1019: 8, 385:8, 668:8, 1120:8,
     1438:8, 1461:8, 391:1
     },
  ],
}


class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [294, 919],                    # HCA_01 Heading Control Assist, LDW_02 Lane Departure Warning
}

DBC = {
  CAR.GENERICMQB: dbc_dict('vw_mqb_2010', None),
}
