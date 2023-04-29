from drugdata import get_drug_details
medical_condition,side_effects,generic_name,brand_names=get_drug_details("doxycycline")
print(generic_name)
print(brand_names)