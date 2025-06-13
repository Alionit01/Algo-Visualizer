# crud.py

def add_record(records, new_record):
    records.append(new_record)

def update_record(records, record_id, updated_record):
    for i, rec in enumerate(records):
        if rec['id'] == record_id:
            records[i] = updated_record
            return True
    return False

def delete_record(records, record_id):
    for i, rec in enumerate(records):
        if rec['id'] == record_id:
            del records[i]
            return True
    return False
