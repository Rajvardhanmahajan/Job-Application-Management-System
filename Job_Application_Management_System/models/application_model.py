
from config.db_config import get_connection
import mysql.connector


# Add a new application
def add_application(job_id, applicant_name, email):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO applications
            (job_id, applicant_name, email, application_date)
            VALUES (%s, %s, %s, CURDATE())
        """

        values = (job_id, applicant_name, email)

        cursor.execute(query, values)
        connection.commit()

        print("Application submitted successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error adding application:", error)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()


# View all applications
def get_all_applications():
    connection = get_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                a.*,
                j.job_title,
                c.company_name
            FROM applications a
            INNER JOIN jobs j ON a.job_id = j.job_id
            INNER JOIN companies c ON j.company_id = c.company_id
            ORDER BY a.application_id
        """

        cursor.execute(query)
        return cursor.fetchall()

    except mysql.connector.Error as error:
        print("Error fetching applications:", error)
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()


# Search application by ID
def get_application_by_id(application_id):
    connection = get_connection()

    if connection is None:
        return None

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                a.*,
                j.job_title,
                c.company_name
            FROM applications a
            INNER JOIN jobs j ON a.job_id = j.job_id
            INNER JOIN companies c ON j.company_id = c.company_id
            WHERE a.application_id = %s
        """

        cursor.execute(query, (application_id,))
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Error fetching application:", error)
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()


# Update application status
def update_application_status(application_id, status):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE applications
            SET status = %s
            WHERE application_id = %s
        """

        cursor.execute(query, (status, application_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Application status updated successfully!")
            return True

        print("Application not found or status unchanged.")
        return False

    except mysql.connector.Error as error:
        print("Error updating application:", error)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()


# Delete application
def delete_application(application_id):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM applications
            WHERE application_id = %s
        """

        cursor.execute(query, (application_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Application deleted successfully!")
            return True

        print("Application not found.")
        return False

    except mysql.connector.Error as error:
        print("Error deleting application:", error)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()
