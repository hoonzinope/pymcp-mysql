import os

MYSQL_CONFIG = {
    "host": os.environ.get("MYSQL_HOST", "172.30.1.4"),
    "port": int(os.environ.get("MYSQL_PORT", 3306)),
    "user": os.environ.get("MYSQL_USER", "readonlyuser"),
    "password": os.environ.get("MYSQL_PASSWORD", "1q2w3e4r"),
    "database": os.environ.get("MYSQL_DATABASE", "BOARD"),
}