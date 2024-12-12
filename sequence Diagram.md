```mermaid
sequenceDiagram
    participant User
    participant "Shelf System" as System
    User ->> System: Add Book Request
    activate System
    System -->> System: Process Request
    System ->> System: Save Book in DB
    System -->> User: Confirmation Message
    deactivate System

```
