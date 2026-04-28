vendor = {"name": "Cloud-X", "mfa": False, "encryption": True, "soc2_report": True}  
score = 100  
if not vendor["mfa"]: score -= 40  
if not vendor["encryption"]: score -= 40  
if not vendor["soc2_report"]: score -= 20  
print(f"--- Vendor Risk Assessment ---")  
print(f"Vendor Name: {vendor['name']}")  
print(f"Final Security Score: {score}")  
if score < 70: print("RESULT: HIGH RISK - Remediation Required")  
else: print("RESULT: LOW RISK - Approved") 
