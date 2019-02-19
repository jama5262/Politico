errorMessage = ""


def validation(errorCode):
    if errorCode == "23505":
        errorMessage = "(Unique Violation), The data aleady exists in the database"
    elif errorCode == "23503":
        errorMessage = "(Foreign Key Violation), Some data was not found in the database"
    else:
        errorMessage = errorCode
    return {
      "error": errorMessage,
      "status": 500
    }
