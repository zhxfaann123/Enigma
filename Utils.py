"""
Utility definitions
"""
NAVALA_cycles = {"I": "(AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)",
                 "II": "(FIXVYOMW) (CDKLHUP) (ESZ) (BJ) (GR) (NT) (A) (Q)",
                 "III": "(ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)",
                 "IV": "(AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)",
                 "V": "(AVOLDRWFIUQ)(BZKSMNHYC) (EGTJPX)",
                 "VI": "(AJQDVLEOZWIYTS) (CGMNHFUX) (BPRK) ",
                 "VII": "(ANOUPFRIMBZTLWKSVEGCJYDHXQ) ",
                 "VIII": "(AFLSETWUNDHOZVICQ) (BKJ) (GXY) (MPR)",
                 "Beta": "(ALBEVFCYODJWUGNMQTZSKPR) (HIX)",
                 "Gamma": "(AFNIRLBSQWVXGUZDKMTPCOYJHE)",
                 "B": "(AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP) (RX) (SZ) (TV)",
                 "C": "(AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW) (QZ) (SX) (UY)",
                 }

NAVALA_type = {"I": "MQ",
               "II": "ME",
               "III": "MV",
               "IV": "MJ",
               "V": "MZ",
               "VI": "MZM",
               "VII": "MZN",
               "VIII": "MZM",
               "Beta": "N",
               "Gamma": "N",
               "B": "R",
               "C": "R",
               }

Default_Alphabet_String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Default_Num_Rotors = 5
Default_Num_Pawls = 3


def list2str(l: list):
    """
    Convert a list of char to str
    """
    string = ""
    for c in l:
        assert isinstance(c, str)
        string += c
    return string
