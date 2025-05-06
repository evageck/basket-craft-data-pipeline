  ## Project Summary

  This project repository demonstrates an end-to-end ELT (extract, load, transform) pipeline using a mock commerce dataset from the MySQL-based Basket Craft database. The pipeline extracts data from the MySQL data lake, loads it into a raw schema within a PostgreSQL warehouse, transforms it using dbt, and visualizes it in Looker Studio. We practiced this process during lesson exercises using the products and orders datasets. For Quiz 3, we applied the same methodology independently, focusing on the website sessions data.

  I wrote three Python scripts to extract and load the Basket Craft orders, products, and website sessions data into the raw PostgreSQL schema. These scripts are now triggered by a GitHub Actions workflow that runs every 15 minutes on a cron schedule and uses GitHub Secrets to manage environment variables securely.

  For the transformation layer, we used dbt (Data Build Tool). The **staging models** served as a clean-up layer—renaming and lightly transforming raw fields for better readability. On top of that, **warehouse models** were built to create analytics-ready tables.

  Finally, I connected the warehouse tables to **Looker Studio** to design a dashboard. The visuals I created help communicate key insights and trends in the session data, telling a clear story for stakeholders. Looker Studio Dashboard link: https://lookerstudio.google.com/reporting/e568bdaf-fc23-4be5-bc8c-2e428297d8fa

<img width="1357" alt="Screenshot 2025-05-04 at 7 58 33 PM" src="https://github.com/user-attachments/assets/d5cbd20e-09d3-4b56-b37e-643593e75efb" />
