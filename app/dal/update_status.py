from app.db import db_client

def update_workflow_status(uid: int, status_name: str):
  try:
      workflow_state_update_query = """UPDATE podcast_details SET state = %s WHERE id = %s"""
      state_to_update = (uid, status_name)
      cursor = db_client.cursor()
      cursor.execute(workflow_state_update_query, state_to_update)
      # commit changes
      db_client.commit()
      print("Workflow state set to {}".format(status_name))
  except Exception:
     print("add exception log")
  finally:
     # closing database connection.
        if db_client:
            cursor.close()