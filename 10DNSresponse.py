import hashlib
def sign_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
original_domain=input("enter originial domain name:")
signature=sign_data(original_domain)
print("\ngenerated DNS signature:",signature)
received_domain=input("\nenter received domain name:")
verify_signature=sign_data(received_domain)
if verify_signature==signature:
    print("\nDNSSEC Verification successful:data is authentic")
else:
    print("\nDNSSEC Verfication failed:data has been modified")
    