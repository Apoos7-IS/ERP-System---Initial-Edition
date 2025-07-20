# ERP-System-Initial-Edition
A simplified ERP system consisting of two interconnected modules: Inventory Management and Invoicing.

Inventory Management: Includes four core models (Product, Product Category, Stock Location, and Stock Move)
enabling users to register products, classify them, track their locations across warehouses, and monitor stock movements.

Invoicing: Includes three models (Invoice, Payment, and Invoice Line) to support invoice creation, manage payment
processes, and directly link them to stock movements.

When a sales invoice is created, the system automatically deducts quantities from inventory, records stock moves, and
links them with the invoice and its lines to ensure synchronization between warehouse and invoicing operations.

Currently, the system is in its first release, and after validating the performance of core modules, further expansion is
planned to include additional modules and features.
### Technical Outcomes:
- Managed database relationships using ORM to ensure seamless interaction between Inventory and Invoicing, while applying inheritance principles.
- Implemented automated workflows to deduct stock quantities upon invoice creation and register corresponding stock moves.
- Performed basic module testing to validate functionality prior to scaling.
