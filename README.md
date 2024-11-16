# FrostKeep Warehouse Solutions

FrostKeep Warehouse Solutions is a robust product management application featuring advanced functionalities such as soft deletion and historical data retention. This ensures data traceability, recoverability, and compliance with operational requirements.

## Features
1. **Soft Deletion**  
   - Allows products to be "soft deleted" (marked with an `is_deleted` attribute) instead of being permanently removed.
   - Prevents accidental data loss while preserving the option to restore records.

2. **Audit History**  
   - Tracks changes in a product’s name, description, price, and quantity.
   - Provides a version history for data compliance and traceability.

3. **Version History**  
   - Restores products to their most recent or specific historical versions.
   - Useful for correcting errors or retrieving past data states.

## Key Functionalities
- **View Inventory**: Displays all active products (not soft-deleted).
- **Create Product**: Adds a new product to the inventory.
- **Update Product**: Updates existing product details while logging the previous state.
- **Soft Delete**: Temporarily removes a product, retaining it in the database for recovery.
- **View Deleted Products**: Lists soft-deleted products for review or restoration.
- **Restore Product**: Recovers a soft-deleted product back to the active inventory.
- **View Product History**: Displays all modifications made to a product.
- **Revert to Specific Version**: Restores a product to a particular historical state.

## Deployment
- **API Documentation**: [Swagger UI](https://inventory-fulfillment.up.railway.app/swagger-ui/)
- **Application**: [FrostKeep Warehouse](https://frostkeepwarehouse.up.railway.app/)
- **GitHub Repositories**:
  - [Frontend Repo](https://github.com/Adityavanakudre/FrostKeep_frontend)
  - [Backend Repo](https://github.com/Adityavanakudre/Inventory)
