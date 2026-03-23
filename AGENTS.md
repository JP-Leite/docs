# Documentation Agent Instructions

## Style and Branding
- Always refer to the platform as **Content Innovation Cloud (CIC)** or **Hyland CIC**.
- Use the **primary blue (#0066CC)** for status highlights or important markers.
- Write for **Solution Architects and Developers**. 

## Page Components
- Use `<CardGroup>` for product grids.
- Use `<Steps>` for any tutorial or getting started guide.
- Use `<Tabs>` for comparing multiple ways to achieve a goal (e.g., CLI vs API).
- Use `<Accordion>` for technical deep-dives or FAQs.

## API Documentation
- Every API section should point to the **Interactive API Reference**.
- Use the standard `api: 'METHOD /endpoint'` frontmatter for manual pages.

## Project Context
- CIC is built on **Hyland Experience Platform (HxP)**.
- Authentication is always via **OAuth2 Client Credentials**.
- The main services are: Runtime, Query, Repository, Modeling, Deployment, and Identity.
