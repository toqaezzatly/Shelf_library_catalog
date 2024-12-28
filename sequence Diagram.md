```mermaid
sequenceDiagram
    participant User
    participant System
    User ->>+ System: Add Book Request
    System ->> System: Save Book in DB
    System -->>- User: Confirmation Message

```
