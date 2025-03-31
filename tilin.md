%% Diagrama generado en Mermaid JS (puedes renderizarlo en herramientas como Mermaid Live Editor)  
useCaseDiagram  
    actor Cuentahabiente as C  
    actor SistemaBancario as SB  
    
    rectangle Cajero_Automático {  
        usecase "UC1: Consultar Saldo" as UC1  
        usecase "UC2: Imprimir Comprobante" as UC2  
        usecase "UC3: Validar NIP" as UC3  
        usecase "UC4: Retirar Tarjeta" as UC4  
        
        C --> UC1  
        UC1 --> SB : Valida tarjeta/NIP  
        UC1 ..> UC3 : <<include>>  
        UC1 ..> UC4 : <<include>>  
        UC1 ..> "NIP Incorrecto" : <<extend>>  
        UC1 ..> "Tarjeta Inválida" : <<extend>>  
        UC1 ..> "Cajero en Fallo" : <<extend>>  
        UC1 --> UC2 : Opcional  
    }  