
from models.company_model import (
    add_company,
    get_all_companies,
    get_company_by_id,
    update_company,
    delete_company
)


# CREATE - Add company
def create_company(company_name, location, industry, website):

    if not company_name or not company_name.strip():
        print("Company name is required!")
        return False

    return add_company(
        company_name.strip(),
        location.strip(),
        industry.strip(),
        website.strip()
    )


# READ - Display all companies
def view_companies():

    companies = get_all_companies()

    if not companies:
        print("No company records found.")
        return

    print("\n========== COMPANY RECORDS ==========")

    for company in companies:
        print(f"ID       : {company['company_id']}")
        print(f"Name     : {company['company_name']}")
        print(f"Location : {company['location']}")
        print(f"Industry : {company['industry']}")
        print(f"Website  : {company['website']}")
        print("-" * 40)


# READ - Search company by ID
def search_company(company_id):

    company = get_company_by_id(company_id)

    if company:
        print("\nCompany Details:")
        for key, value in company.items():
            print(f"{key}: {value}")
        return company

    print("Company not found.")
    return None


# UPDATE - Update company
def modify_company(company_id, company_name, location, industry, website):

    if not company_name or not company_name.strip():
        print("Company name is required!")
        return False

    return update_company(
        company_id,
        company_name.strip(),
        location.strip(),
        industry.strip(),
        website.strip()
    )


# DELETE - Delete company
def remove_company(company_id):

    company = get_company_by_id(company_id)

    if not company:
        print("Company not found.")
        return False

    confirmation = input(
        f"Are you sure you want to delete {company['company_name']}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        return delete_company(company_id)

    print("Deletion cancelled.")
    return False
