

```
graph TD
    subgraph "Data Inputs (The Sources)"
        T1[Tier 1: HRMS Data<br>(Quarterly, Compliance)]
        T2[Tier 2: Luminous Biosensor<br>(Daily, Operations)]
        SCADA[Site Data<br>(SCADA, Process)]
        PDFs[Historical Data<br>(PDFs, Spreadsheets)]
    end

    subgraph "Core Luminous Platform"
        HUB(Tier 3: Confluent<br>Data & Intelligence Hub<br><br>'Data Ingestion, Unification & Querying')
    end

    subgraph "Outputs (The Value)"
        D1[Operator Dashboard<br>(Process Control)]
        D2[Regulator Dashboard<br>(Compliance Metrics)]
        D3[Community Dashboard<br>(Transparency)]
    end

    %% Data Flow Connections
    %% Connect all inputs to the Hub
    T1 --> HUB
    T2 --> HUB
    SCADA --> HUB
    PDFs --> HUB

    %% Connect Hub to all outputs
    HUB --> D1
    HUB --> D2
    HUB --> D3

    %% Styling
    style HUB fill:#222,stroke:#0f0,stroke-width:2px,color:#fff
    style T1 fill:#eee,stroke:#333
    style T2 fill:#bbf,stroke:#333,stroke-width:2px,color:#fff
    style SCADA fill:#eee,stroke:#333
    style PDFs fill:#eee,stroke:#333

    style D1 fill:#bdf,stroke:#333
    style D2 fill:#bdf,stroke:#333
    style D3 fill:#bdf,stroke:#333
```



