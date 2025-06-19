# Receipt Genie: AI-Powered Receipt Dashboard & Budgeting App

Receipt Genie is a modern, full-stack web app for managing receipts, tracking expenses, and setting monthly budgets. Upload your receipt images, analyze your spending, and export your data—all in a beautiful, secure dashboard.

---

## 🚀 Features
- **Secure Authentication:** Register/login with email & password (hashed, never stored in plain text)
- **Receipt Upload:** Upload JPG/JPEG/PNG images; duplicate detection
- **AI-Powered Extraction:** Extracts store info, items, and totals from receipts
- **Advanced Analytics:**
  - Monthly & weekly spending trends
  - Top categories & vendors
  - Interactive charts (Plotly)
- **Budgeting:**
  - Set/view monthly budgets per category
  - Progress bars & alerts when approaching/exceeding budgets
- **Data Export:** Download your data as CSV, Excel, or PDF (with charts)
- **Modern UI:**
  - Light/dark mode toggle
  - Sidebar navigation
  - Responsive, clean design

---

## 🛠️ Tech Stack
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **Backend/Data:** Python, [SQLAlchemy](https://www.sqlalchemy.org/), SQLite
- **Visualization:** [Plotly](https://plotly.com/python/)
- **Other:** Pillow, bcrypt, OpenAI API (for AI extraction)

---

## 🖥️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/receipt-genie.git
   cd receipt-genie
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   streamlit run app.py
   ```
4. **(Optional) Set your OpenAI API key:**
   - Edit `app.py` and replace the placeholder with your own OpenAI API key.

---

## 📸 Screenshots
> Add screenshots or a demo GIF here to showcase the UI and features!

---

## 📝 Usage
- Register a new account or log in.
- Upload receipt images and view extracted data.
- Analyze your spending trends and set monthly budgets.
- Export your data for further analysis or reporting.

---



## 🙌 Credits
- Built with [Streamlit](https://streamlit.io/), [SQLAlchemy](https://www.sqlalchemy.org/), [Plotly](https://plotly.com/python/), and [OpenAI](https://openai.com/)
- Designed and developed by [Shreya Shere]

---

**Ready to take control of your receipts and spending? Give Receipt Genie a try!** 