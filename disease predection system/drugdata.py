import pandas as pd
def get_drug_details(drug):
    df=pd.read_csv("/home/timothi/Desktop/disease predection system/drug.csv")

    c=df.loc[df['drug_name'] == drug]
    return c["medical_condition"][0],c["side_effects"][0],c["generic_name"][0],c["brand_names"][0]

if __name__=="__main__":
    medical_condition,side_effects,generic_name,brand_names=get_drug_details("doxycycline")
    print(generic_name)
    print(brand_names)

