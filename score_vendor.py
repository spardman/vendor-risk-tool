def run_assessment():
    print("--- 🛡️ Vendor Security Risk Calculator ---")
    
    # 1. Collect Vendor Info
    vendor_name = input("Enter Vendor Name: ")
    
    # 2. Assign Scores (100 = Perfect, 0 = Fail)
    score = 100
    
    # 3. Check Critical Controls
    mfa = input("Is MFA enabled? (y/n): ").lower()
    encryption = input("Is Data Encrypted at rest? (y/n): ").lower()
    soc2 = input("Do they have a SOC2 Type II report? (y/n): ").lower()

    # 4. Logic (GRC Weighting)
    if mfa != 'y': score -= 40
    if encryption != 'y': score -= 40
    if soc2 != 'y': score -= 20

    # 5. Output Results
    print(f"\n--- Assessment for {vendor_name} ---")
    print(f"Final Security Score: {score}")
    
    if score < 70:
        print("❌ RESULT: HIGH RISK - Remediation or Waiver Required")
    else:
        print("✅ RESULT: LOW RISK - Approved for Onboarding")

if __name__ == "__main__":
    run_assessment()

