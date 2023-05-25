## DEPLOYMENT
Install requirements by executing `pip install -r requirements.txt`.

Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Execute command `mage start lumkani` in **mage-ai** root folder to initialize the Lumkani Demo Project.

Mage will run on `http://localhost:6789`.

## EXECUTION
### Automated Execution:
Open `http://localhost:6789` in browser of choice to access the Mage UI.

Navigate on left side panel to **Pipelines**.

Select and execute **lumkani_demo** pipeline.

### Granular Execution:
Navigate on left panel to **Edit Pipeline** in order to view source code of sub-processes.

Select block on right **tree-diagram** in order to view source code per process.

Execute each block in sequence of stream.

## TESTING
**Unit tests** are performed during each block process after task execution.

## ALGORITHM DESCRIPTION
Utilising [Mage-ai](https://docs.mage.ai/introduction/overview) for ELT to create a streamlined pipeline approach.

Integration of payment data through data ingestion from csv files.

Transformation and analysis of payment data to generate required reporting.

Exportation of data to required destination storages.
