Facebook Video Downloader API | BDBOTS  

Facebook Video Downloader API
=============================

High-performance service for downloading Facebook videos directly

Live Services
-------------

API **Endpoint:** `https://fb.bdbots.xyz/dl?url=`

WEB **Interface:** [https://fb.bdbots.xyz](https://fb.bdbots.xyz)

API Usage
---------

Make a GET request with the Facebook video URL:

    https://fb.bdbots.xyz/dl?url=FACEBOOK_VIDEO_URL

### Example:

    https://fb.bdbots.xyz/dl?url=https://www.facebook.com/username/videos/123456789/

API Specifications
------------------

### Request Parameters

| Parameter | Required | Description |
|----------|----------|-------------|
| `url`    | Yes      | Facebook video URL (supports videos, reels, shares) |


Facebook video URL (supports videos, reels, shares)

### Successful Response (JSON)

    {
      "status": "success",
      "title": "Video Title",
      "downloads": [
        {
          "quality": "HD",
          "url": "direct-download-link.mp4",
          "size": "25.4 MB"
        },
        {
          "quality": "SD", 
          "url": "direct-download-link.mp4",
          "size": "12.1 MB"
        }
      ]
    }

### Error Response (JSON)

    {
      "status": "error",
      "message": "Descriptive error message",
      "solution": "Suggested fix"
    }

Web Interface
-------------

### Features:

*   Simple paste-and-download functionality
*   Supports all Facebook video formats:
    *   Regular videos (`/videos/`)
    *   Reels (`/reel/`)
    *   Shared videos (`/share/v/`)
    *   Watch links (`/watch/?v=`)
*   Mobile-friendly design

### Important Notes

*   Does **not** support `fb.watch` short links (use direct URLs)
*   Videos must be public/accessible
*   For best results, use URLs copied from desktop browsers

Integration Guide
-----------------

### JavaScript Example:

    fetch('https://fb.bdbots.xyz/dl?url=FACEBOOK_URL')
      .then(response => response.json())
      .then(data => {
        if(data.status === 'success') {
          // Process download links
          data.downloads.forEach(link => {
            console.log(`${link.quality}: ${link.url}`);
          });
        }
      });

Credits
-------

**Developed by:** BDBOTS Organization

[GitHub](https://github.com/bdBOTS) [Telegram Channel](https://t.me/BDBOTS) [Owner](https://t.me/Blackmax_it) [Telegram Bot](https://t.me/bdbots_bot)
