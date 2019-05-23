from input import *
from helper import *
from allocation import *
from input import *

import random
import math

class Chromosome:

    def __init__(self, gene):
        self.gene = gene
    
    def mutate(self, probM):
        new_gene = self.gene



        return new_gene

        
    
    def fitness(self):
        return #value(self.gene)

#test solution as gene
s = []
slot = Slot(0)
slot.distribution = {162: 2, 225: 4, 365: 9, 100: 8,
                   131: 0, 205: 3, 222: 7, 144: 1, 46: 6, 339: 5}
s.append(slot)

slot = Slot(1)
slot.distribution = {270: 2, 104: 4, 391: 0, 227: 3,
                   176: 8, 337: 1, 193: 7, 279: 9, 68: 6, 39: 5}
s.append(slot)

slot = Slot(2)
slot.distribution = {147: 2, 381: 4, 247: 0, 276: 8,
                   48: 5, 14: 1, 356: 3, 226: 6, 208: 9, 99: 7}
s.append(slot)

slot = Slot(3)
slot.distribution = {32: 2, 142: 4, 265: 6, 2: 8,
                   267: 5, 145: 3, 340: 9, 342: 1, 361: 0, 302: 7}
s.append(slot)

slot = Slot(4)
slot.distribution = {282: 2, 115: 4, 269: 1, 395: 0,
                   125: 7, 243: 3, 128: 8, 179: 6, 275: 5, 187: 9}
s.append(slot)

slot = Slot(5)
slot.distribution = {177: 2, 347: 4, 264: 6, 80: 3,
                   112: 9, 291: 5, 360: 8, 155: 1, 362: 0, 232: 7}
s.append(slot)

slot = Slot(6)
slot.distribution = {250: 2, 9: 4, 252: 3, 308: 1,
                   4: 6, 239: 9, 16: 5, 297: 8, 42: 0, 195: 7}
s.append(slot)

slot = Slot(7)
slot.distribution = {54: 2, 93: 4, 30: 3, 234: 9,
                   173: 1, 189: 5, 194: 6, 336: 8, 392: 0, 263: 7}
s.append(slot)

slot = Slot(8)
slot.distribution = {44: 2, 12: 4, 278: 8, 320: 9,
                   191: 3, 152: 6, 129: 1, 383: 0, 318: 5, 217: 7}
s.append(slot)

slot = Slot(9)
slot.distribution = {260: 2, 64: 4, 219: 7, 127: 6,
                   134: 8, 295: 0, 167: 3, 114: 1, 249: 5, 368: 9}
s.append(slot)

slot = Slot(10)
slot.distribution = {307: 2, 259: 4, 23: 6, 371: 3,
                   236: 1, 79: 0, 111: 5, 52: 9, 345: 8, 233: 7}
s.append(slot)

slot = Slot(11)
slot.distribution = {0: 2, 149: 4, 59: 0, 359: 3,
                   379: 9, 132: 1, 220: 8, 26: 5, 103: 6, 210: 7}
s.append(slot)

slot = Slot(12)
slot.distribution = {296: 2, 49: 4, 197: 1, 305: 8,
                   280: 3, 118: 7, 300: 9, 98: 5, 386: 0, 24: 6}
s.append(slot)

slot = Slot(13)
slot.distribution = {353: 2, 322: 4, 242: 5, 95: 6,
                   178: 9, 186: 7, 209: 3, 398: 1, 201: 0, 292: 8}
s.append(slot)

slot = Slot(14)
slot.distribution = {81: 2, 202: 4, 223: 9, 348: 6,
                   258: 3, 183: 1, 330: 8, 283: 5, 394: 0, 139: 7}
s.append(slot)

slot = Slot(15)
slot.distribution = {218: 2, 133: 4, 248: 6, 343: 3,
                   352: 8, 372: 9, 294: 0, 393: 1, 253: 7, 25: 5}
s.append(slot)

slot = Slot(16)
slot.distribution = {96: 2, 69: 4, 34: 5, 90: 8,
                   35: 3, 40: 9, 50: 1, 358: 7, 47: 0, 102: 6}
s.append(slot)

slot = Slot(17)
slot.distribution = {158: 2, 164: 4, 224: 1, 245: 8,
                   10: 5, 397: 0, 3: 3, 57: 6, 357: 9, 290: 7}
s.append(slot)

slot = Slot(18)
slot.distribution = {150: 2, 229: 4, 109: 3, 230: 8,
                   62: 1, 366: 9, 287: 7, 65: 5, 388: 0, 344: 6}
s.append(slot)

slot = Slot(19)
slot.distribution = {256: 2, 105: 4, 301: 7,
                   306: 3, 281: 1, 377: 9, 204: 8, 17: 0, 216: 5}
s.append(slot)

slot = Slot(20)
slot.distribution = {174: 2, 92: 4, 151: 8, 246: 7,
                   123: 3, 136: 1, 163: 9, 27: 5, 141: 6, 56: 0}
s.append(slot)

slot = Slot(21)
slot.distribution = {41: 2, 268: 4, 83: 3, 22: 5,
                   241: 1, 184: 8, 159: 6, 228: 9, 120: 7, 200: 0}
s.append(slot)

slot = Slot(22)
slot.distribution = {122: 2, 29: 4, 154: 3, 323: 8,
                   13: 5, 387: 1, 333: 9, 86: 7, 84: 0, 171: 6}
s.append(slot)

slot = Slot(23)
slot.distribution = {60: 2, 374: 4, 272: 7, 58: 9,
                   182: 3, 349: 8, 156: 6, 328: 1, 389: 0, 327: 5}
s.append(slot)

slot = Slot(24)
slot.distribution = {119: 2, 87: 4, 160: 6, 284: 8,
                   31: 3, 293: 1, 326: 9, 106: 5, 138: 0}
s.append(slot)

slot = Slot(25)
slot.distribution = {21: 2, 75: 4, 369: 9, 288: 7,
                   43: 3, 196: 8, 85: 0, 140: 1, 18: 6, 77: 5}
s.append(slot)

slot = Slot(26)
slot.distribution = {6: 2, 346: 4, 89: 3, 231: 1,
                   53: 9, 319: 8, 67: 7, 36: 0, 311: 5}
s.append(slot)

slot = Slot(27)
slot.distribution = {19: 2, 143: 4, 262: 3, 370: 1,
                   335: 9, 153: 8, 157: 0, 82: 6, 277: 7, 199: 5}
s.append(slot)

slot = Slot(28)
slot.distribution = {137: 4, 271: 3, 78: 1, 97: 9, 71: 7, 61: 8, 1: 0, 8: 2}
s.append(slot)

slot = Slot(29)
slot.distribution = {165: 4, 113: 3, 76: 1, 166: 9,
                   304: 8, 382: 0, 289: 2, 203: 7, 285: 5}
s.append(slot)

slot = Slot(30)
slot.distribution = {390: 4, 148: 3, 310: 1, 350: 9,
                   126: 2, 312: 8, 341: 6, 207: 7, 88: 0, 130: 5}
s.append(slot)

slot = Slot(31)
slot.distribution = {38: 4, 355: 3, 168: 1, 172: 9,
                   261: 8, 396: 0, 251: 2, 181: 6, 237: 7, 299: 5}
s.append(slot)

slot = Slot(32)
slot.distribution = {169: 4, 367: 3, 221: 1, 66: 9,
                   185: 8, 286: 7, 384: 0, 317: 2, 206: 6}
s.append(slot)

slot = Slot(33)
slot.distribution = {121: 4, 107: 3, 266: 1, 376: 9,
                   108: 8, 273: 0, 63: 7, 170: 5, 325: 2, 213: 6}
s.append(slot)

slot = Slot(34)
slot.distribution = {28: 4, 20: 3, 214: 1, 378: 9,
                   124: 8, 364: 0, 175: 7, 309: 5, 334: 2}
s.append(slot)

slot = Slot(35)
slot.distribution = {192: 4, 70: 3, 240: 1, 298: 9,
                   316: 8, 313: 7, 180: 0, 161: 2, 257: 5}
s.append(slot)

slot = Slot(36)
slot.distribution = {188: 4, 5: 3, 73: 1, 329: 9, 354: 8, 91: 7, 215: 2}
s.append(slot)

slot = Slot(37)
slot.distribution = {399: 4, 55: 1, 254: 9, 7: 8,
                   255: 0, 324: 5, 303: 7, 33: 2, 101: 3}
s.append(slot)

slot = Slot(38)
slot.distribution = {373: 4, 11: 3, 51: 1, 375: 9,
                   314: 8, 235: 7, 45: 0, 116: 2, 321: 5}
s.append(slot)

slot = Slot(39)
slot.distribution = {135: 4, 244: 1, 274: 9, 315: 8, 37: 0, 117: 7, 338: 2}
s.append(slot)

slot = Slot(40)
slot.distribution = {385: 4, 198: 1, 380: 9, 94: 8, 110: 7, 190: 0}
s.append(slot)

slot = Slot(41)
slot.distribution = {72: 4, 332: 1, 211: 9, 212: 8, 363: 0, 74: 6}
s.append(slot)

slot = Slot(42)
slot.distribution = {238: 4, 351: 1, 331: 0, 146: 7, 15: 9}
s.append(slot)

slot = Slot(43)
slot.distribution = {}
s.append(slot)

slot = Slot(44)
slot.distribution = {}
s.append(slot)

c = Chromosome(s)
print('gene')
print(c.gene)
print('end gene')
