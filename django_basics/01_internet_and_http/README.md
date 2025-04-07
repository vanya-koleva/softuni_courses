# Internet and HTTP

## What is the Internet?

-   A large network of devices.

-   We get indirectly connected through **ISP**s (Internet Service Providers)

-   Example:

    -   If we disconnect our router and connect it only to our phone and laptop, that forms a (mini) network of 2 devices.

    -   If I run an application on a certain port on my laptop, I’ll be able to access it from my phone.

    -   Then, if we connect the router to the Internet, it becomes a connection between our (mini) network and all the other mini networks, forming one large network.

-   It originated as a scientific research project in 1969.

-   Ways We Connect to the Internet:

    -   Optical cables
    -   Copper cables
    -   Cell towers
    -   Satellites

-   Commands for viewing all individual network interfaces on our machine:

    -   MAC / Linux:
        ```bash
        ifconfig
        ```
    -   Windows:
        ```bash
        ipconfig /all
        ```
    -   Physical interfaces: en0, en1, en2, en3, en4, en5, en6

    -   Virtual interfaces: lo0, bridge0, utun0, utun1, utun2, utun3, awdl0

## Request/Response - Client/Server

-   We want some resource, and if we have access to it, we retrieve it.

-   A **client** is any application that can access a server.

-   A **server** is the machine that can provide resources.

```bash
curl https://softuni.bg/
```

## Network Protocol

-   Set of rules and standards, that allow communication between network devices.

-   A **standard** that allows two devices to communicate.

-   The **rules** that must be followed so the server can understand what the client wants, and when the server sends back a response, the client can understand it.

### Commonly Used Protocols:

-   **HTTP**:

    -   Used for loading web pages. Each request and response is independent.

-   **TCP**:

    -   Ensures data is transmitted reliably and in the correct order. Establishes a connection before transmission.

-   **FTP**:

    -   A protocol for transferring files. Operates in a client-server model and supports different transfer modes.
    -   Often used to download database backups, primarily due to the large volume of data.

-   **SSH**:

    -   Provides secure remote access to networked devices by encrypting the communication.

-   **SMTP**:

    -   Used to send emails to email providers.

-   **IP**:
    -   A protocol for addressing and routing data across networks, ensuring that packets are sent and received between devices.

## Packets

-   When the server and the client exchange data, they exchange it in the form of **packets**.

-   If there is a large amount of data, it will be split into smaller parts (packets).

-   The client will break the data into packets when sending it to the server. The server will then reassemble the packets — and vice versa.

-   The **protocol** defines how the server and client understand how to process the packets.

## IP Address

-   A **unique identifier** within a local network.

-   All IPs within a network must be unique.

-   For this reason, when we connect to a different network, we may have a different IP address in it.

-   If we connect several devices within one network, they can appear under a single IP to the outside world, but inside the network, they each have their own unique IP address.

## IPv4 vs IPv6

### IPv4:

-   Allows the creation of **4.3 billion** unique addresses.
-   Uses **32-bit addresses**.
-   Example:  
    `192.168.14.20`
    -   `192.168` is the **network part**
    -   `14` is the **subnet** (our specific network)
    -   `20` is our **device** within the network

### IPv6:

-   Allows the creation of **3.4×10^38** unique addresses.
-   Uses **128-bit addresses**.

## DNS - Domain Name System

-   Ensures that we can access websites using a **domain name** instead of an IP address.

-   IP addresses can change, so we can’t expect users to remember them.

## HTTP

-   We always receive a response.

-   It is the **protocol of the Internet**.

-   **HTTP/1** and **HTTP/2** use **TCP/IP** underneath.  
    **HTTP/3** uses the **QUIC** protocol.

-   HTTP/2

    -   Major revision of the HTTP network protocol.
    -   Fast and optimized.
    -   Completely Backwards-Compatible.

-   HTTP Verbs:

    -   `GET` – Retrieve data
    -   `POST` – Create a new resource
    -   `PUT` – Update an existing resource
    -   `DELETE` – Remove a resource
    -   ...

## HTTP Request / HTTP Response

-   Request message sent by a client consists of:
    -   **HTTP request line**:
        -   **Method** (GET / POST / PUT / DELETE / …)
        -   Resource **URI** (URL)
        -   **Protocol version**
    -   **HTTP request headers**:
        -   Additional parameters
    -   HTTP request body
        -   Optional data

```http
GET /courses/python HTTP/1.1
Host: softuni.bg
User-Agent: Mozilla/5.0
<CRLF>
```

```html
<form method="get" action="/my-action">
    Name: <input type="text" name="name" /> Age: <input type="text" name="age" />
    <button>Submit</button>
</form>
```

-   **Response message**:

    -   HTTP response **status line**:
        -   Protocol version
        -   Status code
        -   Status text
    -   Response **headers**:
        -   Provide meta data about the returned resource
    -   Response **body**:
        -   The content of the HTTP response (data)

-   [Status codes](https://http.cat/)

## URL (Uniform Resource Locator)

-   A URL is a reference to a web resource that specifies its location on a network and a mechanism for retrieving it.

-   A specific type of URI (Uniform Resource Identifier).

-   Similar to real-world addresses where we have: country, city, neighborhood...

-   Example:
    `http://localhost:8080/demo/html?id=26&lang=en#lecture`

    -   `http` – **Protocol**
    -   `localhost` – **Host** (or domain)
    -   `8080` – **Port**
    -   `/demo/html` – **Path**
    -   `?id=26&lang=en` – **Query string**
    -   `#lecture` – **Fragment**

-   `https://softuni.bg:443` – We can omit the port because HTTPS uses port **443** by default.

-   URLs can contain **Cyrillic** characters.

## MIME (Multi-purpose Internet Mail Extensions)

-   Explains the type of data being sent and received.

-   Used in many Internet protocols like HTTP and SMTP.

| MIME Type / Subtype | Description  |
| ------------------- | ------------ |
| application/json    | JSON data    |
| image/png           | PNG image    |
| image/gif           | GIF image    |
| text/html           | HTML         |
| text/plain          | Text         |
| text/xml            | XML          |
| video/mp4           | MP4 video    |
| application/pdf     | PDF document |

