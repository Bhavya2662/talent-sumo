import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("scores.xls")
sheet = book.sheet_by_name("child_scores")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "mysqlPython")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO child_scores_db (candidate_id, candidate_name, access_id, Question_no, Likealibility, charm, Confidence, Fluency, Content, Overall) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    candidate_id = sheet.cell(r,).value
    candidate_name = sheet.cell(r,1).value
    access_id = sheet.cell(r,2).value
    Question_no = sheet.cell(r,3).value
    Likealibility = sheet.cell(r,4).value
    Charm = sheet.cell(r,5).value
    Confidence = sheet.cell(r,6).value
    Fluency = sheet.cell(r,7).value
    Content = sheet.cell(r,8).value
    Overall = sheet.cell(r,9).value

	# Assign values from each row
    values = (candidate_id, candidate_name, access_id, Question_no, Likealibility, charm, Confidence, Fluency, Content, Overall)
    
    # Execute sql Query
    cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

