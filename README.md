``` mermaid
flowchart LR

    %% External Input
    NET[Ethernet PHY / Network Input]

    %% Deterministic Domain
    subgraph D["Deterministic Domain (TCM / SRAM)"]
        DMA[MAC + DMA Controller]
        SRAM[SRAM1 Buffer]
        PARSER[Zero-Copy Parser\n(*TradePacketStruct)]
        ENGINE[Deterministic HFT Engine\n(Bare-Metal State Machine)]
        GPIO[GPIO Toggle Pin\n(Determinism Signal)]
    end

    %% Control / Telemetry Domain
    subgraph C["Control / Telemetry Domain"]
        UART[UART5 Driver]
        U095[TechSH U095\n(Serial Bridge)]
        TERM[Host Terminal\n(Logging Output)]
    end

    %% Debug / Verification
    LA[Logic Analyzer]

    %% Data Flow (Deterministic Path)
    NET --> DMA
    DMA --> SRAM
    SRAM --> PARSER
    PARSER --> ENGINE

    %% Deterministic Signal Output
    ENGINE --> GPIO
    GPIO --> LA

    %% Telemetry Path (Out-of-Band)
    ENGINE -->|printf / metrics| UART
    UART --> U095
    U095 --> TERM

    %% Styling (optional but nice)
    classDef fast fill:#d1f5d3,stroke:#2e7d32,stroke-width:2px;
    classDef slow fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;

    class DMA,SRAM,PARSER,ENGINE,GPIO fast;
    class UART,U095,TERM slow;
```
