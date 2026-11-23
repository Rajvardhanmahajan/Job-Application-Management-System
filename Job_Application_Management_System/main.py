
from services.company_service import (
    create_company,
    view_companies,
    search_company,
    modify_company,
    remove_company
)

from services.job_service import(
    create_job,
    view_jobs,
    search_job,
    modify_job,
    remove_job
)

from services.application_service import (
    create_application,
    view_applications,
    search_application,
    modify_application_status,
    remove_application
)

def get_company_details():

    print("\nEnter Company Details")

    company_name = input("Company Name: ")
    location = input("Location: ")
    industry = input("Industry: ")
    website = input("Website: ")

    return company_name, location, industry, website


def company_management():

    while True:

        print("\n========== COMPANY MANAGEMENT ==========")
        print("1. Add Company")
        print("2. View All Companies")
        print("3. Search Company")
        print("4. Update Company")
        print("5. Delete Company")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            details = get_company_details()
            create_company(*details)

        elif choice == "2":

            view_companies()

        elif choice == "3":

            try:
                company_id = int(input("Enter Company ID: "))
                search_company(company_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":

            try:
                company_id = int(input("Enter Company ID: "))
                details = get_company_details()

                modify_company(company_id, *details)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":

            try:
                company_id = int(input("Enter Company ID: "))
                remove_company(company_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "6":

            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please try again.")


def get_job_details():

    print("\nEnter Job Details")

    company_id = int(input("Company ID: "))
    job_title = input("Job Title: ")
    job_type = input("Job Type: ")
    salary = input("Salary: ")
    job_description = input("Job Description: ")

    return (
        company_id,
        job_title,
        job_type,
        salary,
        job_description
    )


def job_management():

    while True:

        print("\n========== JOB MANAGEMENT ==========")
        print("1. Add Job")
        print("2. View All Jobs")
        print("3. Search Job")
        print("4. Update Job")
        print("5. Delete Job")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            try:
                details = get_job_details()
                create_job(*details)

            except ValueError:
                print("Invalid input! Please enter numeric values for IDs and salary.")

        elif choice == "2":

            view_jobs()

        elif choice == "3":

            try:
                job_id = int(input("Enter Job ID: "))
                search_job(job_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":

            try:
                job_id = int(input("Enter Job ID: "))
                details = get_job_details()

                modify_job(job_id, *details)

            except ValueError:
                print("Invalid input! Please enter numeric values for IDs and salary.")

        elif choice == "5":

            try:
                job_id = int(input("Enter Job ID: "))
                remove_job(job_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "6":

            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please try again.")

def application_management():

    while True:

        print("\n========== APPLICATION MANAGEMENT ==========")
        print("1. Add Application")
        print("2. View All Applications")
        print("3. Search Application")
        print("4. Update Application Status")
        print("5. Delete Application")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            try:
                job_id = int(input("Job ID: "))
                applicant_name = input("Applicant Name: ")
                email = input("Email: ")

                create_application(job_id, applicant_name, email)

            except ValueError:
                print("Please enter a valid numeric Job ID.")

        elif choice == "2":
            view_applications()

        elif choice == "3":
            try:
                application_id = int(input("Enter Application ID: "))
                search_application(application_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":
            try:
                application_id = int(input("Enter Application ID: "))
                status = input("Enter New Status: ").strip()

                modify_application_status(application_id, status)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":
            try:
                application_id = int(input("Enter Application ID: "))
                remove_application(application_id)

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "6":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please try again.")

def main():

    while True:

        print("\n========== JOB APPLICATION MANAGEMENT SYSTEM ==========")
        print("1. Company Management")
        print("2. Job Management")
        print("3. Application Management")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            company_management()

        elif choice == "2":
            job_management()

        elif choice == "3":
            application_management()

        elif choice == "4":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()



