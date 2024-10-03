#!/bin/bash
# Backs up mydatabase to a file.
source ./.env
TIME=$(date "+%s")
BACKUP_FILE="postgres_${PG_DATABASE}_${TIME}.pgdump"

echo "Backing up $PGDATABASE to $BACKUP_FILE"
pg_dump -h $PG_HOST -p $PG_PORT -U $PG_USERNAME -d $PG_DATABASE -F c -f ./db_backups/$BACKUP_FILE
echo "Backup completed for $PGDATABASE"
