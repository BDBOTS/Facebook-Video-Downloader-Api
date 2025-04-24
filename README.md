  Facebook Video Downloader API | BDBOTS  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; } .header { text-align: center; margin-bottom: 30px; border-bottom: 2px solid #1877f2; padding-bottom: 20px; } h1 { color: #1877f2; margin-bottom: 10px; } h2 { color: #1877f2; border-left: 4px solid #42b72a; padding-left: 10px; margin-top: 30px; } .card { background: #f0f2f5; border-radius: 8px; padding: 20px; margin-bottom: 20px; } .badge { display: inline-block; background: #1877f2; color: white; padding: 3px 8px; border-radius: 4px; font-size: 14px; margin-right: 5px; } pre { background: #1e1e1e; color: #f0f0f0; padding: 15px; border-radius: 6px; overflow-x: auto; } code { font-family: 'Courier New', Courier, monospace; } .credits { background: #f0f2f5; padding: 20px; border-radius: 8px; margin-top: 30px; } .social-links a { color: #1877f2; text-decoration: none; margin-right: 15px; } .social-links a:hover { text-decoration: underline; } .note { background: #fff8e1; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0; }

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

Parameter

Required

Description

`url`

Yes

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
