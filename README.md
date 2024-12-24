# Still-Travelling_Assignment
# YouTube Data Scraper

This project is a Python-based YouTube Data Scraper that retrieves detailed information about YouTube videos for a specific genre and exports it into a CSV file. It leverages the YouTube Data API (v3) to fetch video details such as title, description, views, and more.

### Features

- **Scrapes YouTube Videos by Genre**: The scraper dynamically fetches the top 500 YouTube videos related to a given genre.
- **Extracts Detailed Video Information**: For each video, the scraper collects metadata such as video URL, title, description, channel information, and more.
- **Captions Handling**: It checks for captions availability (placeholder for now).
- **Exports Data to CSV**: The results are saved in a CSV file with a pre-defined column order for easy analysis.

## Requirements

- Python 3.6+
- Required libraries:
  - `requests`
  - `pandas`

You can install the required libraries using the following command:

```bash
pip install requests pandas
```

## Setup

1. **YouTube API Key**: You will need a YouTube Data API key to access the YouTube API. If you don’t have one, follow these steps:
   - Go to [Google Developers Console](https://console.developers.google.com/).
   - Create a project or select an existing one.
   - Enable the "YouTube Data API v3".
   - Go to "Credentials" and create a new API key.

2. **Add API Key**: Replace `"YOUR_API_KEY"` in the code with your actual API key.

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script with:

   ```bash
   python youtube_data_scraper.py
   ```

4. When prompted, input the genre (e.g., "music", "gaming", "technology") for which you want to fetch videos.
5. The script will scrape data and generate a CSV file (`youtube_data.csv`) containing details of the videos.

## CSV Output Format

The generated CSV file contains the following columns:

- **Video URL**: Direct URL of the video.
- **Title**: Title of the video.
- **Description**: Description of the video.
- **Channel Title**: Title of the channel that uploaded the video.
- **Keyword Tags**: A comma-separated list of tags associated with the video.
- **Category**: The YouTube video category ID.
- **Topic Details**: Categories associated with the video topics.
- **Published at**: The date and time when the video was published.
- **Video Duration**: Duration of the video in ISO 8601 format.
- **View Count**: Total number of views on the video.
- **Comment Count**: Total number of comments on the video.
- **Captions Available**: A placeholder field indicating whether captions are available (false by default).
- **Caption Text**: Placeholder for caption text (currently not implemented).

## Code Structure

The project is organized as follows:

- **`youtube_data_scraper.py`**: The main Python script for scraping YouTube data.
- **`YouTubeDataScraper` class**: Handles the logic for fetching videos and details using the YouTube API.
- **`CSVExporter` class**: Responsible for saving the scraped data to a CSV file.
- **`main()` function**: Orchestrates the entire process, from scraping data to exporting it.

## Example

### Input:
```
Enter the genre: gaming
```

### Output:

A CSV file `youtube_data.csv` with data for the top 500 videos related to the "gaming" genre.

## Limitations


- **API Quotas**: The YouTube Data API has daily quotas. Ensure you have enough quota to fetch 500 videos.

## Future Improvements

- **Download Captions**: Implement functionality to download captions for videos where available.
- **Error Handling**: Improve error handling to manage API limits and potential failures.
- **Extended Metadata**: Fetch additional video metadata (e.g., video comments, related videos).

## License

This project is open-source and available under the [MIT License](LICENSE).
