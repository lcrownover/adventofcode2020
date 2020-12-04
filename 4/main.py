#!/usr/bin/env python3

import re

LOG=False

def format_passports(indata):
    out = indata.replace(" ", "\n")
    out = out.split("\n\n")
    out = [e.replace("\n", ';').strip() for e in out]
    return out

def verify_passport(passport,extra_validation=True):
    ignore_missing_cid = True
    missing_fields = []
    valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    parsed_passport = {}
    fields = [field.strip() for field in passport.split(';') if field.strip() != '']
    for field in fields:
        k,v = field.split(':')
        parsed_passport[k] = v
    for vf in valid_fields:
        if ignore_missing_cid and vf == 'cid': continue
        if not vf in parsed_passport.keys():
            missing_fields.append(vf)
    if missing_fields:
        return False
    if not extra_validation:
        return True
    if validate_passport_fields(parsed_passport):
        if LOG: print('valid passport')
        return True
    return False

def validate_passport_fields(parsed_passport):
    validations = {
        'byr': v_byr,
        'iyr': v_iyr,
        'eyr': v_eyr,
        'hgt': v_hgt,
        'hcl': v_hcl,
        'ecl': v_ecl,
        'pid': v_pid,
        'cid': v_cid,
    }
    if LOG: print(parsed_passport)
    for k,v in parsed_passport.items():
        if not validations[k](v):
            return False
    return True


def v_byr(byr):
    if int(byr) >= 1920 and int(byr) <= 2020:
        if LOG: print('byr: pass')
        return True
    if LOG: print('byr: fail')
    return False

def v_iyr(iyr):
    if int(iyr) >= 2010 and int(iyr) <= 2020:
        if LOG: print('iyr: pass')
        return True
    if LOG: print('iyr: fail')
    return False

def v_eyr(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        if LOG: print('eyr: pass')
        return True
    if LOG: print('eyr: fail')
    return False

def v_hgt(hgt):
    if not re.match(r'[0-9]+(cm|in)', hgt):
        return False
    num,unit = re.search(r'([0-9]+)(in|cm)', hgt).groups()
    if unit == "cm" and 150 <= int(num) <= 193:
        if LOG: print('hgt: pass')
        return True
    if unit == "in" and 59 <= int(num) <= 76:
        if LOG: print('hgt: pass')
        return True
    if LOG: print('hgt: fail')
    return False

def v_hcl(hcl):
    if re.match(r'^#[0-9a-f]{6}$', hcl):
        if LOG: print('hcl: pass')
        return True
    if LOG: print('hcl: fail')
    return False

def v_ecl(ecl):
    valid_colors = ['amb','blu','brn','gry','grn','hzl','oth']
    if ecl in valid_colors:
        if LOG: print('ecl: pass')
        return True
    if LOG: print('ecl: fail')
    return False

def v_pid(pid):
    if re.match(r'^\d{9}$', pid):
        if LOG: print('pid: pass')
        return True
    if LOG: print('pid: fail')
    return False

def v_cid(cid):
    return True



def validate_passports(passports, extra_validation=True):
    valid_passports = []
    for passport in passports:
        if verify_passport(passport, extra_validation=extra_validation):
            valid_passports.append(passport)
    return valid_passports


with open('input.txt', 'r') as f:
    indata = f.read()
with open('test_data.txt', 'r') as f:
    testdata = f.read()

# passports = format_passports(testdata)
passports = format_passports(indata)
first_valid_passports = validate_passports(passports, extra_validation=False)
print(len(first_valid_passports))
second_valid_passports = validate_passports(passports, extra_validation=True)
print(len(second_valid_passports))
