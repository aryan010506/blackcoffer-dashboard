#📊 Blackcoffer Dashboard

An interactive, data-driven dashboard built with React.js and FastAPI, designed to analyze insights using filters like End Year, Topic, Sector, Region, PEST, SWOT, Source, Country, and City.

🚀 Live Demo
(Optional — Add link if deployed on Vercel, Netlify, or GitHub Pages)
➡️ Live Demo (coming soon)

📁 Project Structure

bash

Copy

Edit

blackcoffer-dashboard/

├── backend/              # FastAPI backend (Python)

│   ├── main.py

│   └── ... 

├── frontend/             # React frontend

│   ├── src/

│   │   ├── App.js

│   │   └── ...

│   └── package.json

├── README.md

🧰 Tech Stack

Frontend	Backend	Charting	UI Tools

React.js	FastAPI	Recharts	react-select

Axios	Uvicorn		CSS Grid/Flexbox

🎯 Features
📅 Multi-filter Dashboard: End Year, Topic, Sector, Region, PEST, SWOT, Source, Country, and City

📈 Live Charting: Interactive bar charts using recharts

🔄 Real-time Filtering: Dynamic dropdowns that filter backend data instantly

🔌 API-driven: FastAPI backend serves filtered data via REST APIs

⚙️ Setup Instructions
1. Clone the Repository
   
bash

Copy

Edit

git clone https://github.com/your-username/blackcoffer-dashboard.git

cd blackcoffer-dashboard

2. Start the Backend (FastAPI)
   
bash

Copy

Edit

cd backend

pip install fastapi uvicorn

python -m uvicorn main:app --reload

Runs on: http://127.0.0.1:8000

3. Start the Frontend (React)

bash

Copy

Edit

cd ../frontend

npm install

npm start

Runs on: http://localhost:3000

📊 Screenshots
![Image](https://github.com/user-attachments/assets/e1118322-7c18-4d4c-a959-8c005f859cb2)

🧠 Learning Outcomes
Built a full-stack dashboard from scratch

Learned advanced filtering and API integration

Implemented frontend charting and dropdowns using real-time data

📄 License
This project is licensed under the MIT License

🙋‍♂️ Author
Aryan Sunil
📧 Connect on LinkedIn
