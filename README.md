# Asset Manager (Standalone)

A professional, standalone Asset Management and SPMO (Supply and Property Management Office) platform designed for institutional asset tracking, auditing, and lifecycle management.

## 🚀 Key Features
*   **Complete Asset Lifecycle Tracking**: From acquisition and batch registration to maintenance and disposal.
*   **Dynamic Data Masking (Demo Mode)**: Built-in privacy engine to sanitize institutional data for public presentations.
*   **Role-Based Access Control (RBAC)**: Secure workflows for Admins, Chiefs, and Supervisors.
*   **Professional Reporting**: Generates high-fidelity RPCPPE reports, Property Cards, and Audit Trails.
*   **Modern UI**: Sleek, responsive interface with a focus on usability and real-time analytics.

## 🛠️ Technology Stack
*   **Backend**: Django (Python)
*   **Database**: SQLite (Development) / PostgreSQL (Production ready)
*   **Frontend**: Bootstrap 5, FontAwesome 6, Vanilla JS
*   **Authentication**: Django Auth with RBAC expansion

## 🚦 Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver 3001`

## 🛡️ Presentation Mode
This application includes a unique **"Demo Mode"** toggle in the sidebar. When enabled, all institutional names, personnel identities, and specific office identifiers are masked in real-time using a deterministic masking engine, ensuring data privacy during demonstrations.

---
*Created for the SPMO Suite Public Presentation.*
