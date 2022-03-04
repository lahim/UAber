CORS_ALLOW_ORIGINS = "*"  # fixme!
CORS_ALLOW_METHODS = ["GET", "POST", "PATH", "DELETE"]
CORS_ALLOW_HEADERS = ["*"]  # fixme!

DATABASE = {
    "uri": "mongodb://localhost:27017",
    "max_pool_size": 10,
    "db_name": "uaberdb",
}
