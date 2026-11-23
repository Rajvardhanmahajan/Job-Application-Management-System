
from models.application_model import (
    add_application,
    get_all_applications,
    get_application_by_id,
    update_application_status,
    delete_application
)

from models.job_model import get_job_by_id


# Validate application details
def validate_application(job_id, applicant_name, email):

    if get_job_by_id(job_id) is None:
        print("Job ID does not exist!")
        return False

    if not applicant_name or not applicant_name.strip():
        print("Applicant name is required!")
        return False

    if not email or "@" not in email or "." not in email:
        print("Please enter a valid email address!")
        return False

    return True


# Create application
def create_application(job_id, applicant_name, email):

    if not validate_application(job_id, applicant_name, email):
        return False

    return add_application(
        job_id,
        applicant_name.strip(),
        email.strip()
    )


# View all applications
def view_applications():

    applications = get_all_applications()

    if not applications:
        print("No application records found.")
        return

    print("\n========== ALL APPLICATIONS ==========")

    for application in applications:
        print(f"Application ID : {application['application_id']}")
        print(f"Applicant Name : {application['applicant_name']}")
        print(f"Email          : {application['email']}")
        print(f"Job Title      : {application['job_title']}")
        print(f"Company        : {application['company_name']}")
        print(f"Application Date: {application['application_date']}")
        print(f"Status         : {application['status']}")
        print("-" * 45)


# Search application
def search_application(application_id):

    application = get_application_by_id(application_id)

    if application:
        print("\n========== APPLICATION DETAILS ==========")

        for key, value in application.items():
            print(f"{key}: {value}")

        return application

    print("Application not found.")
    return None


# Update application status
def modify_application_status(application_id, status):

    application = get_application_by_id(application_id)

    if application is None:
        print("Application not found.")
        return False

    allowed_statuses = [
        "Applied",
        "Under Review",
        "Shortlisted",
        "Rejected",
        "Selected"
    ]

    if status not in allowed_statuses:
        print("Invalid status!")
        print("Allowed statuses:", ", ".join(allowed_statuses))
        return False

    return update_application_status(application_id, status)


# Delete application
def remove_application(application_id):

    application = get_application_by_id(application_id)

    if application is None:
        print("Application not found.")
        return False

    confirmation = input(
        f"Delete application of {application['applicant_name']}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        return delete_application(application_id)

    print("Deletion cancelled.")
    return False
