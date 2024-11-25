# PROJECT DONE INDIVIDUALLY BY: JAMILE OBEID

############################################################
### use this file to implement the client-side in part 2 ###
############################################################


import socket
import xml.etree.ElementTree as ET
import sys

# GENERATING AN XML QUERY BASED ON INPUT FROM FILE
def create_query(query_file):
    tree = ET.parse(query_file) # READING & PARSING THE XML FILE CONTAINING THE QUERY STRUCTURE 
    root = tree.getroot()
    return ET.tostring(root, encoding='unicode') # CONVERTING THE XML TREE TO STRING FOR TRANSMISSION TO THE SERVER

# PARSING THE SERVER'S RESPONSE & DISPLAING RESULTS (similar to the one shown in zoom recording)
def parse_response(response):
    root = ET.fromstring(response)
    status = root.find('./status').text # GETTING THE STATUS FIELD FROM THE RESPONSE ('success' or 'fail')
    if status == 'success':
        print("received data:")
        print("################################")
        for row in root.findall('./data/row'):
            print("name:", row.find('name').text)
            print("title:", row.find('title').text)
            print("email:", row.find('email').text)
        print("################################")
    else:
        print("query failed")


# SAVING THE RESPONSE TO A FILE
def save_response(response, response_file):
    with open(response_file, 'w') as file:
        file.write(response)
    print("Response saved.")


# MAIN FUNCTION
def main():
    if len(sys.argv) != 3:

        # DISPLAYS INSTRUCTIONS TO THE USER ON HOW TO RUN THE SCRIPT WITH REQUIRED ARGUMENTS
        # (similar to the one shown in zoom recording, e.g. python3 client.py query1.xml response1.xml)
        print("Usage: python3 client.py <query_file.xml> <response_file.xml>")
        sys.exit(1)

    query_file = sys.argv[1]
    response_file = sys.argv[2]

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    # CREATING THE XML QUERY
    print("Sending a query ...")
    query = create_query(query_file)
    client.send(query.encode())
    
    # RECIEVING THE RESPONSE IN CHUNKS
    response = ""
    while True:
        chunk = client.recv(1024).decode()
        if not chunk:
            break
        response += chunk

    print("Receiving a response ...")
    save_response(response, response_file)
    parse_response(response)
    
    client.close()

# CALLING THE MAIN FUNCTION
if __name__ == '__main__':
    main()
