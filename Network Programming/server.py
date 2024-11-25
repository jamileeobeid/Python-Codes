# PROJECT DONE INDIVIDUALLY BY: JAMILE OBEID

############################################################
### use this file to implement the server-side in part 2 ###
############################################################


import socket
import xml.etree.ElementTree as ET
import pandas as pd


# PARSING THE XML QUERY TO EXTRACT CONDITIONS
def parse_query(xml_query):

    conditions = []
    root = ET.fromstring(xml_query)  # PARSING THE XML STRING INTO AN ELEMENT TREE

    for condition in root.findall('./condition'):
        column = condition.find('column').text.strip()  # EXTRACTING THE COLUMN NAME 
        value = condition.find('value').text.strip()    # EXTRACTING THE VALUE TO MATCH 
        match_type = condition.get('type', 'exact').strip().lower()  # MATCH TYPE DEFAULTS TO 'exact' 
        conditions.append((column, value, match_type))  # APPENDING AS A TUPLE
    return conditions

# FILTER THE DATASET BASED ON CONDITIONS
def filter_data(conditions):
    
    # LOADING THE DATASET
    df = pd.read_csv('employees.csv') # READING THE EMPLOYEE DATA FROM CSV TO PANDAS DATAFRAME
    df.columns = df.columns.str.strip().str.lower() 

    # NORMALIZING CONDITIONS FOR CASE-INSENSITIVE MATCHING
    normalized_conditions = [
        (col.strip().lower(), val.strip().lower(), match_type) for col, val, match_type in conditions
    ]

    # CHECKING IF ALL COLUMNS IN CONDITIONS EXIST IN THE DATASET
    for col, _, _ in normalized_conditions:
        if col not in df.columns:
            return None  # RETURNING "None" IF ANY COLUMN DOESN'T EXIST (invalid query)

    # APPLYING FILTER CONDITIONS
    results = df
    for col, val, match_type in normalized_conditions:

        if match_type == 'substring':
            
            # FILTERS ROWS WHERE COLUMN CONTAINS THE VALUE (case-insensitive)
            results = results[results[col].str.contains(val, case=False, na=False)]
        else: 
            # PERFORMING A CASE-INSENSITIVE EXACT MATCH
            results = results[results[col].str.strip().str.lower() == val]
        if results.empty:
            break  # STOPING THE FILTERING IF NO ROWS MATCH THE QUERY CONDITIONS

    return results


# CREATING AN XML RESPONSE FOR THE FILTERED DATA
def create_response(filtered_data):
    
    root = ET.Element('result')
    status = ET.SubElement(root, 'status')

    if filtered_data is None:
        # SETTING STATUS TO "fail" IF INVALID QUERY  (e.g., column doesn't exist like Rank in Query4)
        status.text = 'fail'
    else:
        # SETTING STATUS TO "success" IF VALID QUERY (regardless of whether the result is empty e.g. QUERY3)
        status.text = 'success'

        data = ET.SubElement(root, 'data')
        if not filtered_data.empty:
            for _, row in filtered_data.iterrows():
                row_elem = ET.SubElement(data, 'row')  # ADDING EACH ROW AS A CHILD ELEMENT
                for key, value in row.items():
                    field = ET.SubElement(row_elem, key.lower())  # ADDING EACH FIELD AS A SUB-ELEMENT
                    field.text = str(value)  # CONVERTING THE VALUE TO STRING

    return ET.tostring(root, encoding='unicode')  # CONVERTING THE XML TREE TO A STRING


# MAIN FUNCTION
def main():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # CREATING A SOCKET
    server.bind(('localhost', 12345))  # BINDING TO LOCALHOST ON PORT 1245
    server.listen(1)  # LISTENING FOR ONE CONNECTION AT A TIME

    while True:
        client, addr = server.accept()  # WAITING FOR & ACCEPTING AN INCOMING CONNECTION 

        try:
            # RECIEVING THE XML QUERY FROM THE CLIENT 
            query = client.recv(1024).decode()  # READING UP TO 1024 BYTES 
            print("A query is received")

            # PARSING & PROCESSING THE QUERY
            conditions = parse_query(query)
            print("Generating a response ...")
            filtered_data = filter_data(conditions)
            response = create_response(filtered_data)
            print("Response generation succeeded")

            # SEINDING THE XML RESPONSE BACK TO THE CLIENT 
            client.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")  # PRINTING THE ERROR TO THE CONSOLE
            error_response = create_response(None)  # CREATING & SENDING A FAILURE RESPONSE FOR UNEXPECTED ERRORS
            client.send(error_response.encode())
        finally:
            client.close()  # CLOSING THE CLIENT CONNECTION

#CALLING THR MAIN FUNCTION
if __name__ == '__main__':
    main()
