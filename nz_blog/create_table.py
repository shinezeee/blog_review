from django.utils import connection

with connection.cursor() as cursor:
    cursor.execute(
        """
        CREATE TABLE posts (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        auther VARCHAR(255) NOT NULL,
        title VARCHAR(255) NOT NULL,
        body TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        )"""
    )
