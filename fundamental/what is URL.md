# What is URL? - Definition and Types

## Definition of URL

**URL** stands for **Uniform Resource Locator**. It is a web address used to access resources (web pages, files, images, videos, etc.) on the internet. A URL specifies the location of a resource on a network and a mechanism for retrieving it.

### Key Characteristics of URL:
- **Web Address**: Used to navigate to specific locations on the internet
- **Standardized Format**: Follows a consistent structure defined by RFC 3986
- **Resource Location**: Identifies the exact path to a file, page, or resource
- **Protocol-Based**: Specifies how the resource should be accessed
- **Unique**: Each URL points to a specific resource

### URL vs. URI vs. URN

| Term | Definition | Example |
|------|-----------|---------|
| **URL** | Web address with location and access method | https://www.google.com/search |
| **URI** | Universal Resource Identifier (broader concept) | urn:isbn:0451450523 |
| **URN** | Universal Resource Name (identifies without location) | mailto:user@example.com |

---

## URL Structure and Components

### Basic URL Format
```
protocol://username:password@domain:port/path?query#fragment
```

### Components Breakdown

#### 1. Protocol (Scheme)
- **Definition**: Method used to access the resource
- **Format**: Comes before `://`
- **Common Protocols**:
  - `http://` - HyperText Transfer Protocol (unencrypted)
  - `https://` - HyperText Transfer Protocol Secure (encrypted with SSL/TLS)
  - `ftp://` - File Transfer Protocol
  - `ftps://` - File Transfer Protocol Secure
  - `mailto:` - Email address
  - `file://` - Local file system
  - `ws://` - WebSocket (unencrypted)
  - `wss://` - WebSocket Secure (encrypted)
- **Example**: `https://` in `https://www.example.com`

#### 2. Username & Password (Optional)
- **Definition**: Credentials for accessing protected resources
- **Format**: `username:password@`
- **Usage**: Rarely used in modern URLs due to security concerns
- **Example**: `https://user:pass@example.com`

#### 3. Domain (Host)
- **Definition**: The web server's address
- **Components**:
  - **Subdomain**: Optional prefix (www, mail, api, etc.)
  - **Domain Name**: Actual domain (google, example, etc.)
  - **Top-Level Domain (TLD)**: .com, .org, .edu, .net, etc.
- **Examples**:
  - `www.example.com`
  - `mail.google.com`
  - `api.github.com`

#### 4. Port (Optional)
- **Definition**: Network port number on the server
- **Format**: `:port` after domain
- **Default Ports**:
  - HTTP: 80
  - HTTPS: 443
  - FTP: 21
- **Example**: `https://example.com:8080`

#### 5. Path
- **Definition**: Location of the specific resource on the server
- **Format**: `/path/to/resource`
- **Characteristics**: Case-sensitive on most servers
- **Examples**:
  - `/index.html`
  - `/images/photo.jpg`
  - `/api/users/profile`

#### 6. Query String (Optional)
- **Definition**: Parameters passed to the resource
- **Format**: `?key1=value1&key2=value2`
- **Characteristics**:
  - Starts with `?`
  - Multiple parameters separated by `&`
  - Used for filtering, searching, or passing data
- **Examples**:
  - `?search=data+analytics&page=1`
  - `?id=123&sort=name`

#### 7. Fragment (Optional)
- **Definition**: Anchor or section within a page
- **Format**: `#section-name`
- **Characteristics**:
  - Not sent to server
  - Used for navigation within page
  - Case-sensitive
- **Examples**:
  - `#introduction`
  - `#results`

### URL Example with All Components
```
https://user:password@www.example.com:8080/path/page.html?search=data&page=1#results
```

**Breakdown**:
- Protocol: `https://`
- Username: `user`
- Password: `password`
- Domain: `www.example.com`
- Port: `8080`
- Path: `/path/page.html`
- Query: `?search=data&page=1`
- Fragment: `#results`

---

## Types of URLs

### 1. **By Protocol Type**

#### A. HTTP URL
- **Protocol**: HyperText Transfer Protocol
- **Encryption**: No (unencrypted)
- **Security**: Lower security
- **Usage**: Older websites, non-sensitive data
- **Example**: `http://www.example.com`
- **Warning**: ⚠️ Not recommended for sensitive information

#### B. HTTPS URL
- **Protocol**: HyperText Transfer Protocol Secure
- **Encryption**: Yes (SSL/TLS encryption)
- **Security**: Higher security
- **Usage**: Modern websites, e-commerce, banking, authentication
- **Example**: `https://www.example.com`
- **Advantage**: ✅ Recommended for all websites

#### C. FTP URL
- **Protocol**: File Transfer Protocol
- **Purpose**: File transfer
- **Usage**: Uploading/downloading files from servers
- **Example**: `ftp://files.example.com/documents/file.pdf`

#### D. FTPS URL
- **Protocol**: File Transfer Protocol Secure
- **Purpose**: Secure file transfer
- **Encryption**: Yes (SSL/TLS)
- **Example**: `ftps://secure.example.com/documents/file.pdf`

#### E. File URL
- **Protocol**: Local file system
- **Purpose**: Access local files on computer
- **Usage**: Opening files from disk
- **Example**: `file:///C:/Users/Documents/file.txt`
- **Note**: Three slashes after `file:`

#### F. WebSocket URLs
- **Protocols**: `ws://` (unencrypted), `wss://` (secure)
- **Purpose**: Real-time bidirectional communication
- **Usage**: Chat apps, live notifications, real-time updates
- **Examples**:
  - `ws://example.com/socket`
  - `wss://example.com/socket` (recommended)

#### G. Mailto URL
- **Protocol**: `mailto:`
- **Purpose**: Send email
- **Format**: `mailto:email@example.com?subject=Hello&body=Message`
- **Example**: `mailto:user@example.com`

---

### 2. **By URL Structure**

#### A. Absolute URL
- **Definition**: Complete URL with all components
- **Format**: `protocol://domain/path`
- **Usage**: Linking to external sites, cross-domain references
- **Example**: `https://www.google.com/search?q=data`
- **Characteristics**:
  - ✅ Works from any location
  - ✅ Works in different contexts
  - ✅ Search engine friendly

#### B. Relative URL
- **Definition**: URL relative to current page location
- **Format**: Partial path without protocol and domain
- **Usage**: Internal links within same website
- **Examples**:
  - `./page.html` (same directory)
  - `../page.html` (parent directory)
  - `/page.html` (root directory)
  - `page.html` (current directory)
- **Advantages**:
  - ✅ Shorter notation
  - ✅ Flexible for domain changes
  - ✅ Works offline

#### C. Protocol-Relative URL
- **Definition**: URL without protocol specification
- **Format**: `//domain/path`
- **Usage**: Automatic protocol selection based on current page
- **Example**: `//cdn.example.com/script.js`
- **Benefit**: Uses `https` if page is `https`, `http` if page is `http`

---

### 3. **By Domain Structure**

#### A. Root Domain URL
- **Definition**: URL pointing to main domain
- **Format**: `https://example.com`
- **Usage**: Homepage, main site
- **Characteristics**:
  - No subdomain
  - Highest level of domain

#### B. Subdomain URL
- **Definition**: URL with subdomain prefix
- **Format**: `https://subdomain.example.com`
- **Examples**:
  - `https://www.example.com` (www subdomain)
  - `https://mail.example.com` (mail subdomain)
  - `https://api.example.com` (API subdomain)
  - `https://blog.example.com` (blog subdomain)
- **Usage**: Organizing different services or sections

#### C. Subdirectory URL
- **Definition**: URL with specific path on domain
- **Format**: `https://example.com/subdirectory`
- **Examples**:
  - `https://example.com/blog/`
  - `https://example.com/products/electronics`
  - `https://example.com/api/v1/users`

---

### 4. **By TLD (Top-Level Domain)**

#### A. Generic TLDs (gTLD)
- `.com` - Commercial sites
- `.org` - Organizations, nonprofits
- `.net` - Networks, ISPs
- `.edu` - Educational institutions
- `.gov` - Government agencies
- `.mil` - Military
- `.info` - Information sites
- `.biz` - Business

#### B. Country Code TLDs (ccTLD)
- `.uk` - United Kingdom
- `.jp` - Japan
- `.de` - Germany
- `.fr` - France
- `.in` - India
- `.au` - Australia
- `.br` - Brazil
- `.ca` - Canada

#### C. Sponsored TLDs (sTLD)
- `.aero` - Aviation industry
- `.asia` - Asia-Pacific region
- `.coop` - Cooperatives
- `.museum` - Museums
- `.tel` - Telephone services

#### D. Infrastructure TLD
- `.arpa` - Infrastructure domain

#### E. New Generic TLDs (ngTLD)
- `.app` - Applications
- `.blog` - Blogs
- `.cloud` - Cloud services
- `.dev` - Developers
- `.io` - Input/Output, tech startups
- `.site` - General websites
- `.tech` - Technology

---

### 5. **By Purpose/Functionality**

#### A. Landing Page URL
- **Purpose**: Initial page users see
- **Format**: `https://example.com/`
- **Characteristics**: Homepage of website

#### B. Product/Service URL
- **Purpose**: Specific product or service page
- **Format**: `https://example.com/products/item-name`
- **Usage**: E-commerce, service listing

#### C. API URL
- **Purpose**: Access application programming interface
- **Format**: `https://api.example.com/endpoint`
- **Examples**:
  - `https://api.github.com/users`
  - `https://api.example.com/v1/products`

#### D. Documentation URL
- **Purpose**: Technical or user documentation
- **Format**: `https://docs.example.com`
- **Examples**:
  - `https://docs.python.org`
  - `https://documentation.example.com`

#### E. Static Resource URL
- **Purpose**: Serve static files (images, CSS, JS)
- **Format**: `https://cdn.example.com/resource`
- **Examples**:
  - `https://cdn.example.com/images/logo.png`
  - `https://cdn.example.com/styles/main.css`

#### F. Authentication URL
- **Purpose**: Login, logout, authentication
- **Format**: `https://example.com/auth/login`
- **Examples**:
  - `https://example.com/login`
  - `https://example.com/register`
  - `https://example.com/logout`

---

### 6. **By Content Type**

#### A. Web Page URL
- Ends with `.html` or `/`
- Example: `https://example.com/about.html`

#### B. Image URL
- Image file extensions
- Example: `https://example.com/images/photo.jpg`

#### C. Document URL
- PDF, Word, etc.
- Example: `https://example.com/files/report.pdf`

#### D. Video URL
- Video file extensions
- Example: `https://example.com/videos/tutorial.mp4`

#### E. Audio URL
- Audio file extensions
- Example: `https://example.com/audio/podcast.mp3`

#### F. Data/API URL
- Returns data (JSON, XML, etc.)
- Example: `https://api.example.com/data/users`

---

## URL Encoding

### Definition
Converting special characters in URLs to a format that is safe for transmission.

### URL Encoding Rules
- Spaces → `%20` or `+`
- `&` → `%26`
- `=` → `%3D`
- `#` → `%23`
- `/` → `%2F` (only in query string)

### Example
```
Original: Search data analytics
Encoded: Search%20data%20analytics
         or
         Search+data+analytics
```

---

## URL Best Practices

### ✅ DO:
1. **Use HTTPS**: Always use secure protocol
2. **Use Descriptive Paths**: `/products/laptops` instead of `/p/123`
3. **Use Hyphens**: Separate words with hyphens, not underscores
4. **Keep URLs Short**: Shorter URLs are better for SEO
5. **Use Lowercase**: Most servers treat domains as case-insensitive
6. **Avoid Special Characters**: Stick to alphanumeric characters and hyphens
7. **Use Meaningful Names**: Descriptive keywords in URL path

### ❌ DON'T:
1. Don't use HTTP for sensitive data
2. Don't expose usernames/passwords in URL
3. Don't use spaces in URLs
4. Don't use multiple special characters
5. Don't change URLs frequently
6. Don't use session IDs in URLs
7. Don't make URLs unnecessarily long

---

## URL Examples by Type

| Type | Example |
|------|---------|
| **HTTPS** | `https://www.example.com` |
| **HTTP** | `http://www.example.com` |
| **With Port** | `https://example.com:8080` |
| **With Path** | `https://example.com/blog/article` |
| **With Query** | `https://example.com/search?q=data` |
| **With Fragment** | `https://example.com/page#section` |
| **Subdomain** | `https://api.example.com` |
| **File URL** | `file:///C:/Users/Documents/file.txt` |
| **FTP URL** | `ftp://files.example.com/data` |
| **Email Link** | `mailto:user@example.com?subject=Hello` |
| **WebSocket** | `wss://example.com/socket` |

---

## Key Takeaways

- **URL**: Web address used to locate and access resources on the internet
- **Components**: Protocol, domain, port, path, query, and fragment
- **Types**: Multiple classifications by protocol, structure, domain, TLD, purpose, and content
- **Security**: Always use HTTPS for secure communication
- **Structure**: Follow standardized format for consistency and SEO
- **Best Practice**: Keep URLs short, descriptive, and meaningful
- **Encoding**: Special characters must be encoded for safe transmission
