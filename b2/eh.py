"""
Errors
Notitfications,
Warnings

Errors:
    Synax errors
    compail errors
    runtime/fatel errors
    
EH: try... except

Logs: fileIO/logs
"""
import logging

logging.basicConfig(
    filename=r"D:\Projects\PPS\Python\b2\errors.log",
    filemode="a",
    format="%(levelname)s - [%(asctime)s] - %(name)s : %(message)s",
    level=logging.INFO
)


try:
    logging.info("STart reading file.")
    fs = open(r"D:\Projects\PPS\Python\b2\test.txt", "r");
    data = fs.read()
    print(data)

    fs.close();
except Exception as e:
    #print(e)
    logging.error(e,exc_info=True)
    #logging.debug(e,exc_info=True)
finally:
    logging.info("File IO completed.")
