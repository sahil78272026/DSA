from pyisemail import is_email

address = 'sahil.garg7827nlnalndalnadkl@gmail.com'
bool_result = is_email(address)
detailed_result = is_email(address, diagnose=True)
print(bool_result)
print(detailed_result)

#Domain Check with Email

address = 'sahil.garg78272fsfsfsfsfsfsdffddfdddsdsd026@gmail.com'
bool_result_with_dns = is_email(address, check_dns=True)
detailed_result_with_dns = is_email(address, check_dns=True, diagnose=True)
print(bool_result_with_dns)
print(detailed_result_with_dns)