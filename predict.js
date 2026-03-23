const axios = require('axios');

// Backend API endpoint - set this as environment variable in Netlify
const FLASK_API_URL = process.env.FLASK_API_URL || 'http://localhost:5000';

exports.handler = async (event) => {
  // Enable CORS
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  // Handle CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ message: 'CORS OK' })
    };
  }

  try {
    if (event.httpMethod !== 'POST') {
      return {
        statusCode: 405,
        headers,
        body: JSON.stringify({ error: 'Method not allowed' })
      };
    }

    // Parse the incoming request
    const contentType = event.headers['content-type'] || '';
    
    let formData = new FormData();
    
    if (contentType.includes('multipart/form-data')) {
      // Handle file upload
      const body = event.body;
      const isBase64 = event.isBase64Encoded;
      
      const buffer = isBase64 ? Buffer.from(body, 'base64') : Buffer.from(body);
      
      // Extract boundary from content-type header
      const boundaryMatch = contentType.match(/boundary=([^;]+)/);
      if (!boundaryMatch) {
        return {
          statusCode: 400,
          headers,
          body: JSON.stringify({ error: 'Invalid form data' })
        };
      }

      // For now, forward the multipart data directly to Flask
      const flaskResponse = await axios.post(`${FLASK_API_URL}/predict`, buffer, {
        headers: {
          'Content-Type': contentType
        }
      });

      return {
        statusCode: 200,
        headers,
        body: JSON.stringify(flaskResponse.data)
      };
    } else {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Invalid content type' })
      };
    }

  } catch (error) {
    console.error('Error:', error.message);
    
    if (error.response) {
      return {
        statusCode: error.response.status,
        headers,
        body: JSON.stringify({
          error: error.response.data?.error || 'Backend error'
        })
      };
    }

    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({
        error: 'Failed to connect to Flask backend. Make sure it is running.'
      })
    };
  }
};
