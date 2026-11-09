



hooghoogh = int(input("hooghoogh khod ra vared konid : "))
if hooghoogh > 100:
    maliat = hooghoogh * 0.35
elif hooghoogh >= 80:
    maliat = hooghoogh * 0.25
elif hooghoogh >= 70:
    maliat = hooghoogh * 0.15
elif hooghoogh >= 60:
    maliat = hooghoogh * 0.12
elif hooghoogh >= 50:
    maliat = hooghoogh * 0.10
elif hooghoogh >= 40:
    maliat = hooghoogh * 0.05
else:
    maliat = 0
maliat_hooghoogh = hooghoogh - maliat
print("maliat:", maliat, "million Tomans")
print("hooghoogh ba karse maliat:", maliat_hooghoogh, "million Tomans")