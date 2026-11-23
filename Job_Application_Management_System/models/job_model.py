
from config.db_config import get_connection
import mysql.connector


# CREATE - Add a new job
def add_job(company_id, job_title, job_type, salary, job_description):

    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO jobs
            (company_id, job_title, job_type, salary, job_description)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            company_id,
            job_title,
            job_type,
            salary,
            job_description
        )

        cursor.execute(query, values)
        connection.commit()

        print("Job added successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error adding job:", error)
        return False

    finally:
        cursor.close()
        connection.close()


# READ - Display all jobs
def get_all_jobs():

    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT j.*, c.company_name
            FROM jobs j
            INNER JOIN companies c
            ON j.company_id = c.company_id
            ORDER BY j.job_id
        """

        cursor.execute(query)
        return cursor.fetchall()

    except mysql.connector.Error as error:
        print("Error fetching jobs:", error)
        return []

    finally:
        cursor.close()
        connection.close()


# READ - Search job by ID
def get_job_by_id(job_id):

    connection = get_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT j.*, c.company_name
            FROM jobs j
            INNER JOIN companies c
            ON j.company_id = c.company_id
            WHERE j.job_id = %s
        """

        cursor.execute(query, (job_id,))
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Error fetching job:", error)
        return None

    finally:
        cursor.close()
        connection.close()


# UPDATE - Modify job details
def update_job(job_id, company_id, job_title,
               job_type, salary, job_description):

    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
            UPDATE jobs
            SET company_id = %s,
                job_title = %s,
                job_type = %s,
                salary = %s,
                job_description = %s
            WHERE job_id = %s
        """

        values = (
            company_id,
            job_title,
            job_type,
            salary,
            job_description,
            job_id
        )

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Job updated successfully!")
            return True

        print("Job not found or no changes made.")
        return False

    except mysql.connector.Error as error:
        print("Error updating job:", error)
        return False

    finally:
        cursor.close()
        connection.close()


# DELETE - Remove a job
def delete_job(job_id):

    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = "DELETE FROM jobs WHERE job_id = %s"

        cursor.execute(query, (job_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Job deleted successfully!")
            return True

        print("Job not found.")
        return False

    except mysql.connector.Error as error:
        print("Error deleting job:", error)
        return False

    finally:
        cursor.close()
        connection.close()
