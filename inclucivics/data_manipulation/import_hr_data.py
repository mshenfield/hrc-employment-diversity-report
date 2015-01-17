from include.rethinkdb.vars import IMPORT_PATH, IMPORT_STRING
from inclucivics.project.common.io import rethink_import_data


FILES_TO_IMPORT = [
    dict(
        path=IMPORT_PATH,
        table=IMPORT_STRING
    )
]

print FILES_TO_IMPORT
rethink_import_data(
    FILES_TO_IMPORT,
    file_type="csv",
    delimitter="|"
)

