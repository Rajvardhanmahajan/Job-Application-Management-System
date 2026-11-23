
from models.job_model import (
    add_job,
    get_all_jobs,
    get_job_by_id,
    update_job,
    delete_job
)

from models.company_model import get_company_by_id


# VALIDATION - Check job details
def validate_job_details(company_id, job_title, salary):

    if not job_title or not job_title.strip():
        print("Job title is required!")
        return False

    if get_company_by_id(company_id) is None:
        print("Company ID does not exist!")
        return False

    try:
        if float(salary) < 0:
            print("Salary cannot be negative!")
            return False
    except (ValueError, TypeError):
        print("Please enter a valid salary!")
        return False

    return True


# CREATE - Add a new job
def create_job(company_id, job_title, job_type, salary, job_description):

    if not validate_job_details(company_id, job_title, salary):
        return False

    return add_job(
        company_id,
        job_title.strip(),
        job_type.strip(),
        float(salary),
        job_description.strip()
    )


# READ - Display all jobs
def view_jobs():

    jobs = get_all_jobs()

    if not jobs:
        print("No job records found.")
        return

    print("\n========== AVAILABLE JOBS ==========")

    for job in jobs:

        print(f"Job ID       : {job['job_id']}")
        print(f"Company      : {job['company_name']}")
        print(f"Job Title    : {job['job_title']}")
        print(f"Job Type     : {job['job_type']}")
        print(f"Salary       : {job['salary']}")
        print(f"Description  : {job['job_description']}")

        print("-" * 45)


# READ - Search job by ID
def search_job(job_id):

    job = get_job_by_id(job_id)

    if job:

        print("\n========== JOB DETAILS ==========")

        for key, value in job.items():
            print(f"{key}: {value}")

        return job

    print("Job not found.")
    return None


# UPDATE - Modify job details
def modify_job(job_id, company_id, job_title,
               job_type, salary, job_description):

    if get_job_by_id(job_id) is None:
        print("Job not found.")
        return False

    if not validate_job_details(company_id, job_title, salary):
        return False

    return update_job(
        job_id,
        company_id,
        job_title.strip(),
        job_type.strip(),
        float(salary),
        job_description.strip()
    )


# DELETE - Remove a job
def remove_job(job_id):

    job = get_job_by_id(job_id)

    if job is None:
        print("Job not found.")
        return False

    confirmation = input(
        f"Delete {job['job_title']}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        return delete_job(job_id)

    print("Deletion cancelled.")
    return False
