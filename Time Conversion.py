s = input()
def timeConversion(s):
    maradian = s[-2:]
    if maradian =="PM" and s[:2] != "12":
        s = str(12 + int(s[:2]))+s[2:]
    if maradian == "AM" and s[:2] == "12":
        s = "00"+s[2:]
    return s[:-2]
result = timeConversion(s)
print(result)