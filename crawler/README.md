# News Crawler

This project is a news crawler that extracts news articles from the Yahoo Finance website and stores them in a Firebase Firestore database.

## Features

- Crawls news articles from the Yahoo Finance website
- Extracts relevant information from the news articles, including:
  - Title
  - Content
  - Publisher
  - Author
  - Date
- Stores the extracted news data in a Firebase Firestore database

## Prerequisites

- Node.js (version 14 or higher)
- Firebase account and project
- Environment variables for Firebase configuration and API keys

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/news-crawler.git
   ```

2. Install dependencies:

   ```bash
   cd news-crawler
   npm install
   ```

3. Create a `.env` file in the project root directory and add the following environment variables:

   ```env
   # Firebase configuration
   FIREBASE_API_KEY=your-firebase-api-key
   FIREBASE_AUTH_DOMAIN=your-firebase-auth-domain
   FIREBASE_PROJECT_ID=your-firebase-project-id
   FIREBASE_STORAGE_BUCKET=your-firebase-storage-bucket
   FIREBASE_MESSAGING_ID=your-firebase-messaging-id
   FIREBASE_APP_ID=your-firebase-app-id

   # Admin SDK configuration
   ADMIN_PRIVATE_KEY_ID=your-admin-private-key-id
   ADMIN_PRIVATE_KEY="your-admin-private-key"
   ADMIN_CLIENT_EMAIL=your-admin-client-email
   ADMIN_CLIENT_ID=your-admin-client-id
   ADMIN_AUTH_URI="https://accounts.google.com/o/oauth2/auth"
   ADMIN_TOKEN_URI="https://oauth2.googleapis.com/token"
   ADMIN_AUTH_PROVIDER="https://www.googleapis.com/oauth2/v1/certs"
   ADMIN_CLIENT_CERT_URL="https://www.googleapis.com/robot/v1/metadata/x509/your-admin-client-email"
   ADMIN_UNIVERSE_DOMAIN="googleapis.com"
   ```

   Replace the placeholders with your actual Firebase and Admin SDK configuration values.

4. Start the server:

   ```bash
   npm start
   ```

   The server will start running on `http://localhost:3000`.

## Usage

The project provides two endpoints:

- **GET /**: Triggers the news crawling process and stores the extracted news data in the Firebase Firestore database.
- **GET /test**: Checks the status of a specific URL (used for testing purposes).

To run the news crawling process, send a GET request to the `/` endpoint:

```bash
curl http://localhost:3000/
```

The server will respond with a JSON object containing the message `"Crawling and news extraction completed!"` and the extracted news data.

## File Structure

- `index.js`: The main entry point of the application, which sets up the Express server and defines the API endpoints.
- `firebase.js`: Initializes the Firebase app and exports the `auth` and `db` objects for interacting with Firebase Authentication and Firestore.
- `package.json`: Defines the project dependencies and scripts.
- `.env`: Stores the environment variables for the Firebase and Admin SDK configurations.

## Dependencies

- `express`: Web framework for Node.js
- `axios`: HTTP client for making requests
- `cheerio`: jQuery-like library for web scraping
- `moment`: Library for parsing, validating, manipulating, and formatting dates
- `got`: HTTP client library
- `date-fns`: Date utility library
- `firebase`: Firebase SDK for Node.js
- `dotenv`: Loads environment variables from a `.env` file

## Contribution

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.