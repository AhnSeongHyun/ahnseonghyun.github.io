#!/usr/bin/env python3
import os
import pymysql
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Database connection parameters
DB_CONFIG = {
    'host': 'ls-03dca3d06f9512bfd8c1082b4a22cc76740b5c06.cmm715uaoqmt.ap-northeast-2.rds.amazonaws.com',
    'port': 3306,
    'user': 'ash84',
    'password': 'ash8467501!',
    'database': 'meier',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Directory where markdown files will be created
CONTENT_DIR = 'contents'

def ensure_directory(directory):
    """Ensure directory exists, create if it doesn't"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")

def get_tags_for_post(cursor, post_id):
    """Get tags for a specific post"""
    # Query to get tags for a post based on the custom schema
    tag_query = """
    SELECT t.tag
    FROM tag t
    JOIN post_tag pt ON t.id = pt.tag_id
    WHERE pt.post_id = %s
    """
    cursor.execute(tag_query, (post_id,))
    tags = [tag['tag'] for tag in cursor.fetchall()]
    return tags

def format_date(date_str):
    """Format date string to YYYY-MM-DD"""
    if date_str:
        try:
            date_obj = datetime.strptime(str(date_str), '%Y-%m-%d %H:%M:%S')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            logger.warning(f"Could not parse date: {date_str}")
    return ''

def migrate_posts():
    """Migrate posts from database to markdown files"""
    conn = None
    migrated_count = 0
    total_posts = 0
    
    try:
        # Connect to the database
        logger.info("Connecting to database...")
        conn = pymysql.connect(**DB_CONFIG)
        
        with conn.cursor() as cursor:
            # Query to get all blog posts (is_page = 0)
            post_query = """
            SELECT id, post_name, title, content, mo_date, featured_image
            FROM post
            WHERE is_page = 0
            """
            
            logger.info("Fetching posts from database...")
            cursor.execute(post_query)
            posts = cursor.fetchall()
            
            total_posts = len(posts)
            logger.info(f"Found {total_posts} posts to migrate")
            
            for post in posts:
                post_id = post['id']
                post_name = post['post_name']
                post_title = post['title']
                post_content = post['content']
                post_date = format_date(post['mo_date'])
                featured_image = post.get('featured_image', '') or ''
                
                # Get tags for the post
                tags = get_tags_for_post(cursor, post_id)
                
                # Format tags for markdown
                tags_str = ""
                if tags:
                    tags_str = "', '".join(tags)
                
                # Format markdown content
                md_content = f"""---
title: '{post_title}'
author: 'ash84'
pub_date: '{post_date}'
description: ''
featured_image: '{featured_image}'
tags: ['{tags_str}']
---

{post_content}
"""
                
                # Create directory for the post if it doesn't exist
                post_dir = os.path.join(CONTENT_DIR, post_name)
                ensure_directory(post_dir)
                
                # Create markdown file
                md_path = os.path.join(post_dir, f"{post_name}.md")
                
                # Write to file
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                logger.info(f"Migrated post: {post_name}")
                migrated_count += 1
    
    except pymysql.MySQLError as e:
        logger.error(f"Database error: {e}")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed")
    
    logger.info(f"Migration completed. {migrated_count} out of {total_posts} posts migrated.")
    return migrated_count

if __name__ == "__main__":
    logger.info("Starting migration process...")
    ensure_directory(CONTENT_DIR)
    migrated_count = migrate_posts()
    logger.info(f"Migration completed successfully. Total posts migrated: {migrated_count}")
