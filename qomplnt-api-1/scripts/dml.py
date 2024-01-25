from sqlalchemy.orm import Session
import json
from sqlalchemy import text

class DMLScript:
    db : Session
    def __init__(self, db: Session) -> None:
        self.db = db

    def dml_insert(self, table_name, columns_values):
        for key, value in columns_values.items():
            if isinstance(value, dict) or isinstance(value, list):
                columns_values[key] = json.dumps(value)
        # Construct the INSERT script dynamically based on columns and values
        dml_script = f"""
        INSERT INTO {table_name} ({', '.join(f'`{key}`' for key in columns_values.keys())})
        VALUES ({', '.join(':' + key for key in columns_values.keys())});
        """
        self.db.execute(text(dml_script), columns_values)
        self.db.commit()

        return columns_values
    
   
    def dml_select(self, model, columns_values, selected_columns=None, join_relationships=None):
        # Construct the SELECT script dynamically based on columns and values
        select_columns = ', '.join(f'`{key}`' for key in selected_columns) if selected_columns else '*'
        where_clause = ' AND '.join(f'`{key}` = :{key}' for key in columns_values.keys())

        # Include JOIN clauses based on specified relationships
        join_clauses = ''
        if join_relationships:
            for relationship in join_relationships:
                join_clauses += f' LEFT JOIN {relationship} ON {model.__tablename__}.{relationship}_id = {relationship}.id'

        dml_script =  f"""
            SELECT {select_columns} FROM {model.__tablename__}
            
            WHERE {where_clause};
            """

        result = self.db.execute(text(dml_script), columns_values)
        return result
   