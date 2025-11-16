# 🌍 Wikipedia Country Info Scraper

A Python-based web scraping tool that extracts country information from Wikipedia with a user-friendly GUI interface. Built to explore data collection techniques for machine learning projects.

## 📋 Overview

This project scrapes country-specific data from Wikipedia, including summaries, infobox details, and flag images. The application features a clean Tkinter GUI and allows users to export the collected data as a formatted PDF document.

## ✨ Features

- 🔍 **Real-time Web Scraping**: Fetches live data from Wikipedia
- 🖼️ **Dynamic Flag Display**: Automatically detects and displays country flags as background
- 📊 **Structured Data Extraction**: Parses infobox tables and summary paragraphs
- 💾 **PDF Export**: Save collected information as professionally formatted PDF
- 🎨 **User-Friendly GUI**: Clean interface built with Tkinter
- ⚡ **Error Handling**: Robust error handling for failed requests

## 🛠️ Technologies Used

- **Python 3.x**
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Requests** - HTTP requests
- **Tkinter** - GUI development
- **ReportLab** - PDF generation
- **Pillow (PIL)** - Image processing

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wikipedia-country-scraper.git
cd wikipedia-country-scraper
```

2. Install required dependencies:
```bash
pip install beautifulsoup4 requests reportlab pillow
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Run the application:
```bash
python main.py
```

2. Enter a country name in the input field
3. Click the "Search" button
4. View the extracted information:
   - Country summary
   - Infobox details
   - Flag image (as background)
5. Click "PDF" to save the data as a PDF file

## 📸 Screenshots

<img width="878" height="790" alt="image" src="https://github.com/user-attachments/assets/3957e5ac-e229-4e7a-a576-a1887f771a8e" />


## 🎯 Project Purpose

This project was created to:
- Learn web scraping fundamentals using BeautifulSoup
- Understand data collection techniques for ML/AI projects
- Practice GUI development with Tkinter
- Explore data extraction and formatting workflows

## 📁 Project Structure

```
wikipedia-country-scraper/
│
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── image.jpg           # Temporary image storage (generated)
```

## 🔧 How It Works

1. **User Input**: User enters country name
2. **URL Formation**: Constructs Wikipedia URL with country name
3. **HTTP Request**: Sends GET request with custom headers
4. **HTML Parsing**: BeautifulSoup parses the HTML content
5. **Data Extraction**: 
   - Extracts page title
   - Retrieves summary paragraphs
   - Parses infobox table data
   - Downloads flag image
6. **Display**: Shows data in GUI with flag as background
7. **Export**: Generates formatted PDF with all collected data

## ⚠️ Limitations

- Requires active internet connection
- Dependent on Wikipedia's HTML structure
- Rate limiting through sleep delays (respectful scraping)
- Only works with publicly accessible Wikipedia pages

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 Future Improvements

- [ ] Add support for multiple languages
- [ ] Add more export formats (CSV, JSON)
- [ ] Include historical data comparison
- [ ] Add search suggestions/autocomplete

## 🙏 Acknowledgments

- Wikipedia for providing free access to information
- BeautifulSoup documentation and community
- Python community for excellent libraries

## 📧 Contact

For questions or feedback, reach out via:
- LinkedIn: [Your Profile](https://linkedin.com/in/gurmeet-kumar)

---

⭐ If you found this project helpful, please give it a star!

**Note**: This project is for educational purposes. Please respect Wikipedia's [Terms of Use](https://foundation.wikimedia.org/wiki/Terms_of_Use) and practice responsible web scraping.
