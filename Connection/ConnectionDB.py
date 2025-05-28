import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={Oracle em OraClient19Home1};'
    'UID=username;'
    'PWD=senha;'
    'DBQ=host_name:port/service_name'
)