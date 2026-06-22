import pandas as pd


class ChangeMonitor:

    def __init__(self):
        self.previous_df = None

    def detect_changes(self, current_df):

        if self.previous_df is None:
            self.previous_df = current_df.copy()
            return

        old = self.previous_df
        new = current_df

        old_ids = set(old["Id"])
        new_ids = set(new["Id"])

        inserted = new_ids - old_ids
        deleted = old_ids - new_ids
        common = old_ids.intersection(new_ids)

        # INSERTS
        for row_id in inserted:

            row = new[new["Id"] == row_id].iloc[0]

            print("\n[INSERT]")
            print(row.to_dict())

        # DELETES
        for row_id in deleted:

            row = old[old["Id"] == row_id].iloc[0]

            print("\n[DELETE]")
            print(row.to_dict())

        # UPDATES
        for row_id in common:

            old_row = old[old["Id"] == row_id].iloc[0]
            new_row = new[new["Id"] == row_id].iloc[0]

            if not old_row.equals(new_row):

                print("\n[UPDATE]")
                print(f"ID : {row_id}")

                for col in old.columns:

                    if old_row[col] != new_row[col]:

                        print(
                            f"{col}: "
                            f"{old_row[col]} -> {new_row[col]}"
                        )

        self.previous_df = current_df.copy()