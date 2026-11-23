
from config.db_config import get_connection
import mysql.connector


# CREATE - Add a new company
def add_company(company_name, location, industry, website):
    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO companies
            (company_name, location, industry, website)
            VALUES (%s, %s, %s, %s)
        """

        values = (company_name, location, industry, website)

        cursor.execute(query, values)
        connection.commit()

        print("Company added successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error adding company:", error)
        return False

    finally:
        cursor.close()
        connection.close()


# READ - Display all companies
def get_all_companies():
    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM companies ORDER BY company_id"

        cursor.execute(query)
        return cursor.fetchall()

    except mysql.connector.Error as error:
        print("Error fetching companies:", error)
        return []

    finally:
        cursor.close()
        connection.close()


# READ - Display company by ID
def get_company_by_id(company_id):
    connection = get_connection()

    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM companies WHERE company_id = %s"

        cursor.execute(query, (company_id,))
        return cursor.fetchone()

    except mysql.connector.Error as error:
        print("Error fetching company:", error)
        return None

    finally:
        cursor.close()
        connection.close()


# UPDATE - Modify company details
def update_company(company_id, company_name, location, industry, website):
    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = """
            UPDATE companies
            SET company_name = %s,
                location = %s,
                industry = %s,
                website = %s
            WHERE company_id = %s
        """

        values = (
            company_name,
            location,
            industry,
            website,
            company_id
        )

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Company updated successfully!")
            return True

        print("Company not found or no changes made.")
        return False

    except mysql.connector.Error as error:
        print("Error updating company:", error)
        return False

    finally:
        cursor.close()
        connection.close()


# DELETE - Remove a company
def delete_company(company_id):
    connection = get_connection()

    if connection is None:
        return False

    try:
        cursor = connection.cursor()

        query = "DELETE FROM companies WHERE company_id = %s"

        cursor.execute(query, (company_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Company deleted successfully!")
            return True

        print("Company not found.")
        return False

    except mysql.connector.Error as error:
        print("Error deleting company:", error)
        return False

    finally:
        cursor.close()
        connection.close()
