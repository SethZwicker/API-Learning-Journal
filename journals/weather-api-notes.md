# API Exploration: JSONPlaceholder

## Overview
- **Date:** [Current Date]
- **API Base URL:** https://jsonplaceholder.typicode.com/
- **Purpose:** Learning REST API Fundamentals

## Connection Details
- **Authentication:** None (Public API)
- **API Version:** N/A
- **Rate Limits:** None specified
- **Response Format:** JSON

## Endpoints Explored

### 1. GET /posts
- **Full URL:** https://jsonplaceholder.typicode.com/posts
- **Method:** GET
- **Purpose:** Retrieve all posts
- **Request Parameters:** None
- **Response Structure:** 
  - Array of post objects
  - Each object contains:
    * `id`
    * `title`
    * `body`
    * `userId`

#### Observations
- Total number of posts:
- Typical response time:
- Interesting patterns:

### 2. GET /posts/{id}
- **Full URL:** https://jsonplaceholder.typicode.com/posts/1
- **Method:** GET
- **Purpose:** Retrieve a specific post
- **Response Structure:** Single post object

#### Observations
- Differences from list view:
- Specific details retrieved:

### 3. POST /posts
- **Full URL:** https://jsonplaceholder.typicode.com/posts
- **Method:** POST
- **Purpose:** Create a new post
- **Request Body Example:**
  ```json
  {
    "title": "My First API Post",
    "body": "Learning API interactions",
    "userId": 1
  }
